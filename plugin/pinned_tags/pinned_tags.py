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

from talon import Context, Module

mod = Module()


# We need to track the context and the tag we are pinning
@dataclass
class PinnedTagContext:
    context: Context
    tag: str
    id: str


tracked_contexts = []


@mod.action_class
class Actions:
    def pin_tag(tag: str):
        """Register a Context object with the tag_pin module"""

    def pin_tag_to_context(tag: str, context: Context):
        """Register a Context object with the tag_pin module"""
        if context not in tracked_contexts:
            # FIXME: "foo" needs to change to some way to identify the context
            tracked_contexts.append(PinnedTagContext(context, tag, "foo"))
            # TODO: Need to adjust the tags..

    def dump_tag_pinned_context_list():
        """Dump all tracked contexts"""
        for tracked in tracked_contexts:
            print(tracked)
            print(tracked.context.tags)
