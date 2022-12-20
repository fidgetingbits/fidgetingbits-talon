mode: user.presentation
-

exit presentation mode:
    app.notify("Talon Awake")
    mode.disable("sleep")
    mode.disable("user.presentation")
    mode.enable("command")
    app.notify("Command Mode")
    speech.enable()
