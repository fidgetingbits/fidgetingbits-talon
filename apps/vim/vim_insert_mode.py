from talon import Context, actions

ctx = Context()
ctx.matches = r"""
win.title: /VIM MODE:i/
"""
ctx.tags = ["user.vim_insert_mode"]


@ctx.action_class("edit")
class EditActions:
    def delete_line():
        actions.user.vim_normal_mode("dd")
