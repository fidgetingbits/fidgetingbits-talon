# FIXME: add the fallback support like Andreas
# not tag: user.cursorless
-

# VIM uses find for line searching
# XXX - is a good chance this conflicts with other grammars from certain
# applications
scout:
    edit.find()

scout next:
    edit.find_next()

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

pre line:
    edit.line_start()

post line:
    edit.line_end()

pre file:
    edit.file_start()

post file:
    edit.file_end()

scroll:
    edit.page_down()

punk:
    edit.page_up()

# selecting
take line:
    edit.select_line()

take all:
    edit.select_all()

extend left:
    edit.extend_left()

extend right:
    edit.extend_right()

extend (up | north):
    edit.extend_line_up()

extend (down | south):
    edit.extend_line_down()

take (this|token):
    edit.select_word()

select word left:
    edit.extend_word_left()

select word right:
    edit.extend_word_right()

take head life:
    edit.extend_line_start()

take tail line:
    edit.extend_line_end()

take head file:
    edit.extend_file_start()

take tail file:
    edit.extend_file_end()

# editing
indent [more]:
    edit.indent_more()

de dent:
    edit.indent_less()

# deleting
chuck line:
    edit.delete_line()

clear up:
    edit.extend_line_up()
    edit.delete()

clear down:
    edit.extend_line_down()
    edit.delete()

chuck (this|token):
    edit.delete_word()

chuck head (this|token):
    user.delete_word_left()

chuck tail (this|token):
    user.delete_word_right()

chuck head:
    user.delete_line_start()

chuck tail:
    user.delete_line_end()

chuck head file:
    edit.extend_file_start()
    edit.delete()

chuck tail file:
    edit.extend_file_end()
    edit.delete()

chuck all:
   edit.select_all()
   edit.delete()

# copy this:
#     edit.copy()
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
clone this:
    edit.selection_clone()
clone line:
    edit.line_clone()


slap:
    edit.line_end()
    key(enter)

parrot(side_click):
    app.notify("side_click")
    key(enter)

zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
zoom reset: edit.zoom_reset()
(page | scroll) up: key(pgup)
(page | scroll) down: key(pgdown)
(file save|disk): edit.save()
(file save all|disk all): edit.save_all()

(undo that | nope | scratcher): edit.undo()
(redo that | yes indeed): edit.redo()

# XXX - should be part of some networking thing
link web: "https://"
link insecure web: "http://"
link file: "file://"
link file <user.folder_paths>: "file://{folder_paths}"

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

# This syntax breaks the talon formatter
# talon format test: key(")")
