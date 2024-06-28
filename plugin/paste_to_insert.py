import logging

from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()

mod.setting(
    "paste_to_insert_threshold",
    type=int,
    default=-1,
    desc="""Use paste to insert text longer than this many characters.
Zero means always paste; -1 means never paste.
""",
)


@ctx.action_class("main")
class MainActions:
    def insert(text):
        threshold = settings.get("user.paste_to_insert_threshold")
        if 0 <= threshold < len(text):
            if text[-1] == "\n":
                text = text[:-1]
                actions.user.paste(text)
                actions.key("enter")
            else:
                actions.user.paste(text)
            return
        actions.next(text)
