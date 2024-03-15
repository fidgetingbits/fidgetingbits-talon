import time

from talon import Context, Module, actions

# App definition
mod = Module()
mod.apps.gnome_terminal = """
os: linux
and app.exe: gnome-terminal-server
os: linux
and app.name: Gnome-terminal
os: linux
and app.name: kgx
os: linux
and app.name: Mate-terminal
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: gnome_terminal
"""


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.tabs
    def tab_jump(number):
        actions.key(f"alt-{number}")

    def tabs_show():
        actions.key("ctrl-shift-o")

    def page_find():
        actions.key("ctrl-shift-f")

    def page_find_next():
        actions.key("ctrl-shift-g")

    def page_find_previous():
        actions.key("ctrl-shift-h")


@ctx.action_class("app")
class AppActions:
    # app.tabs
    def tab_open():
        actions.key("ctrl-shift-t")

    def tab_previous():
        actions.key("ctrl-pageup")

    def tab_next():
        actions.key("ctrl-pagedown")

    def tab_close():
        actions.key("ctrl-shift-w")

    # global (overwrite linux/app.py)
    def window_open():
        actions.key("ctrl-shift-n")


# global (overwrite linux/edit.py)
@ctx.action_class("edit")
class EditActions:
    def page_down():
        actions.key("shift-pagedown")

    def page_up():
        actions.key("shift-pageup")

    def paste():
        actions.key("ctrl-shift-v")
        # FIXME: on oedo the paste is super slow for some reason, so without this
        # talon starts inserting before the paste is actually done
        # Should make this type of thing configurable in a setting
        # if I'm gonna have to keep it
        # KILL ME: this is still not long enough sometimes
        time.sleep(1)

    def copy():
        actions.key("ctrl-shift-c")

    def find(text: str = None):
        actions.key("ctrl-shift-f")
        if text:
            actions.insert(text)

    def delete_line():
        actions.edit.line_start()
        actions.key("ctrl-k")

    # afaik not possible in gnome-terminal
    def extend_left():
        pass

    def extend_right():
        pass

    def extend_up():
        pass

    def extend_down():
        pass

    def extend_word_left():
        pass

    def extend_word_right():
        pass
