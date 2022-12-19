not mode: sleep
and not mode: user.presentation
-
^command mode$:
    mode.disable("dictation")
    mode.enable("command")
    app.notify("Command Mode")
^dictation mode$:
    mode.disable("command")
    mode.enable("dictation")
    app.notify("Dictation Mode")
    user.code_clear_language_mode()
    mode.disable("user.gdb")

^presentation mode$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    app.notify("Presentation Mode")
    mode.enable("user.presentation")

# XXX - from https://github.com/AndreasArvidsson/andreas-talon/blob/master/misc/modes/dictation_mode.talon
# Switch to dictation mode and insert a phrase
dictate [<phrase>]$: user.dictation_mode(phrase or "")
