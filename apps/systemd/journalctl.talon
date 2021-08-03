tag: user.systemd
tag: terminal
-

journal disk usage: "journalctl --disk-usage\n"
journal show: "journalctl -k --no-pager --no-hostname\n"
journal vacuum time: "sudo journalctl --vacuum-time=1weeks\n"
journal vacuum size: "sudo journalctl --vacuum-time=100M\n"

# Common Services
# XXX - this should be switched to use create spoken form and a script he list
# them all
journal network: "journalctl -u NetworkManager --no-pager --lines 100\n"
journal docker: "journalctl -u docker --no-pager --lines 100\n"
journal secure shell: "journalctl -u sshd --no-pager --lines 100\n"
journal V P N: "journalctl -u openvpn-client --no-pager --lines 100\n"
journal network time: "journalctl -u ntpd --no-pager --lines 100\n"
journal grep: user.insert_cursor("journalctl -u [|] --no-pager --lines 100 -g")
