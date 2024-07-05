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
    def launch(cmd: str, args: list):
        """Use the built-in launch command to run gnome-shell commands"""
        actions.user.launch_command_prompt()
        actions.sleep("50ms")
        #actions.user.notify(f"Running command: {cmd} {' '.join(args)}")
        actions.user.paste(cmd + " " + " ".join(args))
        actions.sleep("50ms")
        actions.key("enter")

    def launch_command_prompt():
        """The keyboard shortcut to open the launch command prompt"""
        actions.key("alt-f2")

    def window_maximize():
        actions.key("alt-f10")

    def window_pin():
        actions.key("alt-space")
        actions.sleep("500ms")
        actions.key("down:6")
        actions.key("enter")

    def window_unpin():
        actions.user.window_pin()
