# FIXME(nix): That should now integrate the service running on nix
talon restart: user.talon_restart()
talon kill: user.talon_kill()

#talon restart: user.system_command_nb("/home/aa/scripts/talon/restart_talon.sh")
#talon kill: user.system_command_nb("/home/aa/scripts/talon/terminate_talon.sh")
pauly restart: user.system_command_nb("/home/aa/.config/polybar/launch.sh")

# bluetooth
blue tooth open: user.system_command_nb("rofi-bluetooth")
blue tooth on:
    user.system_command_nb("rofi-bluetooth")
    sleep(400ms)
    key(enter)
blue tooth connect:
    user.system_command_nb("rofi-bluetooth")
    sleep(400ms)
    key(enter)
    sleep(400ms)
    key(enter)

customize ({user.talon_settings_csv} | <user.file_paths_string>):
    path = talon_settings_csv or file_paths_string
    user.system_command_nb("code --reuse-window " + path)
    # FIXME: Need to modify code.desktop to not open preexisting window before you switch back to this
    # user.edit_text_file(talon_settings_csv or file_paths_string)
    sleep(500ms)
    edit.file_end()

over: skip()
