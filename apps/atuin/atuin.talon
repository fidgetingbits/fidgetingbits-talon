app: terminal
tag: user.atuin
-
<user.history> help: "atuin help\n"
<user.history> {user.atuin_commands} help: "atuin {atuin_commands} -h\n"
<user.history> last <number>: "atuin search --cmd-only --limit {number}\n"
<user.history> sync: "atuin sync\n"

# enter here auto running is dependent on atuin settings, so we use tab instead of enter to be safe
recall force <user.text>:
    key(ctrl-r)
    insert(text)
    key(tab)

