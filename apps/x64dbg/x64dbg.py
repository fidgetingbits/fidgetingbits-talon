from talon import Context, Module, actions

mod = Module()
mod.apps.x64dbg = """
win.title: /x64dbg \[Elevated\]/
"""

ctx = Context()
ctx.matches = r"""
app: x64dbg
"""


@ctx.action_class("app")
class app_actions:
    def tab_previous():
        actions.key("alt-left")

    def tab_next():
        actions.key("alt-right")


@ctx.action_class("user")
class UserActions:
    # Code execution

    def debugger_step_line():
        actions.key("f7")

    def debugger_step_over_line():
        actions.key("f8")

    def debugger_step_out():
        actions.key("ctrl-f9")

    def debugger_continue():
        actions.key("f9")

    def debugger_stop():
        actions.key("f12")

    def debugger_start():
        actions.key("f9")

    def debugger_restart():
        actions.key("ctrl-f2")

    def debugger_attach():
        actions.key("alt-a")

    def debugger_detach():
        actions.key("ctrl-alt-f2")

    # Breakpoints
    def debugger_breakpoint_toggle():
        actions.key("f2")

    def debugger_show_breakpoints():
        actions.key("alt-b")
