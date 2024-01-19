tag: user.just_commands
-

[run] just list: "just -l\n"
[run] just build: "just build\n"

just dump completions: user.just_dump_completions()
just {user.justfile_commands}: "just {justfile_commands}\n"
