from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: user.tracing_dtruss
"""


@ctx.action_class("user")
class Actions:
    def trace_program():
        """Most basic trace command"""
        actions.insert("sudo dtruss -f ")

    def trace_program_with_log():
        """Trace command with log"""
        actions.user.insert_between("sudo dtruss -f ", "2>&1 > dtruss.txt")
