from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
tag: user.tracing_strace
"""


@ctx.action_class("user")
class Actions:
    def trace_program():
        """Most basic trace command"""
        actions.insert("strace -f ")

    def trace_program_with_log():
        """Trace command with log"""
        actions.insert("strace -f -o strace.log ")
