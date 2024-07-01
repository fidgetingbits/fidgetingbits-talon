os: linux
app: terminal
tag: user.nmcli
-

net man: "nmcli "
net man running: "nmcli -t -f RUNNING general\n"
net man status: "nmcli general\n"
net man devices: "nmcli\n"
net man connect:
    insert("nmcli con up ")
    key(tab)
net man disconnect:
    insert("nmcli con down ")
    key(tab)
net man edit:
    insert("nmcli con edit ")
    key(tab)
net man (connections | connection) list: "nmcli connection show\n"
net man (connections | connection) list active: "nmcli connection show --active\n"

net man (V P N|tunnel) list: "nmcli -t -f NAME,TYPE connection show | rg vpn | cut -f1 -d:\n"
net man (V P N|tunnel) list active: "nmcli -t -f NAME,TYPE,STATE connection show | rg 'vpn:activated' | cut -f1 -d:\n"

# FIXME: Make this globally accessible so I can start and stop them without being in a terminal
net man [(V P N|tunnel)] {user.nmcli_vpns} up: "nmcli con up {nmcli_vpns}\n"
net man [(V P N|tunnel)] {user.nmcli_vpns} down: "nmcli con down {nmcli_vpns}\n"
