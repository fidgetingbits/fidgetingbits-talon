# joycon x
gamepad(east:down):
    tracking.control_toggle()
    print("tracking control toggled: on")
gamepad(east:up):
    tracking.control_toggle()
    print("tracking control toggled: off")
# joycon y
gamepad(north):
    user.talon_sleep()
# joycon a
gamepad(south):
    core.repeat_command(1)
