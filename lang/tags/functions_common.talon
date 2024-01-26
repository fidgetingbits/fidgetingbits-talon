tag: user.code_functions_common
-
toggle funk: user.code_toggle_functions()
funk (<user.code_common_function> | <user.text>):
    user.code_insert_function(code_common_function or text, "")
# FIXME: Maybe a better name for this. A function call with no arguments.
call (<user.code_common_function> | <user.text>):
    user.code_insert_terminated_function(code_common_function or text, "")
# FIXME: Chain conflicts with change in conformer B
meth (<user.code_common_method> | <user.text>):
    user.code_insert_method(code_common_method or text, "")
funk cell <number>: user.code_select_function(number - 1, "")
funk wrap <user.code_common_function>:
    user.code_insert_function(code_common_function, edit.selected_text())
funk wrap <number>: user.code_select_function(number - 1, edit.selected_text())
