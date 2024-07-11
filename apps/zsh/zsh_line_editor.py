import subprocess
from talon import Context, actions

ctx = Context()
# We use a not tag user.readline to allow the user to pin a session temporarily to
# use readline. For instance if from zsh you ssh into a non-zsh-based shell, etc
ctx.matches = r"""
app: zsh
"""

# FIXME(zsh): This should just be a "bindkey" file, and then override various actions not just limited to readline..

# This is everything from bindkey that is set, but missing everything that isn't set
# Need to trim down to the actual readline ones...
# zsh line editor: https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html
readline_commands = {
    "_bash_complete-word": None,
    "_bash_list-choices": None,
    "_complete_debug": None,
    "_complete_help": None,
    "_complete_tag": None,
    "_correct_filename": None,
    "_correct_word": None,
    "_expand_alias": None,
    "_expand_word": None,
    "_history-complete-newer": None,
    "_history-complete-older": None,
    "_list_expansions": None,
    "_most_recent_file": None,
    "_next_tags": None,
    "_read_comp": None,
    "accept-and-hold": None,
    "accept-line-and-down-history": None,
    "accept-line": None,
    "atuin-up-search": None,
    "backward-char": None,
    "backward-delete-char": None,
    "backward-kill-word": None,
    "backward-word": None,
    "beginning-of-buffer-or-history": None,
    "beginning-of-line": None,
    "bracketed-paste": None,
    "capitalize-word": None,
    "clear-screen": None,
    "copy-prev-shell-word": None,
    "copy-prev-word": None,
    "copy-region-as-kill": None,
    "delete-char-or-list": None,
    "delete-char": None,
    "digit-argument": None,
    "down-case-word": None,
    "down-line-or-beginning-search": None,
    "down-line-or-history": None,
    "edit-command-line": None,
    "end-of-buffer-or-history": None,
    "end-of-line": None,
    "exchange-point-and-mark": None,
    "execute-last-named-cmd": None,
    "execute-named-cmd": None,
    "expand-history": None,
    "expand-or-complete": None,
    "expand-word": None,
    "forward-char": None,
    "forward-word": None,
    "get-line": None,
    "history-incremental-search-backward": None,
    "history-incremental-search-forward": None,
    "history-search-backward": None,
    "history-search-forward": None,
    "infer-next-history": None,
    "insert-last-word": None,
    "kill-buffer": None,
    "kill-line": None,
    "kill-region": None,
    "kill-whole-line": None,
    "kill-word": None,
    "list-choices": None,
    "list-expand": None,
    "neg-argument": None,
    "overwrite-mode": None,
    "push-line": None,
    "quote-line": None,
    "quote-region": None,
    "quoted-insert": None,
    "reverse-menu-complete": None,
    "run-help": None,
    "self-insert-unmeta": None,
    "self-insert": None,
    "send-break": None,
    "set-mark-command": None,
    "spell-word": None,
    "transpose-chars": None,
    "transpose-words": None,
    "undo": None,
    "up-case-word": None,
    "up-line-or-beginning-search": None,
    "up-line-or-history": None,
    "vi-cmd-mode": None,
    "vi-find-next-char": None,
    "vi-goto-column": None,
    "vi-join": None,
    "vi-match-bracket": None,
    "what-cursor-position": None,
    "which-command": None,
    "yank-pop": None,
    "yank": None,
}


def _trigger_keys(entry):
    if entry in readline_commands:
        print(f"{entry}: {readline_commands[entry]}")
        for key in readline_commands[entry]:
            print(f"key: {key}")
            actions.key(key)
    else:
        print(f"Unbound readline command: {entry}")
        actions.next()


# This almost definitley needs some Mac-specific switching
zsh_key_to_talon_map = {
    "^": "ctrl",
}

output = subprocess.check_output(("zsh", "-c", "bindkey")).decode("utf-8")

for line in output.split("\n"):
    if not line.strip():
        continue

    bindkey, command = line.split(None, 1)
    command = command.strip()

    # bindkey is something like this: "^[[A" up-line-or-beginning-search
    # We want to pass each to key() as "ctrl-[", "[", "A"
    keys = []
    bindkeys = list(bindkey)[1:-1]
    i = 0
    # print(f"bindkeys: {bindkeys}")
    # "^[ " expand-history breaks this
    if len(bindkeys) == 1 and bindkeys[0] == "^":
        continue
    while i < len(bindkeys):
        char = bindkeys[i]
        if char in zsh_key_to_talon_map:
            keys.append(f"{zsh_key_to_talon_map[char]}-{bindkeys[i+1]}")
            i += 1
        else:
            keys.append(char)
        i += 1
    # print(f"keys: {keys}")
    if command in readline_commands:
        readline_commands[command] = keys

# "\M-^@"-"\M-^?" self-insert breaks shit as well
# print(readline_commands)


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

    def word_left():
        _trigger_keys("backward-word")

    def word_right():
        _trigger_keys("forward-word")

    def line_start():
        # This will skip to earlier lines if already at the start
        _trigger_keys("beginning-of-line")

    def line_end():
        # This will skip to following lines ifa lready at the end
        _trigger_keys("end-of-line")

    ##
    # Modifying Text - https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Modifying-Text
    ##
    def delete_line():
        # WARNING: This should be kill-whole-line, but the default is ctrl-shift-u, which depending on your window
        # manager may be overridden by default. For instance, on GNOME, this is the unicode hotkey:
        # ❯ gsettings list-recursively | grep 'unicode-hotkey'
        # org.freedesktop.ibus.panel.emoji unicode-hotkey ['<Control><Shift>u']
        # So we just combo it
        actions.edit.line_start()
        actions.user.delete_line_end()

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

    def delete_word_right():
        _trigger_keys("delete-word")

    def delete_word_left():
        _trigger_keys("backward-delete-word")

    ##
    # Movement - https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Movement
    ##

    def word_left_long():
        _trigger_keys("vi-backward-blank-word")

    def word_right_long():
        _trigger_keys("vi-forward-blank-word")

    def jump_cursor_to_next_char(key: str):
        _trigger_keys("vi-find-next-char")
        actions.key(key)

    def jump_cursor_to_prev_char(key: str):
        _trigger_keys("vi-find-prev-char")
        actions.key(key)

    ##
    # Miscellaneous - https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Miscellaneous
    ##
    def terminal_clear_screen():
        _trigger_keys("clear-screen")
