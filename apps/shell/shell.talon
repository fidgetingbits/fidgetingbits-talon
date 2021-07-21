os: linux
tag: terminal
-
tag(): user.zsh

(rerun|run) last [command]: "!!\n\n"
cancel [that]: key(ctrl-c)
fucker: key(ctrl-c)
damn (it|that): key(ctrl-d)

# fzf keybindings
history search: key(ctrl-r)
fuzzy (dir|dear|dur): key(alt-c)
fuzzy (dir|dear|dur) <user.text>:
    key(alt-c)
    insert("{text}")


# zsh autosuggestions plugin
(got|run) (it|that): key(ctrl-o)
found [it]: key(ctrl-g)
keep [it]: key(ctrl-f)
