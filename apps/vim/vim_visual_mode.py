from talon import Context, actions, clip

ctx = Context()
ctx.matches = r"""
win.title: /VIM MODE:v/
win.title: /VIM MODE:V/
"""
ctx.tags = ["user.vim_visual_mode"]

@ctx.action_class("edit")
class EditActions:

    # when we're extending a selection in the opposite direction (backwards) we
    # need to a prefix an o beforehand so that it actually extends, rather than
    # changing directions.
    def extend_line_up():
        actions.user.insert("ok^o")

    def extend_line_down():
        actions.user.insert("j^")

    def extend_left():
        actions.user.insert("oho")

    def extend_right():
        actions.user.insert("l")

    def extend_word_left():
        actions.user.insert("obo")

    def extend_word_right():
        actions.user.insert("e")

    def select_word():
        actions.user.insert("e")

    def extend_line_start():
        actions.user.insert("o^o")

    def extend_line_end():
        actions.user.insert("$")

    def extend_file_start():
        actions.user.insert("ogg0o")

    def extend_file_end():
        actions.insert("G")
        # XXX - This should be a callable function so we can do things like:
        #       '.swap on this <highlight motion>'
        #       'swap between line x, y'
        # assumes visual mode

    def selected_text():
        # gv to reselect
        actions.insert("ygv")
        return clip.get()

    def indent_more():
        actions.user.insert(">")

    def indent_less():
        actions.user.insert("<")

    def delete_line():
        actions.user.insert("D")

