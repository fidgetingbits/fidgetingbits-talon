tag: user.debugger
-

# Assembly language selection
current architecture: user.debugger_current_architecture()
cycle architecture: user.debugger_cycle_architecture()

# Code execution

## instruction level
step into: user.debugger_step_into()
step over: user.debugger_step_over()

## line level
step line: user.debugger_step_line()
(step over|next) line: user.debugger_step_over_line()
step out: user.debugger_step_out()
continue: user.debugger_continue()

## these are multi word to avoid accidental utterance
debug start: user.debugger_start()
debug stop: user.debugger_stop()
debug (exit|quit): user.debugger_exit()
debug force (exit|quit): user.debugger_exit_force()
debug detach: user.debugger_detach()
debug restart: user.debugger_restart()

# Register
show registers: user.debugger_show_registers()
# XXX -
get register: user.debugger_get_register()
set register: user.debugger_set_register()

# Breakpoints
break (now|into): user.debugger_break_now()
break here: user.debugger_break_here()
break [point] (list|show): user.debugger_show_breakpoints()
break [point] (set|add): user.debugger_add_sw_breakpoint()
break [point] (set|add) hardware: user.debugger_add_hw_breakpoint()
break [point] clear all :user.debugger_clear_all_breakpoints()
break [point] clear :user.debugger_clear_breakpoint()
break [point] clear <number_small>: user.debugger_clear_breakpoint_id(number_small)
break [point] disable all :user.debugger_disable_all_breakpoints()
break [point] disable :user.debugger_disable_breakpoint()
break [point] disable <number_small>: user.debugger_disable_breakpoint_id(number_small)
break [point] enable all :user.debugger_enable_all_breakpoints()
break [point] enable :user.debugger_enable_breakpoint()
break [point] enable <number_small>: user.debugger_enable_breakpoint_id(number_small)

# Navigation


# Memory Inspection
(stack|back) trace: user.debugger_backtrace()
(disassemble|dizzy): user.debugger_disassemble()
(disassemble|dizzy) here: user.debugger_disassemble_here()
(disassemble|dizzy) clip: user.debugger_disassemble_clipboard()
jump to address: user.debugger_goto_address()
jump to clipboard: user.debugger_goto_clipboard()
jump to highlighted: user.debugger_goto_highlighted()

dump string: user.debugger_dump_ascii_string()
dump unicode [string]: user.debugger_dump_unicode_string()
dump pointers: user.debugger_dump_pointers()

list modules: user.debugger_list_modules()
list sections: user.debugger_show_binary_sections()
list memory [mapping]: user.debugger_show_memory_sections()


# Type inspection
inspect type: user.debugger_inspect_type()
inspect type clip: user.debugger_inspect_type_clip()

# Hex Dumping Memory
#hex dump register:

# Convenience
clear command: user.debugger_clear_line()
