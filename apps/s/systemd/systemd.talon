app: terminal
tag: user.systemd
-

service [demon] reload: "sudo systemctl daemon-reload\n"
service list active: "systemctl list-units --type=service --state=active --no-pager\n"
service list running:
    "systemctl list-units --type=service --state=running --no-pager\n"
service list failed: "systemctl list-units --type=service --state=failed --no-pager\n"
service list exited: "systemctl list-units --type=service --state=exited --no-pager\n"
service verify: "systemd-analyze verify /etc/systemd/system/"

service list all: "systemctl list-unit-files --type=service --no-pager\n"
service find running:
    "systemctl list-files --type=service --state=running --no-pager | grep "
service find active:
    "systemctl list-files --type=service --state=active --no-pager | grep "
service list disabled:
    "systemctl list-unit-files --type=service --no-pager | grep disabled\n"

(system|sys) cuttle: "systemctl "
