from talon import Context, Module, actions, app, settings

mod = Module()
mod.setting(
    "use_stdint_datatypes ",
    type=int,
    default=1,
    desc="Use the stdint datatype naming in commands by default",
)
mod.list("c_pointers", desc="Common C pointers")
mod.list("c_signed", desc="Common C datatype signed modifiers")
mod.list("c_types", desc="Common C types")
mod.list("c_basic_signed", desc="A list of default C signed operators")
mod.list("c_basic_types", desc="A list of default C datatypes")
mod.list("c_stdint_signed", desc="Common stdint C datatype signed modifiers")
mod.list("c_stdint_types", desc="A list of stdint.h C datatypes")


ctx = Context()
ctx.matches = r"""
mode: user.c

mode: user.auto_lang
and code.language: c
"""

basic_ctx = Context()
basic_ctx.matches = r"""
tag: user.c_basic_datatypes
"""

basic_types = {
    "character": "char",
    "char": "char",
    "short": "short",
    "long": "long",
    "int": "int",
    "integer": "int",
    "void": "void",
    "double": "double",
    "struck": "struct",
    "enumerate": "enum",
    "union": "union",
    "float": "float",
}
basic_signed = {
    "un signed": "unsigned",
}
basic_ctx.lists["user.c_types"] = basic_types
basic_ctx.lists["user.c_signed"] = basic_signed
ctx.lists["user.c_basic_signed"] = basic_signed


stdint_ctx = Context()
stdint_ctx.matches = r"""
tag: user.c_stdint_datatypes
"""
stdint_types = {
    "character": "int8_t",
    "char": "int8_t",
    "short": "int16_t",
    "long": "int32_t",
    "long long": "int64_t",
    "int": "int32_t",
    "integer": "int32_t",
    "void": "void",
    "double": "double",
    "struck": "struct",
    "enumerate": "enum",
    "union": "union",
    "float": "float",
}
stdint_signed = {
    "un signed": "u",
}

stdint_ctx.lists["user.c_types"] = stdint_types
stdint_ctx.lists["user.c_signed"] = stdint_signed
ctx.lists["user.c_stdint_signed"] = stdint_signed


ctx.lists["self.c_pointers"] = {
    "pointer": "*",
    "pointer to pointer": "**",
}


common_types = {
    "static": "static",
    "volatile": "volatile",
    "register": "register",
}

ctx.lists["user.c_stdint_types"] = stdint_types
ctx.lists["user.c_basic_types"] = basic_types

ctx.lists["user.code_libraries"] = {
    "assert": "assert.h",
    "type": "ctype.h",
    "error": "errno.h",
    "float": "float.h",
    "limits": "limits.h",
    "locale": "locale.h",
    "math": "math.h",
    "set jump": "setjmp.h",
    "signal": "signal.h",
    "arguments": "stdarg.h",
    "definition": "stddef.h",
    "input": "stdio.h",
    "output": "stdio.h",
    "library": "stdlib.h",
    "string": "string.h",
    "time": "time.h",
    "standard int": "stdint.h",
    "unix standard": "unistd.h",
}

ctx.lists["user.code_functions"] = {
    "mem copy": "memcpy",
    "mem set": "memset",
    "string cat": "strcat",
    "stir cat": "strcat",
    "stir en cat": "strncat",
    "stir elle cat": "strlcat",
    "stir copy": "strcpy",
    "stir en copy": "strncpy",
    "stir elle copy": "strlcpy",
    "string char": "strchr",
    "string dupe": "strdup",
    "stir dupe": "strdup",
    "stir comp": "strcmp",
    "stir en comp": "strncmp",
    "string len": "strlen",
    "stir len": "strlen",
    "is digit": "isdigit",
    "get char": "getchar",
    "print eff": "printf",
    "es print eff": "sprintf",
    "es en print eff": "sprintf",
    "stir to int": "strtoint",
    "stir to unsigned int": "strtouint",
    "ay to eye": "atoi",
    "em map": "mmap",
    "ma map": "mmap",
    "em un map": "munmap",
    "size of": "sizeof",
    "ef open": "fopen",
    "ef write": "fwrite",
    "ef read": "fread",
    "ef close": "fclose",
    "exit": "exit",
    "signal": "signal",
    "set jump": "setjmp",
    "get op": "getopt",
    "malloc": "malloc",
    "see alloc": "calloc",
    "alloc ah": "alloca",
    "re alloc": "realloc",
    "free": "free",
}


class CLangState:
    def __init__(self, mod):
        self.datatypes = ["c_basic_datatypes", "c_stdint_datatypes"]

        default = "c_basic_datatypes"
        if settings.get("user.use_stdint_datatypes"):
            default = "c_stdint_datatypes"

        index = 0
        for type in self.datatypes:
            if default == type:
                break
            index += 1
        self.datatype_index = index

        for datatype in self.datatypes:
            mod.tag(datatype, desc="Tag for enabling {datatype} datatype")
        self.datatype = self.datatypes[self.datatype_index]
        ctx.tags = [f"user.{self.datatype}"]

    def cycle_datatype(self):
        """Switch between supported datatypes"""
        # actions.mode.disable(f"user.{self.architecture}")
        self.datatype_index += 1
        if self.datatype_index == len(self.datatypes):
            self.datatype_index = 0
        self.datatype = self.datatypes[self.datatype_index]
        ctx.tags = [f"user.{self.datatype}"]
        app.notify(subtitle=f"Cycled to C lang datatype: {self.datatype}")

    def current_datatype(self):
        """Display the current datatype"""
        app.notify(subtitle=f"Current C lang datatype: {self.datatype}")


c_lang_state = CLangState(mod)


@mod.capture(rule="{self.c_pointers}")
def c_pointers(m) -> str:
    "Returns a string"
    return m.c_pointers


@mod.capture(rule="{user.c_signed}")
def c_signed(m) -> str:
    "Returns a string"
    return m.c_signed


@mod.capture(rule="{user.c_types}")
def c_types(m) -> str:
    "Returns a string"
    return m.c_types


@mod.capture(rule="{self.c_basic_types}")
def c_basic_types(m) -> str:
    "Returns a string"
    return m.c_basic_types


@mod.capture(rule="{self.c_stdint_types}")
def c_stdint_types(m) -> str:
    "Returns a string"
    return m.c_stdint_types


@mod.capture(rule="{self.c_basic_signed}")
def c_basic_signed(m) -> str:
    "Returns a string"
    return m.c_basic_signed


@mod.capture(rule="{self.c_stdint_signed}")
def c_stdint_signed(m) -> str:
    "Returns a string"
    return m.c_stdint_signed


@mod.capture(rule="[<user.c_signed>] <user.c_types> [<self.c_pointers>+]")
def c_cast(m) -> str:
    "Returns a string"
    return "(" + " ".join(list(m)) + ")"


@mod.capture(rule="[<self.c_basic_signed>] <self.c_basic_types> [<self.c_pointers>+]")
def c_basic_cast(m) -> str:
    "Returns a string"
    return "(" + " ".join(list(m)) + ")"


@mod.capture(rule="[<self.c_stdint_signed>] <self.c_stdint_types> [<self.c_pointers>+]")
def c_stdint_cast(m) -> str:
    "Returns a string"
    return "(" + "".join(list(m)) + ")"


@mod.capture(rule="[<user.c_signed>] <user.c_types>[<self.c_pointers>]")
def c_variable(m) -> str:
    "Returns a string"
    if hasattr(m, 'c_signed') and len(m.c_signed) == 1:
        return m.c_signed + " ".join(list(m[1:]))
    else:
        return " ".join(list(m))


@ctx.action_class("user")
class UserActions:
    def code_operator_indirection():           actions.auto_insert('*')
    def code_operator_address_of():            actions.auto_insert('&')
    def code_operator_structure_dereference(): actions.auto_insert('->')
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
    #action(user.code_operator_exponent): " ** "
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
    def code_operator_and():                             actions.auto_insert(' && ')
    def code_operator_or():                              actions.auto_insert(' || ')
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
    def code_insert_null():                                     actions.auto_insert('NULL')
    def code_insert_is_null():                                  actions.auto_insert(' == NULL ')
    def code_insert_is_not_null():                              actions.auto_insert(' != NULL')
    def code_state_if():
        actions.insert('if () {\n}\n')
        actions.key('up:2 left:3')
    def code_state_else_if():
        actions.insert('else if () {\n}\n')
        actions.key('up:2 left:3')
    def code_state_else():
        actions.insert('else\n{\n}\n')
        actions.key('up:2')
    def code_state_switch():
        actions.insert('switch ()')
        actions.edit.left()
    def code_state_case():
        actions.insert('case \nbreak;')
        actions.edit.up()
    def code_state_for():   actions.auto_insert('for ')
    def code_state_go_to(): actions.auto_insert('goto ')
    def code_state_while():
        actions.insert('while ()')
        actions.edit.left()
    def code_state_return():    actions.auto_insert('return ')
    def code_break():           actions.auto_insert('break;')
    def code_next():            actions.auto_insert('continue;')
    def code_insert_true():            actions.auto_insert('true')
    def code_insert_false():           actions.auto_insert('false')
    def code_comment_line_prefix(): actions.auto_insert('//')

    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()

    # TODO - it would be nice that you integrate that types from c_basic_cast
    # instead of defaulting to void
    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_private_static_function(text: str):
        """Inserts private static function"""
        result = "static void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_insert_library(text: str, selection: str):
        actions.user.paste("#include <{}>".format(selection))

    def code_import():
        """Inserts an empty include line for the selected library header"""
        actions.user.paste("include <>")
        actions.edit.left()

    def code_import_local():
        """Inserts an empty include line for the selected local header"""
        actions.user.paste('include ""')
        actions.edit.left()


@mod.action_class
class Actions:
    def cycle_c_datatype():
        """Switch to the next datatype mode"""
        global c_lang_state
        c_lang_state.cycle_datatype()

    def current_c_datatype():
        """display next datatype mode"""
        global c_lang_state
        c_lang_state.current_datatype()

