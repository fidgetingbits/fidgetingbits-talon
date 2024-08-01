os: linux
not app: terminal
# tag: user.nmcnmcli con downnmcli con down manila_tcp_splitli
-

net man [(V P N|tunnel)] {user.nmcli_vpns}:
    user.nmcli_connection_toggle(nmcli_vpns)
net man [(V P N|tunnel)] {user.nmcli_vpns} up:
    user.nmcli_connection_up(nmcli_vpns)
net man [(V P N|tunnel)] {user.nmcli_vpns} down:
    user.nmcli_connection_down(nmcli_vpn)
