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
(state|put) unsafe: "unsafe "
unsafe block: user.code_state_unsafe()

## rust centric struct and enum definitions
(state|put) (struct | structure) <user.text>:
    insert("struct ")
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))

(state|put) enum <user.text>:
    insert("enum ")
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))

toggle use: user.code_toggle_libraries()

## Simple aliases
borrow: "&"
borrow (mutable|mute): "&mut "
(state|put) (a sink | async | asynchronous): "async "
(state|put) (pub | public): "pub "
(state|put) (pub | public) crate: "pub(crate) "
(state|put) (dyn | dynamic): "dyn "
(state|put) constant: "const "
(state|put) (funk | func | function): "fn "
(state|put) (imp | implements): "impl "
(state|put) let mute: "let mut "
(state|put) let: "let "
(state|put) (mute | mutable): "mut "
(state|put) (mod | module): "mod "
(state|put) ref (mute | mutable): "ref mut "
(state|put) ref: "ref "
(state|put) trait: "trait "
(state|put) match: user.code_state_switch()
(state|put) (some | sum): "Some"
(state|put) static: "static "
self taught: "self."
(state|put) use: user.code_import()

use <user.code_libraries>:
    user.code_insert_library(code_libraries, "")
    key(; enter)

## specialist flow control
(state|put) if let some: user.code_insert_if_let_some()
(state|put) if let (ok | okay): user.code_insert_if_let_okay()
(state|put) if let error: user.code_insert_if_let_error()

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
put right [inclusive] range: "..="
put left [inclusive] range: "=.."
put range: ".."
put turbo fish: "::<>"
put new vec: "Vec::new()"
put new box: "Box::new()"
put returns box error: "-> Result<(), Box<dyn std::error::Error>>"
put result box error: "Result<(), Box<dyn std::error::Error>>"
