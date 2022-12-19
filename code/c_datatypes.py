from talon import Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: disabled
"""
# mode: command
# and code.language: c
#
# mode: command
# and tag: user.gdb
# """

ctx.lists["self.c_pointers"] = {
    "pointer": "*",
    "pointer to pointer": "**",
}

ctx.lists["self.c_signed"] = {
    "signed": "signed",
    "unsigned": "unsigned",
}

# ctx.lists["self.c_types"] = {
#    "character": "char",
#    "char": "char",
#    "short": "short",
#    "long": "long",
#    "int": "int",
#    "integer": "int",
#    "void": "void",
#    "double": "double",
#    "struct": "struct",
# }

mod.list("c_pointers", desc="Common C pointers")
mod.list("c_signed", desc="Common C datatype signed modifiers")
mod.list("c_types", desc="Common C types")


@mod.capture(rule="{self.c_pointers}")
def c_pointers(m) -> str:
    "Return a pointer symbol"
    return m.c_pointers


@mod.capture(rule="{self.c_signed}")
def c_signed(m) -> str:
    "Return a signed or unsigned symbol"
    return m.c_signed


@mod.capture(rule="{self.c_types}")
def c_types(m) -> str:
    "Return a C datatype symbol"
    return m.c_types


@mod.capture(rule="[<self.c_signed>] <self.c_types> [<self.c_pointers>+]")
def datatype(m) -> str:
    "Return a C declaration string matching a datatype"
    return "(" + " ".join(list(m)) + ")"
