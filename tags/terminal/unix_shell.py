from talon import Context, Module, actions

mod = Module()

unix_ctx = Context()
unix_ctx.matches = r"""
os: linux
and tag: terminal
os: mac
and tag: terminal
"""

linux_environment_variables = {}
mac_environment_variables = {}
common_environment_variables = {
    "home": "HOME",
    "temp": "TMPDIR",
    "path": "PATH",
    "shell": "SHELL",
    "user": "USER",
    "username": "USERNAME",
    "host": "HOSTNAME",
    "editor": "EDITOR",
    "visual": "VISUAL",
    "term": "TERM",
    "working directory": "PWD",
    # nix
    "nix path": "NIX_PATH",
    "nix profiles": "NIX_PROFILES",
    # git
    "git editor": "GIT_EDITOR",
}
unix_ctx.lists["user.environment_variables"] = {
    **linux_environment_variables,
    **mac_environment_variables,
    **common_environment_variables,
}

ctx = Context()
ctx.matches = r"""
tag: user.generic_unix_shell
"""

# Uncomment the following line to enable common unix utilities from unix_utilities.py
# ctx.tags = ["user.unix_utilities"]


@ctx.action_class("user")
class Actions:
    # Implements the functions from terminal.py for unix shells

    def terminal_list_directories():
        """Lists directories"""
        actions.insert("ls -l")
        actions.key("enter")

    def terminal_list_all_directories():
        """Lists all directories including hidden"""
        actions.insert("ls -la")
        actions.key("enter")

    def terminal_change_directory(path: str):
        """Lists change directory"""
        actions.insert(f"cd {path}")
        if path:
            actions.key("enter")

    def terminal_change_directory_root():
        """Root of current drive"""
        actions.insert("cd /")
        actions.key("enter")

    def terminal_clear_screen():
        """Clear screen"""
        actions.insert("clear")
        actions.key("enter")

    def terminal_run_last():
        """Repeats the last command"""
        actions.key("up enter")

    def terminal_rerun_search(command: str):
        """Searches through the previously executed commands"""
        actions.key("ctrl-r")
        actions.insert(command)

    def terminal_kill_all():
        """kills the running command"""
        actions.key("ctrl-c")
        actions.insert("y")
        actions.key("enter")
