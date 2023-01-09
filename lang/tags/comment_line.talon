tag: user.code_comment_line
-
comment: user.code_comment_line_prefix()
#comment line:
#    #todo: this should probably be a single function once
#    #.talon supports implementing actions with parameters?
#    edit.line_start()
#    user.code_comment_line_prefix()
##adds comment to the start of the line
#comment line <user.text> over:
#    #todo: this should probably be a single function once
#    #.talon supports implementing actions with parameters?
#    edit.line_start()
#    user.code_comment_line_prefix()
#    insert(user.text)
#    insert(" ")
#comment <user.text> over:
#    #todo: this should probably be a single function once
#    #.talon supports implementing actions with parameters?
#    user.code_comment_line_prefix()
#    insert(user.text)
#comment <user.text>$:
#    #todo: this should probably be a single function once
#    #.talon supports implementing actions with parameters?
#    user.code_comment_line_prefix()
#    insert(user.text)
#(line | inline) comment <user.text> over:
#    #todo: this should probably be a single function once
#    #.talon supports implementing actions with parameters?
#    edit.line_end()
#    user.code_comment_line_prefix()
#    insert(user.text)
#(line | inline) comment <user.text>$:
#    #todo: this should probably be a single function once
#    #.talon supports implementing actions with parameters?
#    edit.line_end()
#    user.code_comment_line_prefix()
#    insert(user.text) */

comment to do:
    user.code_comment_line_prefix()
    insert("TODO: ")
comment note:
    user.code_comment_line_prefix()
    insert("NOTE: ")
comment hack:
    user.code_comment_line_prefix()
    insert("HACK: ")
comment warn:
    user.code_comment_line_prefix()
    insert("WARN: ")
comment perf:
    user.code_comment_line_prefix()
    insert("PERF: ")
comment fix me:
    user.code_comment_line_prefix()
    insert("FIXME: ")
