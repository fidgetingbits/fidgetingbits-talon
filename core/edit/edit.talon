-

# VIM uses find for line searching
# XXX - is a good chance this conflicts with other grammars from certain
# applications
search: edit.find()

next one: edit.find_next()

find <user.unmodified_key>: user.line_find_forward(unmodified_key)

find last <user.unmodified_key>: user.line_find_backward(unmodified_key)

go (word left | back): edit.word_left()

go (word right | word): edit.word_right()

go left: edit.left()

go right: edit.right()

go (up | north): edit.up()

go (down | south): edit.down()

go (line start | head): edit.line_start()

go (line end | tail): edit.line_end()

go way left: edit.line_start()

go way right: edit.line_end()

go way down: edit.file_end()

go way up: edit.file_start()

go bottom: edit.file_end()

go top: edit.file_start()

scroll: edit.page_down()

(go page up | punk): edit.page_up()

# selecting
select line: edit.select_line()

select all: edit.select_all()

select left: edit.extend_left()

select right: edit.extend_right()

select (up | north): edit.extend_line_up()

select (down | south): edit.extend_line_down()

select word: edit.select_word()

select word left: edit.extend_word_left()

select word right: edit.extend_word_right()

select (way left | bend): edit.extend_line_start()

select (way right | lend): edit.extend_line_end()

select (way up | loft): edit.extend_file_start()

select (way down | gut): edit.extend_file_end()

# editing
indent [more]: edit.indent_more()

de dent: edit.indent_less()

# deleting
clear line: edit.delete_line()

clear left: key(backspace)

clear right: key(delete)

clear up:
    edit.extend_line_up()
    edit.delete()

clear down:
    edit.extend_line_down()
    edit.delete()

#clear word:
#    edit.delete_word()

(clear word left | clear back): user.delete_word_left()

clear word [right]: user.delete_word_right()

(clear way left | clear bend): user.delete_line_beginning()

(clear way right | clear lend): user.delete_line_remaining()

clear way up:
    edit.extend_file_start()
    edit.delete()

clear way down:
    edit.extend_file_end()
    edit.delete()

#clear all:
#    edit.select_all()
#    edit.delete()

copy that: edit.copy()
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

copy word:
    edit.select_word()
    edit.copy()

copy word left:
    edit.extend_word_left()
    edit.copy()

copy word right:
    edit.extend_word_right()
    edit.copy()

copy line:
    edit.select_line()
    edit.copy()

#cut commands
cut all:
    edit.select_all()
    edit.cut()
#to do: do we want these variants
# cut left:
#      edit.select_all()
#      edit.cut()
# cut right:
#      edit.select_all()
#      edit.cut()
# cut up:
#      edit.select_all()
#     edit.cut()
# cut down:
#     edit.select_all()
#     edit.cut()

cut word:
    edit.select_word()
    edit.cut()

cut word left:
    edit.extend_word_left()
    edit.cut()

cut word right:
    edit.extend_word_right()
    edit.cut()

cut line:
    edit.select_line()
    edit.cut()

assign: " = "
(pace | paste) all:
    edit.select_all()
    edit.paste()
