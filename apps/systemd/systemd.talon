tag: terminal
and tag: user.systemd
-


service list: "systemctl list-units --type=service\n"
service list active: "systemctl list-units --type=service --state=active\n"
service list running: "systemctl list-units --type=service --state=running\n"
service list failed: "systemctl list-units --type=service --state=failed\n"
service list exited: "systemctl list-units --type=service --state=exited\n"
service verify: "systemd-analyze verify /etc/systemd/system/"

# TODO - generic
system timer user list: "systemctl --user list-timers --no-pager\n"
system timer user all: "systemctl --user --all list-timers --no-pager\n"
system timer list: "systemctl list-timers --no-pager\n"
system timer all: "systemctl --all list-timers --no-pager\n"

system cuttle: "systemctl "
