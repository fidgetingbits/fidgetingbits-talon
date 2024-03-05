from typing import Any, Callable, TypeVar

from talon import Context, Module, actions, settings

mod = Module()
# rust specific grammar
mod.list("code_type_modifier", desc="List of type modifiers for active language")
mod.list("code_macros", desc="List of macros for active language")
mod.list("code_trait", desc="List of traits for active language")
mod.list("rust_crates", desc="List of common rust crates")
mod.list("closed_format_strings", desc="List of common closed rust format strings")
mod.list("inner_format_strings", desc="List of common rust format strings")
mod.list("rust_types", desc="List of common rust types")
mod.list("code_containing_types", desc="List of common rust container types")
mod.list("formatted_functions", desc="List of common rust formatted functions")
mod.list("rust_allocatable_types", desc="List of common rust allocatable types")
mod.list("rust_std_modules", desc="List of common rust std modules")
mod.list("rust_targets", desc="List of common rust compile targets")
mod.list("rust_toolchains", desc="List of common rust toolchains")


@mod.action_class
class Actions:
    def code_state_implements():
        """Inserts implements block, positioning the cursor appropriately"""

    def code_insert_if_let_okay():
        """Inserts if let ok block, positioning the cursor appropriately"""

    def code_insert_if_let_some():
        """Inserts if let some block, positioning the cursor appropriately"""

    def code_insert_if_let_error():
        """Inserts if let error block, positioning the cursor appropriately"""

    def code_insert_trait_annotation(type: str):
        """Inserts type annotation for implementor of trait"""

    def code_insert_return_trait(type: str):
        """Inserts a return type for implementor of trait"""

    def code_insert_macro(text: str, selection: str):
        """Inserts a macro and positions the cursor appropriately"""

    def code_insert_macro_array(text: str, selection: str):
        """Inserts a macro array and positions the cursor appropriately"""

    def code_insert_macro_block(text: str, selection: str):
        """Inserts a macro block and positions the cursor appropriately"""

    def code_state_unsafe():
        """Inserts an unsafe block and positions the cursor appropriately"""

    def code_comment_documentation_block():
        """Inserts a block document comment and positions the cursor appropriately"""

    def code_comment_documentation_inner():
        """Inserts an inner document comment and positions the cursor appropriately"""

    def code_comment_documentation_block_inner():
        """Inserts an inner block document comment and positions the cursor appropriately"""


ctx = Context()
# NOTE: This used to have user.rust_apps, but deleted during community merge. Re-add it if stuff breaks
ctx.matches = r"""
code.language: rust
"""

ctx.lists["user.rust_std_modules"] = {
    "compare": "cmp",
    "convert": "convert",
    "format": "fmt",
    "I O": "io",
}

scalar_types = {
    "eye eight": "i8",
    "you eight": "u8",
    "bytes": "u8",
    "eye sixteen": "i16",
    "you sixteen": "u16",
    "eye thirty two": "i32",
    "you thirty two": "u32",
    "eye sixty four": "i64",
    "you sixty four": "u64",
    "eye one hundred and twenty eight": "i128",
    "you one hundred and twenty eight": "u128",
    "eye size": "isize",
    "you size": "usize",
    "float thirty two": "f32",
    "float sixty four": "f64",
    "boolean": "bool",
    "bool": "bool",
    "character": "char",
}

compound_types = {
    "tuple": "()",
    "array": "[]",
}


standard_library_types = {
    "box": "Box",
    "vector": "Vec",
    "string": "String",
    "string slice": "&str",
    "os string": "OsString",
    "os string slice": "&OsStr",
    "see string": "CString",
    "see string slice": "&CStr",
    "option": "Option",
    "result": "Result",
    "okay": "Ok",
    "error": "Err",  # TODO: These aren't really types I guess
    "big error": "Error",
    "hashmap": "HashMap",
    "hash set": "HashSet",
    "reference count": "Rc",
    "path": "Path",
    "path buf": "PathBuf",
}

# TODO: This needs to get integrated into other lists rather than duplication
allocatable_types = {
    "vector": "Vec",
    "string": "String",
    "path": "Path",
}
ctx.lists["user.rust_allocatable_types"] = allocatable_types

# types that allow us say for example 'vector of you eight' to get Vec<u8>
containing_types = {
    "vector": "Vec",
    "veck": "Vec",
    "okay": "Ok",
    "result": "Result",
    "option": "Option",
    "reference count": "Rc",
    "arc": "Arc",
    "cell": "Cell",
    "ref cell": "RefCell",
    "mutex": "Mutex",
    "rw lock": "RwLock",
    "box": "Box",
}


standard_sync_types = {
    "arc": "Arc",
    "barrier": "Barrier",
    "condition variable": "Condvar",
    "mutex": "Mutex",
    "once": "Once",
    "read write lock": "RwLock",
    "receiver": "Receiver",
    "sender": "Sender",
    "sink sender": "SyncSender",
}

all_types = {
    **scalar_types,
    **compound_types,
    **standard_library_types,
    **standard_sync_types,
}

standard_function_macros = {
    "panic": "panic!",
    "concatenate": "concat!",
    "con cat": "concat!",
    "to do": "todo!",
    "debug": "dbg!",
    "sys call": "syscall!",
}

string_formatted_standard_function_macros = {
    "format": "format!",
    "print": "print!",
    "print line": "println!",
    "error print line": "eprintln!",
    "write": "write!",
    "write line": "writeln!",
}


standard_array_macros = {
    "vector": "vec!",
}

common_implementations = {
    "ok or": "ok_or",
    "ok or else": "ok_or_else",
    "unwrap": "unwrap",
    "await": "await",
    "some": "Some",
}

standard_block_macros = {
    "macro rules": "macro_rules!",
}

logging_macros = {
    "debug": "debug!",
    "info": "info!",
    "warning": "warn!",
    "warn": "warn!",
    "error": "error!",
}

testing_macros = {
    "assert": "assert!",
    "assert equal": "assert_eq!",
    "assert not equal": "assert_ne!",
}

errno_values = {
    "success": "ESUCCESS",  # 0
    "permission denied": "EPERM",  # 1
}

error_methods = {"raw os error": "raw_os_error"}

all_string_formatted_functions_macros = {
    **string_formatted_standard_function_macros,
    **logging_macros,
}

all_function_macros = {
    **standard_function_macros,
    **testing_macros,
}

all_array_macros = {
    **standard_array_macros,
}

all_block_macros = {
    **standard_block_macros,
}

all_macros = {
    **all_function_macros,
    **all_array_macros,
    **all_block_macros,
}

all_function_macro_values = set(all_function_macros.values())
all_array_macro_values = set(all_array_macros.values())
all_block_macro_values = set(all_block_macros.values())

closure_traits = {
    "closure": "Fn",
    "closure once": "FnOnce",
    "closure mutable": "FnMut",
}

conversion_traits = {
    "into": "Into",
    "from": "From",
}

iterator_traits = {
    "iterator": "Iterator",
}

all_traits = {
    **closure_traits,
    **conversion_traits,
    **iterator_traits,
}


# tag: libraries_gui

# TODO: A lot of people refer to these as "stood" something, so we should possibly include a optional
# "stood" prefix command disk for these
standard_imports = {
    "atomic": "std::sync::atomic",
    "eye oh": "std::io",
    "file system": "std::fs",
    "F S": "std::fs",
    "path": "std::path",
    "envy": "std::env",
    "collections": "std::collections",
    "process": "std::process",
    "thread": "std::thread",
    "sync": "std::sync",
    "future": "std::future",
    "pin": "std::pin",
    "error": "std::error",
    "error error": "std::error::Error",
    "error kind": "std::io::ErrorKind",
    "from stir": "std::str::FromStr",
    "channel": "std::sync::mpsc",
}
tokio_imports = {"tracing": "tracing::{info};"}
common_imports = {
    "glob": "glob::glob",
    "serde json": "serde_json::json",
    "serde": "serde::{Serialize, Deserialize}",
    "log": "log::{debug, error, info, warn}",
    "iterator tools": "itertools::Itertools",
    "iter tools": "itertools::Itertools",
    "lazy static": "lazy_static::lazy_static",
    "perfect hash map": "phf::phf_map",
    "follow redirects": "follow_redirects::ClientExt",
    "clap parser": "clap::{App, Arg, ArgMatches, Parser, SubCommand}",
}

ctx.lists["user.code_libraries"] = {
    **standard_imports,
    **tokio_imports,
    **common_imports,
}


# tag: functions_common
ctx.lists["user.code_common_function"] = {
    "drop": "drop",
    "catch unwind": "catch_unwind",
    "iterator": "iter",
    "into iterator": "into_iter",
    "into iter": "into_iter",
    "from iterator": "from_iter",
    "from iter": "from_iter",
    "as stir": "as_str",
    "to string": "to_string",
    "to string lossy": "to_string_lossy",
    "to stir": "to_str",
    "as bytes": "as_bytes",
    "to bytes": "to_bytes",
    "as pointer": "as_ptr",
    "as mutable pointer": "as_mut_ptr",
    "as reference": "as_ref",
    "as ref": "as_ref",
    "as mute": "as_mut",
    "is some": "is_some",
    "is none": "is_none",
    "is ok": "is_ok",
    "is error": "is_err",
    "is empty": "is_empty",
    "to path buf": "to_path_buf",
    "unwrap": "unwrap",
    "unwrap or": "unwrap_or",
    "unwrap or else": "unwrap_or_else",
    "expect": "expect",
    "to vec": "to_vec",
    "to vector": "to_vec",
    "trim": "trim",
    "split white space": "split_whitespace",
    "display": "display",
    "or insert": "or_insert",
    "or insert with": "or_insert_with",
    "cloned": "cloned",
    "clone": "clone",
    "is digit": "is_digit",
    "is alphanum": "is_alphanumeric",
    "is ascii": "is_ascii",
    "is ascii hex digit": "is_ascii_hex_digit",
    "in to": "into",
    **common_implementations,
    **all_macros,
}

# tag: functions
ctx.lists["user.code_type"] = all_types

# rust specific grammar
ctx.lists["user.code_type_modifier"] = {
    "mutable": "mut ",
    "mute": "mut ",
    "borrowed": "&",
    "borrowed mutable": "&mut ",
    "borrowed mute": "&mut ",
    "mutable borrowed": "&mut ",
    "mute borrowed": "&mut ",
    "dynamic": "dyn ",
    "dine": "dyn ",
}

ctx.lists["user.rust_crates"] = {
    "native T L S": "native_tls",
    "hyper": "hyper",
    "tokyo": "tokio",
    "futures": "futures",
    "async standard": "async_std",
    "follow redirects": "follow_redirects",
    "log": "log",
    "request": "reqwest",
    "clap": "clap",
    "cap stone": "capstone",
    "key stone": "keystone_engine",  # official crate is buggy
    "goblin": "goblin",
    "random": "rand",
    "walk dir": "walkdir",
    "log": "log",
    "open S S L": "openssl",
    "serde": "serde",
    "serde JSON": "serde_json",
    "thirty four": "thirtyfour",
    "simple log": "simplelog",
    "async recursion": "async_recursion",
    "serde": "serde",
    "serde json": "serde_json",
    "ray on": "rayon",
    "shaw two": "sha2",
    "glob": "glob",
    "iter tools": "itertools",
    "lazy static": "lazy_static",
    "which": "which",
    "base sixty four": "base64",
    "regex": "regex",
}

ctx.lists["user.rust_toolchains"] = {
    "stable": "stable",
    "nightly": "nightly",
    "beta": "beta",
}

# TODO: These are a little loose with the architecture's atm
ctx.lists["user.rust_targets"] = {
    "windows M S V C": "x86_64-pc-windows-msvc",
    "windows G N U": "x86_64-pc-windows-gnu",
    "mac O S": "x86_64-apple-darwin",
    "mac O S arm": "aarch64-apple-darwin",
    "linux": "x86_64-unknown-linux-gnu",
    "linux muscle": "x86_64-unknown-linux-musl",
    "linux arm sixty four": "aarch64-unknown-linux-gnu",
    "linux muscle arm sixty four": "aarch64-unknown-linux-musl",
    "linux arm": "armv7-unknown-linux-gnueabihf",
    "linux muscle arm": "armv7-unknown-linux-musleabihf",
}

ctx.lists["user.formatted_functions"] = {**all_string_formatted_functions_macros}


ctx.lists["user.closed_format_strings"] = {
    "hex": r"{:#x}",
    "octal": r"{:#o}",
    "binary": r"{:#b}",
    "decimal": r"{:#}",
    "float": r"{:.2}",
    "debug": r"{:?}",
}

ctx.lists["user.inner_format_strings"] = {
    "hex": r":#x",
    "octal": r":#o",
    "binary": r":#b",
    "decimal": r":#",
    "float": r":.2",
    "debug": r":?",
}


ctx.lists["user.code_macros"] = all_macros

ctx.lists["user.code_trait"] = all_traits

ctx.lists["user.code_containing_types"] = {**containing_types}


@ctx.action_class("user")
class UserActions:
    # tag: comment_line

    def code_comment_line_prefix():
        actions.auto_insert("// ")

    # tag: comment_documentation

    def code_comment_documentation():
        actions.auto_insert("/// ")

    # tag: imperative

    def code_state_if():
        actions.auto_insert("if ")

    def code_state_else_if():
        actions.auto_insert(" else if ")

    def code_state_else():
        actions.user.insert_between(" else { ", " }")

    def code_state_switch():
        actions.auto_insert("match ")

    def code_state_for():
        actions.auto_insert("for  in  {}")
        actions.edit.left()
        actions.key("enter")
        actions.edit.up()
        actions.edit.line_end()
        repeat_call(6, actions.edit.left)

    def code_state_while():
        actions.auto_insert("while  {}")
        actions.edit.left()
        actions.key("enter")
        actions.edit.up()
        actions.edit.line_end()
        repeat_call(2, actions.edit.left)

    def code_state_infinite_loop():
        actions.user.insert_between("loop {", "}")
        actions.key("enter")

    def code_state_return():
        actions.auto_insert("return ")

    def code_break():
        actions.auto_insert("break;")

    def code_next():
        actions.auto_insert("continue;")

    # tag: object_oriented

    def code_operator_object_accessor():
        actions.auto_insert(".")

    def code_self():
        actions.auto_insert("self")

    def code_define_class():
        actions.auto_insert("struct ")

    # tag: data_bool

    def code_insert_true():
        actions.auto_insert("true")

    def code_insert_false():
        actions.auto_insert("false")

    # tag: data_null

    def code_insert_null():
        actions.auto_insert("None")

    def code_insert_is_null():
        actions.auto_insert(".is_none()")

    def code_insert_is_not_null():
        actions.auto_insert(".is_some()")

    # tag: functions

    def code_default_function(text: str):
        actions.user.code_private_function(text)

    def code_private_function(text: str):
        actions.auto_insert("fn ")
        formatter = settings.get("user.code_private_function_formatter")
        function_name = actions.user.formatted_text(text, formatter)
        actions.user.code_insert_function(function_name, None)

    def code_protected_function(text: str):
        actions.auto_insert("pub(crate) fn ")
        formatter = settings.get("user.code_protected_function_formatter")
        function_name = actions.user.formatted_text(text, formatter)
        actions.user.code_insert_function(function_name, None)

    def code_public_function(text: str):
        actions.auto_insert("pub fn ")
        formatter = settings.get("user.code_public_function_formatter")
        function_name = actions.user.formatted_text(text, formatter)
        actions.user.code_insert_function(function_name, None)

    def code_insert_type_annotation(type: str):
        actions.auto_insert(f": {type}")

    def code_insert_return_type(type: str):
        actions.auto_insert(f" -> {type}")

    # tag: functions_common

    def code_insert_function(text: str, selection: str):
        code_insert_function_or_macro(text, selection, "(", ")")

    # tag: libraries

    def code_import():
        actions.auto_insert("use ")

    # tag: libraries_gui

    def code_insert_library(text: str, selection: str):
        actions.user.paste(f"use {text}")

    # tag: operators_array

    def code_operator_subscript():
        actions.auto_insert("[]")
        actions.edit.left()

    # tag: code_operators_assignment

    def code_operator_assignment():
        actions.auto_insert(" = ")

    def code_operator_subtraction_assignment():
        actions.auto_insert(" -= ")

    def code_operator_addition_assignment():
        actions.auto_insert(" += ")

    def code_operator_multiplication_assignment():
        actions.auto_insert(" *= ")

    def code_operator_division_assignment():
        actions.auto_insert(" /= ")

    def code_operator_modulo_assignment():
        actions.auto_insert(" %= ")

    def code_operator_bitwise_and_assignment():
        actions.auto_insert(" &= ")

    def code_operator_bitwise_or_assignment():
        actions.auto_insert(" |= ")

    def code_operator_bitwise_exclusive_or_assignment():
        actions.auto_insert(" ^= ")

    def code_operator_bitwise_left_shift_assignment():
        actions.auto_insert(" <<= ")

    def code_operator_bitwise_right_shift_assignment():
        actions.auto_insert(" >>= ")

    # tag: operators_bitwise

    def code_operator_bitwise_and():
        actions.auto_insert(" & ")

    def code_operator_bitwise_or():
        actions.auto_insert(" | ")

    def code_operator_bitwise_exclusive_or():
        actions.auto_insert(" ^ ")

    def code_operator_bitwise_left_shift():
        actions.auto_insert(" << ")

    def code_operator_bitwise_right_shift():
        actions.auto_insert(" >> ")

    # tag: operators_math

    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    def code_operator_exponent():
        actions.auto_insert(".pow()")
        actions.edit.left()

    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_modulo():
        actions.auto_insert(" % ")

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
        actions.auto_insert(" && ")

    def code_operator_or():
        actions.auto_insert(" || ")

    def code_operator_increment():
        actions.auto_insert(" += 1")

    # rust specific grammar

    def code_operator_structure_dereference():
        actions.auto_insert("*")

    def code_state_implements():
        actions.auto_insert("impl  {}")
        actions.edit.left()
        actions.key("enter")
        actions.edit.up()
        actions.edit.line_end()
        repeat_call(2, actions.edit.left)

    def code_insert_macro(text: str, selection: str):
        if text in all_array_macro_values:
            code_insert_function_or_macro(text, selection, "[", "]")
        elif text in all_block_macro_values:
            code_insert_function_or_macro(text, selection, "{", "}")
        else:
            code_insert_function_or_macro(text, selection, "(", ")")

    def code_state_unsafe():
        actions.user.insert_between("unsafe {", "}")
        actions.key("enter")

    def code_comment_documentation_block():
        actions.user.insert_between("/**", "*/")
        actions.key("enter")

    def code_comment_documentation_inner():
        actions.auto_insert("//! ")

    def code_comment_documentation_block_inner():
        actions.user.insert_between("/*!", "*/")
        actions.key("enter")


def code_insert_function_or_macro(
    text: str,
    selection: str,
    left_delim: str,
    right_delim: str,
):
    if selection:
        out_text = text + f"{left_delim}{selection}{right_delim}"
    else:
        out_text = text + f"{left_delim}{right_delim}"
    actions.user.paste(out_text)
    actions.edit.left()


RT = TypeVar("RT")  # return type


def repeat_call(n: int, f: Callable[..., RT], *args: Any, **kwargs: Any):
    for i in range(n):
        f(*args, **kwargs)
