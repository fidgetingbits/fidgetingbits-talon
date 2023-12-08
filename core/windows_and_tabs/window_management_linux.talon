os: linux
tag: user.gnome
-

# FIXME: These should go through an action that are window manager specific
run command: key(alt-f2)
run command <user.text>:
    key(alt-f2)
    sleep(100ms)
    insert(text)
launch: key(super)
launch <user.text>:
    key(super)
    sleep(100ms)
    insert(text)
