tag: user.debugger
-

# Assembly language selection
(architecture|arch|ark) show: user.debugger_current_architecture()
(architecture|arch|ark) cycle: user.debugger_cycle_architecture()

# Code execution

## instruction level
step (in|into): user.debugger_step_into()
step (oh|over): user.debugger_step_over()
step next jump: user.debugger_step_jump()
step next call: user.debugger_step_call()
step next ret: user.debugger_step_ret()
step next sys call: user.debugger_step_syscall()

## line level (NOTE: pwndbg doesn't override these)
step line: user.debugger_step_line()
(step over | next) line: user.debugger_step_over_line()
(step out | finish): user.debugger_step_out()
continue: user.debugger_continue()

## these are multi word to avoid accidental utterance
debug start: user.debugger_start()
debug stop: user.debugger_stop()
debug (exit | quit): user.debugger_exit()
(quitter | debug force exit): user.debugger_exit_force()
debug attach: user.debugger_attach()
debug detach: user.debugger_detach()
debug restart: user.debugger_restart()

# Register
(show | info) (reg | regs | registers): user.debugger_show_registers()
# XXX -
(show | get) register [{user.registers}]: user.debugger_get_register(registers or "")
(register|reg) {user.registers}: user.debugger_register_variable(registers)
set (register|reg) {user.registers}: user.debugger_set_register(registers)

# Breakpoints
# FIXME: When in
<user.breakpoint> toggle: user.debugger_breakpoint_toggle()
<user.breakpoint> (now | into): user.debugger_break_now()
<user.breakpoint> here: user.debugger_break_here()
<user.breakpoint> [point] (list | show): user.debugger_show_breakpoints()
<user.breakpoint> [point] (set | add): user.debugger_add_sw_breakpoint()
<user.breakpoint> [point] (set | add) hardware: user.debugger_add_hw_breakpoint()
<user.breakpoint> [point] (clear | remove) all: user.debugger_clear_all_breakpoints()
<user.breakpoint> [point] (clear | remove): user.debugger_clear_breakpoint()
<user.breakpoint> [point] (clear | remove) <number_small>:
    user.debugger_clear_breakpoint_id(number_small)
<user.breakpoint> [point] disable all: user.debugger_disable_all_breakpoints()
<user.breakpoint> [point] disable: user.debugger_disable_breakpoint()
<user.breakpoint> [point] disable <number_small>: user.debugger_disable_breakpoint_id(number_small)
<user.breakpoint> [point] enable all: user.debugger_enable_all_breakpoints()
<user.breakpoint> [point] enable: user.debugger_enable_breakpoint()
<user.breakpoint> [point] enable <number_small>: user.debugger_enable_breakpoint_id(number_small)

<user.breakpoint> [(set | add)] (indirect | star):
    user.debugger_add_sw_breakpoint()
    key(*)

<user.breakpoint> star clip:
    user.debugger_add_sw_breakpoint()
    key(*)
    edit.paste()
    key(enter)

<user.breakpoint> add clip:
    user.debugger_add_sw_breakpoint()
    edit.paste()
    key(enter)

# Navigation

# Memory Inspection
(stack | back) trace: user.debugger_backtrace()
(disassemble | dizzy) [<number>]: user.debugger_disassemble(number or 10)
(disassemble | dizzy) [<number>] here: user.debugger_disassemble_here(number or 10)
(disassemble | dizzy) [<number>] clip:
    user.debugger_disassemble_clipboard(number or 10)
jump to address: user.debugger_goto_address()
jump to clipboard: user.debugger_goto_clipboard()
jump to highlighted: user.debugger_goto_highlighted()

list modules: user.debugger_list_modules()
list sections: user.debugger_show_binary_sections()
(memory list | memory map | list memory [mapping]):
    user.debugger_show_memory_sections()

# Type inspection
inspect type: user.debugger_inspect_type()
inspect type clip: user.debugger_inspect_type_clip()
inspect all types:
    user.debugger_inspect_all_types()
    key(enter)
type search [<user.text>]:
     user.debugger_search_types(text or "")

# Memory Analysis
hex dump help: user.debugger_hexdump_help()
hex dump [<number>] [from {user.registers}]:
    user.debugger_hexdump(number or 0, registers or "")
hex dump [<number>] bytes [from {user.registers}]:
    user.debugger_hexdump_bytes(number or 0, registers or "")
hex dump [<number>] words [from {user.registers}]:
    user.debugger_hexdump_word(number or 0, registers or "")
hex dump [<number>] (D | long) words [from {user.registers}]:
    user.debugger_hexdump_dword(number or 0, registers or "")
hex dump [<number>] (Q | quad) words [from {user.registers}]:
    user.debugger_hexdump_qword(number or 0, registers or "")

hex dump [<number>] [from] clip: user.debugger_hexdump_clip(number or 0)
hex dump [<number>] bytes [from] clip: user.debugger_hexdump_bytes_clip(number or 0)
hex dump [<number>] words [from] clip: user.debugger_hexdump_word_clip(number or 0)
hex dump [<number>] (D | long) words [from] clip:
    user.debugger_hexdump_dword_clip(number or 0)
hex dump [<number>] (Q | quad) words [from] clip:
    user.debugger_hexdump_qword_clip(number or 0)

dump [<number> byte] string [from {user.registers}]:
    user.debugger_dump_ascii_string(number or 0, registers or "")
dump [<number> byte] string from clip:
    user.debugger_dump_ascii_string_clip(number or 0)
dump [<number> byte] unicode [string] [from {user.registers}]:
    user.debugger_dump_unicode_string(number or 0, registers or "")
dump [<number> byte] unicode [string] from clip:
    user.debugger_dump_unicode_string_clip(number or 0)
dump pointers [from {user.registers}]: user.debugger_dump_pointers(registers or "")
dump pointers from clip: user.debugger_dump_pointers_clip()

# Convenience
clear command: user.debugger_clear_line()
(reg | register) {user.registers}: user.debugger_access_register(registers)
