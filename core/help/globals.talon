# work auto-commands
(start working | open active work space | load active work session):
    user.system_command_nb("/home/aa/scripts/workflow/work_workspace.sh")

open alternate work space:
    user.system_command_nb("/home/aa/scripts/workflow/work_workspace.sh")

(connect | start) work (tunnel | vpn):
    user.system_command_nb("/home/aa/scripts/connect_work_vpn.sh")
(disconnect | stop) work (tunnel | vpn):
    user.system_command_nb("/home/aa/scripts/disconnect_work_vpn.sh")

screen keyboard show: user.system_command_nb("/home/aa/scripts/florence_show.sh")
screen keyboard hide: user.system_command_nb("/home/aa/scripts/florence_hide.sh")
talon restart: user.system_command_nb("/home/aa/scripts/talon/restart_talon.sh")
talon kill: user.system_command_nb("/home/aa/scripts/talon/terminate_talon.sh")
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

blue tooth fix audio: user.system_command_nb("/usr/local/bin/a2dp-fix")

keyboard flash now: user.system_command_nb("/home/aa/scripts/flash_keyboard.sh")

over: skip()
