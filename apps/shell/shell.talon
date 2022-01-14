os: linux
tag: terminal
-
tag(): user.zsh

cancel [that]: key(ctrl-c)
# fzf keybindings
history search: key(ctrl-r)
fuzzy (dir|dear|dur): key(alt-c)
fuzzy (dir|dear|dur) <user.text>:
    key(alt-c)
    insert("{text}")


# zsh autosuggestions plugin
(got|run) (it|that): key(ctrl-o)
#found [it]: key(ctrl-g)
keep [it]: key(ctrl-f)
