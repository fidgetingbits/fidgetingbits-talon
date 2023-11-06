import re

from talon import Context, Module, actions, clip, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
code.language: python
"""

# https://docs.python.org/3/library/functions.html
builtin_functions = {
    "abs": "abs",
    "all": "all",
    "any": "any",
    "ascii": "ascii",
    "bin": "bin",
    "bool": "bool",
    "breakpoint": "breakpoint",
    "byte array": "bytearray",
    "bytes": "bytes",
    "callable": "callable",
    "char": "chr",
    "class method": "classmethod",
    "compile": "compile",
    "complex": "complex",
    "delete attribute": "delattr",
    "dict": "dict",
    "dir": "dir",
    "divmod": "divmod",
    "enumerate": "enumerate",
    "eval": "eval",
    "exec": "exec",
    "filter": "filter",
    "float": "float",
    "format": "format",
    "frozen set": "frozenset",
    "get attribute": "getattr",
    "globals": "globals",
    "has attribute": "hasattr",
    "hash": "hash",
    "help": "help",
    "hex": "hex",
    "I D": "id",
    "input": "input",
    "int": "int",
    "is instance": "isinstance",
    "is subclass": "issubclass",
    "iter": "iter",
    "len": "len",
    "list": "list",
    "locals": "locals",
    "map": "map",
    "max": "max",
    "memory view": "memoryview",
    "min": "min",
    "next": "next",
    "object": "object",
    "octal": "oct",
    "open": "open",
    "ord": "ord",
    "power": "pow",
    "print": "print",
    "property": "property",
    "range": "range",
    "rep er": "repr",
    "reversed": "reversed",
    "round": "round",
    "set": "set",
    "set attribute": "setattr",
    "slice": "slice",
    "sorted": "sorted",
    "static method": "staticmethod",
    "str": "str",
    "sum": "sum",
    "super": "super",
    "tuple": "tuple",
    "type": "type",
    "vars": "vars",
    "zip": "zip",
    "import": "__import__",
}
# https://www.w3schools.com/python/python_ref_string.asp
string_functions = {
    "split lines": "splitlines",
    "capitalize": "capitalize",
    "is lower": "islower",
    "is upper": "isupper",
}

common_functions = {
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
    "path": "pathlib.Path",
}
ctx.lists["user.code_common_function"] = {
    **builtin_functions,
    **common_functions,
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
    "base sixty four": "base64",
    "pie test": "pytest",
    "inspect": "inspect",
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
    "byte array": "bytearray",
    "sequence": "Sequence",
    "callable": "Callable",
    "list": "List",
    "no return": "NoReturn",
}

ctx.lists["user.code_keyword"] = {
    "break": "break",
    "continue": "continue",
    "class": "class ",
    "return": "return ",
    "import": "import ",
    "null": "None",
    "none": "None",
    "true": "True",
    "false": "False",
    "yield": "yield ",
    "from": "from ",
    "pass": "pass",
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

decorator_list = [
    "classmethod",
    "property",
    "staticmethod",
    "abstractmethod",
    "wraps",
    "abstractproperty",
]
mod.list("python_decorator", desc="python decorator")
ctx.lists["user.python_decorator"] = {
    " ".join(re.findall("[A-Z][^A-Z]*", decorator)).lower(): decorator
    for decorator in decorator_list
}


@mod.capture(rule="{self.code_type}")
def python_type_list(m) -> str:
    "Returns a string"
    return m.code_type


@mod.capture(rule="{self.python_docstring_fields}")
def python_docstring_fields(m) -> str:
    "Returns a string"
    return m.python_docstring_fields


@ctx.action_class("user")
class UserActions:
    def code_operator_lambda():
        actions.user.insert_between("lambda ", ": ")

    def code_operator_subscript():
        actions.user.insert_between("[", "]")

    def code_operator_assignment():
        actions.auto_insert(" = ")

    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_subtraction_assignment():
        actions.auto_insert(" -= ")

    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_addition_assignment():
        actions.auto_insert(" += ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    def code_operator_multiplication_assignment():
        actions.auto_insert(" *= ")

    def code_operator_exponent():
        actions.auto_insert(" ** ")

    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_division_assignment():
        actions.auto_insert(" /= ")

    def code_operator_modulo():
        actions.auto_insert(" % ")

    def code_operator_modulo_assignment():
        actions.auto_insert(" %= ")

    def code_operator_equal():
        actions.auto_insert(" == ")

    def code_operator_not_equal():
        actions.auto_insert(" != ")

    def code_operator_greater_than():
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(" >= ")

    def code_operator_less_than():
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(" <= ")

    def code_operator_and():
        actions.auto_insert(" and ")

    def code_operator_or():
        actions.auto_insert(" or ")

    def code_operator_in():
        actions.auto_insert(" in ")

    def code_operator_not_in():
        actions.auto_insert(" not in ")

    def code_operator_bitwise_and():
        actions.auto_insert(" & ")

    def code_operator_bitwise_and_assignment():
        actions.auto_insert(" &= ")

    def code_operator_bitwise_or():
        actions.auto_insert(" | ")

    def code_operator_bitwise_or_assignment():
        actions.auto_insert(" |= ")

    def code_operator_bitwise_exclusive_or():
        actions.auto_insert(" ^ ")

    def code_operator_bitwise_exclusive_or_assignment():
        actions.auto_insert(" ^= ")

    def code_operator_bitwise_left_shift():
        actions.auto_insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.auto_insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.auto_insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.auto_insert(" >>= ")

    def code_self():
        actions.auto_insert("self")

    def code_operator_object_accessor():
        actions.auto_insert(".")

    def code_insert_null():
        actions.auto_insert("None")

    def code_insert_is_null():
        actions.auto_insert(" is None")

    def code_insert_is_not_null():
        actions.auto_insert(" is not None")

    def code_state_if():
        actions.user.insert_between("if ", ":")

    def code_state_else_if():
        actions.user.insert_between("elif ", ":")

    def code_state_else():
        actions.insert("else:")
        actions.key("enter")

    def code_state_switch():
        actions.user.insert_between("match ", ":")

    def code_state_case():
        actions.user.insert_between("case ", ":")

    def code_state_for():
        actions.auto_insert("for ")

    def code_state_for_each():
        actions.user.insert_between("for ", " in ")

    def code_state_while():
        actions.user.insert_between("while ", ":")

    def code_define_class():
        actions.auto_insert("class ")

    def code_import():
        actions.auto_insert("import ")

    def code_comment_line_prefix():
        actions.auto_insert("# ")

    def code_state_return():
        actions.insert("return ")

    def code_insert_true():
        actions.auto_insert("True")

    def code_insert_false():
        actions.auto_insert("False")

    def code_comment_documentation():
        actions.user.insert_between('"""', '"""')

    def code_insert_function(text: str, selection: str):
        text += f"({selection or ''})"
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
