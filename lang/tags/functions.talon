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
^{user.code_function_modifier}* function <user.text>$:
    user.code_modified_function(code_function_modifier_list or 0, text)

# TODO: The should have single versions that encapsulate the containing type style
# for annotating function parameters
is type <user.code_type>: user.code_insert_type_annotation(code_type)
is type <user.code_containing_type> of <user.code_type>: 
    return_type = "{code_containing_type}<{code_type}>"
    user.code_insert_type_annotation(return_type)

returns [type] <user.code_type>: user.code_insert_return_type(code_type)
returns <user.code_containing_type> of <user.code_type>: 
    return_type = "{code_containing_type}<{code_type}>"
    user.code_insert_return_type(return_type)

# for generic reference of types
(type|put) <user.code_type>: insert(code_type)
put <user.code_containing_type> of <user.code_type>: 
    insert("{code_containing_type}<{code_type}>")

(type|put) {user.code_function_modifier} <user.code_type>: 
    user.code_modified_function(code_function_modifier_list or 0, text)
    insert(code_type)