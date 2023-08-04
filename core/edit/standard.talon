(shock | hawk | slap): key(enter)
parrot(side_click):
    app.notify("side_click")
    key(enter)

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

(undo that | nope): edit.undo()
(redo that | yes indeed): edit.redo()
paste match: edit.paste_match_style()
disk: edit.save()
disk oliver: edit.save_all()

# XXX - should be part of some networking thing
link web: "https://"
link insecure web: "http://"
link file: "file://"
link git: "git://"
link secure shell: "ssh://"



###
# Chat
###
# XXX - these could be part of brief
smiley: ":)"
sad face: ":("
big smiley: ":D"
jiff smiley: ">\\o "
padding: user.insert_between(" ", " ")