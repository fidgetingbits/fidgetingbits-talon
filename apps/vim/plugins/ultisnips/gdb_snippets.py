from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
and tag: user.gdb
"""
# spoken name -> snippet name
ultisnips_snippets = {}

private_snippets = {
    "new big break": "bigbr",
    "commands": "brcommands",
}

ctx.lists["user.snippets"] = {**ultisnips_snippets, **private_snippets}
