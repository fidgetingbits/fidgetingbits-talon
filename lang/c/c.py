from talon import Context, Module, actions, app, settings

mod = Module()
mod.setting(
    "use_stdint_datatypes",
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
mod.list("c_signals", desc="Common C signals")
mod.list("c_errors", desc="Common C errors")


ctx = Context()
ctx.matches = r"""
tag: user.c
"""

basic_ctx = Context()
basic_ctx.matches = r"""
tag: user.c_basic_datatypes
"""

common_types = {
    "enumerate": "enum",
    "float": "float",
    "struck": "struct",
    "union": "union",
    "void": "void",
    "size T": "size_t",
    "S size T": "ssize_t",
    "double": "double",
    "pid": "pid_t",
    "file": "FILE",
    "G I D": "gid_t",
    "U I D": "uid_t",
    "offset": "off_t",
    "offset sixty four": "off64_t",
    "time": "time_t",
    "mode": "mode_t",
    "sig info": "siginfo_t",
    "sig set": "sigset_t",
    "V A list": "va_list",
    "boole": "bool",
    "boolean": "bool",
    "clock": "clock_t",
    "pointer": "intptr_t",
}

basic_types_ints = {
    "character": "char",
    "char": "char",
    "integer": "int",
    "int": "int",
    "long": "long",
    "short": "short",
}
basic_signed = {
    "un signed": "unsigned",
}
basic_types = {**basic_types_ints, **common_types}
basic_ctx.lists["user.c_types"] = basic_types
basic_ctx.lists["user.c_signed"] = basic_signed
ctx.lists["user.c_basic_signed"] = basic_signed


stdint_ctx = Context()
stdint_ctx.matches = r"""
tag: user.c_stdint_datatypes
"""
stdint_types_ints = {
    "short": "int16_t",
    "integer": "int32_t",
    "int": "int32_t",
    "long": "int64_t",
    "character": "char",
    "char": "char",
    "byte": "int8_t",
}

stdint_signed = {
    "un signed": "u",
    "unsigned": "u",
    "signed": "",  # this just helps in case we say it
}

stdint_types = {**stdint_types_ints, **common_types}

stdint_ctx.lists["user.c_types"] = stdint_types
stdint_ctx.lists["user.c_signed"] = stdint_signed
ctx.lists["user.c_stdint_signed"] = stdint_signed


ctx.lists["self.c_pointers"] = {
    "pointer": "*",
    "pointer to pointer": "**",
}


common_types = {
    "register": "register",
    "static": "static",
    "volatile": "volatile",
    "const": "const",
    "constant": "const",
    "external": "extern",
    "extern": "extern",
}

ctx.lists["user.c_stdint_types"] = stdint_types
ctx.lists["user.c_basic_types"] = basic_types

ctx.lists["user.code_libraries"] = {
    "arba I net": "arpa/inet.h",
    "assert": "assert.h",
    "type": "ctype.h",
    "error": "err.h",
    "err no": "errno.h",
    "error numbers": "errno.h",
    "F control": "fcntl.h",
    "file control": "fcntl.h",
    "float": "float.h",
    "fuse": "fuse.h",
    "fuse low level": "fuse_lowlevel.h",
    "key utils": "keyutils.h",
    "limits": "limits.h",
    "key control": "linux/keyctl.h",
    "localization": "locale.h",
    "math": "math.h",
    "poll": "poll.h",
    "P thread": "pthread.h",
    "threading": "pthread.h",
    "password": "pwd.h",
    "schedule": "sched.h",
    "set jump": "setjmp.h",
    "signal": "signal.h",
    "arguments": "stdarg.h",
    "definition": "stddef.h",
    "standard deaf": "stddef.h",
    "standard int": "stdint.h",
    "standard I O": "stdio.h",
    "standard lib": "stdlib.h",
    "standard library": "stdlib.h",
    "string": "string.h",
    "event F D": "sys/eventfd.h",
    "sys event F D": "sys/eventfd.h",
    "system I P C": "sys/ipc.h",
    "sys I P C": "sys/ipc.h",
    "memory management": "sys/mman.h",
    "sys M man": "sys/mman.h",
    "M map": "sys/mman.h",
    "system message": "sys/msg.h",
    "sys message": "sys/msg.h",
    "system parameters": "sys/param.h",
    "sys param": "sys/param.h",
    "system shared memory": "sys/shm.h",
    "socket": "sys/socket.h",
    "sys socket": "sys/socket.h",
    "stat": "sys/stat.h",
    "sys stat": "sys/stat.h",
    "sys call": "sys/syscall.h",
    "user I O": "sys/uio.h",
    "sys user I O": "sys/uio.h",
    "U name": "sys/utsname.h",
    "sys U name": "sys/utsname.h",
    "wait": "sys/wait.h",
    "sys wait": "sys/wait.h",
    "time": "time.h",
    "unix standard": "unistd.h",
    "net I net in": "netinet/in.h",
    "sys cuddle": "linux/sysctl.h",
    "ex adder": "sys/xattr.h",
}

code_functions_private = {
    "hex dump": "hexdump",
}
code_functions_public = {
    "alloc A": "alloca",
    "A to I": "atoi",
    "see alloc": "calloc",
    "see lock": "calloc",
    "exit": "exit",
    "ef close": "fclose",
    "F open": "fopen",
    "fork": "fork",
    "F read": "fread",
    "free": "free",
    "F control": "fcntl",
    "file control": "fcntl",
    "F flush": "fflush",
    "ef write": "fwrite",
    "get char": "getchar",
    "get op": "getopt",
    "get pid": "getpid",
    "get U I D": "getuid",
    "get G I D": "getgid",
    "is digit": "isdigit",
    "malloc": "malloc",
    "mem copy": "memcpy",
    "mem set": "memset",
    "M map": "mmap",
    "ma map": "mmap",
    "make dir": "mkdir",
    "M un map": "munmap",
    "offset of": "offsetof",
    "P R cuddle": "prctl",
    "print F": "printf",
    "print": "printf",
    "puts": "puts",
    "P error": "perror",
    "pierre": "perror",
    "P thread create": "pthread_create",
    "P thread join": "pthread_join",
    "re alloc": "realloc",
    "set jump": "setjmp",
    "signal": "signal",
    "size of": "sizeof",
    "S print F": "sprintf",
    "S N print F": "snprintf",
    "skid yield": "sched_yield",
    "stir cat": "strcat",
    "string cat": "strcat",
    "string char": "strchr",
    "stir comp": "strcmp",
    "stir compare": "strcmp",
    "string compare": "strcmp",
    "stir copy": "strcpy",
    "stir dupe": "strdup",
    "string dupe": "strdup",
    "stir L cat": "strlcat",
    "stir L copy": "strlcpy",
    "stir len": "strlen",
    "sterling": "strlen",
    "string len": "strlen",
    "stir stir": "strstr",
    "stir N cat": "strncat",
    "stir N comp": "strncmp",
    "system": "system",
    "stir N copy": "strncpy",
    "stir to int": "strtoint",
    "stir to unsigned int": "strtouint",
    "message send": "msgsnd",
    "message get": "msgget",
    "send message": "sendmsg",
    "receive message": "recvmsg",
    "sys cuttle": "sysctl",
    "I O cuddle": "ioctl",
}

ctx.lists["user.code_common_function"] = {
    **code_functions_public,
    **code_functions_private,
}


ctx.lists["user.c_signals"] = {
    "sig child": "SIGCHLD",
    "sig kill": "SIGKILL",
    "sig term": "SIGTERM",
    "sig user": "SIGUSR1",
    "sig stop": "SIGSTOP",
    # XXX maybe make this a separate list
    "sig default": "SIG_DFLT",
    "sig ignore": "SIG_IGN",
}

ctx.lists["user.c_errors"] = {
    "exists": "EEXIST",
    "perm": "EPERM",
    "I O": "EIO",
    "not exists": "ENOENT",
    "interrupt": "EINTR",
    "no process": "ESRCH",
    "access": "EACCESS",
    "address in use": "EADDRINUSE",
    "busy": "EBUSY",
    "child": "ECHILD",
}


class CLangState:
    def __init__(self, mod):
        self.datatypes = ["c_basic_datatypes", "c_stdint_datatypes"]

        default = "c_basic_datatypes"
        if settings.get("user.use_stdint_datatypes"):
            default = "c_stdint_datatypes"

        index = 0
        for dt in self.datatypes:
            if default == dt:
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
        app.notify(f"Cycled to C lang datatype: {self.datatype}")

    def current_datatype(self):
        """Display the current datatype"""
        app.notify(f"Current C lang datatype: {self.datatype}")


c_lang_state = CLangState(mod)
mod.list("c_pointers", desc="Common C pointers")
mod.list("c_signed", desc="Common C datatype signed modifiers")
mod.list("c_types", desc="Common C types")
mod.list("stdint_types", desc="Common stdint C types")
mod.list("stdint_signed", desc="Common stdint C datatype signed modifiers")


@mod.capture(rule="{self.c_pointers}")
def c_pointers(m) -> str:
    "Returns a string"
    return m.c_pointers


@mod.capture(rule="{user.c_signed}")
def c_signed(m) -> str:
    "Returns a string"
    return m.c_signed


@mod.capture(rule="{self.c_keywords}")
def c_keywords(m) -> str:
    "Returns a string"
    return m.c_keywords


@mod.capture(rule="[<user.c_signed>] {user.c_types} [<self.c_pointers>+]")
def c_types(m) -> str:
    "Returns a string"
    if hasattr(m, "c_signed") and len(m.c_signed) == 1:
        return m.c_signed + " ".join(list(m[1:]))
    else:
        return " ".join(list(m))


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


@mod.capture(rule="[<user.c_signed>] <user.c_types> [<self.c_pointers>]")
def c_variable(m) -> str:
    "Returns a string"
    if hasattr(m, "c_signed") and len(m.c_signed) == 1:
        return m.c_signed + " ".join(list(m[1:]))
    else:
        return " ".join(list(m))


@ctx.action_class("user")
class UserActions:
    ###
    # code_operators_pointers
    ###
    def code_operator_indirection():
        actions.insert("*")

    def code_operator_address_of():
        actions.insert("&")

    def code_operator_structure_dereference():
        actions.insert("->")

    ###
    # code_operators_array
    ###
    def code_operator_subscript():
        actions.insert("[]")
        actions.key("left")

    ##
    # code_operators_assignment
    ##
    def code_operator_assignment():
        actions.insert(" = ")

    ##
    # code_operators_math
    ##
    def code_operator_subtraction():
        actions.insert(" - ")

    def code_operator_subtraction_assignment():
        actions.insert(" -= ")

    def code_operator_addition():
        actions.insert(" + ")

    def code_operator_addition_assignment():
        actions.insert(" += ")

    def code_operator_increment():
        actions.insert("++")

    def code_operator_decrement():
        actions.insert("--")

    def code_operator_multiplication():
        actions.insert(" * ")

    def code_operator_multiplication_assignment():
        actions.insert(" *= ")

    # action(user.code_operator_exponent): " ** "
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
        actions.insert(" && ")

    def code_operator_or():
        actions.insert(" || ")

    ##
    # code_operators_bitwise
    ##
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

    def code_insert_null():
        actions.insert("NULL")

    def code_insert_is_null():
        actions.insert(" == NULL ")

    def code_insert_is_not_null():
        actions.insert(" != NULL")

    # code_imperative
    def code_block():
        actions.insert("{\n\n}\n")
        actions.key("up:2 left:3")

    def code_state_if():
        actions.insert("if () {\n}\n")
        actions.key("up:2 left:3")

    def code_state_else_if():
        actions.insert("else if () {\n}\n")
        actions.key("up:2 left:3")

    def code_state_else():
        actions.insert("else\n{\n}\n")
        actions.key("up:2")

    def code_state_switch():
        actions.insert("switch ()")
        actions.edit.left()

    def code_state_case():
        actions.insert("case \nbreak;")
        actions.edit.up()

    def code_state_for():
        actions.insert("for ")

    def code_state_go_to():
        actions.insert("goto ")

    def code_state_while():
        actions.insert("while ()")
        actions.edit.left()

    def code_state_return():
        actions.insert("return ")

    def code_break():
        actions.insert("break;")

    def code_next():
        actions.insert("continue;")

    def code_insert_true():
        actions.insert("true")

    def code_insert_false():
        actions.insert("false")

    def code_comment_line_prefix():
        actions.insert("//")

    # code_functions
    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + f"({selection})"
        else:
            text = text + "()"
        actions.user.paste(text)
        actions.edit.left()

    def code_insert_terminated_function(text: str, selection: str):
        if selection:
            text = text + f"({selection})"
        else:
            text = text + "();"
        actions.user.paste(text)

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
        actions.user.paste(f"#include <{selection}>")

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
