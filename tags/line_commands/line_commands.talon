tag: user.line_commands
-
#this defines some common line commands. More may be defined that are ide-specific.
tail: edit.line_end()
head: edit.line_start()
go row <number>: edit.jump_line(number)
push row <number>:
    edit.jump_line(number)
    edit.line_end()
comment [line] <number>:
    user.select_range(number, number)
    code.toggle_comment()
comment <number> until <number>:
    user.select_range(number_1, number_2)
    code.toggle_comment()
clear line <number>:
    user.select_range(number, number)
    edit.delete()
clear <number> until <number>:
    user.select_range(number_1, number_2)
    edit.delete()
copy line <number>:
    user.select_range(number, number)
    edit.copy()
copy <number> until <number>:
    user.select_range(number_1, number_2)
    edit.copy()
cut line <number>:
    user.select_range(number, number)
    edit.cut()
cut line <number> until <number>:
    user.select_range(number_1, number_2)
    edit.cut()
(paste | replace) <number> until <number>:
    user.select_range(number_1, number_2)
    edit.paste()
(select | cell | sell) [line] <number>: user.select_range(number, number)
(select | cell | sell) <number> until <number>: user.select_range(number_1, number_2)
indent: edit.indent_more()
indent [row] <number>:
    edit.jump_line(number)
    edit.indent_more()
indent [row] <number> until [row] <number>:
    user.select_range(number_1, number_2)
    edit.indent_more()
retab that: edit.indent_less()
retab [line] <number>:
    user.select_range(number, number)
    edit.indent_less()
retab <number> until <number>:
    user.select_range(number_1, number_2)
    edit.indent_less()
drag [line] down: edit.line_swap_down()
drag [line] up: edit.line_swap_up()
drag up [line] <number>:
    user.select_range(number, number)
    edit.line_swap_up()
drag up <number> until <number>:
    user.select_range(number_1, number_2)
    edit.line_swap_up()
drag down [line] <number>:
    user.select_range(number, number)
    edit.line_swap_down()
drag down <number> until <number>:
    user.select_range(number_1, number_2)
    edit.line_swap_down()
clone [line] <number>: user.line_clone(number)

select camel left: user.extend_camel_left()
select camel right: user.extend_camel_right()
go camel left: user.camel_left()
go camel right: user.camel_right()

go (char|car) <user.unmodified_key>: user.jump_cursor_to_next_char(unmodified_key)
go (prev|previous|last|lass) [(char|car)] <user.unmodified_key>: user.jump_cursor_to_prev_char(unmodified_key)
join line: user.join_lines()
