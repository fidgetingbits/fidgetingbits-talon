app: terminal
tag: user.just_commands
-

[run] just list:
    edit.delete_line()
    insert("just -l\n")
just {user.justfile_commands}:
    edit.delete_line()
    insert("just {justfile_commands}\n")
