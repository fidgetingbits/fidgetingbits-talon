os: linux
tag: terminal
-
tag(): user.zsh

cancel [that]:
    key(ctrl-c)
# fzf keybindings
# history search: key(ctrl-r)
folder fuzzy:
    key(alt-c)
folder fuzzy <user.text>:
    key(alt-c)
    insert("{text}")

# zsh autosuggestions plugin
keep:
    key(ctrl-g)
parrot(tut):
    key(ctrl-g)
(partial|keep one):
    key(ctrl-f)
(keeper | run it):
    key(ctrl-o)
