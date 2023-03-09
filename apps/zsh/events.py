"""
events.py contains a select-based event loop within the talon process
(but otherwise independent of talon) for supporting IPC for advanced talon
integrations.

When this file is reloaded, it will shut down any modules which depended on
this event loop; and they must also be reloaded.
"""

import socket
import contextlib
import selectors
import threading
import traceback
import logging

from . import singletons


class EventConsumer:
    def startup(self, ctx):
        """A consumer should register all of its objects"""
        raise NotImplementedError()

    def shutdown(self):
        """A consumer must shut down because the event loop is closing."""
        raise NotImplementedError()

    def event(self, key, mask):
        """A consumer got a select event"""
        raise NotImplementedError()

    def notify(self, msg):
        """A consumer got a notify msg"""
        raise NotImplementedError()


# LoopContext is the interface to the event loop provided to a consumer.
class LoopContext:
    def __init__(self, loop, consumer):
        self.loop = loop
        self.consumer = consumer
        self.evicted = False

    def register(self, fileobj, mask, data=None):
        if self.evicted:
            return
        self.loop.selector.register(fileobj, mask, data)
        self.loop.consumers[fileobj] = self.consumer

    def modify(self, fileobj, mask, data=None):
        if self.evicted:
            return
        self.loop.selector.modify(fileobj, mask, data)

    def unregister(self, fileobj):
        if self.evicted:
            return
        self.loop.selector.unregister(fileobj)
        del self.loop.consumers[fileobj]

    def shut_me_down(self):
        """close_me is safe to call from off-thread"""
        if self.evicted:
            return
        with self.loop.cond:
            if self.loop.closed:
                return
            self.loop.stoppables.append(self.consumer)
            self.loop.ctrl_w.send(b"wake\n")

    def notify_me(self, msg):
        """noitfy_me is safe to call from off-thread"""
        if self.evicted:
            return
        with self.loop.cond:
            if self.loop.closed:
                logging.warning("dropping notify_me() while event loop is closed")
                return
            self.loop.notifiables.append((self.consumer, msg))
            self.loop.ctrl_w.send(b"wake\n")


class EventLoop(threading.Thread):
    def __init__(self):
        # This is the one selector that everyone will use.
        self.selector = selectors.DefaultSelector()

        # Open a control channel.  ctrl_r will be part of the event loop,
        # ctrl_w is for outside of the event loop.
        self.ctrl_r, self.ctrl_w = socket.socketpair()
        self.ctrl_r.setblocking(False)
        self.selector.register(self.ctrl_r, selectors.EVENT_READ)

        # consumers maps fileobjs in the select loop to EventConsumers
        self.consumers = {}

        # singletons maps names to consumers
        self.singletons = {}

        # contexts maps EventConsumers to their LoopContexts
        self.contexts = {}

        self.startables = []
        self.stoppables = []
        # notifiables is a list of (consumer, msg) tuples from ctx.notify_me
        self.notifiables = []

        self.closed = False
        self.paused = False
        self.cond = threading.Condition()

        super().__init__()

    def evict_consumer(self, old):
        """do any cleanup after a failed or shitty consumer shuts down"""

        ctx = self.contexts.pop(old)
        ctx.evicted = True

        for fileobj, consumer in list(self.consumers.items()):
            if consumer == old:
                self.select.unregister(fileobj)
                del self.consumers[fileobj]

        for singleton, consumer in list(self.singletons.items()):
            if consumer == old:
                del self.singletons[singleton]

        try:
            self.startables.remove(old)
        except ValueError:
            pass

        try:
            self.stoppables.remove(old)
        except ValueError:
            pass

        # remove from notifiables in reverse order
        for i in range(len(self.notifiables) - 1, -1, -1):
            consumer, _ = self.notifiables[i]
            if consumer == old:
                self.notifiables.pop(i)

    @contextlib.contextmanager
    def evict_on_fail(self, consumer):
        try:
            yield
        except Exception as e:
            logging.error("failure in consumer code:\n" + traceback.format_exc())
            try:
                consumer.shutdown()
            except Exception as e:
                logging.error(
                    "failure in shutdown after failure in consumer code:\n"
                    + traceback.format_exc()
                )
            self.evict_consumer(consumer)

    def run_one(self, key, mask):
        """returns True if loop should exit"""
        if key.fileobj == self.ctrl_r:
            msg = self.ctrl_r.recv(4096)
            for line in msg.splitlines():
                if line == b"quit":
                    for consumer, ctx in self.contexts:
                        self.consumer.close()
                    return True
                if line == b"wake":
                    with self.cond:
                        while self.stoppables:
                            consumer = self.stoppables.pop()
                            try:
                                consumer.shutdown()
                            except Exception as e:
                                logging.error(
                                    "failure in shutdown:\n" + traceback.format_exc()
                                )
                            self.evict_consumer(consumer)
                        while self.startables:
                            consumer = self.startables.pop()
                            ctx = LoopContext(self, consumer)
                            self.contexts[consumer] = ctx
                            with self.evict_on_fail(consumer):
                                consumer.startup(ctx)
                        while self.notifiables:
                            consumer, msg = self.notifiables.pop()
                            with self.evict_on_fail(consumer):
                                consumer.notify(msg)
                    return False
                raise ValueError(f"unknown control message: {line}")

        # all other fileobjs are from consumers.
        consumer = self.consumers[key.fileobj]
        with self.evict_on_fail(consumer):
            consumer.event(key, mask)
        return False

    def run(self):
        try:
            while True:
                for key, mask in self.selector.select():
                    if self.run_one(key, mask):
                        return
        finally:
            self._close()
            with self.cond:
                self.closed = True
                self.cond.notify()

    def _close(self):
        for consumer in list(self.contexts):
            try:
                self.consumer.shutdown()
            except Exception:
                logging.error("failure in shutdown:\n" + traceback.format_exc())
            self.evict_consumer(consumer)
        self.selector.unregister(self.ctrl_r)
        self.selector.unregister(self.ctrl_w)
        self.ctrl_r.close()
        self.ctrl_w.close()
        self.selector.close()

    def singleton(self, fn):
        """singleton is always be called off-thread"""
        name = f"{fn.__module__}.{fn.__name__}"

        # Do any cleanup actions from before.
        if name in self.singletons:
            old = self.singletons.pop(name)
            ctx = self.contexts[old]
            ctx.shut_me_down()

        # get the new object
        obj = fn()

        with self.cond:
            if not self.closed:
                self.startables.append(obj)
                self.singletons[name] = obj
                self.ctrl_w.send(b"wake\n")
            else:
                logging.warning(
                    "not starting @event_loop.singleton:{name} because event "
                    "loop is not running"
                )

        # We want the object returned to be available at the name of the
        # function, so instead of returning a function we return an object.
        return obj

    def close(self):
        with self.cond:
            if self.closed:
                return
            self.ctrl_w.send(b"quit\n")
        self.join()


# @singletons.singleton
# def event_loop():
#     x = EventLoop()
#     x.start()
#     try:
#         yield x
#     finally:
#         x.close()


# singleton = event_loop.singleton
