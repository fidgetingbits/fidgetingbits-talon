from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
mode: user.gdb
mode: command
and code.language: gdb
"""
# spoken name -> snippet name
ultisnips_snippets = {}

private_snippets = {
    "new big break": "bigbr",
    "commands": "brcommands",
}

ctx.lists["user.snippets"] = {**ultisnips_snippets, **private_snippets}
