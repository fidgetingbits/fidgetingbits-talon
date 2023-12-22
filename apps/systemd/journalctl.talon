tag: terminal
and tag: user.systemd
-

journal disk usage: "journalctl --disk-usage\n"
journal (list | show) kernel:
    'journalctl -k --no-pager --no-hostname --since "1 hour ago"\n'
journal (list | show): 'journalctl --no-pager --no-hostname --since "1 hour ago"\n'
journal errors: "journalctl --no-pager --no-hostname -p 3 -xb"
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
journal grep: user.insert_between("journalctl -u ", " --no-pager --lines 100 -g")
journal service: user.insert_between("journalctl -u ", " --no-pager --lines 100")
