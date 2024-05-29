tag: user.code_types
-

# for generic reference of types
(type | put) [type] <user.code_type>: insert(code_type)
# TODO: It would be nice if this was nestable, so we could say something like:
# put result of vector of you eight and box of dine error
# and get: Result<Vec<u8>, Box<dyn Error>>
put <user.code_containing_type> of [<user.code_type>]:
    type = user.code_type or ""
    insert("{code_containing_type}<{type}>")

# TODO: The should have single versions that encapsulate the containing type style
# for annotating function parameters
is type <user.code_type>: user.code_insert_type_annotation(code_type)

# FIXME: The containing part is probably language specific so may need to be made and overwrite
is type <user.code_containing_type> of <user.code_type>:
    return_type = "{code_containing_type}<{code_type}>"
    user.code_insert_type_annotation(return_type)

(type | put) {user.code_function_modifier} <user.code_type>:
    user.code_modified_function(code_function_modifier_list or 0, text)
    insert(code_type)
