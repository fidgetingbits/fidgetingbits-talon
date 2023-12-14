code.language: lua
-

tag(): user.code_imperative

tag(): user.code_comment_line
tag(): user.code_comment_block
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_libraries
tag(): user.code_libraries_gui
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_math
tag(): user.code_operators_pointer

# Use this tag if you use the stylua linter
tag(): user.stylua
# Add neovim specific lua language commands
# tag(): user.lua_nvim
tag(): user.lua_redis
settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

put local: "local"
put end: "end"
put then: "then"
put repeat: "repeat"
put until: "until"
put return (null | nil): "return nil"
put return true: "return true"
put return false: "return false"
put return table: user.insert_between("return {", "}")
put append string: " .. "

put label <user.text>:
    insert("::")
    user.insert_formatted(text, "snake")
    insert("::")

require <user.code_libraries>:
    user.code_insert_library("", code_libraries)
    key(end enter)

put (variable | var) [<user.text>] [over]: user.code_public_variable_formatter(text)

put local (variable | var) [<user.text>] [over]:
    insert("local ")
    user.code_private_variable_formatter(text)

# for built in object methods, ex: foo:gsub()
method <user.text>:
    insert(":")
    user.code_public_function_formatter(text)
    insert("()")
    edit.left()

self dot: "self."

index <user.word>: '["{word}"]'
index (var | variable) <user.text>:
    var = user.formatted_text(text, "snake")
    insert("[{var}]")

put return dick: user.insert_between("return {", "}")
