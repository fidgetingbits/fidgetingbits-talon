from talon import Context, Module, actions

mod = Module()
mod.tag("tracing_dtruss", desc="Tag for enabling generic tracing commands")
mod.tag("tracing_strace", desc="Tag for enabling generic tracing commands")


@mod.action_class
class Actions:
    def trace_program():
        """Most basic trace command"""

    def trace_program_with_log():
        """Trace command with log"""
