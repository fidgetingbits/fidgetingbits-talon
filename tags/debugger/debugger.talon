tag: user.debugger
-

# Assembly language selection
architecture show: user.debugger_current_architecture()
architecture cycle: user.debugger_cycle_architecture()

# Code execution

## instruction level
step into: user.debugger_step_into()
step over: user.debugger_step_over()
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
debug force exit: user.debugger_exit_force()
debug detach: user.debugger_detach()
debug restart: user.debugger_restart()

# Register
(show | info) (reg | regs | registers): user.debugger_show_registers()
# XXX -
(show | get) register [{user.registers}]: user.debugger_get_register(registers or "")
register {user.registers}: user.debugger_register_variable(registers)
set register {user.registers}: user.debugger_set_register(registers)

# Breakpoints
break (now | into): user.debugger_break_now()
break here: user.debugger_break_here()
break [point] (list | show): user.debugger_show_breakpoints()
break [point] (set | add): user.debugger_add_sw_breakpoint()
break [point] (set | add) hardware: user.debugger_add_hw_breakpoint()
break [point] (clear | remove) all: user.debugger_clear_all_breakpoints()
break [point] (clear | remove): user.debugger_clear_breakpoint()
break [point] (clear | remove) <number_small>:
    user.debugger_clear_breakpoint_id(number_small)
break [point] disable all: user.debugger_disable_all_breakpoints()
break [point] disable: user.debugger_disable_breakpoint()
break [point] disable <number_small>: user.debugger_disable_breakpoint_id(number_small)
break [point] enable all: user.debugger_enable_all_breakpoints()
break [point] enable: user.debugger_enable_breakpoint()
break [point] enable <number_small>: user.debugger_enable_breakpoint_id(number_small)

break [(set | add)] (indirect | star):
    user.debugger_add_sw_breakpoint()
    key(*)

break star clip:
    user.debugger_add_sw_breakpoint()
    key(*)
    edit.paste()
    key(enter)

break add clip:
    user.debugger_add_sw_breakpoint()
    edit.paste()
    key(enter)

# Navigation

# Memory Inspection
(stack | back) trace: user.debugger_backtrace()
(disassemble | dizzy): user.debugger_disassemble()
(disassemble | dizzy) here: user.debugger_disassemble_here()
(disassemble | dizzy) clip: user.debugger_disassemble_clipboard()
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
