# These are ones that conflict with cursorless that need to be fixed with fallback
not tag: user.cursorless
-

# selecting
take line:
    edit.select_line()


take (this|token):
    edit.select_word()

take head line:
    edit.extend_line_start()

take tail line:
    edit.extend_line_end()

take head file:
    edit.extend_file_start()

take tail file:
    edit.extend_file_end()

# deleting
chuck line:
    edit.delete_line()

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

cut line: user.cut_line()

copy line:
    edit.select_line()
    edit.copy()

    # duplication
clone this:
    edit.selection_clone()
clone line:
    edit.line_clone()

