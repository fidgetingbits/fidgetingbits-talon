# NOTE: If you want to use gnome-shell you must enable the tag settings.talon. i.e.: `tag(): user.gnome-shell`
os: linux
and tag: user.gnome-shell
-

launch command: key(alt-f2)
launch app: key(super)
app show: key(super-a)

power off: key(ctrl-alt-delete)
lock screen: key(super-l)
notify show: key(super-v)
notify close: key(esc)

term me: 
    key(super)
    insert("console")
    sleep(200ms)
    key(ctrl-enter)