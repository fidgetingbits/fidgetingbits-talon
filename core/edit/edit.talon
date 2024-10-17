# FIXME: add the fallback support like Andreas
# not tag: user.cursorless
-

tag(): user.zoom

# VIM uses find for line searching
# XXX - is a good chance this conflicts with other grammars from certain
# applications
scout:
    edit.find()

scout next:
    edit.find_next()

go [short] (word left | back):
    user.word_short_left()

go [short] (word right | word):
    user.word_short_right()


# FIXME(edit): have to implement this in zle
# go word end:
#     user.word_short_end()

go long (word left | back):
    user.word_long_left()

go long (word right | word):
    user.word_long_right()

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

scroll top:
    user.scroll_start()

scroll bottom:
    user.scroll_end()

punk:
    edit.page_up()


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

select word left:
    edit.extend_word_left()

select word right:
    edit.extend_word_right()



# editing
indent [more]:
    edit.indent_more()

de dent:
    edit.indent_less()


clear up:
    edit.extend_line_up()
    edit.delete()

clear down:
    edit.extend_line_down()
    edit.delete()

clear word: edit.delete_word()

clear line: edit.delete_line()
clear head: user.delete_line_start()
clear tail: user.delete_line_end()

(clear|chuck) [short] back:
    user.delete_word_short_left()

(clear|chuck) long back:
    user.delete_word_long_left()

(clear|chuck) [short] word:
    user.delete_word_short_right()

(clear|chuck) long word:
    user.delete_word_long_right()

clear way left:
    edit.extend_line_start()
    edit.delete()

clear way right:
    edit.extend_line_end()
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

cut line start: user.cut_line_start()
cut line end: user.cut_line_end()
cut block: user.cut_paragraph()
cut word: user.cut_word()
cut word left: user.cut_word_left()
cut word right: user.cut_word_right()

copy word left:
    user.copy_word_left()

copy word right:
    user.copy_word_right()



paste all: user.paste_all()
paste line: user.paste_line()
paste line start: user.paste_line_start()
paste line end: user.paste_line_end()
paste word: user.paste_word()

(pasty|paste that): edit.paste()
paste clean: user.paste_without_new_lines()

# This should just be some sort of function with arg to specify the symbol
paste in quotes:
    key(")
    sleep(0.1)
    edit.paste()
    key(")

paste match: edit.paste_match_style()
(pace | paste) [to] all: user.paste_all()
(pace | paste) [to] line: user.paste_line()
(pace | paste) [to] line start: user.paste_line_start()
(pace | paste) [to] line end: user.paste_line_end()
(pace | paste) [to] block: user.paste_paragraph()
(pace | paste) [to] word: user.paste_word()

slap:
    edit.line_end()
    key(enter)

parrot(side_click):
    app.notify("side_click")
    key(enter)

# FIXME: This should be pages
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

[go] line mid: user.line_middle()
go match: user.jump_cursor_to_matching_char()
