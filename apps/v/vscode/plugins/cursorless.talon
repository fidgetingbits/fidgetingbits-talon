tag: user.cursorless
not app: terminal
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
# NOTE: You can use void wrap
bully <user.cursorless_target>:
    user.cursorless_command("setSelectionAfter", cursorless_target)
    key(space)
    user.cursorless_command("setSelectionBefore", cursorless_target)
    key(space)

# crush air: <foo> a </foo> -> <foo>a</foo>
# WARNING: This isn't reliable with multiple targets, so select first
crush <user.cursorless_target>:
    user.cursorless_command("setSelectionBefore", cursorless_target)
    key(backspace)
    user.cursorless_command("setSelectionAfter", cursorless_target)
    key(right delete)

# tug air: <foo>a -> <foo> a
tug <user.cursorless_target>:
    user.cursorless_command("setSelectionBefore", cursorless_target)
    key(space)

# bump air: a</foo> -> a </foo>
bump <user.cursorless_target>:
    user.cursorless_command("setSelectionAfter", cursorless_target)
    key(space)

# pull air: b a -> ba
pull <user.cursorless_target>:
    user.cursorless_command("setSelectionBefore", cursorless_target)
    key(left delete)

# mag b: b a -> ba
mag <user.cursorless_target>:
    user.cursorless_command("setSelectionAfter", cursorless_target)
    key(delete)

# Allow unambiguous commands
then: skip()

trouble fix <user.cursorless_target>:
    user.cursorless_command("setSelectionBefore", cursorless_target)
    user.vscode("editor.action.quickFix")

repeat length of <user.cursorless_target>:
    len  = user.c_get_target_length(cursorless_target)
    core.repeat_command(len-1)

confetti:
    user.vscode('cursorless.toggleDecorations')

(bug|debug) to <user.cursorless_target>:
    user.cursorless_command("setSelectionBefore", cursorless_target)
    user.vscode("editor.debug.action.runToCursor")

terminate <user.cursorless_target>:
    user.cursorless_command("setSelectionAfter", cursorless_target)
    user.code_state_terminate()

# This is meant for use with strings, to quickly add new lines to them
newt <user.cursorless_target>:
    user.cursorless_command("setSelectionAfter", cursorless_target)
    key(left)
    insert("\\n")
