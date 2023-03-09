app: O10editor
-

###
# File menu
###

file menu:
    key(alt-f)
file open:
    key(ctrl-o)

###
# Edit menu
###
edit menu:
    key(alt-e)
copy as hex:
    key(ctrl-shift-c)
paste from hex:
    key(ctrl-shift-v)
(select|take) range:
    key(ctrl-shift-a)
undo:
    key(ctrl-z)
redo:
    key(ctrl-shift-z)

###
# Search menu
###
search menu:
    key(alt-s)
find strings:
    key(alt-s i)

file find:
    key(ctrl-f)
find next:
    key(F3)
find prev:
    key(ctrl-F3)

###
# Tools menu
###
tools check sum:
    key(ctrl-k)

###
# Navigation
###

(jump|go to) (offset|address):
    key(ctrl-g)

jump [to] clip:
    key(ctrl-g)
    edit.paste()
    key(enter)

jump (back|again):
    key(ctrl-shift-g)


###
# Non-default
###
copy offset:
    key(ctrl-shift-o)
