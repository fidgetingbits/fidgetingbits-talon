# NOTE: If you want to use gnome-shell you must enable the tag settings.talon. i.e.: `tag(): user.gnome-shell`
os: linux
and tag: user.gnome-shell
-

launch command: user.launch_command_prompt()
launch [app]: key(super)
app show: key(super-a)

power off: key(ctrl-alt-delete)
lock screen: key(super-l)
notify show: key(super-v)
(dismiss|notify close): key(esc)

app select:
    key(alt:down)
    key(tab)

app next:
    key(tab)

app choose:
    key(alt:up)
