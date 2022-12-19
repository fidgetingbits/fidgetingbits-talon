# A rarely-updated module to assist in writing reload-safe talon modules using
# things like threads, which are not normally safe for reloading with talon.

# If this file is ever updated, you'll need to restart talon.

import logging

_singletons = {}


def singleton(fn):
    name = f"{fn.__module__}.{fn.__name__}"
    # Do any cleanup actions from before.
    if name in _singletons:
        old = _singletons.pop(name)
        try:
            next(old)
        except StopIteration:
            pass
        else:
            logging.error(
                f"the old @singleton function {name} had more than one yield!"
            )

    # Do the startup actions on the new object.
    it = iter(fn())
    obj = next(it)

    # Remember the iterator so we can call the cleanup actions later.
    _singletons[name] = it

    # We want the object yielded by the iterator to be available at the name
    # of the function, so instead of returning a function we return an object.
    return obj
