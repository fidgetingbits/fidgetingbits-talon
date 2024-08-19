# commands for when you're inside the repl repl. The nix language will also be loaded
app: nix_repl
-

[repl] load expression: ":l "
[repl] load flake: ":lf "
[repl] load flake here: ":lf .\n"

repl reload: ":r\n"

# NOTE: This will open your external editor
repl edit: ":e "
repl edit clip:
    insert(":e ")
    edit.paste()
    key(enter)

repl quit: ":q\n"
repl help: ":?\n"

repl print: user.insert_between(':p "', '"')
repl print this:
    edit.line_start()
    insert(":p ")
    key(enter)

repl reload: ":r\n"

repl build: ":b "
repl build clip:
    insert(":b ")
    edit.paste()
    key(enter)

repl [build] log: ":log "

[repl] describe: ":t "
repl doc: ":doc "

repl trace enable: ":te true\n"
repl trace disable: ":te false\n"
repl trace toggle: ":te\n"

# FIXME: It would be nice to know the local architecture, to reference
<user.operator> packages: "legacyPackages.x86_64-linux."
