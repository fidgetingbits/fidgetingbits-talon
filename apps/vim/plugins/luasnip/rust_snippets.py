from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_luasnip
and tag: user.rust
"""
# spoken name -> snippet name
luasnip_snippets = {}

private_snippets = {
    # "print success": "psuccess",
    # "print fail": "pfail",
}

ctx.lists["user.snippets"] = {**luasnip_snippets, **private_snippets}
# print(ctx.lists["user.snippets"])
