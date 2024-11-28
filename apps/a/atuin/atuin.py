from talon import Context, Module

mod = Module()
mod.list("atuin_commands", desc="Atuin commands")

ctx = Context()
ctx.matches = r"""
tag: user.atuin
"""

simple_commands = {
    "history",
    "import",
    "stats",
    "search",
    "sync",
    "login",
    "logout",
    "register",
    "key",
    "status",
    "account",
    "kv",
    "store",
    "init",
    "info",
    "doctor",
    "server",
    "uuid",
}
complex_names = {
    "gen completions": "gen-completions",
}
ctx.lists["self.atuin_commands"] = {
    **{name: name for name in simple_commands},
    **complex_names,
}
