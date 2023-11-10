code.language: python
-
tag(): user.code_imperative
tag(): user.code_object_oriented

tag(): user.code_comment_documentation
tag(): user.code_comment_line
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_keywords
tag(): user.code_libraries
tag(): user.code_libraries_gui
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_lambda
tag(): user.code_operators_math

settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_protected_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

####
# Operators
####
empty dict: "{}"
empty list: "()"
word (dickt | dictionary): "dict"
state (def | deaf | deft): "def "
class <user.text>:
    insert("class ")
    insert(user.formatted_text(text, "hammer"))
    insert("():\n")
dunder in it: "__init__"
state try: "try:\n"
state except: "except "
state except clip:
    insert("except ")
    edit.paste()
state raise: "raise "
state continue: "continue"
self taught: "self."
state for in:
    insert("for in ")
    key(left)
    edit.word_left()
    key(space)
    edit.left()
half dock string: key(":3)
big dock string:
    key(":3)
    key(enter:2)
    key(":3)
    edit.up()

####
# Keywords
####
return: "return "
return none: "return None"
return true: "return True"
return false: "return False"
state none: "None"
true: "True"
false: "False"
#pass: "pass"
self dot: "self,"

index <user.word>: '["{word}"]'
index (var | variable) <user.text>:
    var = user.formatted_text(text, "snake")
    insert("[{var}]")

pie test: "pytest"
# for things like None comparsion
state is not: " is not "
state is: " is "
state is none: " is None"
state as string: '.decode("utf-8")'
state as bytes: '.encode("utf-8")'
[put] F string: user.insert_between('f"', '"')
[put] F [string] arg: user.insert_between('f"{', '}"')
raw string: user.insert_between('r"', '"')

^init <user.text>$:
    var = user.formatted_text(text, "snake")
    insert("self.{var} = {var}")

[state] raise {user.python_exception}:
    user.insert_between("raise {python_exception}(", ")")
[state] except {user.python_exception}: "except {python_exception}:"
[state] except {user.python_exception} as:
    user.insert_cursor("except {python_exception} as [|]:")

# function # for annotating function parameters
is type {user.code_type}: insert(": {code_type}")
returns [type] {user.code_type}: insert(" -> {code_type}")
# for generic reference of types
type {user.code_type}: insert("{code_type}")

# decorators
(deck | put) {user.python_decorator}: insert("@{python_decorator}")

dock string: user.code_comment_documentation()
dock {user.python_docstring_fields}:
    insert("{python_docstring_fields}")
    edit.left()
    insert(" ")
dock type {user.code_type}: user.insert_between(":type ", ": {code_type}")
dock returns type {user.code_type}: user.insert_between(":rtype ", ": {code_type}")

toggle imports: user.code_toggle_libraries()
import <user.code_libraries>:
    user.code_insert_library(code_libraries, "")
    key(end)

from import: user.insert_between("from ", " import ")
from <user.code_libraries> import:
    insert("from ")
    user.code_insert_library(code_libraries, "")
    insert(" import ")

# XXX - it would be good to have a set of common overrides?
funk bug:
    insert('print(f"!!! ")')
    key(left:2)
funk pretty print:
    insert("pp.pprint()")
    key(left)

assign to <user.text>: user.assign_variable(text)

append to <user.text>: user.append_variable(text)

pack little byte: user.insert_cursor('struct.pack("<B", [|])')
pack big byte: user.insert_cursor('struct.pack(">B", [|])')
pack little word: user.insert_cursor('struct.pack("<H", [|])')
pack big word: user.insert_cursor('struct.pack(">H", [|])')
pack little int: user.insert_cursor('struct.pack("<I", [|])')
pack big int: user.insert_cursor('struct.pack(">I", [|])')
pack little long: user.insert_cursor('struct.pack("<Q"", [|])')
pack big long: user.insert_cursor('struct.pack(">Q"", [|])')

state arg <number>: "sys.argv[{number}]"
state arg count: "len(sys.argv)"
