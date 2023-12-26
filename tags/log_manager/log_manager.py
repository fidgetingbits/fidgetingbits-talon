from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: terminal
and tag: user.log_manager
"""

mod.tag("log_manager", desc="Generic log manager support")


@mod.action_class
class Actions:
    def log_show():
        """List the whole log"""
