mode: command
and mode: user.c
mode: command
and mode: user.auto_lang
and code.language: c

-
tag(): user.code_imperative

tag(): user.code_comment_line
tag(): user.code_comment_block_c_like
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_gui
tag(): user.code_libraries
tag(): user.code_libraries_gui
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_math
tag(): user.code_operators_pointer

settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_protected_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"
    # whether or not to use uint_8 style datatypes
    #    user.use_stdint_datatypes = 1

^funky <user.text>$: user.code_default_function(text)
^static funky <user.text>$: user.code_private_static_function(text)

# NOTE: migrated from generic, as they were only used here, though once cpp support is added, perhaps these should be migrated to a tag together with the commands below
state include:
    insert('#include ')
state include system:
    insert('#include <>')
    edit.left()
state include local:
    insert('#include ""')
    edit.left()
state type deaf:
    insert('typedef ')
state type deaf struct:
    insert('typedef struct')
    insert('{\n\n}')
    edit.up()
    key('tab')

signal <user.c_signals>: "{c_signals}"
error <user.c_errors>: "{c_errors}"

block:
    insert("{\n\n}")
    key(up)

#declare <user.c_variable>:

# Declare variables or structs etc.
# Ex: int * myList
#declare <user.c_variable> <phrase>:
#    insert("{c_variable} ")
#    insert(user.formatted_text(phrase, "PRIVATE_CAMEL_CASE,NO_SPACES"))

declare <user.c_variable> <user.letter>:
    insert("{c_variable} {letter} ")

# Ex. (int *)
cast to <user.c_cast>: "{c_cast}"
basic cast to <user.c_basic_cast>: "{c_basic_cast}"
standard cast to <user.c_stdint_cast>: "{c_stdint_cast}"
[state] type <user.c_types>: "{c_types}"
<user.c_pointers>: "{c_pointers}"
<user.c_signed>: "{c_signed}"
basic <user.c_basic_types>: "{c_basic_types}"
standard <user.c_stdint_types>: "{c_stdint_types}"
toggle includes: user.code_toggle_libraries()
include <user.code_libraries>:
    user.code_insert_library("", code_libraries)
    key(end enter)

cycle data type: user.cycle_c_datatype()
show data type: user.current_c_datatype()

state return <number>: "return {number};"
state return negative <number>: "return -{number};"
state return null: "return NULL;"
state continue: "continue;"
state break: "break;"

state define: "#define "
state undefine: "#undef "
state if define: "#ifdef "
state pre if: "#if "
state pre if zero: "#if 0"
state error: "#error "
state pre else if: "#elif "
state pre end: "#endif"
state pragma: "#pragma "
state default: "default:\nbreak;"
state pre if block: 
    insert("#if 0\n#endif")
    key(up)

state define new source: "#define _GNU_SOURCE"
state go to label <user.text>:
    user.code_private_variable_formatter(text)
    key(":")

###
# Documentation
###
# JavaDoc-style Doxygen
# https://www.doxygen.nl/manual/docblocks.html
# TODO - this might be something to generalize and have set up in settings
dock fun:
    user.paste("/**\n* \n*/")
    key(up end)
dock var:
    user.insert_cursor("/**< [|].*/")
dock in:
    insert("@param[in] ")
dock out:
    insert("@param[out] ")
dock in out:
    insert("@param[in, out] ")
dock return:
    insert("@return")
dock file:
    insert("/** @file */")
