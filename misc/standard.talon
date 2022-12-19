(shock | hawk): key(enter)

# XXX - block alone conflicts with vim key words
add code block:
    insert("{}")
    key(left enter enter up tab)

zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
zoom reset: edit.zoom_reset()
(page | scroll) up: key(pgup)
(page | scroll) down: key(pgdown)
copy that: edit.copy()
cut that: edit.cut()
paste that: edit.paste()
pasty: edit.paste()
paste match: edit.paste_match_style()
file save: edit.save()

#menu help: key(F1)
#spotlight: key(super)
#(undo that | skunks): edit.undo()
#redo that: edit.redo()

# XXX - conflicts with piper
#hyper:
#    edit.copy()
#    edit.paste()
#sucker:
#    edit.copy()
#    edit.paste()
#    key(enter)
#pucker:
#    edit.paste()
#    key(enter)

# XXX - should be part of some networking thing
link web: "https://"
link insecure web: "http://"
link file: "file://"
link git: "git://"
link secure shell: "ssh://"

# this should be part of comment plugin
add to do: "# XXX - "

###
# Networking
###
net local host: "127.0.0.1"
net star: "0.0.0.0"
net mask [type] C: "255.255.255.0"
net mask [type] B: "255.255.0.0"
net mask [type] A: "255.0.0.0"
net type C: ".0/24"
net type B: ".0/16"
net type A: ".0/8"

###
# Chat
###
# XXX - these could be part of brief
smiley: ":)"
sad face: ":("
big smiley: ":D"
jiff smiley: ">\\o "
(pad | padding): user.insert_between(" ", " ")
#slap: edit.line_insert_down()
