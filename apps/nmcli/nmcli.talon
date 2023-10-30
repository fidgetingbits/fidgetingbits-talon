os: linux
tag: terminal
and tag: user.nmcli
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
