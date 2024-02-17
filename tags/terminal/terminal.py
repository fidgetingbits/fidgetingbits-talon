# NOTE: If you use bindkeys -e setting in your shell (the default) also see
# text/readline.py

from talon import Context, Module, actions, settings

mod = Module()
mod.list("environment_variables", "Common environment variables")
mod.setting(
    "terminal_app",
    type=str,
    default="alacritty",
    desc="The terminal app to spawn in various places",
)


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

    def terminal_default_app() -> str:
        """Returns the default terminal app"""
        return settings.get("user.terminal_app")


linux_ctx = Context()
linux_ctx.matches = r"""
os: linux
tag: terminal
"""

mac_ctx = Context()
mac_ctx.matches = r"""
os: mac
tag: terminal
"""

common_variables = {
    "home": "HOME",
    "user": "USER",
    "path": "PATH",
    "desktop": "DESKTOP",
    "tunnel auth sock": "SSH_AUTH_SOCK",
    "editor": "EDITOR",
    "shell": "SHELL",
    "nix profiles": "NIX_PROFILES",
    "L S colors": "LS_COLORS",
}
linux_variables = {
    "config": "XDG_CONFIG_HOME",
    "cache": "XDG_CACHE_HOME",
    "runtime": "XDG_RUNTIME_DIR",
    "session type": "XDG_SESSION_TYPE",
}
mac_variables = {}

linux_ctx.lists["user.environment_variables"] = {
    **common_variables,
    **linux_variables,
}
mac_ctx.lists["user.environment_variables"] = {
    **common_variables,
    **mac_variables,
}


@linux_ctx.action_class("edit")
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


@linux_ctx.action_class("app")
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
