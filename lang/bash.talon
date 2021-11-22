mode: user.bash
mode: command
and code.language: bash
-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_generic
settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_protected_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

call interpreter: "#!/bin/sh\n"
(new sub|state) command: "$()"
(new|state) expression: "$(())"
# XXX
parameter:
    insert("${}")
    edit.left()

    # XXX - check how other talon files invoke variable names
state [empty] (variable|var):
    insert("${}")
    key(left)

    # XXX - check how other talon files invoke variable names
state (variable|var) <user.text>$:
    insert("${}")
    edit.left()
    snake_text = user.formatted_text(text, "snake")
    upper_text = user.formatted_text(snake_text, "upper")
    insert(upper_text)

state echo: "echo "

# XXX will overlap somewhat with core shell commands use terminals, show me one
# to combine somehow
copy file:
    insert("cp ")

recursive copy file:
    insert("cp -R ")

state redirect out: "1>&2"
state redirect error: "2>&1"
