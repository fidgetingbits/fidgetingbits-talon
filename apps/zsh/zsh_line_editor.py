import subprocess
from talon import Context, actions

ctx = Context()
# We use a not tag user.readline to allow the user to pin a session temporarily to
# use readline. For instance if from zsh you ssh into a non-zsh-based shell, etc
ctx.matches = r"""
tag: zsh
not tag: user.readline
"""

# FIXME(zsh): This should just be a "bindkey" file, and then override various actions not just limited to readline..

# This is everything from bindkey that is set, but missing everything that isn't set
# Need to trim down to the actual readline ones...
# zsh line editor: https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html
readline_commands = {
    "set-mark-command": None,
    "beginning-of-line": None,
    "backward-char": None,
    "delete-char-or-list": None,
    "end-of-line": None,
    "forward-char": None,
    "send-break": None,
    "backward-delete-char": None,
    "expand-or-complete": None,
    "accept-line": None,
    "kill-line": None,
    "clear-screen": None,
    "accept-line": None,
    "down-line-or-history": None,
    "accept-line-and-down-history": None,
    "up-line-or-history": None,
    "push-line": None,
    "history-incremental-search-forward": None,
    "transpose-chars": None,
    "kill-whole-line": None,
    "quoted-insert": None,
    "backward-kill-word": None,
    "vi-match-bracket": None,
    "edit-command-line": None,
    "vi-find-next-char": None,
    "vi-join": None,
    "kill-buffer": None,
    "infer-next-history": None,
    "overwrite-mode": None,
    "_read_comp": None,
    "undo": None,
    "vi-cmd-mode": None,
    "exchange-point-and-mark": None,
    "expand-word": None,
    "what-cursor-position": None,
    "_complete_debug": None,
    "_correct_filename": None,
    "list-expand": None,
    "_expand_alias": None,
    "_correct_word": None,
    "_list_expansions": None,
    "_expand_word": None,
    "list-expand": None,
    "_complete_help": None,
    "_most_recent_file": None,
    "_next_tags": None,
    "history-incremental-search-backward": None,
    "history-incremental-search-forward": None,
    "_complete_tag": None,
    "undo": None,
    "_bash_list-choices": None,
    "yank": None,
    "list-choices": None,
    "send-break": None,
    "backward-kill-word": None,
    "self-insert-unmeta": None,
    "clear-screen": None,
    "self-insert-unmeta": None,
    "copy-prev-word": None,
    "expand-history": None,
    "quote-region": None,
    "spell-word": None,
    "quote-line": None,
    "_history-complete-newer": None,
    "neg-argument": None,
    "insert-last-word": None,
    "_history-complete-older": None,
    "digit-argument": None,
    "delete-char": None,
    "beginning-of-buffer-or-history": None,
    "end-of-buffer-or-history": None,
    "which-command": None,
    "accept-and-hold": None,
    "backward-word": None,
    "capitalize-word": None,
    "kill-word": None,
    "forward-word": None,
    "get-line": None,
    "run-help": None,
    "down-case-word": None,
    "history-search-forward": None,
    "up-line-or-beginning-search": None,
    "atuin-up-search": None,
    "forward-char": None,
    "backward-char": None,
    "end-of-line": None,
    "beginning-of-line": None,
    "history-search-backward": None,
    "push-line": None,
    "spell-word": None,
    "transpose-words": None,
    "up-case-word": None,
    "copy-region-as-kill": None,
    "forward-word": None,
    "backward-word": None,
    "bracketed-paste": None,
    "overwrite-mode": None,
    "kill-word": None,
    "delete-char": None,
    "up-line-or-history": None,
    "down-line-or-history": None,
    "up-line-or-beginning-search": None,
    "down-line-or-beginning-search": None,
    "forward-char": None,
    "backward-char": None,
    "reverse-menu-complete": None,
    "insert-last-word": None,
    "accept-and-hold": None,
    "backward-word": None,
    "capitalize-word": None,
    "kill-word": None,
    "forward-word": None,
    "get-line": None,
    "run-help": None,
    "copy-prev-shell-word": None,
    "history-search-forward": None,
    "history-search-backward": None,
    "push-line": None,
    "spell-word": None,
    "transpose-words": None,
    "up-case-word": None,
    "kill-region": None,
    "execute-named-cmd": None,
    "yank-pop": None,
    "execute-last-named-cmd": None,
    "vi-goto-column": None,
    "_bash_complete-word": None,
    "backward-kill-word": None,
    "undo": None,
    "self-insert": None,
    "backward-delete-char": None,
}

def _trigger_keys(entry):
    if entry in readline_commands:
        for key in readline_commands[entry]:
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
    print(f"bindkeys: {bindkeys}")
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
    print(f"keys: {keys}")
    if command in readline_commands:
        readline_commands[command] = keys

# "\M-^@"-"\M-^?" self-insert breaks shit as well
print(readline_commands)

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
        _trigger_keys("kill-whole-line")

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
        _trigger_keys("vi-backward-blank-word"):

    def word_right_long():
        _trigger_keys("vi-forward-blank-word"):

    def jump_cursor_to_next_char():
        _trigger_keys("vi-find-next-char")

    def jump_cursor_to_prev_char():
        _trigger_keys("vi-find-prev-char")

    ##
    # Miscellaneous - https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Miscellaneous
    ##
    def terminal_clear_screen():
        _trigger_keys("clear-screen")
