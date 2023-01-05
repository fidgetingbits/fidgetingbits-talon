from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
and tag: user.cmake
"""
# spoken name -> ultisnips snippet name
ctx.lists["user.snippets"] = {}
