os: linux
# tag: user.nmcli
-

<user.vpn> {user.nmcli_vpns}:
    user.nmcli_connection_toggle(nmcli_vpns)
<user.vpn> {user.nmcli_vpns} up:
    user.nmcli_connection_up(nmcli_vpns)
<user.vpn> {user.nmcli_vpns} down:
    user.nmcli_connection_down(nmcli_vpn)
<user.vpn> show:
    user.nmcli_connection_toggle_list()
