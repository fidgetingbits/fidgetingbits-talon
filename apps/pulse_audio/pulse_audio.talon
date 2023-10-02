tag: user.pulse_audio
-

# XXX - Use pactl for setting volume since it has percentages
pulse command: "pacmd "
pulse control: "pactl "
pulse control help: "pactl help\n"
pulse command help: "pacmd help\n"
pulse list sources: "pacmd "
pulse devices: "pacmd list-sources | grep -e 'index:' -e device.string -e 'name:'\n"
# simplified list to show device names
pulse sources: "pacmd list-sources | grep -e 'index:' -e device.string -e 'name:'\n"

pulse edit defaults: "sudo vim /etc/pulse/default.pa\n"
pulse interface: user.system_command("pavucontrol")
pulse restart: user.system_command("pulseaudio -k && pulseaudio --start")
