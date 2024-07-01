app: terminal
tag: user.borg
-

borg: insert(user.action.borg_command())
borg help: "borg -h\n"
borg {user.borg_commands} help: "borg {user.borg_commands} -h\n"
borg {user.borg_commands}:
    insert(user.action.borg_command())
    insert(user.borg_commands)

