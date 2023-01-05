from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
and tag: user.bash

tag: user.vim_ultisnips
and tag: user.zsh
"""
# spoken name -> snippet name
ultisnips_snippets = {
    "header": "#!",
    "if": "if",
    "else if": "elif",
    "for loop": "four",
    "four in loop": "fourin",
    "while loop": "while",
    "until": "until",
    "switch": "switch",
}

private_snippets = {
    "if node exists": "ifnodeexists",
    "if not node exists": "ifnotnodeexists",
    "if file exists": "iffileexists",
    "if not file exists": "ifnotfileexists",
    "if folder exists": "iffolderexists",
    "if not folder exists": "ifnotfolderexists",
    "if variable set": "ifvarset",
    "if variable not set": "ifnotvarset",
    "if arg set": "ifargset",
    "if arg not set": "ifnotargset",
}

ctx.lists["user.snippets"] = {**ultisnips_snippets, **private_snippets}
