tag: user.rust
-
tag(): user.code_comment_line
tag(): user.code_comment_block_c_like
tag(): user.code_comment_documentation

tag(): user.code_imperative
tag(): user.code_object_oriented

tag(): user.code_data_bool
tag(): user.code_data_null

tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_libraries
tag(): user.code_libraries_gui

tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_math

settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_protected_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

# rust-specific grammars

## for unsafe rust
put unsafe: "unsafe "
(put) unsafe block: user.code_state_unsafe()

## rust centric struct and enum definitions
put (struct | structure) [<user.text>]:
    insert("struct ")
    insert(user.formatted_text(text or "", "PUBLIC_CAMEL_CASE"))

put enum [<user.text>]:
    insert("enum ")
    insert(user.formatted_text(text or "", "PUBLIC_CAMEL_CASE"))

toggle use: user.code_toggle_libraries()

# TODO: It would be nice if there was a way to not let text match on certain words, because this conflict with
# the let type command below

put let <user.text>:
    insert("let ")
    insert(user.formatted_text(text or "", "SNAKE_CASE"))
    insert(" = ")

put let mute <user.text>:
    insert("let mut ")
    insert(user.formatted_text(text or "", "SNAKE_CASE"))

put let type <user.code_type> <user.text>:
    insert("let ")
    insert(user.formatted_text(text or "", "SNAKE_CASE"))
    insert(": ")
    insert(user.code_type())
    insert(" = ")

## Simple aliases
[put] (borrowed|borrow): "&"
[put] (borrowed|borrow) (mutable|mute): "&mut "
put (a sink | async | asynchronous): "async "
put (pub | public): "pub "
put (pub | public) crate: "pub(crate) "
put (dyn | dynamic): "dyn "
put type: "type "
put (const|constant): "const "
put (funk | func | function): "fn "
put (imp | implements): "impl "
put let mute: "let mut "
put let: "let "
put (mute | mutable): "mut "
put (mod | module): "mod "
put ref (mute | mutable): "ref mut "
put ref: "ref "
put trait: "trait "
put match: user.code_state_switch()
put (some | sum): "Some"
put static: "static "
self taught: "self."
put use: user.code_import()
put a sync block: user.insert_between("async {" , "}")
put match a sync block: user.insert_between("match async {" , "}.await {}")
put await: ".await"

put init defaults: "..Default::default()"


use <user.code_libraries>:
    user.code_insert_library(code_libraries, "")
    key(; enter)
use {user.rust_crates} prelude:
    insert("use {rust_crates}::prelude::*;")
    key(enter)
use crate: user.insert_between("use crate::", ";")

## specialist flow control
put if let some: user.code_insert_if_let_some()
put if let (ok | okay): user.code_insert_if_let_okay()
put if let error: user.code_insert_if_let_error()

## rust centric synonyms
is some: user.code_insert_is_not_null()

## for implementing
implement (struct | structure): user.code_state_implements()

## for annotating function parameters
is implemented trait {user.code_trait}: user.code_insert_trait_annotation(code_trait)
is implemented trait: ": impl "
returns implemented trait {user.code_trait}: user.code_insert_return_trait(code_trait)
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


put returns: " -> "
# TODO: They should use a list
put empty ok: "Ok(())"
put empty error: "Err(())"
put empty some: "Some(())"
put doc [comment]: "///"
put empty result: "Result::Ok(())"
put arm: "=> "
put arm open: "=> {"
put arm block: "=> {}"
put right [inclusive] range: "..="
put left [inclusive] range: "=.."
put range: ".."
put at range: "@ .."
[put] turbo fish: "::<>"
turbo crate: "crate::"
turbo stood: "std::"
[put] turbo <user.word>: "{word}::"
put at <user.text>: "{text} @ "
put label range: user.insert_between("", "@ ..")
put new vec: "Vec::new()"
put new box: "Box::new()"
put use: "use "
put use block: user.insert_between("use {", "};")
put use {user.rust_crates}: user.insert_between("use {rust_crates}::", ";")
put tokyo main: #[tokio::main]
put async: "async "
put pub: "pub "
put mod: "mod "
put static ref: "static ref "

# TODO: Make all derivable trait values something we can say and have automatically added
put derive: user.insert_between("#[derive(", ")]")
put derive debug: "#[derive(Debug)]"
put derive clone: "#[derive(Clone)]"
put derive copy: "#[derive(Copy)]"
put derive default: "#[derive(Default)]"
put derive display: "#[derive(Display)]"
put derive error: "#[derive(Error)]"
put default: "#[default]"
funk {user.formatted_functions}: 
    insert(formatted_functions)
    user.insert_between('("', '");')
put A sink trait: "#[async_trait]"

put used: "#[used]"
put test: "#[test]"
put ignore: "#[ignore]"
put ignored test: "#[test]\n#[ignore]"
put config test: "#[cfg(test)]"
put config any: user.insert_between("#[cfg(any(", "))]")
put config X sixty four: "#[cfg(target_arch = \"x86_64\")]"
put config X thirty two: "#[cfg(target_arch = \"x86\")]"
put config arm: "#[cfg(target_arch = \"arm\")]"
put config arm sixty four: "#[cfg(target_arch = \"aarch64\")]"
# TODO: It would be nice to automatically be able to specify multiple
# architecture's and wrap it inside of any()
# TODO: automatically create test module in functions, add things like expect panic
put (rep|represent) C: "#[repr(C)]"

put global warn unused variables: "#![warn(unused_variables)]"
put global warn unused imports: "#![warn(unused_imports)]"
put global warn unused results: "#![warn(unused_results)]"
put global warn unused mut: "#![warn(unused_mut)]"
put global warn dead code: "#![warn(dead_code)]"

put warn unused variables: "#[warn(unused_variables)]"
put warn unused imports: "#[warn(unused_imports)]"
put warn unused results: "#[warn(unused_results)]"
put warn unused mut: "#[warn(unused_mut)]"
put warn dead code: "#[warn(dead_code)]"

put global allow unused variables: "#![allow(unused_variables)]"
put global allow unused imports: "#![allow(unused_imports)]"
put global allow unused results: "#![allow(unused_results)]"
put global allow unused mut: "#![allow(unused_mut)]"
put global allow non camel [case] [types] : "#![allow(non_camel_case_types)]"
put global allow dead code: "#![allow(dead_code)]"
put global allow unreachable code: "#![allow(unreachable_code)]"

put allow unused variables: "#[allow(unused_variables)]"
put allow unused imports: "#[allow(unused_imports)]"
put allow unused results: "#[allow(unused_results)]"
put allow unused mut: "#[allow(unused_mut)]"
put allow non camel [case] [types] : "#[allow(non_camel_case_types)]"
put allow dead code: "#[allow(dead_code)]"
put allow unreachable code: "#[allow(unreachable_code)]"


[put] returns [result] box error: "-> Result<(), Box<dyn Error>>"
put result box error: "Result<(), Box<dyn Error>>"

put result of <user.code_type> and <user.code_type>: "Result<{code_type}, Box<dyn Error>>"

put form {user.closed_format_strings}:
    insert("{closed_format_strings}")
put form inner  {user.inner_format_strings}:
    insert(":{inner_format_strings}")

put [{user.code_type_modifier}] sliced <user.code_type>: 
    insert(code_type_modifier or "")
    insert("[{code_type}]")

put [{user.code_type_modifier}] <number> element <user.code_type> array: 
    insert(code_type_modifier or "")
    insert("[{code_type}; {number}]")

put [{user.code_type_modifier}] <user.code_type> array:
    insert(code_type_modifier or "")
    user.insert_between("[{code_type}; ", "]")

put zero init <number> elements:
    insert("[0; {number}]")

put as <user.code_type>: "as {code_type}"

put new {user.rust_allocatable_types}:
    insert("{rust_allocatable_types}::new()")


put (stood|standard) {user.rust_std_modules}:
    insert("std::{rust_std_modules}::")

put (stood|standard) {user.rust_std_modules} <user.text>:
    insert("std::{rust_std_modules}::")
    insert(user.formatted_text(text or "", "PUBLIC_CAMEL_CASE"))

put collect as <user.code_containing_type> of [<user.code_type>]:
    type = user.code_type or ""
    insert("collect::{code_containing_type}<{type}>()")