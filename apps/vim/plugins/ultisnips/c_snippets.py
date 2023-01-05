from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
and tag: user.c
"""


# these snippets are from vim-snippets/UltiSnips/c.snippets
ultisnips_snippets = {
    "define": "def",
    "if not define": "#ifndef:",
    "main": "main",
    "for loop": "for",
    "for eye loop": "fori",
    "else if": "eli",
    "print": "printf",
    "struct": "st",
    "function": "fun",
    "function declaration": "fund",
    "file header": "head",
    "function header": "func",
}

# these snippets are from your personal snippet file
private_snippets = {
    "print status": "printfs",
    "print fail": "printff",
    "exit success": "exits",
    "exit failure": "exitf",
    "dock fun": "doxyb",
    "dock var": "doxyv",
    "dock in": "doxypi",
    "dock out": "doxypo",
    "dock in out": "doxypio",
    "main": "main",
    "unshare": "unshare",
    "N F T headers": "nft_headers",
}

ctx.lists["user.snippets"] = {**ultisnips_snippets, **private_snippets}
