os: linux
-

dunce pause: user.system_command('notify-send "DUNST_COMMAND_PAUSE"')
dunce resume: user.system_command('notify-send "DUNST_COMMAND_RESUME"')
test notification: user.system_command('notify-send "Hello from Talon"')
dismiss [notifications]: user.system_command("dunstctl close")
dismiss all [notifications]: user.system_command("dunstctl close-all")
follow notification: key(ctrl+shift+period)
show notifications: user.system_command("dunstctl history-pop")
toggle notifications: user.system_command("dunstctl set-paused toggle")
