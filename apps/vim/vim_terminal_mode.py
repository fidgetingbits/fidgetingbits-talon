import re
from talon import Context, Module, actions, settings, ui

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: user.vim_terminal
"""


@ctx.action_class("edit")
class EditActions:
    def page_up():
        actions.key("ctrl-\\ ctrl-n ctrl-b")

    # XXX - this might be a bit much if eventually we want this to mean to let
    # everything on the command-line itself, although then we might be able to
    # just use things like select line/graph, etc
    def select_all():
        actions.user.vim_normal_mode_exterm("ggVG")

    def paste():
        actions.key("ctrl-shift-v")


@mod.action_class
class Actions:
    def vim_set_normal_mode():
        """set normal mode"""
        v = VimMode()
        v.set_normal_mode(auto=False)


def parse_vim_term_title(window):
    """a variety of parsing to gracefully handle various shell commands
    running inside of a vim terminal.
    :returns: TODO

    """

    if (
        window != ui.active_window()
        or not window.title.startswith("VIM MODE:t")
        or "TERM:" not in window.title
    ):
        return

    # pull a TERM: line out of something potentially like
    # VIM MODE:t RPC:/tmp/nvimlVeccr/0  TERM:gdb (term://~//161917:/usr/bin/zsh) zsh
    index = window.title.find("TERM:")
    shell_command = window.title[index + len("TERM:") :]
    if ":" in shell_command:
        shell_command = shell_command.split(":")[0]
    if shell_command.startswith("sudo"):
        # Handle something like:
        # VIM MODE:t RPC:/tmp/nvimlVeccr/0  TERM:sudo gdb (term://~//161917:/usr/bin/zsh) zsh
        shell_command = shell_command.split(" ")[1]
    else:
        shell_command = shell_command.split(" ")[0]

    populate_shell_tags(shell_command, window.title)
    populate_language_modes(shell_command)


def populate_language_modes(shell_command):
    """TODO: Docstring for populate_language_modes.

    :shell_command: TODO
    :returns: TODO

    """
    language_specific_commands = {
        "repl": "python",
    }

    for command in language_specific_commands.keys():
        if shell_command.endswith(command):
            actions.user.code_set_context_language(language_specific_commands[command])
            return

    # XXX - sometimes this throws an exception saying it's not declared, but it
    # should be a global module action from code.py
    actions.user.code_clear_context_language()
    return


def populate_shell_tags(shell_command, window_title):
    """TODO: Docstring for populate_shell_tags.
    :returns: TODO

    """
    # XXX - this should have eventually become a list of possible tags to
    # set?
    shell_tags = {
        "zsh": "terminal",
        "bash": "terminal",
        "sh": "terminal",
        "ssh": "terminal",
        "sudo": "terminal",
        "gdb": "user.gdb",
        "pwndbg": ["user.gdb", "user.pwndbg"],
        "gef": ["user.gdb", "user.gef"],
        "htop": "user.htop",
        "taskwarrior-tui": "user.taskwarrior_tui",
        "~/.talon/bin/repl": "user.talon_repl",
    }
    # XXX - there's probably a better way to deal with this
    fuzzy_shell_tags = {
        # Match on stuff like fzf running in floating term
        # "term://": "user.readline",
        "root@": "terminal",  # hacky match for docker containers
    }
    regex_shell_tags = {
        r"^\w*@\w*": "terminal",
        r"^\w*@\w*:.*[$#]": "terminal",  # this is redundant with above, but ideally I would rather have something like this
        ".*virsh start --console.*": "terminal",  # hacky match for libvirt containers
    }
    if shell_command in shell_tags:
        if isinstance(shell_tags[shell_command], list):
            ctx.tags = shell_tags[shell_command]
            print(ctx.tags)
        else:
            ctx.tags = [shell_tags[shell_command]]
    else:
        found_fuzzy = False
        for tag in fuzzy_shell_tags:
            if shell_command.startswith(tag):

                ctx.tags = [fuzzy_shell_tags[tag]]
                found_fuzzy = True
                break

        for expression in regex_shell_tags:
            m = re.match(expression, shell_command)
            if m is not None:
                ctx.tags = [regex_shell_tags[expression]]
                break
            m = re.match(expression, window_title)
            if m is not None:
                ctx.tags = [regex_shell_tags[expression]]
                break
#        if not found_fuzzy:
#            print(f"WARNING: missing tag for shell cmd: {shell_command}")
#            print(f"WARNING: consider updating vim_terminal.py: {shell_command}")
#

ui.register("win_title", parse_vim_term_title)
ui.register("win_focus", parse_vim_term_title)
