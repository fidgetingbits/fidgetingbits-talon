code.language: rust
-
tag(): user.code_comment_line
tag(): user.code_comment_block_c_like
tag(): user.code_comment_documentation

tag(): user.code_block_c_like
tag(): user.code_imperative
tag(): user.code_object_oriented

tag(): user.code_data_bool
tag(): user.code_data_null

tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_libraries
tag(): user.code_libraries_gui
tag(): user.code_types

tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_math

tag(): user.code_format_strings_interpolated

settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_protected_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

# rust-specific grammars

## for unsafe rust
<user.operator> unsafe: "unsafe "
(<user.operator>) unsafe block: user.code_state_unsafe()

## rust centric struct and enum definitions
<user.operator> (struct | structure) [<user.text>]:
    insert("struct ")
    insert(user.formatted_text(text or "", "PASCAL_CASE"))

<user.operator> enum [<user.text>]:
    insert("enum ")
    insert(user.formatted_text(text or "", "PASCAL_CASE"))

toggle use: user.code_toggle_libraries()

# TODO: It would be nice if there was a way to not let text match on certain words, because this conflict with
# the let type command below

[<user.operator>] let untyped <user.text>:
    insert("let ")
    insert(user.formatted_text(text or "", "SNAKE_CASE"))
    insert(" = ")

[<user.operator>] let untyped mute <user.text>:
    insert("let mut ")
    insert(user.formatted_text(text or "", "SNAKE_CASE"))

# let type bytes called data: "let data: u8 = "
[<user.operator>] let type <user.code_type> called <user.text>:
    insert("let ")
    insert(user.formatted_text(text or "", "SNAKE_CASE"))
    insert(": {code_type} = ")

# let type borrowed vector of bytes called data: "let data: &Vec<u8> = "
[<user.operator>] let type <user.code_containing_type> of <user.code_type> called <user.text>:
    insert("let ")
    insert(user.formatted_text(text or "", "SNAKE_CASE"))
    insert(": {code_containing_type}<{code_type}> = ")


## Simple aliases
[<user.operator>] (borrowed | borrow): "&"
[<user.operator>] (borrowed | borrow) (mutable | mute): "&mut "
<user.operator> (a sink | async | asynchronous): "async "
<user.operator> (pub | public): "pub "
<user.operator> (pub | public) crate: "pub(crate) "
<user.operator> (dyn | dynamic): "dyn "
# <user.operator> type: "type "
<user.operator> (const | constant): "const "
<user.operator> (funk | func | function): "fn "
<user.operator> (imp | implements): "impl "
<user.operator> let mute: "let mut "
<user.operator> let: "let "
<user.operator> (mute | mutable): "mut "
<user.operator> (mod | module): "mod "
<user.operator> ref (mute | mutable): "ref mut "
<user.operator> ref: "ref "
<user.operator> trait: "trait "
<user.operator> match: user.code_state_switch()
<user.operator> (some | sum): "Some"
<user.operator> static: "static "
self taught: "self."
<user.operator> a sync block: user.insert_between("async {", "}")
<user.operator> match a sync block: user.insert_between("match async {", "}.await {}")
<user.operator> await: ".await"

<user.operator> init defaults: "..Default::default()"

# FIXME(rust): We need to merge code libraries and rust crate somehow, may be the rust crate needs like a pure prefix to
# imply we're not bringing in additional things yet
use <user.code_libraries>:
    user.code_insert_library(code_libraries, "")
    key(; enter)
use {user.rust_crates} prelude:
    insert("use {rust_crates}::prelude::*;")
    key(enter)

# This is for local use crate:: only, use "use <user.code_libraryes>" for external crates
use crate:    user.insert_between("use crate::", ";")


## specialist flow control
# <user.operator> if let some: user.code_insert_if_let_some()
<user.operator> if let (ok | okay): user.code_insert_if_let_okay()
# <user.operator> if let error: user.code_insert_if_let_error()

## rust centric synonyms
is some: user.code_insert_is_not_null()

## for implementing
implement (struct | structure): user.code_state_implements()

## for annotating function parameters
is implemented trait {user.code_trait}: ": impl {code_trait}"
is implemented trait: ": impl "
returns implemented trait {user.code_trait}: " -> impl {code_trait}"
returns implemented trait: " -> impl "

## for generic reference of traits
trait {user.code_trait}: insert("{code_trait}")
implemented trait {user.code_trait}: insert("impl {code_trait}")
dynamic trait {user.code_trait}: insert("dyn {code_trait}")

## for generic reference of macro
macro {user.code_macros}: user.code_insert_macro(code_macros, "")
macro wrap {user.code_macros}:
    user.code_insert_macro(code_macros, edit.selected_text())

## rust specific document comments
block dock comment: user.code_comment_documentation_block()
inner dock comment: user.code_comment_documentation_inner()
inner block dock comment: user.code_comment_documentation_block_inner()

<user.operator> returns: " -> "
# TODO: They should use a list
<user.operator> empty ok: "Ok(())"
<user.operator> empty error: "Err(())"
<user.operator> empty some: "Some(())"
<user.operator> doc [comment]: "///"
<user.operator> empty result: "Result::Ok(())"
<user.operator> arm: "=> "
<user.operator> arm open: "=> {"
<user.operator> arm block: "=> {}"
<user.operator> right [inclusive] range: "..="
<user.operator> left [inclusive] range: "=.."
<user.operator> range: ".."
<user.operator> at range: "@ .."
[<user.operator>] turbo fish: "::<>"
turbo crate: "crate::"
turbo stood: "std::"
[<user.operator>] turbo <user.word>: "{word}::"
<user.operator> at <user.text>: "{text} @ "
<user.operator> label range: user.insert_between("", "@ ..")
<user.operator> new vec: "Vec::new()"
<user.operator> new box: "Box::new()"
<user.operator> use: user.code_import()
#<user.operator> use: "use "
<user.operator> use block: user.insert_between("use {", "};")
<user.operator> use {user.rust_crates}: user.insert_between("use {rust_crates}::", ";")
<user.operator> tokyo main: "#[tokio::main]"
<user.operator> A sink: "async "
<user.operator> pub: "pub "
<user.operator> mod: "mod "
<user.operator> static ref: "static ref "

# TODO: Make all derivable trait values something we can say and have automatically added
<user.operator> derive: user.insert_between("#[derive(", ")]")
<user.operator> derive debug: "#[derive(Debug)]"
<user.operator> derive clone: "#[derive(Clone)]"
<user.operator> derive copy: "#[derive(Copy)]"
<user.operator> derive default: "#[derive(Default)]"
<user.operator> derive display: "#[derive(Display)]"
<user.operator> derive error: "#[derive(Error)]"
<user.operator> default: "#[default]"
funk {user.formatted_functions}:
    insert(formatted_functions)
    user.insert_between('("', '");')
<user.operator> A sink trait: "#[async_trait]"

<user.operator> used: "#[used]"
<user.operator> test: "#[test]"
<user.operator> ignore: "#[ignore]"
<user.operator> ignored test: "#[test]\n#[ignore]"
<user.operator> config test: "#[cfg(test)]"
<user.operator> config any: user.insert_between("#[cfg(any(", "))]")
<user.operator> config X sixty four: '#[cfg(target_arch = "x86_64")]'
<user.operator> config X thirty two: '#[cfg(target_arch = "x86")]'
<user.operator> config arm: '#[cfg(target_arch = "arm")]'
<user.operator> config arm sixty four: '#[cfg(target_arch = "aarch64")]'
<user.operator> config windows: '#[cfg(target_os = "windows")]'
<user.operator> config linux: '#[cfg(target_os = "linux")]'
<user.operator> config mac: '#[cfg(target_os = "macos")]'
# TODO: It would be nice to automatically be able to specify multiple
# architecture's and wrap it inside of any()
# TODO: automatically create test module in functions, add things like expect panic
<user.operator> (rep | represent) C: "#[repr(C)]"

<user.operator> global warn unused variables: "#![warn(unused_variables)]"
<user.operator> global warn unused imports: "#![warn(unused_imports)]"
<user.operator> global warn unused results: "#![warn(unused_results)]"
<user.operator> global warn unused mut: "#![warn(unused_mut)]"
<user.operator> global warn dead code: "#![warn(dead_code)]"

<user.operator> warn unused variables: "#[warn(unused_variables)]"
<user.operator> warn unused imports: "#[warn(unused_imports)]"
<user.operator> warn unused results: "#[warn(unused_results)]"
<user.operator> warn unused mut: "#[warn(unused_mut)]"
<user.operator> warn dead code: "#[warn(dead_code)]"

<user.operator> global allow unused variables: "#![allow(unused_variables)]"
<user.operator> global allow unused imports: "#![allow(unused_imports)]"
<user.operator> global allow unused results: "#![allow(unused_results)]"
<user.operator> global allow unused mut: "#![allow(unused_mut)]"
<user.operator> global allow non camel [case] [types]: "#![allow(non_camel_case_types)]"
<user.operator> global allow dead code: "#![allow(dead_code)]"
<user.operator> global allow unreachable code: "#![allow(unreachable_code)]"

<user.operator> allow unused variables: "#[allow(unused_variables)]"
<user.operator> allow unused imports: "#[allow(unused_imports)]"
<user.operator> allow unused results: "#[allow(unused_results)]"
<user.operator> allow unused mut: "#[allow(unused_mut)]"
<user.operator> allow non camel [case] [types]: "#[allow(non_camel_case_types)]"
<user.operator> allow dead code: "#[allow(dead_code)]"
<user.operator> allow unreachable code: "#[allow(unreachable_code)]"

[<user.operator>] returns [result] box error: "-> Result<(), Box<dyn Error>>"
<user.operator> result box error: "Result<(), Box<dyn Error>>"

<user.operator> result of <user.code_type> and <user.code_type>:
    "Result<{code_type}, Box<dyn Error>>"

# FIXME(rust): switch this to work with the format strings tag instead
# https://doc.rust-lang.org/std/fmt/
<user.operator> form {user.format_strings}: insert("{{{format_strings}}}")
<user.operator> form inner {user.format_strings}: insert("{format_strings}")

<user.operator> [{user.code_type_modifier}] sliced <user.code_type>:
    insert(code_type_modifier or "")
    insert("[{code_type}]")

<user.operator> [{user.code_type_modifier}] <number> element <user.code_type> array:
    insert(code_type_modifier or "")
    insert("[{code_type}; {number}]")

<user.operator> [{user.code_type_modifier}] <user.code_type> array:
    insert(code_type_modifier or "")
    user.insert_between("[{code_type}; ", "]")

<user.operator> zero init <number> elements: insert("[0; {number}]")

<user.operator> as <user.code_type>: "as {code_type}"

<user.operator> new {user.rust_allocatable_types}: insert("{rust_allocatable_types}::new()")

<user.operator> (stood | standard) {user.rust_std_modules}: insert("std::{rust_std_modules}::")

<user.operator> (stood | standard) {user.rust_std_modules} <user.text>:
    insert("std::{rust_std_modules}::")
    insert(user.formatted_text(text or "", "PASCAL_CASE"))

<user.operator> collect as <user.code_containing_type> of [<user.code_type>]:
    type = user.code_type or ""
    insert("collect::{code_containing_type}<{type}>()")

<user.operator> target <user.rust_targets>: "{rust_targets}"

##
# Cursorless-only commands
##
rust docs <user.cursorless_target>:
    text = user.c_get_target_string(cursorless_target)
    user.open_url("https://doc.rust-lang.org/std/index.html?search={text}")
