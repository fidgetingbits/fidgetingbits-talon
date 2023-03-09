# A lot of this was taken from the fireeye voiceattackprofile, under the
# assumption either people might already be familiar with the commands
# https://fireeye.github.io/IDA_Pro_VoiceAttack_profile/Reference_sheet.html
app: ida
-
tag(): user.ida
tag(): user.disassembler
tag(): user.retsync
tag(): user.hexrayspytools

settings():
    # the number of opcodes to display next to assembly instructions, this will
    # depend on your architecture
    user.ida_opcode_count = 8
toggle graph:
    key(space)

# Documenting
block comment:
    key(insert)
comment:
    key(/)

##
# Menu
##
open file menu:
    key(alt-f)
open edit menu:
    key(alt-e)
open debugger menu:
    key(alt-u)
open jump menu:
    key(alt-j)
open lumina menu:
    key(alt-n)
open options menu:
    key(alt-o)
open search menu:
    key(alt-h)
open view menu:
    key(alt-v)
open windows menu:
    key(alt-w)
# File Menu
[file] (quit | exit) without saving:
    key(alt-x)
    sleep(500ms)
    key(tab down space tab enter)
file quit:
    key(alt-x)
    sleep(500ms)
    key(enter)
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
open last [file]:
    key(alt-f)
    sleep(500ms)
    key(0)
load script [file]:
    key(alt-f7)

# C header
load header:
    key(ctrl-f9)
load last header:
    key(ctrl-f9)
    sleep(500ms)
    key(enter)

# Open subviews
quick view:
    key(ctrl-1)
decompile:
    key(f5)
view names:
    key(shift-f4)
view functions:
    key(shift-f3)
view strings:
    key(shift-f12)
view segments:
    key(shift-f7)
view segment registers:
    key(shift-f8)
view signatures:
    key(shift-f5)
view type libraries:
    key(shift-f11)
view structures:
    key(shift-f9)
view (enumerations | E numbs):
    key(shift-f10)
view [local] types:
    key(shift-f1)

##
# General options management
##
open general options:
    user.ida_open_general_options()
toggle (addresses | [line] prefixes):
    user.ida_open_general_options()
    key(alt-p)
    user.accept_change()

toggle opcodes:
    user.ida_open_general_options()
    key(alt-d)
    user.accept_change()

##
# Decompile
##

collapse:
    key(keypad_minus)
expand:
    key(keypad_plus)
set type:
    key(y)
matching:
    key(%)
refresh:
    key(f5)

##
# Misc
##

(jump mark | [book] marks show):
    key(ctrl-m)
[book] mark new:
    key(alt-m)

# Data Window
make pointer:
    key(o)

##
# Lumina
##

lumina push:
    key(f12)
lumina pull:
    key(ctrl-f12)
lumina view:
    key(alt-f12)

##
# Window Focusing
#
# Some of these are custom, you have to set them in Options->Shortcuts. You can
# also see the current ones with shortcuts in the quick view (ctrl-1). You can
# see the OpenXXX Actions in the shortcuts to find most of the views, although
# it's missing the disassembly view.
##
go quick view:
    key(ctrl-1)

go in numbs:
    key(shift-f10)
go command:
    key(ctrl-.)
go functions:
    key(shift-f3)
go local types:
    key(shift-f1)
go names:
    key(shift-f4)
go segment registers:
    key(shift-f8)
go segment:
    key(shift-f7)
go signatures:
    key(shift-f5)
go stack variables:
    key(ctrl-k)
go strings:
    key(shift-f12)
go structures:
    key(shift-f9)
go type libraries:
    key(shift-f11)

go code:
    key(tab)

# Custom Actions
go callers:
    key(ctrl-shift-f10)
go exports:
    key(ctrl-shift-f12)
go imports:
    key(ctrl-shift-f9)
#go notepad: key()
#go problems: key()
#go selectors: key()
#go source file: key()

tabby close:
    key(alt-f3)
tabby left:
    key(shift-f6)
tabby right:
    key(f6)

##
# Dialog Boxes
##
box confirm:
    key(alt-k)
box close:
    key(alt-f4)

## Navigation

go (home | top):
    key(home:3)
go bend:
    key(home)
go lend:
    key(end)
go bottom:
    key(end:3)

move up:
    key(ctrl-up)
move down:
    key(ctrl-down)
jump code start:
    key(ctrl-pgup)
jump code end:
    key(ctrl-pgdown)

tabby next:
    key(F6)
jump refs:
    key(x)
jump forward:
    key(ctrl-enter)
