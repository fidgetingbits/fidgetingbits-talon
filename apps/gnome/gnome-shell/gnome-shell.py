from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.tag("gnome-shell", desc="tag for loading gnome-shell related files")

ctx.matches = """
tag: user.gnome-shell
"""


@ctx.action_class("app")
class AppActions:
    def window_open():
        actions.key("ctrl-shift-n")

    def window_close():
        actions.key("alt-f4")
        # actions.key("ctrl-shift-w")


@ctx.action_class("user")
class UserActions:
    def window_maximize():
        actions.key("alt-f10")

    def window_pin():
        actions.key("alt-space")
        actions.sleep("500ms")
        actions.key("down:6")
        actions.key("enter")

    def window_unpin():
        actions.user.window_pin()
