from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_luasnip
and tag: user.python
"""
# spoken name -> snippet name
luasnip_snippets = {}

private_snippets = {
    # "print success": "psuccess",
    # "print fail": "pfail",
    "dick string": "dstr",
    "dick format string": "dfstr",
    # "new arg parser": "argparse"
    # "add argument": "narg",
    # "dock param": "dockparam",
    # "import cap stone": "capstone_import",
}

ctx.lists["user.snippets"] = {**luasnip_snippets, **private_snippets}
# print(ctx.lists["user.snippets"])
