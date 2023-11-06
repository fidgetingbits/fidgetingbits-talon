code.language: bpftrace
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

block:
    insert("{\n\n}")
    key(up)

[state] type <user.bpftrace_types>: "{bpftrace_types}"
cast to <user.bpftrace_cast>: "{bpftrace_cast}"
<user.bpftrace_pointers>: "{bpftrace_pointers}"
<user.bpftrace_signed>: "{bpftrace_signed}"
probe {user.bpftrace_probes}: "{user.bpftrace_probes}:"
state array:
    insert("@[]")
    edit.left()
state global: "@"
state local: "$"
state define: "#define "
state include system:
    insert("#include <>")
    edit.left()

state filter:
    insert("//")
    edit.left()

state filter {user.bpftrace_builtins}:
    insert("/{bpftrace_builtins} /")
    edit.left()

global {user.bpftrace_builtins}: "{bpftrace_builtins}"
