tag: user.cyberpower-pdu
-

power list [all]: user.cyberpower_list()
power status <user.cyberpower_outlet>: user.cyberpower_outlet_status(cyberpower_outlet)
power on <user.cyberpower_outlet>: user.cyberpower_outlet_on(cyberpower_outlet)
power off <user.cyberpower_outlet>: user.cyberpower_outlet_off(cyberpower_outlet)
power (cycle|reboot) <user.cyberpower_outlet>: user.cyberpower_outlet_reboot(cyberpower_outlet)
power rename <user.cyberpower_outlet> [<user.text>]:
    user.cyberpower_outlet_rename(cyberpower_outlet)
    insert(text or "")
