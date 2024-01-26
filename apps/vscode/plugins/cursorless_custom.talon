tag: user.cursorless
-

# Command to repeat the last action on a new target
# proper approach is to implement https://github.com/cursorless-dev/cursorless/issues/455
# hacky way as long as you didn't provide targets, and only used "this"
# in the original command, e.g. "pre air", "format title at this", "also bat"
also <user.cursorless_target>:
    prev_command = user.history_get(1)
    user.cursorless_command("setSelectionBefore", cursorless_target)
    user.engine_mimic(prev_command)

<user.formatters> {user.cursorless_reformat_action} <user.cursorless_target>:
    user.private_cursorless_reformat(cursorless_target, formatters)

# chomp air: abcd -> abc
chomp <user.cursorless_target>:
    user.cursorless_command("setSelectionAfter", cursorless_target)
    edit.delete()

# bully air: <foo>a</foo> -> <foo> a </foo>
bully <user.cursorless_target>:
    user.cursorless_command("setSelectionAfter", cursorless_target)
    key(space)
    user.cursorless_command("setSelectionBefore", cursorless_target)
    key(space)

# tug air: <foo>a -> <foo> a
tug <user.cursorless_target>:
    user.cursorless_command("setSelectionBefore", cursorless_target)
    key(space)

# bump air: a</foo> -> a </foo>
bump <user.cursorless_target>:
    user.cursorless_command("setSelectionAfter", cursorless_target)
    key(space)

# Allow unambiguous commands
then: skip()

trouble fix <user.cursorless_target>:
    user.cursorless_command("setSelectionBefore", cursorless_target)
    user.vscode("editor.action.quickFix")
