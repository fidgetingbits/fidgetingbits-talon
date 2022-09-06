# A lot of this was taken from the fireeye voiceattackprofile, under the
# assumption either people might already be familiar with the commands
# https://fireeye.github.io/IDA_Pro_VoiceAttack_profile/Reference_sheet.html
app: ida
-
tag(): user.ida
tag(): user.disassembler
settings():
    # the number of opcodes to display next to assembly instructions, this will
    # depend on your architecture
    user.ida_opcode_count = 8
toggle graph: key(space)

# Documenting

##
# Menu
##
open file menu: key(alt-f)
open edit menu: key(alt-e)
open debugger menu: key(alt-u)
open jump menu: key(alt-j)
open lumina menu: key(alt-n)
open options menu: key(alt-o)
open search menu: key(alt-h)
open view menu: key(alt-v)
open windows menu: key(alt-w)
(quit|exit) without saving:
    key(alt-x)
    sleep(500ms)
    key(tab down space tab enter)

# File Menu
open new instance:
    key(alt-f)
    sleep(500ms)
    key(down)
    key(enter)
open new file:
    key(alt-f)
    sleep(500ms)
    key(down:1)
    key(enter)

load script [file]:
    key(alt-f7)

# C header
load header: key(ctrl-f9)

# Open subviews
quick view: key(ctrl-1)
decompile: key(f5)
view names: key(shift-f4)
view functions: key(shift-f3)
view strings: key(shift-f12)
view segments: key(shift-f7)
view segment registers: key(shift-f8)
view signatures: key(shift-f5)
view type libraries: key(shift-f11)
view structures: key(shift-f9)
view (enumerations|E numbs): key(shift-f10)
view [local] types: key(shift-f1)

##
# General options management
##
open general options: user.ida_open_general_options()
toggle (addresses|[line] prefixes):
    user.ida_open_general_options()
    key(alt-p)
    user.accept_change()

toggle opcodes:
    user.ida_open_general_options()
    key(alt-d)
    user.accept_change()

##
# Decompiler
##

collapse: key(keypad_minus)
expand: key(keypad_plus)
set type: key(y)
matching: key(%)
refresh: key(f5)

##
# Misc
##

(jump mark|[book] marks show): key(ctrl-m)
[book] mark new : key(alt-m)

# Data Window
make pointer: key(o)
