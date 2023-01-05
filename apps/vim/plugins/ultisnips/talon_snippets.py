from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
and tag: user.talon
"""
# spoken name -> snippet name
ultisnips_snippets = {}

private_snippets = {
    "talon file": "tf",
    "insert": "tsi",
    "big insert": "tmi",
    "key": "tk",
    "snippet": "tsnip",
    "heading": "tcom",
    "settings": "tset",
}

ctx.lists["user.snippets"] = {**ultisnips_snippets, **private_snippets}
