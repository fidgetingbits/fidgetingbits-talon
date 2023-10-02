# This fowl contains editing actions that are only enabled in some sort of
# motion mode, so not including terminal or command line mode. To see the
# additional edit action overrides that are available in terminal, see
# vim_editing.py


from talon import Context, actions

ctx = Context()
ctx.matches = r"""
app:vim
not tag: user.vim_terminal
and not tag: user.vim_command_mode
"""


@ctx.action_class("edit")
class EditActions:
    def save():
        actions.user.vim_command_mode(":w\n")

    def find_next():
        actions.user.vim_any_motion_mode_key("n")

    def word_left():
        actions.user.vim_any_motion_mode_key("b")

    def word_right():
        actions.user.vim_any_motion_mode_key("w")

    def line_start():
        actions.user.vim_any_motion_mode_key("^")

    def line_end():
        actions.user.vim_any_motion_mode_key("$")

    def file_end():
        actions.user.vim_any_motion_mode_key("G")

    def file_start():
        actions.user.vim_any_motion_mode("gg")

    def extend_line_up():
        actions.user.vim_visual_mode("k^")

    def extend_line_down():
        actions.user.vim_visual_mode("j^")

    def extend_left():
        actions.user.vim_visual_mode("h")

    def extend_right():
        actions.user.vim_visual_mode("l")

    def extend_word_left():
        actions.user.vim_visual_mode("b")

    def extend_word_right():
        actions.user.vim_visual_mode("e")

    def select_word():
        actions.user.vim_visual_mode("e")

    def extend_line_start():
        actions.user.vim_visual_mode("^")

    def extend_line_end():
        actions.user.vim_visual_mode("$")

    def extend_file_start():
        actions.user.vim_visual_mode("gg0")

    def extend_file_end():
        actions.user.vim_visual_mode("G")

    def select_line(n: int = None):
        actions.user.vim_visual_mode("V")

    def select_all():
        actions.user.vim_normal_mode("ggVG")
        # See vim_normal.talon and vim_visual.talon for edit.extend_ commands

    def delete_word():
        actions.user.vim_normal_mode("dw")

    def delete():
        actions.user.vim_insert_mode_key("backspace")

    def redo():
        actions.user.vim_normal_mode_key("ctrl-r")

    def undo():
        actions.user.vim_normal_mode_key("u")

    # Note following two are for mouse/highlighted copy/paste. shouldn't be
    # used for actual vim commands

    def copy():
        actions.key("ctrl-shift-c")

    def paste():
        # actions.user.vim_normal_mode("p")
        actions.key("ctrl-shift-v")
        # NOTE: There is it delay that happens inside of vim that can cause out
        # of order key pressing, in it seems to be that it's because the output
        # of this key press actually happens after other key presses start
        # getting interpreted? in example would be "sit graves pasty round".
        # typically the output of this will be something like:
        # `(<pasted content>)`
        # but the intended output would be
        # `<pasted content>()`
        # for now the only way i see to fix this is to introduce an artificial
        # delay to allow vim to actually paste the content...
        # time.sleep(0.800)
        #  XXX - This might be one solution for it, but i haven't got it to
        #  work yet
        # actions.user.vim_normal_mode('"+p')


@ctx.action_class("user")
class UserActions:
    def delete_word_right():
        actions.user.vim_normal_mode("dw")

    def delete_word_left():
        actions.user.vim_normal_mode("db")

    def delete_line_remaining():
        actions.user.vim_normal_mode("d$")

    def delete_line_beginning():
        actions.user.vim_normal_mode("d0")

    def line_find_forward(key: str):
        # print(key)
        actions.user.vim_any_motion_mode(f"f{key}")

    def line_find_backward(key: str):
        actions.user.vim_any_motion_mode(f"F{key}")
