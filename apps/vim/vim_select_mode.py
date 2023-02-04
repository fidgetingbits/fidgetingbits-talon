from talon import Context, actions

ctx = Context()
ctx.matches = r"""
win.title: /VIM MODE:s/
"""
ctx.tags = ["user.vim_select_mode"]
