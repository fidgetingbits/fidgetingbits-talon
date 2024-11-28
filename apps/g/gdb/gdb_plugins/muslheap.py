from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
tag: user.muslheap
"""


mod = Module()
mod.list("mallocng_structs", desc="List of known musl next gen malloc structs")

# FIXME: This should be a generic list of types known to gdb, that we can extend by
# a language thing
ctx.lists["user.mallocng_structs"] = {
    "meta": "struct meta",
    "group": "struct mgroup",  # FIXME: This is my own symbol due to gdb confusion
    "context": "struct malloc_context",
}


@ctx.action_class("user")
class UserActions:
    def heap_analysis_chunk():
        actions.auto_insert("mchunkinfo ")
