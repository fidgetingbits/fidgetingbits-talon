from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
and tag: user.python
"""
# spoken name -> snippet name
ultisnips_snippets = {
    "header": "#!",
    "if main": "ifmain",
    "for loop": "for",
    "class": "class",
    "function": "def",
    "method": "deff",
    "class method": "defc",
    "static method": "defs",
    "from": "from",
    "if": "if",
    "if else": "ife",
    "if if else": "ifee",
    "try": "try",
    "try except": "trye",
    "finally": "tryf",
    "trip string": '"',
    "trip tick": "'",
}

private_snippets = {
    "print success": "psuccess",
    "print fail": "pfail",
    "dick string": "dstr",
    "dick format string": "dfstr",
    "new arg parser": "argparse",
    "add argument": "narg",
    "dock param": "dockparam",
    "import cap stone": "capstone_import",
}

ctx.lists["user.snippets"] = {**ultisnips_snippets, **private_snippets}
