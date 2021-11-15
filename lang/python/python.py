import re

from talon import Context, Module, actions, settings, clip

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: command
and tag: user.python

mode: command
and code.language: python
"""
ctx.lists["user.code_functions"] = {
    "enumerate": "enumerate",
    "integer": "int",
    "length": "len",
    "list": "list",
    "print": "print",
    "range": "range",
    "set": "set",
    "split": "split",
    "string": "str",
    "update": "update",
    "help": "help",
}

ctx.lists["user.code_libraries"] = {
    "a sink": "asyncio",
    "arg parse": "argparse",
    "bin ask E": "bitascii",
    "click": "click",
    "docker": "docker",
    "funk tools": "functools",
    "get pass": "getpass",
    "hash lib": "hashlib",
    "heck stump": "hexdump",
    "import lib": "importlib",
    "jason": "json",
    "logging": "logging",
    "multiprocessing": "multiprocessing",
    "os": "os",
    "path lib": "pathlib",
    "pea expect": "pexpect",
    "pretty print": "pprint",
    "random": "random",
    "reg ex": "re",
    "shell utils": "shutil",
    "socket": "socket",
    "string": "string",
    "struct": "struct",
    "subprocess": "subprocess",
    "system": "sys",
    "tar file": "tarfile",
    "threading": "threading",
    "time": "time",
    "trace back": "traceback",
    "unit test": "unittest",
    "warnings": "warnings",
}


"""a set of fields used in python docstrings that will follow the
reStructuredText format"""
docstring_fields = {
    "class": ":class:",
    "function": ":func:",
    "parameter": ":param:",
    "param": ":param:",
    "raise": ":raise:",
    "returns": ":return:",
    "type": ":type:",
    "return type": ":rtype:",
    # these are sphinx-specific
    "see also": ".. seealso:: ",
    "notes": ".. notes:: ",
    "warning": ".. warning:: ",
    "todo": ".. todo:: ",
}

mod.list("python_docstring_fields", desc="python docstring fields")
ctx.lists["user.python_docstring_fields"] = docstring_fields

type_list = {
    "boolean": "bool",
    "integer": "int",
    "string": "str",
    "none": "None",
    "dick": "Dict",
    "float": "float",
    "any": "Any",
    "tuple": "Tuple",
    "union": "UnionAny",
    "iterable": "Iterable",
    "vector": "Vector",
    "bytes": "bytes",
    "sequence": "Sequence",
    "callable": "Callable",
    "list": "List",
    "no return": "NoReturn",
}

mod.list("python_type_list", desc="python types")
ctx.lists["user.python_type_list"] = type_list

exception_list = [
    "BaseException",
    "SystemExit",
    "KeyboardInterrupt",
    "GeneratorExit",
    "Exception",
    "StopIteration",
    "StopAsyncIteration",
    "ArithmeticError",
    "FloatingPointError",
    "OverflowError",
    "ZeroDivisionError",
    "AssertionError",
    "AttributeError",
    "BufferError",
    "EOFError",
    "ImportError",
    "ModuleNotFoundError",
    "LookupError",
    "IndexError",
    "KeyError",
    "MemoryError",
    "NameError",
    "UnboundLocalError",
    "OSError",
    "BlockingIOError",
    "ChildProcessError",
    "ConnectionError",
    "BrokenPipeError",
    "ConnectionAbortedError",
    "ConnectionRefusedError",
    "ConnectionResetError",
    "FileExistsError",
    "FileNotFoundError",
    "InterruptedError",
    "IsADirectoryError",
    "NotADirectoryError",
    "PermissionError",
    "ProcessLookupError",
    "TimeoutError",
    "ReferenceError",
    "RuntimeError",
    "NotImplementedError",
    "RecursionError",
    "SyntaxError",
    "IndentationError",
    "TabError",
    "SystemError",
    "TypeError",
    "ValueError",
    "UnicodeError",
    "UnicodeDecodeError",
    "UnicodeEncodeError",
    "UnicodeTranslateError",
    "Warning",
    "DeprecationWarning",
    "PendingDeprecationWarning",
    "RuntimeWarning",
    "SyntaxWarning",
    "UserWarning",
    "FutureWarning",
    "ImportWarning",
    "UnicodeWarning",
    "BytesWarning",
    "ResourceWarning",
]
mod.list("python_exception", desc="python exceptions")
ctx.lists["user.python_exception"] = {
    " ".join(re.findall("[A-Z][^A-Z]*", exception)).lower(): exception
    for exception in exception_list
}

decorator_list = ["classmethod", "property", "staticmethod"]
mod.list("python_decorator", desc="python decorator")
ctx.lists["user.python_decorator"] = {
    " ".join(re.findall("[A-Z][^A-Z]*", decorator)).lower(): decorator
    for decorator in decorator_list
}


@mod.capture(rule="{self.python_type_list}")
def python_type_list(m) -> str:
    "Returns a string"
    return m.python_type_list


@mod.capture(rule="{self.python_docstring_fields}")
def python_docstring_fields(m) -> str:
    "Returns a string"
    return m.python_docstring_fields


@ctx.action_class("user")
class UserActions:
    def code_operator_indirection():           actions.auto_insert('')
    def code_operator_address_of():            actions.auto_insert('')
    def code_operator_structure_dereference(): actions.auto_insert('')
    def code_operator_lambda():                actions.auto_insert('')
    def code_operator_subscript():
        actions.insert('[]')
        actions.key('left')
    def code_operator_assignment():                      actions.auto_insert(' = ')
    def code_operator_subtraction():                     actions.auto_insert(' - ')
    def code_operator_subtraction_assignment():          actions.auto_insert(' -= ')
    def code_operator_addition():                        actions.auto_insert(' + ')
    def code_operator_addition_assignment():             actions.auto_insert(' += ')
    def code_operator_multiplication():                  actions.auto_insert(' * ')
    def code_operator_multiplication_assignment():       actions.auto_insert(' *= ')
    def code_operator_exponent():                        actions.auto_insert(' ** ')
    def code_operator_division():                        actions.auto_insert(' / ')
    def code_operator_division_assignment():             actions.auto_insert(' /= ')
    def code_operator_modulo():                          actions.auto_insert(' % ')
    def code_operator_modulo_assignment():               actions.auto_insert(' %= ')
    def code_operator_equal():                           actions.auto_insert(' == ')
    def code_operator_not_equal():                       actions.auto_insert(' != ')
    def code_operator_greater_than():                    actions.auto_insert(' > ')
    def code_operator_greater_than_or_equal_to():        actions.auto_insert(' >= ')
    def code_operator_less_than():                       actions.auto_insert(' < ')
    def code_operator_less_than_or_equal_to():           actions.auto_insert(' <= ')
    def code_operator_and():                             actions.auto_insert(' and ')
    def code_operator_or():                              actions.auto_insert(' or ')
    def code_operator_bitwise_and():                     actions.auto_insert(' & ')
    def code_operator_bitwise_and_assignment():          actions.auto_insert(' &= ')
    def code_operator_bitwise_or():                      actions.auto_insert(' | ')
    def code_operator_bitwise_or_assignment():           actions.auto_insert(' |= ')
    def code_operator_bitwise_exclusive_or():            actions.auto_insert(' ^ ')
    def code_operator_bitwise_exclusive_or_assignment(): actions.auto_insert(' ^= ')
    def code_operator_bitwise_left_shift():              actions.auto_insert(' << ')
    def code_operator_bitwise_left_shift_assignment():   actions.auto_insert(' <<= ')
    def code_operator_bitwise_right_shift():             actions.auto_insert(' >> ')
    def code_operator_bitwise_right_shift_assignment():  actions.auto_insert(' >>= ')
    def code_self():                                     actions.auto_insert('self')
    def code_null():                                     actions.auto_insert('None')
    def code_is_null():                                  actions.auto_insert(' is None')
    def code_is_not_null():                              actions.auto_insert(' is not None')
    def code_state_if():
        actions.insert('if :')
        actions.key('left')
    def code_state_else_if():
        actions.insert('elif :')
        actions.key('left')
    def code_state_else():
        actions.insert('else:')
        actions.key('enter')
    def code_state_switch():
        actions.insert('switch ()')
        actions.edit.left()
    def code_state_case():
        actions.insert('case \nbreak;')
        actions.edit.up()
    def code_state_for(): actions.auto_insert('for ')
    def code_state_for_each():
        actions.insert('for in ')
        actions.key('left')
        actions.edit.word_left()
        actions.key('space')
        actions.edit.left()
    def code_state_while():
        actions.insert('while :')
        actions.edit.left()
    def code_type_class(): actions.auto_insert('class ')
    def code_import():     actions.auto_insert('import ')
    def code_from_import():
        actions.insert('from import ')
        actions.key('left')
        actions.edit.word_left()
        actions.key('space')
        actions.edit.left()
    def code_comment(): actions.auto_insert('# ')
    def code_state_return():
        actions.insert('return ')
    def code_true():            actions.auto_insert('True')
    def code_false():           actions.auto_insert('False')
    def code_document_string(): actions.user.insert_cursor('"""[|]"""')
    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"
        actions.user.paste(text)
        actions.edit.left()

    def code_default_function(text: str):
        actions.user.code_public_function(text)

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "def _{}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_public_function(text: str):
        result = "def {}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_insert_library(text: str, selection: str):
        actions.user.paste(f"import {text}")



@mod.action_class
class module_actions:
    # TODO this could go somewhere else
    def insert_cursor(text: str):
        """Insert a string. Leave the cursor wherever [|] is in the text"""
        if "[|]" in text:
            end_pos = text.find("[|]")
            s = text.replace("[|]", "")
            actions.insert(s)
            actions.key(f"left:{len(s) - end_pos}")
        else:
            actions.insert(text)

    def insert_cursor_paste(text1: str, text2: str):
        """Insert a string, . Leave the cursor after text1"""
        if "[|]" in text1:
            end_pos = text1.find("[|]")
            text1 = text1.replace("[|]", "")
        else:
            end_pos = len(text1)
        s = text1 + clip.get() + text2
        actions.insert(s)
        actions.key(f"left:{len(s) - end_pos}")

    # Non overrides
    def assign_variable(text: str):
        """Assign to a variable"""
        # XXX - This should use a variable naming formatter
        result = actions.user.formatted_text(
            text, settings.get("user.code_private_function_formatter")
        )

        actions.user.paste(result)
        actions.user.code_operator_assignment()


    # Non overrides
    def append_variable(text: str):
        """Append to a variable"""
        # XXX - This should use a variable naming formatter
        result = actions.user.formatted_text(
            text, settings.get("user.code_private_function_formatter")
        )

        actions.user.paste(result)
        actions.user.code_operator_addition_assignment()
