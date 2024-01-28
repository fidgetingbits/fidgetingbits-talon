from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
tag: user.tracing_strace
"""

ctx.lists["user.tracing_filters"] = {
    "file": "%file",
    "process": "%process",
    "network": "%network",
    "signal": "%signal",
    "ipc": "%ipc",
    "desc": "%desc",
    "memory": "%memory",
    "creds": "%creds",
    "stat": "%stat",
    "L stat": "%lstat",
    "F stat": "%fstat",
    "regex": "/",
    "clock": "%clock",
    "pure": "%pure",
}


@ctx.action_class("user")
class Actions:
    def trace_program():
        """Most basic trace command"""
        actions.insert("strace -f ")

    def trace_program_with_log():
        """Trace command with log"""
        actions.insert("strace -f -o strace.log ")

    def trace_program_with_filter(filter: str):
        """Trace command with filter"""
        actions.user.insert_between("strace -e 'trace={filter}", "'")

    def trace_program_with_path():
        """Trace command with path"""
        actions.user.insert_between('strace --trace-path="', '"')
