os: linux
mode: command
and tag: terminal
-

edit (vim|them) config: "vim ~/.vimrc\n"
edit shell config: "vim ~/.zshrc\n"
resource shell: "source ~/.zshrc"

# config
edit (ignore file|git ignore): "vim .gitignore\n"
(edit|at it) (secure shell| S S H) config: "vim ~/.ssh/config\n"
(edit|at it) (eye three|window manager) config: "vim ~/.i3/config\n"
(edit|at it) window manager config: "vim ~/.i3/config\n"

# snippets
edit custom snippets: "vim ~/.vim/custom-snippets\n"
edit vim snippets:
    "vim ~/.vim/plugged/vim-snippets/UltiSnips/\n"
edit markdown snippets:
    "vim ~/.vim/plugged/vim-snippets/UltiSnips/markdown.snippets\n"
edit python snippets:
    "vim ~/.vim/plugged/vim-snippets/UltiSnips/python.snippets\n"
edit latest talon log:
    "vim ~/talon/logs/$(ls -rt | tail -n1)"
new talon pull branch: "new_talon_pull_repo.sh "


fuzzy vimdiff:
    insert("edit -d $(find . -name \"**\")")
    edit.left()
    edit.left()

###
# Work
###

# shell helpers
go to work:
    insert("source ~/projects/current &&")
    insert(" cd $ACTIVE_PROJECT\n")
(go|jump) [to] alternate [work] (project|directory):
    insert("source ~/projects/alternate &&")
    insert(" cd $ACTIVE_PROJECT\n")
edit [to] (current|active) [work] project: "vim ~/projects/current\n"
build project: insert("build_active_project\n")
super kill g d b: "sudo pkill gdb\n"
resource config:
    insert("delete br\ny\n")
    insert("source debug_scripts/4.90.gdb\n")

edit sue do config: "sudo visudo\n"
edit find results:
    insert("vim $(find . -name \"\")")
    edit.left()
    edit.left()

# run command
run talon update: "~/.talon/bin/update\n"
run debug: "./debug.sh\n"
run update: "update.sh\n"
run project: insert("run_active_project\n")
run talon shell: insert("~/.talon/bin/repl\n")
run [talon] event log: insert('echo "events.tail()"|~/.talon/bin/repl\n')
run noisy log: insert('echo "events.tail(noisy=True)"|~/.talon/bin/repl\n')
run filter log: insert('echo "events.tail(search="", noisy=True)"|~/.talon/bin/repl\n')

# markdown to docx
generate dock: user.insert_cursor("pandoc [|].md --self-contained --highlight-style=tango -o .docx")

net (remote desktop|R D P) share:
    user.insert_cursor("xfreerdp /timeout:90000 /size:1280x800 /v:[|] /u: /p: /drive:share,rdp/share")
