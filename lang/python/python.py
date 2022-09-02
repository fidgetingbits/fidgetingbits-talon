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
    "len": "len",
    "list": "list",
    "print": "print",
    "range": "range",
    "set": "set",
    "split": "split",
    "string": "str",
    "update": "update",
    "help": "help",
    "starts with": "startswith",

    # sys
    "exit": "sys.exit",

    # os
    "get U I D": "os.getuid",

    # gdb
    "G D B execute": "gdb.execute",

    # pathlib
    "path": "pathlib.Path"

}

ctx.lists["user.code_libraries"] = {
    "a sink": "asyncio",
    "arg parse": "argparse",
    "bin ask E": "bitascii",
    "click": "click",
    "docker": "docker",
    "funk tools": "functools",
    "get pass": "getpass",
    "glob": "glob",
    "G D B": "gdb",
    "git lab": "gitlab",
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
    "requests": "requests",
    "shell utils": "shutil",
    "shlacks": "shlex",
    "socket": "socket",
    "string": "string",
    "struct": "struct",
    "subprocess": "subprocess",
    "system": "sys",
    "tar file": "tarfile",
    "temp file": "tempfile",
    "threading": "threading",
    "time": "time",
    "trace back": "traceback",
    "unit test": "unittest",
    "warnings": "warnings",
    "date time": "datetime",
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

ctx.lists["user.code_type"] = {
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
    def code_operator_subscript():
        actions.insert("[]")
        actions.key("left")

    def code_operator_assignment():
        actions.insert(" = ")

    def code_operator_subtraction():
        actions.insert(" - ")

    def code_operator_subtraction_assignment():
        actions.insert(" -= ")

    def code_operator_addition():
        actions.insert(" + ")

    def code_operator_addition_assignment():
        actions.insert(" += ")

    def code_operator_multiplication():
        actions.insert(" * ")

    def code_operator_multiplication_assignment():
        actions.insert(" *= ")

    def code_operator_exponent():
        actions.insert(" ** ")

    def code_operator_division():
        actions.insert(" / ")

    def code_operator_division_assignment():
        actions.insert(" /= ")

    def code_operator_modulo():
        actions.insert(" % ")

    def code_operator_modulo_assignment():
        actions.insert(" %= ")

    def code_operator_equal():
        actions.insert(" == ")

    def code_operator_not_equal():
        actions.insert(" != ")

    def code_operator_greater_than():
        actions.insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.insert(" >= ")

    def code_operator_less_than():
        actions.insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.insert(" <= ")

    def code_operator_and():
        actions.insert(" and ")

    def code_operator_or():
        actions.insert(" or ")

    def code_operator_bitwise_and():
        actions.insert(" & ")

    def code_operator_bitwise_and_assignment():
        actions.insert(" &= ")

    def code_operator_bitwise_or():
        actions.insert(" | ")

    def code_operator_bitwise_or_assignment():
        actions.insert(" |= ")

    def code_operator_bitwise_exclusive_or():
        actions.insert(" ^ ")

    def code_operator_bitwise_exclusive_or_assignment():
        actions.insert(" ^= ")

    def code_operator_bitwise_left_shift():
        actions.insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.insert(" >>= ")

    def code_self():
        actions.insert("self")

    def code_operator_object_accessor():
        actions.insert(".")

    def code_insert_null():
        actions.insert("None")

    def code_insert_is_null():
        actions.insert(" is None")

    def code_insert_is_not_null():
        actions.insert(" is not None")

    def code_state_if():
        actions.insert("if :")
        actions.key("left")

    def code_state_else_if():
        actions.insert("elif :")
        actions.key("left")

    def code_state_else():
        actions.insert("else:")
        actions.key("enter")

    def code_state_switch():
        actions.insert("match :")
        actions.edit.left()

    def code_state_case():
        actions.insert("case :")
        actions.edit.left()

    def code_state_for():
        actions.insert("for ")

    def code_state_for_each():
        actions.insert("for in ")
        actions.key("left")
        actions.edit.word_left()
        actions.key("space")
        actions.edit.left()

    def code_state_while():
        actions.insert("while :")
        actions.edit.left()

    def code_define_class():
        actions.insert("class ")

    def code_import():
        actions.insert("import ")

    def code_comment_line_prefix():
        actions.insert("# ")

    def code_state_return():
        actions.insert("return ")

    def code_break():
        actions.insert("break")

    def code_insert_true():
        actions.insert("True")

    def code_insert_false():
        actions.insert("False")

    def code_comment_documentation():
        actions.user.insert_cursor('"""[|]"""')

    def code_insert_function(text: str, selection: str):

        formatted_text = actions.user.formatted_text(
            text, settings.get("user.code_private_function_formatter")
        )

        if selection:
            result = formatted_text + "({})".format(selection)
        else:
            result = formatted_text + "()"
        actions.user.paste(result)
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

    def code_insert_type_annotation(type: str):
        actions.insert(f": {type}")

    def code_insert_return_type(type: str):
        actions.insert(f" -> {type}")


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
