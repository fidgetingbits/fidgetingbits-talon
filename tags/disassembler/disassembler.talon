tag: user.disassembler
-

# File handling
file open:
    user.disassembler_open_file()
(file save | sage):
    user.disassembler_save_file()
file close:
    user.disassembler_close_file()

# Formatting
make array:
    user.disassembler_make_array()
make binary:
    user.disassembler_make_binary()
make character:
    user.disassembler_make_character()
make code:
    user.disassembler_make_code()
make data:
    user.disassembler_make_data()
make decimal:
    user.disassembler_make_decimal()
make enum:
    user.disassembler_make_enum()
make hex:
    user.disassembler_make_hex()
make string:
    user.disassembler_make_string()
make (structure variable | struct var):
    user.disassembler_make_structure_variable()
make unicode:
    user.disassembler_make_unicode()

# Navigation
[(jump | go)] [to] entry point:
    user.disassembler_entry_point()
(jump | go) back:
    user.disassembler_jump_back()
(jump | go) [to] address:
    user.disassembler_jump_address()
[(jump | go) to] next call:
    user.disassembler_next_call()
[(jump | go) to] previous call:
    user.disassembler_previous_call()
[go] (funk | function) start:
    user.disassembler_function_start()
[go] (funk | function) end:
    user.disassembler_function_end()
follow false:
    user.disassembler_false_branch()
follow true:
    user.disassembler_true_branch()
[cross] references to:
    user.disassembler_cross_references_to()
[cross] references from:
    user.disassembler_cross_references_from()

# Windowing
show disassembly:
    user.disassembler_focus_disassembly()
close window:
    user.disassembler_close_window()

# Searching
search bytes:
    user.disassembler_search_bytes()
search text:
    user.disassembler_search_text()
search value:
    user.disassembler_search_value()
next bytes:
    user.disassembler_next_bytes()
next code:
    user.disassembler_next_code()
next data:
    user.disassembler_next_data()
next explored:
    user.disassembler_next_explored()
next text:
    user.disassembler_next_text()
next unexplored:
    user.disassembler_next_unexplored()
next value:
    user.disassembler_next_value()
next void:
    user.disassembler_next_void()

# Documenting
undo:
    user.disassembler_undo()
redo:
    user.disassembler_redo()
