tag: user.code_functions_common
-
toggle funk:
    user.code_toggle_functions()
funk (<user.code_common_function> | <user.text>):
    user.code_insert_function(code_common_function or text, "")
(chain|meth) (<user.code_common_function> | <user.text>):
    insert(".")
    user.code_insert_function(code_common_function or text, "")
funk cell <number>:
    user.code_select_function(number - 1, "")
funk wrap <user.code_common_function>:
    user.code_insert_function(code_common_function, edit.selected_text())
funk wrap <number>:
    user.code_select_function(number - 1, edit.selected_text())
