os: linux
tag: user.iptables
-

firewall list: insert("sudo iptables -L\n")
firewall list nat: insert("sudo iptables -t nat -L\n")
