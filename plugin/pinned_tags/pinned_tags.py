import os
from dataclasses import dataclass

from talon import Context, Module, actions, app, cron, ui

mod = Module()


@dataclass
class PinnedTagId:
    id: int
    type: str


@dataclass
class PinnedTagContext:
    context: Context
    tag: str
    tag_id: PinnedTagId
    category: str


tracked_contexts = []


@mod.scope
def scope():
    return {"pinged_tag_id": {_get_pinned_tag_id().id}}


def _get_pinned_tag_id() -> PinnedTagId:
    id = actions.user.get_pinned_tag_id()
    return PinnedTagId(id=id[0], type=id[1])


@mod.action_class
class Actions:
    def pin_tag(tag: str, category: str) -> None:
        """Register a Context object with the pinned_tags module"""
        tag_id = _get_pinned_tag_id()
        if tag_id is None:
            return
        print(f"INFO: Pinned tag {tag} to process {tag_id}")
        # Maybe update an existing context
        global tracked_contexts
        for tracked in tracked_contexts:
            if tracked.tag_id == tag_id and tracked.category == category:
                if tracked.tag == tag:
                    return
                tracked.tag = [tag]
                app.notify(f"Pinned {category} tag: {tag}")
                return

        # Otherwise create a new context
        ctx = Context()
        ctx.tags = [tag]
        ctx.matches = f"user.pinned_tag_id: {tag_id}"
        tracked_contexts.append(PinnedTagContext(ctx, tag, tag_id, category))

    def unpin_tag(tag: str, category: str) -> None:
        """Unregister a Context object with the pinned_tags module"""
        global tracked_contexts
        tag_id = _get_pinned_tag_id()
        if tag_id is None:
            return
        tracked_contexts = [
            x
            for x in tracked_contexts
            if x.tag_id != tag_id and x.tag != tag and x.category != category
        ]

    def find_pinned_tag(category: str) -> str:
        """Find a tag associated with the category that's pinned to the current context"""
        tag_id = _get_pinned_tag_id()
        if tag_id is None:
            print("WARN: Could not get a pinned_tag identifier for current window")
            return None
        for tracked in tracked_contexts:
            if tracked.tag_id == tag_id and tracked.category == category:
                return tracked.tag
        return None

    def get_pinned_contexts() -> list[PinnedTagContext]:
        """Return a list of all pinned contexts"""
        return tracked_contexts

    def get_pinned_tag_id() -> tuple[int, str]:
        """Return the identifier for pinning a tag

        This can be overridden by certain applications to allow more granular identifiers. By default
        we use the window ID, but sometimes you may have a window that runs many sub processes (like a terminal)
        so you want to be able to drive down further into the pid of the shell process.
        """
        return (ui.active_window().id, "window")

    def dump_tag_pinned_context_list():
        """Dump all contexts pin to the current zsh process"""
        for tracked in tracked_contexts:
            if tracked.tag_id == _get_pinned_tag_id():
                print(tracked)
                print(tracked.context.tags)
                print(tracked.context.matches)

    def dump_active_pinned_tag_id() -> None:
        """Dump the PID of the active process"""
        print(_get_pinned_tag_id())


def _find_dead_unix_processes(pid_list: list[int]) -> list[int]:
    """Find dead processes from a list of PIDs

    This is a *nix-specific function that uses the ps command to check for the existence of a process
    """

    dead_processes = []
    for pid in pid_list:
        if os.system(f"ps -p {pid} > /dev/null") != 0:
            dead_processes.append(pid)
    return dead_processes


# FIXME: This needs to only drop pids if the active window id is of type window, if it's of type pid then we use this method
def _garbage_collect():
    """Clean up the tracked context list periodically

    This is required because we don't know when a given process is terminated from inside talon
    """
    print("INFO: Garbage collecting pinned tags")
    global tracked_contexts
    active_pid_contexts = []
    pid_list = [x.tag_id.id for x in tracked_contexts if x.tag_id.type == "pid"]
    active_window_contexts = []
    window_list = [x.tag_id.id for x in tracked_contexts if x.tag_id.type == "window"]

    if len(pid_list):
        if app.platform == "linux" or app.platform == "mac":
            clean_up = _find_dead_unix_processes(pid_list)
            print("Found dead processes", clean_up)
            active_pid_contexts = [
                x
                for x in tracked_contexts
                if x.tag_id.type == "pid" and x.tag_id.id not in clean_up
            ]
    if len(window_list):
        active_window_ids = [x.id for x in ui.windows()]
        active_window_contexts = [
            x
            for x in tracked_contexts
            if x.tag_id.type == "window" and x.tag_id.id in active_window_ids
        ]
        if len(active_window_contexts) != len(window_list):
            print("INFO: Found dead windows")
            print("INFO: Active windows", active_window_ids)
            print("INFO: Pinned windows", window_list)

    tracked_contexts = active_pid_contexts + active_window_contexts


cron.interval("10s", _garbage_collect)
