# USAGE: - See doc/vim.md for usage and tutorial
#  - See code/vim.py very implementation and additional motion grammars
#
# FILES:
#  Files are split up as follows largely to reduce the grammar size and prevent
#  talent from being overloaded when trying to switch contexts process the
#  grammar tree. Unfortunately this makes it slightly more difficult to find
#  commands quickly.
#   * vim.talon - general settings, tag management, and commands the work across
#                 all modes
#   * vim_motion_mode.talon   - commands that work across all motion modes
#   * vim_terminal_mode.talon - commands that only work in terminal mode
#   * vim_normal_mode.talon   - commands that only work in normal mode
#   * vim_visual_mode.talon   - commands that only work in visual mode
#   * vim_insert_mode.talon   - commands that only work in insert mode
#
# NOTE:
# Where applicable I try to explicitly select appropriate API for terminal
# escaping, etc. However in cases where it is unlikely you will say a command
# from terminal mode, I don't bother. Example "save file" doesn't have explicit
# terminal escaping. This also helps an embedded vim running inside of a vim
# terminal work properly.
#
# TODO:
#  - add word jumping and searching for command mode
#  - test on windows and mac
#  - everything in this files should technically use _exterm() version of
#    functions
#
# BUGS:
#  - With sending the command-line mode commands in the background via RPC we
#  miss out on the display of some features. Ex: ALEInfo becomes unreadable...
#  need to figure out how to fix this.
app: vim
and not tag: user.vim_command_mode
-

tag(): user.vim
tag(): user.tabs
# TODO - add line_commands, etc

# Talon VIM plugin tags - see plugins/ for implementations Comment out plugins
# below that you don't use Also see vim_motion_mode.talon for plugin grammars
# that aren't enabled in terminal mode

# they should only include things that you want enabled in effectively all
# modes, including terminal mode. anything else should be more granularly
# enabled
#tag(): user.vim_fern
#tag(): user.vim_fern_mapping_fzf
tag(): user.vim_floaterm
#tag(): user.vim_fzf
tag(): user.vim_telescope
tag(): user.vim_mkdx
tag(): user.vim_nerdtree
tag(): user.vim_obsession
#tag(): user.vim_plug
#tag(): user.vim_lightspeed
tag(): user.vim_signature
tag(): user.vim_taboo
tag(): user.vim_tabular
#tag(): user.vim_taskwiki
tag(): user.vim_test
tag(): user.vim_unicode
tag(): user.vim_wiki
tag(): user.vim_you_are_here
tag(): user.vim_zoom
tag(): user.vim_zenmode
tag(): user.vim_codeql
tag(): user.vim_mason
tag(): user.vim_lazy

# To the settings below dictate how certain parts of Talon VIM will work. You
# can leave them or tweak them to your needs.
settings():
    # Whether or not to always revert back to the previous mode. Example, if
    # you are in insert mode and say 'delete word' it will delete one word and
    # keep you in insert mode. Same as ctrl-o in VIM.
    user.vim_preserve_insert_mode = 1

    # Whether or not to automatically adjust modes when using commands. Example
    # saying "go line 50" will first switch you out of INSERT into NORMAL and
    # then jump to the line. Disabling this setting would put :50\n into your
    # file if you say "row 50" while in INSERT mode.
    user.vim_adjust_modes = 1

    # Select whether or not talon should dispatch notifications on mode changes
    # that are made. Not yet completed, as notifications are kind of wonky on
    # Linux
    user.vim_notify_mode_changes = 0

    # Whether or not all commands that transfer out of insert mode should also
    # automatically escape out of terminal mode. Turning this on is quite
    # troublesome.
    user.vim_escape_terminal_mode = 0

    # When issuing counted actions in vim you can prefix a count that will
    # dictate how many times the command is run, however some peoples talon
    # grammar already allows you to utter a number without a prefix (ex: voice
    # command "ten" will put 10 in your file) so we want to cancel any existing
    # counts that might already by queued in vim in error.
    #
    # This also helps prevent accidental number queueing if talon
    # mishears a command such as "delete line" as "delete" "nine". Without this
    # setting, if you then said "undo" it would undo the last 9 changes, which
    # is annoying.
    #
    # This setting only applies to commands run through the actual counted
    # actions grammar itself
    user.vim_cancel_queued_commands = 1

    # When you are escaping queued commands, it seems vim needs time to recover
    # before issuing the subsequent commands. This controls how long it waits,
    # in seconds
    user.vim_cancel_queued_commands_timeout = 0.20

    # It how long to wait before issuing commands after a mode change. You
    # want adjust this if when you say things like undo from INSERT mode, an
    # "u" gets inserted into INSERT mode. It in theory that shouldn't be
    # required if using pynvim.
    user.vim_mode_change_timeout = 0.25

    # When you preserve mode and switch into into insert mode it will often
    # move your cursor, which can mess up the commands you're trying to run from
    # insert. This setting controls the cursor move
    user.vim_mode_switch_moves_cursor = 0

    # Whether or not use pynvim rpc if it is available
    user.vim_use_rpc = 1

    # Adds debug output to the talon log
    user.vim_debug = 0

###
# File editing and management
###
file save all: user.vim_command_mode_exterm(":wa\n")

# no \n as a saftey measure
(close | quit) all: user.vim_command_mode_exterm(":qa")

force (close | quit) all: user.vim_command_mode_exterm(":qa!")

force (close | quit): user.vim_command_mode_exterm(":q!\n")
file (edit | open): user.vim_command_mode_exterm(":e ")
file (edit | open) clip:
    user.vim_command_mode_exterm(":e ")
    edit.paste()
file (edit | open) <user.paths>: user.vim_command_mode_exterm(":e {paths}\n")
(reload [vim] config | config reload): user.vim_command_mode_exterm(":so $MYVIMRC\n")

###
# Navigation, movement and jumping
#
# NOTE: Majority of more core movement verbs are in code/vim.py
###
go row <number>: user.vim_command_mode_exterm(":{number}\n")

# These are especially useful when in terminal mode and you want to jump to
# something in normal mode that is in the history. Doubley so if you use
# set relativenumber in terminal mode
[go] relative up [line] <number_small>:
    user.vim_any_motion_mode_exterm("{number_small}k")

[go] relative down [line] <number_small>:
    user.vim_any_motion_mode_exterm("{number_small}j")

push line <number>:
    user.vim_command_mode_exterm(":{number}\n")
    user.vim_normal_mode_np("$a")

# jump list
# XXX - I'm not sure these are well usable from the terminal?
jump list show: user.vim_command_mode_exterm(":jumps\n")
jump list clear: user.vim_command_mode_exterm(":clearjumps\n")
jump list last [entry]: user.vim_normal_mode_exterm_key("ctrl-o")
jump list next [entry]: user.vim_normal_mode_exterm_key("ctrl-i")

# scrolling and page position
# NOTE counted scrolling his handled in vim.py
# XXX - it seems like comboing \n in command mode doesn't work well?
scroll [on] line <number>: user.vim_command_mode_exterm(":{number}\nzt")
center [on] line <number>: user.vim_command_mode_exterm(":{number}\nz.")
scroll top: user.vim_normal_mode_exterm("zt")
scroll middle: user.vim_normal_mode_exterm("zz")
scroll bottom: user.vim_normal_mode_exterm("zb")
# XXX - change these exist scroll top curse ?
scroll top reset cursor: user.vim_normal_mode_exterm("z\n")
scroll middle reset cursor: user.vim_normal_mode_exterm("z.")
scroll bottom reset cursor: user.vim_normal_mode_exterm("z ")

###
# Buffers
###
(buf | buffer) list: user.vim_command_mode_exterm(":ls\n")
(buf | buffer) (close | delete) <number_small>:
    user.vim_command_mode_exterm(":bd {number_small} ")
(buf | buffer) delete: user.vim_command_mode_exterm(":bd ")
(buf | buffer) close [current]: user.vim_command_mode_exterm(":bd\n")
(buf | buffer) close last: user.vim_command_mode_exterm(":bd #\n")
(buf | buffer) force close: user.vim_command_mode_exterm(":bd!\n")
force botch: user.vim_command_mode_exterm(":bd!\n")
(buf | buffer) open: user.vim_command_mode_exterm(":b ")
[go] (buf | buffer) (first | rewind): user.vim_command_mode_exterm(":br\n")
[go] (buf | buffer) (left | prev): user.vim_command_mode_exterm(":bprev\n")
[go] (buf | buffer) (right | next): user.vim_command_mode_exterm(":bnext\n")
[go] (buf | buffer) flip: user.vim_command_mode_exterm(":b#\n")
# this is more consistent with some of my other editing commands
file back: user.vim_command_mode_exterm(":b#\n")
[go] (buf | buffer) last: user.vim_command_mode_exterm(":bl\n")
close (bufs | buffers): user.vim_command_mode_exterm(":bd ")
(buf | buffer) open <number>: user.vim_command_mode_exterm(":b {number}\n")
# creates a split and then moves the split to a tab. required for when the
# current tab has only one split
(buf | buffer) (move to | make) tab:
    user.vim_normal_mode_exterm(":split\n")
    key(ctrl-w)
    key(T)
(buf | buffer) rename: user.vim_command_mode_exterm(":file ")
(buf | buffer) rename <user.text>: user.vim_command_mode_exterm(":file {text}")
new (empty | unnamed) buffer: user.vim_command_mode_exterm(":enew\n")
(buf | buffer) do: user.vim_command_mode_exterm(":bufdo ")
(buf | buffer) show:
    user.vim_command_mode_exterm(":let g:buf_num = bufnr('%') | echo g:buf_num\n")
(buf | buffer) open (cached | last):
    user.vim_command_mode_exterm(':execute "buffer" g:buf_num\n')

###
# Splits
#
# XXX - it may be cleaner to have these in a vim.py function
# XXX - most split open commands should be able to take a buffer argument
###
# creating splits
(split new [horizontal] | river):
    user.vim_set_normal_mode_exterm()
    key("ctrl-w")
    key(s)

river term: user.vim_command_mode_exterm(":split term://zsh\n")
(split new vertical | pillar):
    user.vim_set_normal_mode_exterm()
    key("ctrl-w")
    key(v)
pillar term: user.vim_command_mode_exterm(":vsplit term://zsh\n")

new top left split: user.vim_command_mode_exterm(":to split\n")

new left above split: user.vim_command_mode_exterm(":lefta split\n")

new right below split: user.vim_command_mode_exterm(":rightb split\n")

new (bot | bottom) right split: user.vim_command_mode_exterm(":bo split\n")

new vertical top left split: user.vim_command_mode_exterm(":vertical to split\n")

new vertical left above split: user.vim_command_mode_exterm(":vertical lefta split\n")

new vertical right below split:
    user.vim_command_mode_exterm(":vertical rightb split\n")

new vertical (bot | bottom) right split:
    user.vim_command_mode_exterm(":vertical bo split\n")

    # open specified buffer in new split
split (buf | buffer) <number_small>:
    user.vim_set_normal_mode_exterm()
    insert("{number_small}")
    key("ctrl-w")
    key("ctrl-^")

# open specified buffer in new vertical split
vertical split (buf | buffer) <number_small>:
    user.vim_command_mode_exterm(":vsplit {number_small}")

# creating and auto-entering splits

split (close | kill):
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(q)

# technically this won't always work
split reopen vertical: user.vim_command_mode_exterm(":vsplit#\n")
split reopen [horizontal]: user.vim_command_mode_exterm(":split#\n")

new (empty | unnamed) [horizontal] split: user.vim_command_mode_exterm(":new\n")
new (empty | unnamed) (vertical | v) split: user.vim_command_mode_exterm(":vnew\n")

# navigating splits
# XXX - we could leverage split.talon stuff here?
split <user.vim_arrow>:
    user.vim_normal_mode("\\<c-w>{vim_arrow}")
    #user.vim_set_normal_mode_exterm()
    #key(ctrl-w)
    #key("{vim_arrow}")
(split flip | spitter):
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(p)
split top left:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(t)
split next:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(w)
split (previous | prev):
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(W)
split bottom right:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(b)
split preview:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(P)
split <number_small>:
    user.vim_set_normal_mode_exterm()
    insert("{number_small}")
    key(ctrl-w ctrl-w)

# personal convenience shortcuts

# split right
sprite:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(l)

# split left
spliff:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(h)

# moving windows
split (only | exclusive):
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(o)
split swap:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(x)
split rotate [right]:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(r)
split rotate left:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(R)
split move (up | top):
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(K)
split move (down | bottom):
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(J)
split move right:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(L)
split move left:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(H)
split (move to | make) tab:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(T)

# window resizing
(split equalize | balance):
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(=)

# this is for easily isolating a split in the middle of a window to make it
# easier to read well full screen
# XXX - we can calculate this automatically using the trick here:
# https://stackoverflow.com/questions/12952479/how-to-center-horizontally-the-contents-of-the-open-file-in-vim
# if you have zen mode plug in it's better than this...
split (zen mode | center):
    user.vim_set_normal_mode_exterm()
    insert(":topleft vnew\n")
    insert(":botright vnew\n")
    key(ctrl-w)
    key(=)
    key(ctrl-w h)

#split grow:
# XXX - it would be nice if this could grow it fatter but keep it centered,
# like if were in split zen mode, but we want to make the middle split
# bigger

# XXX - it would be nice to have percents for these resizes..
# atm comboing these with ordinals is best, but may add number support
split taller:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(+)
    # XXX - This should restore the original mode, is sometimes I use this from
    # terminal mode
split shorter:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(-)
    # XXX - This should restore the original mode, is sometimes I use this from
    # terminal mode
split fatter:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(>)
    # XXX - This should restore the original mode, is sometimes I use this from
    # terminal mode
split skinnier:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(<)
set split width: user.vim_command_mode_exterm(":resize ")
set split height: user.vim_set_command_mode_exterm(":vertical resize ")

# XXX - this has conflicted with split zoom before
(split | window) do: user.vim_command_mode_exterm(":windo ")

###
# Diffing
###
(split | window) (start diff | compare):
    user.vim_command_mode_exterm(":windo diffthis\n")

(split | window) (end diff | compare):
    user.vim_command_mode_exterm(":windo diffoff!\n")

buffer (start diff | compare): user.vim_command_mode_exterm(":bufdo diffthis\n")

buffer (end diff | compare): user.vim_command_mode_exterm(":bufdo diffoff!\n")

# XXX - talon doesn't like the word diff
(refresh | update) (changes | diff | compare):
    user.vim_command_mode_exterm(":diffupdate\n")

[go] next (conflict | change): user.vim_normal_mode_exterm("]c")

[go] (prev | previous) (conflict | change): user.vim_normal_mode_exterm("[c")

###
# Tab
#
# This is a combination of Talon generic commands from `misc/tab.talon` and my
# own extras.
###

# `misc/tab.talon` versions
[go] tabby <number_small>: user.vim_normal_mode_exterm("{number_small}gt")

tabby list: user.vim_command_mode(":tabs\n")

# XXX - overlaps with the user.tabs stuff
[go] tabby (next | right): user.vim_command_mode_exterm(":tabnext\n")
[go] tabby (left | prev | previous): user.vim_command_mode_exterm(":tabprevious\n")
[go] tabby first: user.vim_command_mode_exterm(":tabfirst\n")
[go] tabby last: user.vim_command_mode_exterm(":tablast\n")
[go] tabby flip: user.vim_normal_mode_exterm("g\t")
tabby edit: user.vim_command_mode_exterm(":tabedit ")
tabby move right: user.vim_command_mode_exterm(":tabm +\n")
tabby move left: user.vim_command_mode_exterm(":tabm -\n")
edit (buf | buffer) <number_small> [in] new tab:
    user.vim_command_mode_exterm(":tabnew #{number_small}\n")

[new] tabby terminal: user.vim_command_mode_exterm(":tabe term://bash\n")

###
# Settings
###
# Sometimes the command bar height is too big, this makes it smaller
rebalance command: user.vim_command_mode_exterm(":set cmdheight=1\n")
# XXX - this is a weird edge case because we actually probably want to slip back
# to the terminal mode after setting options, but atm
# user.vim_normal_mode_exterm() implies no preservation
(show | set) highlight search: user.vim_command_mode_exterm(":set hls\n")
lights out: user.vim_command_mode_exterm(":set nohls\n")
lights on:
    user.vim_command_mode_exterm(":set hls\n")
    # only disable until next search
lights off: user.vim_command_mode_exterm(":noh\n")
(show | set) line numbers: user.vim_command_mode_exterm(":set nu\n")
(show | set) absolute [line] [numbers]:
    user.vim_command_mode_exterm(":set norelativenumber\n")
    user.vim_command_mode_exterm(":set number\n")
(show | set) relative [line] [numbers]:
    user.vim_command_mode_exterm(":set nonumber\n")
    user.vim_command_mode_exterm(":set relativenumber\n")
    # XXX - make a vimrc function to toggle
(unset | set no | hide) line numbers: user.vim_command_mode_exterm(":set nonu\n")
show [current] settings: user.vim_command_mode_exterm(":set\n")
(unset paste | set no paste): user.vim_command_mode_exterm(":set nopaste\n")
# very useful for reviewing code you don't want to accidintally edit if talon
# mishears commands
set modifiable: user.vim_command_mode_exterm(":set modifiable\n")
(unset modifiable | set no modifiable):
    user.vim_command_mode_exterm(":set nomodifiable\n")
show filetype: user.vim_command_mode_exterm(":set filetype\n")
show tab stop:
    user.vim_command_mode_exterm(":set tabstop\n")
    user.vim_command_mode_exterm(":set shiftwidth\n")
set tab stop <digits>:
    user.vim_command_mode_exterm(":set tabstop={digits}\n")
    user.vim_command_mode_exterm(":set shiftwidth={digits}\n")
set see indent: user.vim_command_mode_exterm(":set cindent\n")
(set no see indent | unset see indent):
    user.vim_command_mode_exterm(":set nocindent\n")
set smart indent: user.vim_command_mode_exterm(":set smartindent\n")
(set no smart indent | unset smart indent):
    user.vim_command_mode_exterm(":set nosmartindent\n")
set file format unix: user.vim_command_mode_exterm(":set ff=unix\n")

###
# Marks
###
# TODO - need to fix this "True" for terminal return stuff
mark (add | new | create) <user.letter>:
    user.vim_normal_mode_exterm_keys("m {letter}", "True")

mark global [(new | create)] <user.upper_letter>:
    user.vim_normal_mode_exterm_keys("m {upper_letter}", "True")

(marker | jump mark) <user.letter>:
    user.vim_set_normal_mode_exterm()
    key(`)
    key(letter)

(marker global | gallop | jump mark global) <user.upper_letter>:
    user.vim_set_normal_mode_exterm()
    key(`)
    key(upper_letter)

(mark | marks) (del | delete | remove): user.vim_command_mode_exterm(":delmarks ")
(mark | marks) (del | delete | remove) all: user.vim_command_mode_exterm(":delmarks! ")
(mark | marks) (list | show) [all]: user.vim_command_mode_exterm(":marks\n")
(mark | marks) (list | show) specific: user.vim_command_mode_exterm(":marks ")

###
# Session
###
session save: user.vim_command_mode_exterm(":mksession ")
session force save: user.vim_command_mode_exterm(":mksession! ")
# XXX - this path could be made into a setting
session load: user.vim_command_mode_exterm(":source ~/.config/nvim/sessions/")
session show: user.vim_command_mode_exterm(":echo v:this_session\n")

# XXX - this is quite slow pasting into a terminal, so might want to move
# this register into the paste register and then use the native?
(paste from | pastor) [register] <user.unmodified_key>:
    user.vim_any_motion_mode_exterm('"{unmodified_key}p')

###
# Informational
###
man page: user.vim_command_mode_exterm(":Man ")
man page sys call: user.vim_command_mode_exterm(":Man 2 ")
man page this: user.vim_normal_mode("K")

###
# Mode Switching
###
[mode] normal: user.vim_set_normal_mode_np()
[mode] insert: user.vim_set_insert_mode()
mode terminal: user.vim_set_terminal_mode()
# command mode: user.vim_set_command_mode()
mode command [line]: user.vim_any_motion_mode_exterm_key(":")
(mode replace | overwrite): user.vim_set_replace_mode()
mode visual replace: user.vim_set_visual_replace_mode()
# This always conflicts with virtual pop somehow...
[mode] visual: user.vim_set_visual_mode()
mode line: user.vim_set_visual_line_mode()
mode block: user.vim_set_visual_block_mode()

# sort of quasi-modes - see vim_command_line.talon
show history: user.vim_command_mode(":hist\n")
command line (search | history) [mode]: user.vim_any_motion_mode_exterm_key("q:")
search command [mode]: user.vim_any_motion_mode_exterm_key("q/")

###
# Searching
###
# case insensitive search
search: user.vim_any_motion_mode_exterm("/\\c")

search clip:
    user.vim_any_motion_mode_exterm("/\\c")
    edit.paste()

# case sensitive search
search exact: user.vim_any_motion_mode_exterm("/\\C")

search exact clip:
    user.vim_any_motion_mode_exterm("/\\C")
    edit.paste()

#search <user.text>$:
#    user.vim_any_motion_mode_exterm("/\\c{text}\n")

#search <user.text> sensitive$:
#    user.vim_any_motion_mode_exterm("/\\C{text}\n")

#search <user.ordinals> <user.text>$:
#    user.vim_any_motion_mode_exterm("{ordinals}/\\c{text}\n")

# XXX - probably rename these
#search (reversed|reverse) <user.text>$:
#    user.vim_any_motion_mode_exterm("?\\c{text}\n")

search (reversed | reverse): user.vim_any_motion_mode_exterm("?\\c")

search exact (reversed | reverse): user.vim_any_motion_mode_exterm("?\\C")

###
# Visual Mode
###
(select | highlight) all: user.vim_normal_mode_exterm("ggVG")
reselect: user.vim_normal_mode_exterm("gv")

###
# Terminal mode
###

# NOTE: Below is duplicate command with vim_terminal.talon, but included in
# case user doesn't have `VIM mode:t` in titlestring
(escape | pop) (term | terminal):
    key(ctrl-\)
    key(ctrl-n)

new (term | terminal): user.vim_normal_mode_exterm(":term\n")

force new (term | terminal): user.vim_normal_mode_exterm(":term!\n")

[new] (split | horizontal) (term | terminal):
    # NOTE: if your using zsh you might have to switch this, though depending
    # on your setup it will still work (this loads zsh on mine)
    user.vim_normal_mode_exterm(":split term://bash\n")

[new] vertical split (term | terminal):
    user.vim_normal_mode_exterm(":vsplit term://bash\n")

###
# Functions
###
function list: user.vim_command_mode_exterm(":function\n")
function show: user.vim_command_mode_exterm(":function ")
function show brief: user.vim_command_mode_exterm(":function! ")
function search: user.vim_command_mode_exterm(":function / ")
function call: user.vim_command_mode_exterm(":call ")
recall last function:
    user.vim_command_mode_exterm(":call ")
    key(up)
    key(enter)

###
# Command mode
###
last command: user.vim_command_mode_exterm(":!!\n")
messages last: user.vim_normal_mode_exterm("g<")
messages show: user.vim_command_mode_exterm(":messages\n")

# This allows to see plug-in and script errors from the messages screen in a
# new editable buffer.
# WARNING: clobbers register a
messages extract:
    user.vim_command_mode_exterm(":vsplit\n")
    sleep(500ms)
    user.vim_command_mode(":enew\n")
    sleep(1000ms)
    user.vim_command_mode(":redir @a\n")
    sleep(200ms)
    user.vim_command_mode(":silent messages\n")
    sleep(200ms)
    user.vim_command_mode(":redir END\n")
    sleep(200ms)
    user.vim_normal_mode('"ap')
    user.vim_normal_mode("G")

###
# Convenience
###
command force:
    user.vim_command_mode_exterm(":")
    key(up !)

# useful for turning a git status list already yanked into a register into a
# space delimited list you can paste into the command line
remove newlines from register <user.unmodified_key>:
    user.vim_command_mode_exterm(":let @{unmodified_key}=substitute(strtrans(@{unmodified_key}),'\\^@',' ','g')\n")

# this assumes you have some sort of visual block selection that you want to
# become a single line. a good example of this would be something like a list
# of git changed files that you want to select and then all run an operation on
# ex:
#
# Unmerged paths:
#   (use "git add <file>..." to mark resolution)
#         both modified:   libheap/frontend/commands/gdb/ptchunk.py
#         both modified:   libheap/frontend/frontend_gdb.py
#         both modified:   libheap/ptmalloc/malloc_chunk.py
#         both modified:   libheap/ptmalloc/ptmalloc.py
yank as line:
    insert("y")
    user.vim_command_mode_exterm(":let @+=substitute(strtrans(@+),'\\^@',' ','g')\n")

paste as line:
    user.vim_command_mode_exterm(":let @+=substitute(strtrans(@+),'\\^@',' ','g')\n")
    sleep(200ms)
    edit.paste()

louis call func: user.vim_command_mode_exterm(":lua ")
louis reload (plug in | module):
    user.vim_command_mode_exterm(":lua require('plenary').reload_module('')")
