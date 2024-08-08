import subprocess
import pprint
from talon import Module, Context, actions

mod = Module()
ctx = Context()
# `not tag user.readline` allows pinning a shell session temporarily to
# use readline. For instance if from zsh you ssh into a non-zsh-based shell, etc
ctx.matches = r"""
app: zsh
and not tag: user.readline
"""

custom_zle_functions = [
    # "indent-line",
    # "unindent-line",
]

builtin_zle_functions = [
    "accept-and-hold",
    "accept-line-and-down-history",
    "accept-line",
    "backward-char",
    "backward-delete-char",
    "backward-kill-line",
    "backward-kill-word",
    "backward-word",
    "beginning-of-buffer-or-history",
    "beginning-of-line",
    "bracketed-paste",
    "capitalize-word",
    "clear-screen",
    "copy-prev-shell-word",
    "copy-prev-word",
    "copy-region-as-kill",
    "delete-char-or-list",
    "delete-char",
    "digit-argument",
    "down-case-word",
    "down-line-or-beginning-search",
    "down-line-or-history",
    "edit-command-line",
    "end-of-buffer-or-history",
    "end-of-line",
    "exchange-point-and-mark",
    "execute-last-named-cmd",
    "execute-named-cmd",
    "expand-history",
    "expand-or-complete",
    "expand-word",
    "forward-char",
    "forward-word",
    "get-line",
    "insert-last-word",
    "kill-buffer",
    "kill-line",
    "kill-region",
    "kill-whole-line",
    "kill-word",
    "list-choices",
    "list-expand",
    "neg-argument",
    "overwrite-mode",
    "push-line",
    "quote-line",
    "quote-region",
    "quoted-insert",
    "redo",
    "self-insert-unmeta",
    "self-insert",
    "send-break",
    "set-mark-command",
    "spell-word",
    "transpose-chars",
    "transpose-words",
    "undo",
    "up-case-word",
    "up-line-or-beginning-search",
    "up-line-or-history",
    "vi-backward-blank-word",
    "vi-cmd-mode",
    "vi-find-next-char",
    "vi-forward-blank-word",
    "vi-goto-column",
    "vi-join",
    "vi-match-bracket",
    "what-cursor-position",
    "which-command",
    "yank-pop",
    "yank",
]

# This is everything from bindkey that is set, but missing everything that isn't set
# Need to trim down to the actual readline ones...
# zsh line editor: https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html
zle_keymap = {name: None for name in custom_zle_functions + builtin_zle_functions}


def _trigger_keys(entry):
    if entry in zle_keymap:
        print(f"{entry}: {zle_keymap[entry]}")
        for key in zle_keymap[entry]:
            print(f"key: {key}")
            actions.key(key)
    else:
        print(f"Unbound zle command: {entry}")
        actions.next()


# This almost definitley needs some Mac-specific switching
zsh_key_to_talon_map = {
    "^": "ctrl",
}

zle_command_ignore_list = [
    '"ls^J"',
]


def _read_zle_keymap():
    """Reads the output from `bindkey` and populates a map the keybindings.

    Note we use an interactive zsh shell to get the keybindings."""

    global zle_keymap

    # FIXME(zsh): I'm not entirely clear why I have to source this file still, better works
    output = subprocess.check_output(
        ("zsh", "-ic", "source ~/.config/zsh/.zshrc; bindkey")
    ).decode("utf-8")
    # print(output)
    for line in output.split("\n"):
        if not line.strip():
            continue
        bindkey, command = line.split(None, 1)
        # command = command.strip()

        # bindkey is something like this: "^[[A" up-line-or-beginning-search
        # We want to pass each to key() as "ctrl-[", "[", "A"
        keys = []
        # "ctrl-[A" -> ctrl-[A
        bindkeys = list(bindkey)[1:-1]
        # FIXME(zle): '"\M-^@"-"\M-^?" self-insert' seems broken

        # Skip anything too small to be a ctrl sequence
        if len(bindkeys) <= 1:
            continue
        i = 0
        while i < len(bindkeys):
            char = bindkeys[i]
            if char in zsh_key_to_talon_map:
                # ['^', 'A', ...] -> ['ctrl-a', ...]
                modifier = zsh_key_to_talon_map[char]
                key = bindkeys[i + 1].lower()
                keys.append(f"{modifier}-{key}")
                i += 1
            else:
                keys.append(char)
            i += 1

        if command in zle_keymap:
            if zle_keymap[command] is None:
                zle_keymap[command] = keys
        else:
            if command not in zle_command_ignore_list:
                # print(
                #     f"Unsupported zle command: ' {command} ', update zle_keymap in zsh_line_editor.py"
                # )
                pass
    # print(f"zle_keymap: {pprint.pformat(zle_keymap)}")


_read_zle_keymap()


@mod.action_class
class Actions:
    def zle_update_keymap():
        """Updates the zle keymap"""
        global zle_keymap
        old_zle_keymap = zle_keymap
        _read_zle_keymap()
        # print(f"zle_keymap: {pprint.pformat(zle_keymap)}")
        print("Added keybindings:")
        for key, value in zle_keymap.items():
            if key not in old_zle_keymap:
                print(f"{key}: {value}")
        print("Removed keybindings:")
        for key, value in old_zle_keymap.items():
            if key not in zle_keymap:
                print(f"{key}: {value}")


@ctx.action_class("edit")
class EditActions:
    ##
    # Movement - https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Movement
    ##
    def up():
        actions.key("up")

    def down():
        actions.key("down")

    def left():
        _trigger_keys("backward-char")

    def right():
        _trigger_keys("forward-char")

    def line_start():
        # This will skip to earlier lines if already at the start
        _trigger_keys("beginning-of-line")

    def line_end():
        # This will skip to following lines ifa lready at the end
        _trigger_keys("end-of-line")

    def word_left():
        actions.user.word_short_left()

    ##
    # Modifying Text - https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Modifying-Text
    ##
    def delete_word():
        actions.user.delete_word_short_right()

    def delete_line():
        _trigger_keys("kill-whole-line")

    # def indent_more():
    #     _trigger_keys("indent-line")

    # def indent_less():
    #     _trigger_keys("unindent-line")

    ##
    # Miscellaneous - https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Miscellaneous
    ##
    def undo():
        _trigger_keys("undo")

    def redo():
        _trigger_keys("redo")


@ctx.action_class("user")
class UserActions:
    ##
    # Modifying Text - https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Modifying-Text
    ##
    def delete_line_start():
        _trigger_keys("backward-kill-line")

    def delete_line_end():
        _trigger_keys("kill-line")

    def delete_word_short_right():
        _trigger_keys("kill-word")

    def delete_word_short_left():
        _trigger_keys("backward-kill-word")

    def delete_word_long_right():
        # There's no native zsh command for this, so we'll leverage marks
        _trigger_keys("set-mark-command")
        actions.user.word_long_right()
        _trigger_keys("kill-region")

    def delete_word_long_left():
        # There's no native zsh command for this, so we'll leverage marks
        _trigger_keys("set-mark-command")
        actions.user.word_long_left()
        _trigger_keys("kill-region")

    def join_lines():
        _trigger_keys("vi-join")

    ##
    # Movement - https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Movement
    ##

    def word_short_left():
        _trigger_keys("backward-word")

    def word_short_right():
        _trigger_keys("forward-word")

    def word_long_left():
        _trigger_keys("vi-backward-blank-word")

    def word_long_right():
        _trigger_keys("vi-forward-blank-word")

    def jump_cursor_to_next_char(char: str):
        _trigger_keys("vi-find-next-char")
        actions.key(char)

    def jump_cursor_to_prev_char(char: str):
        _trigger_keys("vi-find-prev-char")
        actions.key(char)

    def jump_cursor_to_matching_char():
        _trigger_keys("vi-match-bracket")

    ##
    # Miscellaneous - https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Miscellaneous
    ##
    def terminal_clear_screen():
        _trigger_keys("clear-screen")
