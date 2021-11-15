mode: user.c
mode: user.auto_lang
and code.language: c

-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_block_comment
tag(): user.code_generic
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


hash define: "#define "
hash undefine: "#undef "
hash if define: "#ifdef "
hash if: "#if "
hash error: "#error "
hash else if: "#elif "
hash end if: "#endif "
hash pragma: "#pragma "
state default: "default:\nbreak;"

block:
    insert("{\n\n}")
    key(up)

#control flow
#best used with a push like command
#the below example may not work in editors that automatically add the closing bracket
#if so uncomment the two lines and comment out the rest accordingly
push brackets:
    edit.line_end()
    insert("{}")
    edit.left()
    key(enter)
    key(enter)
    edit.up()

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
state <user.c_types>: "{c_types}"
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
