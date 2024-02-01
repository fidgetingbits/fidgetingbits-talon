code.language: nix
-
tag(): user.code_imperative

tag(): user.code_comment_documentation
tag(): user.code_comment_line
tag(): user.code_comment_block
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_keywords
tag(): user.code_libraries
tag(): user.code_libraries_gui
tag(): user.code_operators_assignment
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_lambda
tag(): user.code_operators_math

settings():
    user.code_private_function_formatter = "CAMEL_CASE"
    user.code_protected_function_formatter = "CAMEL_CASE"
    user.code_public_function_formatter = "CAMEL_CASE"
    user.code_private_variable_formatter = "CAMEL_CASE"
    user.code_protected_variable_formatter = "CAMEL_CASE"
    user.code_public_variable_formatter = "CAMEL_CASE"

tickle: user.insert_between("''", "''")

put trace: user.insert_between('renameMe1 = builtins.trace "', '" true;')
put trace <user.text>:
    user.insert_between("renameMe1", ' = builtins.trace "{text}" true;')

[put] dummy hash: "sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
set hash dummy: 'hash = "sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=";'

put {user.nix_builtin_keywords}: "{nix_builtin_keywords}"
funk {user.nix_builtins_functions}: "{nix_builtins_functions}"
funk <user.nix_pkg_functions>: "{nix_pkg_functions}"

set list: user.insert_between(" = [ ", " ];")
set map: user.insert_between(" = { ", " };")
