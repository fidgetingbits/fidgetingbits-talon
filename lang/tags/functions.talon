tag: user.code_functions
-
# TODO: these scopes should be named as some sort of scope rather than in a list named function,

# Default implementation of capture listens for the following keywords in any
# order: private pro pub static
#
# The default action implementation looks for the token combination on the left
# (funky is added here for searchability) and calls the function on the right:
#
#   * funky -> code_default_function
#   * private funky -> code_private_function
#   * pro funky -> code_protected_function
#   * pub funky -> code_public_function
#   * static funky -> code_private_static_function
#   * private static funky -> code_private_static_function
#   * pro static funky -> code_protected_static_function
#   * pub static funky -> code_public_static_function
#
put new [{user.code_function_modifier}] (funk | function) <user.text>$:
    user.code_modified_function(code_function_modifier_list or 0, text)

[put] returns [type] <user.code_type>: user.code_insert_return_type(code_type)
[put] returns <user.code_containing_type> of <user.code_type>:
    return_type = "{code_containing_type}<{code_type}>"
    user.code_insert_return_type(return_type)

