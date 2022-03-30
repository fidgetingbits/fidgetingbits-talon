from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
mode: user.lua
mode: command
and code.language: lua
"""
# spoken name -> ultisnips snippet name
# spoken name -> snippet name
ultisnips_snippets = {}

private_snippets = {
    "dump table": "dumpt",
}

ctx.lists["user.snippets"] = {**ultisnips_snippets, **private_snippets}
