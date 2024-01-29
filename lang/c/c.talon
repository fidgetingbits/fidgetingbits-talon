code.language: c
-
tag(): user.code_imperative
tag(): user.code_comment_line
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
    # Whether or not to use uint8_t style datatypes
    #    user.use_stdint_datatypes = 1

^funky <user.text>$: user.code_default_function(text)
^static funky <user.text>$: user.code_private_static_function(text)

# NOTE: migrated from generic, as they were only used here, though once cpp support is added, perhaps these should be migrated to a tag together with the commands below
put include: insert("#include ")
put include system: user.insert_between("#include <", ">")
[put] include local [<user.text>]:
    user.insert("#include \"{user.formatted_text(text or '', 'NOOP')}.h\"")
[put] type deaf: insert("typedef ")
[put] type deaf struck:
    insert("typedef struct")
    insert("{\n\n}")
    edit.up()
    key('tab')

signal {user.c_signals}: "{c_signals}"
error {user.c_errors}: "{c_errors}"

prot <user.c_protections>: "{c_protections}"
ret {user.c_return_values}: "{c_return_values}"

# XXX - create a preprocessor tag for these, as they will match cpp, etc
put define: "#define "
put (undefine | undeaf): "#undef "
put if (define | deaf): "#ifdef "
put [short] if not (define | deaf): "#ifndef "
[put] define <user.text>$:
    "#define {user.formatted_text(text, 'ALL_CAPS,SNAKE_CASE')}"
[put] (undefine | undeaf) <user.text>$:
    "#undef {user.formatted_text(text, 'ALL_CAPS,SNAKE_CASE')}"
[put] if (define | deaf) <user.text>$:
    "#ifdef {user.formatted_text(text, 'ALL_CAPS,SNAKE_CASE')}"
put pre if: "#if "
put pre if zero: "#if 0"
put error: "#error "
put pre else: "#else"
put pre else if: "#elif "
put pre end: "#endif"
put pragma: "#pragma "
put default: "default:\nbreak;"
put pre if end:
    insert("#if 0\n#endif")
    key(up)
put long pre if defined: insert("#if defined()")
put long pre if not defined: insert("#if !defined()")
put define new source: "#define _GNU_SOURCE"

set <user.c_variable>: user.insert_between("{c_variable} = ", ";")
declare <user.c_variable>: "{c_variable}"

# XXX - we should make these expressible to gdb
# Ex. (int *)
cast to <user.c_cast>: "{c_cast}"
basic cast to <user.c_basic_cast>: "{c_basic_cast}"
standard cast to <user.c_stdint_cast>: "{c_stdint_cast}"
[put] type <user.c_types>: "{c_types}"
put <user.c_pointers>: "{c_pointers}"
put <user.c_signed>: "{c_signed}"
basic <user.c_basic_types>: "{c_basic_types}"
basic <user.c_basic_signed>: "{c_basic_signed}"
standard <user.c_stdint_types>: "{c_stdint_types}"
standard <user.c_stdint_signed>: "{c_stdint_signed}"

# XXX - shouldn't this be generic now?
toggle includes: user.code_toggle_libraries()
[put] include <user.code_libraries>:
    user.code_insert_library("", code_libraries)
    key(end enter)

cycle data type: user.cycle_c_datatype()
show data type: user.current_c_datatype()

put return <number>: "return {number};"
put return negative <number>: "return -{number};"
put return null: "return NULL;"
put return false: "return false;"
put return true: "return true;"
put continue: "continue;"
put break: "break;"

put go to label <user.text>:
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
dock var: user.insert_between("/**< ", ".*/")
dock brief: insert("@brief ")
dock return: insert("@return")
dock param: insert("@param ")
dock in: insert("@param[in] ")
dock out: insert("@param[out] ")
dock in out: insert("@param[in, out] ")
dock file: insert("/** @file */")
