from talon import Context, actions

ctx = Context()
ctx.matches = r"""
win.title: /VIM MODE:n/
"""
ctx.tags = ["user.vim_normal_mode"]


@ctx.action_class("edit")
class EditActions:
    # These differ slightly if we're in normal mode versus visual mode. in normal
    # mode we select up we want to select the current line in the one above, as
    # otherwise there is no current selection
    def extend_line_up():
        actions.insert("Vk")

    def extend_line_down():
        actions.insert("Vj")

    def indent_more():
        actions.insert(">>")

    def indent_less():
        actions.insert("<<")

    def delete_line():
        actions.insert("dd")
