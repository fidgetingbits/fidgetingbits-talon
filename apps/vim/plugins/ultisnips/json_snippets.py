from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
and tag: user.json
"""
# spoken name -> ultisnips snippet name
ultisnips_snippets = {
    "array": "a",
    "bool": "b",
    "named array": "na",
    "named object": "no",
    "null": "null",
    "number": "n",
    "object": "o",
    "string": "s",
}
private_snippets = {
    "dick string": "dstr",
}
ctx.lists["user.snippets"] = {**ultisnips_snippets, **private_snippets}
