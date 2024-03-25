# This is an experiment to solve a problem I have. Say I have one of 5 open terminals. One of those terminals
# I am ssh'd into a remote machine. I want to be able to use a specific package manager, but use the generic
# packager/ commands I have configured. I need a way to "pin" a specific tag that I enable to that context only,
# such that all other terminals continue to use the other default package manager, but if I return to the other
# context, then I can use the specific package manager. This is a way to "pin" a tag to a specific context.
#
# Questions:
# - How do I detect if a an application has terminated, meaning the context object should go away?
#   - Could we periodically GC by walking all windows and checking if the window ID is still valid?

from dataclasses import dataclass

from talon import Context, Module, actions, ui

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
            print("WARN: Could not get zsh pid for current window")
            return

        # Maybe update an existing context
        global tracked_contexts
        for tracked in tracked_contexts:
            if tracked.pid == zsh_pid and tracked.category == category:
                if tracked.tag == tag:
                    print("WARN: Tag already pinned")
                    return
                tracked.tag = [tag]
                return

        # Create a new context
        ctx = Context()
        ctx.tags = [tag]
        ctx.matches = f"win.title: /{zsh_pid}:/"
        # print(ctx.matches)
        tracked_contexts.append(PinnedTagContext(ctx, tag, zsh_pid, category))
        # FIXME: check if we already have one pinned...

    def unpin_tag(tag: str):
        """Unregister a Context object with the tag_pin module"""
        global tracked_contexts
        zsh_pid = actions.user.zsh_get_pid()
        if zsh_pid is None:
            print("WARN: Could not get zsh pid for current window")
            return
        tracked_contexts = [
            x for x in tracked_contexts if x.pid != zsh_pid and x.tag != tag
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

    def dump_tag_pinned_context_list():
        """Dump all tracked contexts"""
        for tracked in tracked_contexts:
            print(tracked)
            print(tracked.context.tags)
            print(tracked.context.matches)
