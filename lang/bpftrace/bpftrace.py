from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
code.language: bpftrace
"""

mod = Module()

mod.list("bpftrace_pointers", desc="Common bpftrace pointers")
mod.list("bpftrace_types", desc="Common bpftrace types")
mod.list("bpftrace_probes", desc="Common bpftrace probe types")
mod.list("bpftrace_signed", desc="A list of default bpftrace signed to operators")
mod.list("bpftrace_builtins", desc="A list of default bpftrace builtin variables")

ctx.lists["user.bpftrace_signed"] = {
    "un signed": "u",
    "unsigned": "u",
}
ctx.lists["self.bpftrace_pointers"] = {
    "pointer": "*",
    "pointer to pointer": "**",
}
ctx.lists["user.bpftrace_types"] = {
    "struck": "struct",
    "short": "int16",
    "integer": "int32",
    "int": "int32",
    "long": "int64",
    "character": "int8",
    "char": "int8",
}

# https://github.com/iovisor/bpftrace/blob/master/docs/reference_guide.md#1-builtins-1
ctx.lists["user.code_common_function"] = {
    "print F": "printf",
    "time": "time",
    "join": "join",
    "string": "str",
    "K sym": "ksym",
    "U sym": "usym",
    "K adder": "kaddr",
    "U adder": "uaddr",
    "register": "register",
    "system": "system",
    "exit": "exit",
    "C group": "cgroupid",
    "K stack": "kstack",
    "U stack": "ustack",
    "N top": "ntop",
    "cat": "cat",
    "signal": "signals",
    "string compare": "strncmp",
    "stir compare": "strncmp",
    "override": "override",
    "buf": "buf",
    "size of": "sizeof",
    "stir F time": "strftime",
    "path": "path",
    "you pointer": "uptr",
    "K pointer": "kptr",
    "mac adder": "macaddr",
    # map functions
    # https://github.com/iovisor/bpftrace/blob/master/docs/reference_guide.md#map-functions
    "count": "count",
    "some": "sum",
    "average": "avg",
    "min": "min",
    "max": "max",
    "stats": "stats",
    "hist": "hist",
    "L hist": "lhist",
    "delete": "delete",
    "print": "print",
    "clear": "clear",
    "zero": "zero",
}

# https://github.com/iovisor/bpftrace/blob/master/docs/reference_guide.md#1-builtins
ctx.lists["user.bpftrace_builtins"] = {
    "process": "pid",
    "pid": "pid",
    "thread": "tid",
    "tid": "tid",
    "you I D": "uid",
    "G I D": "gid",
    "seconds": "nsecs",
    "N sex": "nsecs",
    "elapsed": "elapsed",
    "C P U": "cpu",
    "calm": "comm",
    "K stack": "kstack",
    "U stack": "ustack",
    "arg": "arg",
    "stack arg": "sarg",
    "ret val": "retval",
    "funk": "func",
    "probe": "probe",
    "current": "curtask",
    "see group": "cgroup",
    "see pit": "cpid",
}

# https://github.com/iovisor/bpftrace/blob/master/docs/reference_guide.md#probes
ctx.lists["user.bpftrace_probes"] = {
    "trace point": "tracepoint",
    "user defined": "usdt",
    "K probe": "kprobe",
    "K ret probe": "kretprobe",
    "K funk": "kfunc",
    "K ret funk": "kretfunc",
    "U probe": "uprobe",
    "U ret probe": "uretprobe",
    "software": "software",
    "hardware": "hardware",
    "watch point": "watchpoint",
    "profile": "profile",
    "interval": "interval",
    "iterate": "iter",
    "begin": "BEGIN",
    "end": "END",
    # XXX - this is still missing map modification methods
}


@mod.capture(
    rule="[{user.bpftrace_signed}] {user.bpftrace_types} [{self.bpftrace_pointers}+]"
)
def bpftrace_types(m) -> str:
    "Returns a string"
    if hasattr(m, "bpftrace_signed") and len(m.bpftrace_signed) == 1:
        return m.bpftrace_signed + " ".join(list(m[1:]))
    else:
        return " ".join(list(m))


@mod.capture(rule="[<user.c_signed>] <user.c_types> [<self.c_pointers>+]")
def c_cast(m) -> str:
    "Returns a string"
    return "(" + " ".join(list(m)) + ")"


@ctx.action_class("user")
class UserActions:
    ###
    # code_operators_pointers
    ###
    def code_operator_indirection():
        actions.auto_insert("*")

    ###
    # code_operators_assignment
    ###
    def code_operator_assignment():
        actions.auto_insert(" = ")

    def code_operator_increment():
        actions.auto_insert("++")

    def code_operator_decrement():
        actions.auto_insert("--")

    ##
    # code_operators_math
    ##
    def code_operator_subtraction():
        actions.insert(" - ")

    def code_operator_addition():
        actions.insert(" + ")

    def code_operator_multiplication():
        actions.insert(" * ")

    def code_operator_division():
        actions.insert(" / ")

    def code_operator_modulo():
        actions.insert(" % ")

    def code_operator_equal():
        actions.insert(" == ")

    def code_operator_not_equal():
        actions.insert(" != ")

    def code_operator_greater_than():
        actions.insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.insert(" >= ")

    def code_operator_less_than():
        actions.insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.insert(" <= ")

    ###
    # code_functions
    ###
    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + f"({selection})"
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()

    ###
    # code_comment_line
    ###
    def code_comment_line_prefix():
        actions.auto_insert("//")

    ###
    # code_imperative
    ###
    def code_state_if():
        actions.insert("if () {\n}\n")
        actions.key("up:2 left:3")

    def code_state_else_if():
        actions.insert("else if () {\n}\n")
        actions.key("up:2 left:3")

    def code_state_else():
        actions.insert("else\n{\n}\n")
        actions.key("up:2")

    def code_state_for():
        actions.auto_insert("for ")

    def code_state_while():
        actions.insert("while ()")
        actions.edit.left()

    ###
    # code_operator_bitwise
    ###
    def code_operator_bitwise_and():
        actions.auto_insert(" & ")

    def code_operator_bitwise_and_assignment():
        actions.auto_insert(" &= ")

    def code_operator_bitwise_or():
        actions.auto_insert(" | ")

    def code_operator_bitwise_or_assignment():
        actions.auto_insert(" |= ")

    def code_operator_bitwise_exclusive_or():
        actions.auto_insert(" ^ ")

    def code_operator_bitwise_exclusive_or_assignment():
        actions.auto_insert(" ^= ")

    def code_operator_bitwise_left_shift():
        actions.auto_insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.auto_insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.auto_insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.auto_insert(" >>= ")
