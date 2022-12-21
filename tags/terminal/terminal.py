# NOTE: If you use bindkeys -e setting in your shell (the default) also see
# text/readline.py

from talon import Module, Context, actions

mod = Module()

@mod.action_class
class Actions:
    def terminal_list_directories():
        """Lists directories"""

    def terminal_list_all_directories():
        """Lists all directories including hidden"""

    def terminal_change_directory(path: str):
        """Lists change directory"""

    def terminal_change_directory_root():
        """Root of current drive"""

    def terminal_clear_screen():
        """Clear screen"""

    def terminal_run_last():
        """Repeats the last command"""

    def terminal_rerun_search(command: str):
        """Searches through the previously executed commands"""

    def terminal_kill_all():
        """kills the running command"""



ctx = Context()
ctx.matches = r"""
os: linux
tag: terminal
"""

@ctx.action_class("edit")
class EditActions:
    # todo: generic tab commands
    # tag(): tabs
    def page_down():
        actions.key("shift-pagedown")

    def page_up():
        actions.key("shift-pageup")

    def paste():
        actions.key("ctrl-shift-v")

    def copy():
        actions.key("ctrl-shift-c")

    def find(text: str = None):
        actions.key("ctrl-shift-f")


@ctx.action_class("app")
class AppActions:
    def tab_open():
        actions.key("ctrl-shift-t")

    def tab_close():
        actions.key("ctrl-shift-w")

    def tab_next():
        actions.key("ctrl-pagedown")

    def tab_previous():
        actions.key("ctrl-pageup")

    def window_open():
        actions.key("ctrl-shift-n")
