code.language: codeql
-

tag(): user.code_comment_line
tag(): user.code_comment_block_c_like
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_libraries
tag(): user.code_libraries_gui

settings():
    user.code_private_function_formatter = "CAMEL_CASE"
    user.code_protected_function_formatter = "CAMEL_CASE"
    user.code_public_function_formatter = "CAMEL_CASE"
    user.code_private_variable_formatter = "CAMEL_CASE"
    user.code_protected_variable_formatter = "CAMEL_CASE"
    user.code_public_variable_formatter = "CAMEL_CASE"

state where: "where "
state from: "from "
state select: "select "

# XXX - shouldn't this be generic now?
toggle imports: user.code_toggle_libraries()
import <user.code_libraries>:
    user.code_insert_library("", code_libraries)
    key(end enter)
