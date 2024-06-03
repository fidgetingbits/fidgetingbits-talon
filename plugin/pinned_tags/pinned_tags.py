import subprocess
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


def _is_unix_pid_alive(pid: int) -> bool:
    """Check if a process is still running

    This is a *nix-specific function that uses the ps command to check for the existence of a process
    """

    try:
        subprocess.check_call(
            ["ps", "-p", str(pid)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False


def _garbage_collect():
    """Clean up the tracked context list periodically"""
    global tracked_contexts
    active_pid_contexts = []
    active_window_contexts = []
    window_list = [x.id for x in ui.windows()]

    for ctx in tracked_contexts:
        match ctx.tag_id.type:
            case "pid":
                if _is_unix_pid_alive(ctx.tag_id.id):
                    active_pid_contexts.append(ctx)
            case "window":
                if ctx.tag_id.id in window_list:
                    active_window_contexts.append(ctx)
    tracked_contexts = active_pid_contexts + active_window_contexts


cron.interval("10m", _garbage_collect)
