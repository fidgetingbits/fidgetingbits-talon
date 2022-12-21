tag: user.c
-
tag(): user.code_imperative

tag(): user.code_comment_line
tag(): user.code_comment_block_c_like
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
    user.insert_between("#include <", ">")
[state] include local [<user.text>]:
    user.insert('#include "{user.formatted_text(text or \'\', \'NOOP\')}.h"')
state type deaf:
    insert('typedef ')
state type deaf struct:
    insert('typedef struct')
    insert('{\n\n}')
    edit.up()
    key('tab')

signal {user.c_signals}: "{c_signals}"
error {user.c_errors}: "{c_errors}"

# XXX - create a preprocessor tag for these, as they will match cpp, etc
state define: "#define "
state (undefine | undeaf): "#undef "
state if (define | deaf): "#ifdef "
[state] define <user.text>$:
    "#define {user.formatted_text(text, 'ALL_CAPS,SNAKE_CASE')}"
[state] (undefine | undeaf) <user.text>$:
    "#undef {user.formatted_text(text, 'ALL_CAPS,SNAKE_CASE')}"
[state] if (define | deaf) <user.text>$:
    "#ifdef {user.formatted_text(text, 'ALL_CAPS,SNAKE_CASE')}"

#declare <user.c_variable>:

# Declare variables or structs etc.
# Ex: int * myList
#declare <user.c_variable> <phrase>:
#    insert("{c_variable} ")
#    insert(user.formatted_text(phrase, "PRIVATE_CAMEL_CASE,NO_SPACES"))

declare <user.c_variable> <user.letter>:
    insert("{c_variable} {letter} ")

# XXX - we should make these expressible to gdb
# Ex. (int *)
cast to <user.c_cast>: "{c_cast}"
basic cast to <user.c_basic_cast>: "{c_basic_cast}"
standard cast to <user.c_stdint_cast>: "{c_stdint_cast}"
[state] type <user.c_types>: "{c_types}"
state <user.c_pointers>: "{c_pointers}"
state <user.c_signed>: "{c_signed}"
basic <user.c_basic_types>: "{c_basic_types}"
standard <user.c_stdint_types>: "{c_stdint_types}"

# XXX - shouldn't this be generic now?
toggle includes: user.code_toggle_libraries()
[state] include <user.code_libraries>:
    user.code_insert_library("", code_libraries)
    key(end enter)

cycle data type: user.cycle_c_datatype()
show data type: user.current_c_datatype()

state return <number>: "return {number};"
state return negative <number>: "return -{number};"
state return null: "return NULL;"
state return false: "return false;"
state return true: "return true;"
state continue: "continue;"
state break: "break;"

state define: "#define "
state undefine: "#undef "
state [short] if define: "#ifdef "
state [short] if not define: "#ifndef "
state pre if: "#if "
state pre if zero: "#if 0"
state error: "#error "
state pre else: "#else"
state pre else if: "#elif "
state pre end: "#endif"
state pragma: "#pragma "
state default: "default:\nbreak;"
state pre if end:
    insert("#if 0\n#endif")
    key(up)
state long pre if defined:
    insert("#if defined()")

state long pre if not defined:
    insert("#if !defined()")

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
dock brief:
    insert("@brief ")
dock return:
    insert("@return")
dock param:
    insert("@param ")
dock in:
    insert("@param[in] ")
dock out:
    insert("@param[out] ")
dock in out:
    insert("@param[in, out] ")
dock file:
    insert("/** @file */")
