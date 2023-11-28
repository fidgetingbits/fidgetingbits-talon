-

# VIM uses find for line searching
# XXX - is a good chance this conflicts with other grammars from certain
# applications
search:
    edit.find()

next one:
    edit.find_next()

find <user.unmodified_key>:
    user.line_find_forward(unmodified_key)

find last <user.unmodified_key>:
    user.line_find_backward(unmodified_key)

go (word left | back):
    edit.word_left()

go (word right | word):
    edit.word_right()

go left:
    edit.left()

go right:
    edit.right()

go (up | north):
    edit.up()

go (down | south):
    edit.down()

go (line start | head):
    edit.line_start()

go (line end | tail):
    edit.line_end()

go way left:
    edit.line_start()

go way right:
    edit.line_end()

go way down:
    edit.file_end()

go way up:
    edit.file_start()

go bottom:
    edit.file_end()

go top:
    edit.file_start()

scroll:
    edit.page_down()

(go page up | punk):
    edit.page_up()

# selecting
select line:
    edit.select_line()

(select | take) all:
    edit.select_all()

select left:
    edit.extend_left()

select right:
    edit.extend_right()

select (up | north):
    edit.extend_line_up()

select (down | south):
    edit.extend_line_down()

select word:
    edit.select_word()

select word left:
    edit.extend_word_left()

select word right:
    edit.extend_word_right()

select (way left | bend):
    edit.extend_line_start()

select (way right | lend):
    edit.extend_line_end()

select (way up | loft):
    edit.extend_file_start()

select (way down | gut):
    edit.extend_file_end()

# editing
indent [more]:
    edit.indent_more()

de dent:
    edit.indent_less()

# deleting
clear line:
    edit.delete_line()

clear left:
    key(backspace)

clear right:
    key(delete)

clear up:
    edit.extend_line_up()
    edit.delete()

clear down:
    edit.extend_line_down()
    edit.delete()

#clear word:
#    edit.delete_word()

(clear word left | clear back):
    user.delete_word_left()

clear word [right]:
    user.delete_word_right()

(clear way left | clear bend):
    user.delete_line_beginning()

(clear way right | clear lend):
    user.delete_line_remaining()

clear way up:
    edit.extend_file_start()
    edit.delete()

clear way down:
    edit.extend_file_end()
    edit.delete()

#clear all:
#    edit.select_all()
#    edit.delete()

copy that:
    edit.copy()
#copy commands
copy all:
    edit.select_all()
    edit.copy()
#to do: do we want these variants, seem to conflict
# copy left:
#      edit.extend_left()
#      edit.copy()
# copy right:
#     edit.extend_right()
#     edit.copy()
# copy up:
#     edit.extend_up()
#     edit.copy()
# copy down:
#     edit.extend_down()
#     edit.copy()

# Cut
cut that: edit.cut()
cut all: user.cut_all()
cut line: user.cut_line()
cut line start: user.cut_line_start()
cut line end: user.cut_line_end()
cut word: user.cut_word()
cut word left: user.cut_word_left()
cut word right: user.cut_word_right()

copy word left:
    user.copy_word_left()

copy word right:
    user.copy_word_right()

copy line:
    edit.select_line()
    edit.copy()

paste all: user.paste_all()
paste line: user.paste_line()
paste line start: user.paste_line_start()
paste line end: user.paste_line_end()
paste word: user.paste_word()

(pasty|paste that): edit.paste()

# This should just be some sort of function with arg to specify the symbol
paste in quotes:
    key(")
    sleep(0.1)
    edit.paste()
    key(")

paste match: edit.paste_match_style()


# duplication
clone that:
    edit.selection_clone()
clone line:
    edit.line_clone()


slap: key(enter)
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
file save: edit.save()

(undo that | nope | scratcher): edit.undo()
(redo that | yes indeed): edit.redo()
disk: edit.save()
disk oliver: edit.save_all()

# XXX - should be part of some networking thing
link web: "https://"
link insecure web: "http://"
link file: "file://"
link git: "git://"
link secure shell: "ssh://"
link bucket: "s3://"
link F T P: "ftp://"



###
# Chat
###
# XXX - these could be part of brief
smiley: ":)"
sad face: ":("
big smiley: ":D"
jiff smiley: ">\\o "
padding: user.insert_between(" ", " ")

grow [<number>] left: user.grow_left(number or 1)
grow [<number>] right: user.grow_right(number or 1)
shrink [<number>] left: user.shrink_left(number or 1)
shrink [<number>] right: user.shrink_right(number or 1)
curse swap: user.swap_cursor_anchor()

talon format test: key(")")
