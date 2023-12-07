code.language: bash
-
tag(): user.code_imperative

# XXX - this might be missing some since the split of operators
tag(): user.code_comment_line
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_libraries
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_math

settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_protected_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

# NOTE: If using cursorless/snippets also check those out for general building blocks

put command: "$()"
put expression: "$(())"

put [empty] (variable | var): user.insert_between("${", "}")

put [big] (variable | var) <user.text>$:
    user.insert_between("${", "}")
    snake_text = user.formatted_text(text, "snake")
    upper_text = user.formatted_text(snake_text, "upper")
    insert(upper_text)

put small (variable | var) <user.text>$:
    user.insert_between("${", "}")
    snake_text = user.formatted_text(text, "snake")
    insert(upper_text)

put echo: "echo "

copy file: insert("cp ")

recursive copy file: insert("cp -R ")

put out to error: "1>&2"
put error to out: "2>&1"
put error to null: "2>/dev/null"
put read key press: "read -r -n 1 -s\n"
