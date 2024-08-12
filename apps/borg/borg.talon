app: terminal
tag: user.borg
-

borg: insert(user.borg_command())
borg help: "borg -h\n"
borg {user.borg_commands} help: "borg {user.borg_commands} -h\n"
borg {user.borg_commands}:
    insert(user.borg_command())
    insert(user.borg_commands)

# These custom script specific to my system
[borg] backup list: "sudo borg-backup-list\n"
[borg] backup mount: "sudo borg-backup-mount\n"
[borg] backup rename: "sudo borg-backup-rename\n"
[borg] backup test email: "sudo borg-backup-test-email\n"
[borg] backup prune: "sudo borg-backup-prune\n"
[borg] backup paths: "sudo borg-backup-paths\n"
[borg] backup subvolume: "sudo borg-backup-btrfs-subvolume\n"
