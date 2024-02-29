from talon import Context, Module

mod = Module()
mod.list("lua_structs", desc="List of known lua structs")
ctx = Context()

# FIXME: This should be strict for a lua thing
ctx.matches = r"""
app: gdb
"""

# FIXME: This should be a generic list of types known to gdb, that we can extend by
# a language thing.
ctx.lists["user.lua_structs"] = {
    "state": "lua_State",
    "value": "TValue",
    "string": "TString",
    "table": "Table",
    "C funk": "CClosure",
    "lua funk": "LClosure",
}
