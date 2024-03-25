import os
from dataclasses import dataclass

from talon import Context, Module, actions, app, cron

mod = Module()


# We need to track the context and the tag we are pinning
@dataclass
class PinnedTagContext:
    context: Context
    tag: str
    pid: int
    category: str


tracked_contexts = []


@mod.action_class
class Actions:
    def pin_tag(tag: str, category: str):
        """Register a Context object with the tag_pin module"""
        zsh_pid = actions.user.zsh_get_pid()
        if zsh_pid is None:
            return

        # Maybe update an existing context
        global tracked_contexts
        for tracked in tracked_contexts:
            if tracked.pid == zsh_pid and tracked.category == category:
                if tracked.tag == tag:
                    return
                tracked.tag = [tag]
                app.notify(f"Pinned {category} tag: {tag}")
                return

        # Otherwise create a new context
        ctx = Context()
        ctx.tags = [tag]
        ctx.matches = f"win.title: /{zsh_pid}:/"
        tracked_contexts.append(PinnedTagContext(ctx, tag, zsh_pid, category))

    def unpin_tag(tag: str, category: str):
        """Unregister a Context object with the tag_pin module"""
        global tracked_contexts
        zsh_pid = actions.user.zsh_get_pid()
        if zsh_pid is None:
            return
        tracked_contexts = [
            x
            for x in tracked_contexts
            if x.pid != zsh_pid and x.tag != tag and x.category != category
        ]

    def find_pinned_tag(category: str):
        """Find a tag associated with the category that's pinned to the current process"""
        global tracked_contexts
        zsh_pid = actions.user.zsh_get_pid()
        if zsh_pid is None:
            print("WARN: Could not get zsh pid for current window")
            return None
        for tracked in tracked_contexts:
            if tracked.pid == zsh_pid and tracked.category == category:
                return tracked.tag
        return None

    def get_pinned_contexts():
        """Return a list of all pinned contexts"""
        return tracked_contexts

    def dump_tag_pinned_context_list():
        """Dump all contexts pin to the current zsh process"""
        for tracked in tracked_contexts:
            if tracked.pid == actions.user.zsh_get_pid():
                print(tracked)
                print(tracked.context.tags)
                print(tracked.context.matches)


def find_dead_processes(pid_list: list[int]) -> list[int]:
    """Find dead processes from a list of PIDs

    This is a *nix-specific function that uses the ps command to check for the existence of a process
    """

    dead_processes = []
    for pid in pid_list:
        if os.system(f"ps -p {pid} > /dev/null") != 0:
            dead_processes.append(pid)
    return dead_processes


def _garbage_collect():
    """Clean up the tracked context list periodically

    This is required because we don't know when a given process is terminated from inside talon
    """
    print("_garbage_collect()")

    global tracked_contexts
    pid_list = [x.pid for x in tracked_contexts]
    print(pid_list)
    if app.platform == "linux" or app.platform == "mac":
        clean_up = find_dead_processes(pid_list)
    else:
        return
    if len(clean_up) > 0:
        print(f"PACKAGE MANAGER: Cleaning up {len(clean_up)} dead processes")
    tracked_contexts = [x for x in tracked_contexts if x.pid not in clean_up]


cron.interval("10s", _garbage_collect)
