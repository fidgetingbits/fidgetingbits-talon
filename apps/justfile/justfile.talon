tag: user.just_commands
-

[run] just list: "just -l\n"
just {user.justfile_commands}: "just {justfile_commands}\n"

just dump completions: user.just_dump_completions()
