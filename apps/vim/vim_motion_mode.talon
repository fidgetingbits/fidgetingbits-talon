# This file is for commands that should work in all motion modes (NORMAL,
# VISUAL, VBLOCK, INSERT) but it won't work for command or terminal mode. If
# you're not sure a command should be placed here it might be better to just
# put it in vim.talon, but mostly just ask yourself can you ever imagine being
# in command mode or inside of a terminal and wanting to run the command? If
# you can't imagine doing it, it suits this file over vim.talon

app:vim
not tag: user.vim_terminal
and not tag: user.vim_command_mode
-

# Talon VIM plugin tags - see plugins/ for implementations
# Comment out plugins below that you don't use
# Is the list below is only plugins that have grammars we use when outside of
# terminal mode.
tag(): user.vim_easymotion
tag(): user.vim_change_inside_surroundings
tag(): user.vim_surround
tag(): user.vim_ultisnips
tag(): user.vim_ale
tag(): user.vim_cscope
tag(): user.vim_fugitive
tag(): user.vim_fugitive_summary
tag(): user.vim_grammarous
tag(): user.vim_markdown
tag(): user.vim_markdown_toc
tag(): user.vim_youcompleteme
tag(): user.vim_easy_align
tag(): user.vim_eunuch
tag(): user.vim_rooter
tag(): user.vim_suda
tag(): user.vim_treesitter
tag(): user.vim_treesitter_textobjects

###
# `code/vim.py` actions - includes most motions and core commands
###
# commands that can be triggered in visual or normal mode, and generally don't
# have counting, etc
# XXX - I still need to investigate whether or not a subset of these should be
# exposed in terminal mode
<user.vim_normal_counted_motion_command>:
    user.vim_any_motion_mode("{vim_normal_counted_motion_command}")
<user.vim_normal_counted_motion_keys>:
    user.vim_any_motion_mode_key("{vim_normal_counted_motion_keys}")
<user.vim_motions_all_adjust>:
    user.vim_any_motion_mode("{vim_motions_all_adjust}")
<user.vim_normal_counted_action>:
    user.vim_any_motion_mode("{vim_normal_counted_action}")
<user.vim_normal_counted_actions_keys>:
    user.vim_any_motion_mode_key("{vim_normal_counted_actions_keys}")
<user.vim_counted_motion_command_with_ordinals>:
   user.vim_any_motion_mode("{vim_counted_motion_command_with_ordinals}")


###
# File editing and management
###
# These are prefix with `file` to match the `file save` action defined by talon
sage:
    user.vim_command_mode(":w\n")
file save as:
    key(escape)
    user.vim_command_mode(":w ")
# XXX - This should be vim_command_mode, but there's a bug in at lest
# vim-fugitive commit where you lose the commit text if called from INSERT
# mode, due to an unmodifiable buffer error
(file save and (quit|close)|squeak):
    user.vim_normal_mode(":wq\n")
file (close|quite):
    user.vim_command_mode(":q\n")
file (refresh|reload):
    user.vim_command_mode(":e!\n")
file show:
    user.vim_normal_mode_keys("ctrl-G")
(print working directory|folder show): user.vim_command_mode(":pwd\n")
pivot file:
    user.vim_command_mode(":lcd %:p:h\n")
pivot clip:
    user.vim_command_mode(":lcd ")
    edit.paste()
    key(enter)
#pivot (parent|back):
#    user.vim_command_mode(":lcd ..\n")
pivot select:
    user.vim_command_mode(":lcd ")
# Note below includes pivot back
pivot <user.folder_paths>:
    user.vim_command_mode(":lcd {folder_paths}\n")
file yank path:
    user.vim_command_mode(":let @+ = expand('%:p')\n")
file recover:
    user.vim_command_mode(":recover")


# For when the VIM cursor is hovering on a path
# NOTE: gx only works if you use netrw were custom mapped
#open [this] link: user.vim_normal_mode("gx")
# XXX - this is broken if the link has some special characters like #, it will
# replace with the act of buffer name
open [this] link:
    user.vim_command_mode(":!xdg-open ")
    key(ctrl-r ctrl-a enter)
(open this file|file jump): user.vim_normal_mode("gf")
(open this file offset|file jump offset): user.vim_normal_mode("gF")
# XXX - should automate this with the previous open for cases when a file
# doesn't exist...
file create this: 
    user.vim_command_mode(':call writefile([], expand("<cfile>"), "b")\n')
(river this [file]|file river jump):
    user.vim_set_normal_mode()
    key(ctrl-w)
    key(f)
open this file in vertical [split|window]:
    user.vim_command_mode(":vertical wincmd f\n")
(pillar this [file]|file pillar jump):
    user.vim_command_mode(":vertical wincmd f\n")


###
# Navigation, movement and jumping
###

# XXX - add support for [{, [(, etc
matching: user.vim_any_motion_mode_key("%")
matching <user.symbol_key>: user.vim_any_motion_mode("f{symbol_key}%")

# ctags/symbol
taggy jump: user.vim_normal_mode_key("ctrl-]")
taggy back: user.vim_normal_mode_key("ctrl-t")

###
# Text editing, copying, and manipulation
###

# indenting
indent [line] <number> through <number>$:
    user.vim_command_mode(":{number_1},{number_2}>\n")
unindent [line] <number> through <number>$:
    user.vim_command_mode(":{number_1},{number_2}>\n")

change remaining line: user.vim_normal_mode_key("C")
change line: user.vim_normal_mode("cc")
# XXX - technically these might be doable in command line mode, but life should
# become default talon and actions
# XXX - this might be suited for some automatic motion thing in vim.py
swap (bytes|char|characters):
    user.vim_normal_mode("x")
    user.vim_normal_mode("p")

# NOTE: this handles spaces
swap words:
    user.vim_normal_mode("de")
    user.vim_normal_mode('"_xw')
    user.vim_insert_mode(" ")
    user.vim_normal_mode("P")
swap lines:
    user.vim_normal_mode("dd")
    user.vim_normal_mode("p")
swap (paragraph|graph):
    user.vim_normal_mode("d}}")
    user.vim_normal_mode("p")
patch <user.unmodified_key>:
    user.vim_any_motion_mode("r{unmodified_key}")
patch (ship|upper|upper case) <user.letters>:
    user.vim_any_motion_mode_key("r")
    user.insert_formatted(letters, "ALL_CAPS")
# Delete the next in since of this specified character
shoot <user.unmodified_key>:
    user.vim_any_motion_mode("f{unmodified_key}")
    user.vim_any_motion_mode("x")

# deleting
(delete|trim) remaining [line]:
    user.vim_normal_mode_key("D")
# XXX - are temporarily disabled for speed testing
#delete line [at|number] <number>$:
#    user.vim_command_mode(":{number}d\n")
#delete (line|lines) [at|number] <number> through <number>$:
#    user.vim_command_mode(":{number_1},{number_2}d\n")
#delete (until|till) line <number>:
#    user.vim_normal_mode_np("m'")
#    insert(":{number}\n")
#    user.vim_set_visual_line_mode()
#    insert("''d")

# XXX - For stuff like this where we have multiple inputs in a motion mode but
# at the very end we want the preservation of the original mode, technically we
# could use a more complicated function that takes a variable list of
# arguments, and detects that this is happening doesn't bother keep switching
# the mode until the very last one
wipe line:
    # Purposely two calls for insert preservation
    user.vim_normal_mode("0")
    user.vim_normal_mode("d$")

# delete a line without clobbering the paste register
# XXX - this should become a general yank, delete, etc command prefix imo
forget line:
    user.vim_normal_mode("\"_dd")

# copying
# XXX - are temporarily disabled for speed testing
yank line <number>$:
    user.vim_command_mode_exterm(":{number}y\n")
#(copy|yank) <number_small> lines at line <number>$:
#    user.vim_command_mode_exterm(":{number}\n")
#    user.vim_normal_mode_exterm("y{number_small}y")
#(copy|yank) line (at|number) <number> through <number>:
#    user.vim_command_mode_exterm(":{number_1},{number_2}y\n")
#    user.vim_command_mode(":{number_1},{number_2}y\n")
#    user.vim_command_mode("p")
#
#(copy|yank) line relative up <number>:
#    user.vim_command_mode_exterm("{number}k")
#    user.vim_command_mode("yy")
#(copy|yank) <number_small> lines relative up <number>:
#    user.vim_command_mode_exterm("{number}k")
#    user.vim_command_mode("{number_small}yy")
(copy|yank) (above|last) <number_small> lines:
    user.vim_normal_mode_exterm("{number_small}k")
    user.vim_normal_mode_exterm("y{number_small}y")
    user.vim_normal_mode_exterm("{number_small}j")

# duplicating
# These are multi-line like this to perserve INSERT.
# XXX - are temporarily disabled for speed testing
#(duplicate|paste) line <number> on line <number>$:
#    user.vim_command_mode(":{number_1}y\n")
#    user.vim_command_mode(":{number_2}\n")
#    user.vim_command_mode("p")
#(duplicate|paste) lines <number> through <number>$:
#     user.vim_command_mode(":{number_1},{number_2}y\n")
#     user.vim_command_mode("p")
bring line <number>$:
    user.vim_command_mode(":{number}y\n")
    user.vim_normal_mode("p")
#(dup|duplicate) line: 
#    user.vim_normal_mode_np("yy")
#    user.vim_normal_mode_np("p")


paste below:
    user.vim_normal_mode_np("o")
    user.vim_normal_mode("p")

# start ending at end of file
file append:
    user.vim_normal_mode_np("Go")

push:
    user.vim_normal_mode_np("$a")
# NOTE - We need a separate key() call because some unmodified keys have
# special names, like backspace.
push <user.unmodified_key>:
    user.vim_normal_mode_np("$a")
    key('{unmodified_key}')

# paste to the end of a line
# XXX
push it:
    user.vim_normal_mode_np("A ")
    key(escape p)

# insert at the end of the current word
jammie:
    user.vim_normal_mode_np("ea")
jammie <user.unmodified_key>:
    user.vim_normal_mode_np("ea")
    key("{unmodified_key}")

chompie:
    user.vim_normal_mode_np("ex")

insert <user.text>:
    user.vim_insert_mode("{text}")

# helpful for fixing typos or bad lexicons that miss a character
(inject|crammie) <user.unmodified_key> [before]:
    user.vim_insert_mode_key("{unmodified_key}")
    # since there is no ctrl-o equiv coming from normal
    key(escape)

(inject|crammie) <user.unmodified_key> after:
    user.vim_normal_mode_key("a {unmodified_key}")
    # since we can't perserve mode with ctrl-o
    key(escape)

# XXX - look into how this works
filter line: "=="

[add] gap above:
    user.vim_command_mode(":pu! _\n")
    user.vim_command_mode(":'[+1\n")
[add] gap below:
    user.vim_command_mode(":pu _\n")
    user.vim_command_mode(":'[-1\n")

# Selects current line in visual mode and triggers a word swap
swap [word] on [this] line:
    key(V)
    insert(":")
    sleep(50ms)
    insert("s///g")
    key(left:3)

swap global:
    user.vim_command_mode(":%s///g")
    key(left:3)

global clear:
    user.vim_command_mode(":g //d")
    key(left:3)

global inverted clear:
    user.vim_command_mode(":v //d")
    key(left:3)

###
# Macros and registers
###
macro play <user.letter>: user.vim_any_motion_mode("@{letter}")
macro (again|repeat|replay): user.vim_any_motion_mode("@@")
macro (start|record) <user.letter>: user.vim_any_motion_mode("q{letter}")
macro (done|finish|stop): user.vim_any_motion_mode("q")

[copy] register <user.unmodified_key> [in] to [register] <user.unmodified_key>:
    user.vim_command_mode(":let@{unmodified_key_2}=@{unmodified_key_1}\n")

yank (into|to) [register] <user.unmodified_key>:
    user.vim_any_motion_mode('"{unmodified_key}y')
clear (into|to) [register] <user.unmodified_key>:
    user.vim_any_motion_mode('"{unmodified_key}d')

# XXX - this should allow counted yanking, into register should become an
# optional part of vim.py matching
# XXX - I can't get this to work
yank <user.vim_text_objects> (into|to) [register] <user.unmodified_key>:
    user.vim_any_motion_mode('"{unmodified_key}y{vim_text_objects}')
clear <user.vim_text_objects> (into|to) [register] <user.unmodified_key>:
    user.vim_any_motion_mode('"{unmodified_key}d{vim_text_objects}')

(register|registers|macros) list: user.vim_command_mode(":reg\n")
(register|macro) show <user.letter>: user.vim_command_mode(":reg {letter}\n")
(register|macro) (edit|modify) <user.letter>:
    user.vim_command_mode(":let @{letter}='")
    key(ctrl-r)
    key(ctrl-r)
    insert("{letter}")
    key(')

###
# Folding
###

# creation
fold (row|line): user.vim_normal_mode("zF")
# NOTE: see vim.py for zf usage

# deletion
fold delete: user.vim_normal_mode("zd")
fold delete nested: user.vim_normal_mode("zD")
fold delete all: user.vim_normal_mode("zE")


# navigation
fold open: user.vim_normal_mode("zo")
fold open nested: user.vim_normal_mode("zO")
fold close: user.vim_normal_mode("zc")
fold close nested: user.vim_normal_mode("zC")
fold open all: user.vim_normal_mode("zR")
fold open curse: user.vim_normal_mode("zv")
fold close all: user.vim_normal_mode("zM")
fold line <number> through <number>$: user.vim_normal_mode(":{number_1},{number_2}fo\n")


fold start: user.vim_normal_mode("[z")
fold end: user.vim_normal_mode("]z")
fold next: user.vim_normal_mode("zj")
fold last: user.vim_normal_mode("zk")

# misc
fold reset: user.vim_normal_mode("zn")
fold normal: user.vim_normal_mode("zN")

fold update: user.vim_normal_mode("zx")
fold undo: user.vim_normal_mode("zX")

# TODO: folddoo
# TODO: folddoc

###
# Spell check
#
# Recommend you `set spellfile` somewhere
###

spell add: user.vim_normal_mode('zg')
spell wrong: user.vim_normal_mode('zw')
spell undo add: user.vim_normal_mode('zug')
spell undo wrong: user.vim_normal_mode('zug')
spell (suggest|fix): user.vim_normal_mode('z=')
spell next: user.vim_normal_mode(']s')
spell last: user.vim_normal_mode('[s')


###
# Special Marks
###

(go|jump) [to] last edit: user.vim_normal_mode("`.")
(go|jump) [to] last insert: user.vim_normal_mode("`^")
# differences this puts you into insert mode
# TODO - change the way you say this?
(continue|continue last insert): user.vim_normal_mode("gi")
jump last curse: user.vim_normal_mode("``")
jump last line: user.vim_normal_mode("''")
(go|jump) [to] last change: user.vim_normal_mode("g;")
(go|jump) [to] next change: user.vim_normal_mode("g,")
# XXX - add jump to <id>


###
# QuickFix list
###
vim grep:
    user.vim_command_mode(":vimgrep // **")
    key(left:4)
vim real grep:
    user.vim_command_mode(":grep -r  *")
    key(left:2)
quick [fix] next: user.vim_command_mode(":cn\n")
quick [fix] (back|last|prev|previous): user.vim_command_mode(":cp\n")
quick [fix] (show|hide): user.vim_command_mode(":cw\n")
quick [fix] close: user.vim_command_mode(":ccl\n")
quick [fix] files:
    user.vim_command_mode(':cexpr system("fd -g \'*.py\' .")')
    key(left:3)
    # XXX - top?
quick [fix] bottom: user.vim_command_mode(":cbo\n")
quick [fix] do:
    user.vim_command_mode(":cdo | update")
    key(left:8)
quick [fix] swap:
    user.vim_command_mode(":cdo s///g| update")
    key(left:11)
set auto write all: user.vim_command_mode(":set autowriteall\n")


###
# Argument list
#
# TODO missing write and movement ex: :wnext
###
(arg|argument) do:
    user.vim_command_mode(":argdo | update")
    key(left:9)
    # XXX - using this `<command>` method doesn't seem to be working
(arg|argument) files:
    user.vim_command_mode(":arg `fd -g '\\*.py' .`")
    key(left:4)
(arg|argument) list show:
    user.vim_command_mode(":arg\n")
(arg|argument) add:
    user.vim_command_mode(":argadd ")
(arg|argument) next:
    user.vim_command_mode(":next\n")
(arg|argument) previous:
    user.vim_command_mode(":prev\n")
(arg|argument) first:
    user.vim_command_mode(":first\n")
(arg|argument) last:
    user.vim_command_mode(":last\n")

###
# Informational
###
man page this: user.vim_normal_mode("K")
file info: user.vim_normal_mode_key(ctrl-g)
# shows buffer number by pressing 2
file extra info:
    user.vim_normal_mode_key("2 ctrl-g")
vim help: user.vim_command_mode_exterm(":help ")
show ask e code:
    user.vim_normal_mode_key("g 8")
show last output:
    user.vim_normal_mode_key("g <")

display current line number: user.vim_normal_mode_key(ctrl-g)

###
# Searching
###

# XXX - is it possible to integrate these with vim_motions_with_character?
# ordinals work different for `t` for some reason, so we don't need to -1
till <user.ordinals> <user.unmodified_key>:
    user.vim_any_motion_mode("t{unmodified_key}{ordinals};")

till (reversed|previous) <user.ordinals> <user.unmodified_key>:
    user.vim_any_motion_mode("T{unmodified_key}{ordinals};")

find <user.ordinals> <user.unmodified_key>:
    user.vim_any_motion_mode("f{unmodified_key}{ordinals-1};")

find (reversed|previous) <user.ordinals> <user.unmodified_key>:
    user.vim_any_motion_mode("F{unmodified_key}{ordinals-1};")

###
# Visual Text Selection
###
make ascending: user.vim_normal_mode_key("g ctrl-a")
(paint|light|highlight) line: user.vim_visual_mode("V")
block (paint|light|highlight): user.vim_any_motion_mode_exterm_key("ctrl-v")

(paint|light|highlight) <user.vim_motions>:
    user.vim_visual_mode("{vim_motions}")
block (paint|light|highlight) <user.vim_motions>:
    user.vim_visual_block_mode("{vim_motions}")

(paint|light|highlight) lines <number> through <number>:
    user.vim_normal_mode_np("{number_1}G")
    user.vim_set_visual_mode()
    insert("{number_2}G")

block (paint|light|highlight) lines <number> through <number>:
    user.vim_normal_mode_np("{number_1}G")
    user.vim_set_visual_block_mode()
    insert("{number_2}G")

(paint|light|highlight) <number_small> lines:
    user.vim_set_visual_line_mode()
    insert("{number_small-1}j")

block (paint|light|highlight) <number_small> lines:
    user.vim_set_visual_block_mode()
    insert("{number_small-1}j")

(paint|light|highlight) <number_small> lines at line <number>:
    user.vim_normal_mode_np("{number}G")
    user.vim_set_visual_line_mode()
    insert("{number_small-1}j")

block (paint|light|highlight) <number_small> lines at line <number>:
    user.vim_normal_mode_np("{number}G")
    user.vim_set_visual_block_mode()
    insert("{number_small-1}j")

(paint|light|highlight) <number_small> above:
    user.vim_normal_mode_np("{number_small}k")
    user.vim_set_visual_line_mode()
    insert("{number_small-1}j")

block (paint|light|highlight) <number_small> above:
    user.vim_normal_mode_np("{number_small}k")
    user.vim_set_visual_block_mode()
    insert("{number_small-1}j")

(paint|light|highlight) (until|till) line <number>:
    user.vim_normal_mode_np("m'")
    insert(":{number}\n")
    user.vim_set_visual_line_mode()
    insert("''")

block (paint|light|highlight) (until|till) line <number>:
    user.vim_normal_mode_np("m'")
    insert(":{number}\n")
    user.vim_set_visual_block_mode()
    insert("''")

# Greedily highlight whatever is under the cursor. Doesn't work if on the first
# character of the entry, in which case you should say a normal motion like
# "light big end", etc
(paint|light) this:
    user.vim_normal_mode_np("B")
    user.vim_visual_mode("E")

###
# Visual Text Editing
###
prefix <user.vim_select_motion> with <user.unmodified_key>:
    user.vim_visual_mode("{vim_select_motion}")
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(50ms)
    insert("s/^/{unmodified_key}/g\n")

###
# Command execution
###
run python script:
    user.vim_normal_mode_np(":w\n")
    user.insert_cursor(":exec '!python3 [|]'")
run sandbox script:
    user.vim_normal_mode_np(":w\n")
    user.insert_cursor(":exec '!env/bin/python3 [|]'")

# Change how these get displayed in splits?
run make:
    user.vim_normal_mode_np(":w\n")
    insert(":!make\n")
run make all:
    user.vim_normal_mode_np(":w\n")
    insert(":!make all\n")

exec repeat:
    user.vim_normal_mode_np(":exec ")
    key(up)

script repeat:
    user.vim_normal_mode_np(":!")
    key(up)

# Run the current script view the command line
# XXX - These should only enable in python lang mode
invoke this:
    user.vim_command_mode(":!%\n")
run as python:
    user.vim_normal_mode_np(":w\n")
    insert(":exec '!python' shellescape(@%, 1)\n")
run as bash:
    user.vim_normal_mode_np(":w\n")
    insert(":exec '!bash' shellescape(@%, 1)\n")
run as sandbox:
    user.vim_normal_mode_np(":w\n")
    insert(":exec '!env/bin/python3' shellescape(@%, 1)\n")

###
# Convenience
###
trim white space: user.vim_normal_mode(":%s/\\s\\+$//e\n")
(remove all|normalize) tabs: user.vim_normal_mode(":%s/\\t/    /eg\n")
normalize spaces: user.vim_command_mode(":%s/\\S\\zs\\s\\+/ /g\n")
normalize new lines: user.vim_command_mode(":%s/\r//g\n")
(delete|trim) empty lines:
    insert(":")
    sleep(100ms)
    insert("g/^$/d\n")


# remove first byte from a line
pinch: user.vim_normal_mode("0x")
prefix <user.unmodified_key>: user.vim_normal_mode("I{unmodified_key}")
squish: user.vim_command_mode(":s/  / /g\n")
# XXX - this could be a generic talon thing
# XXX - this seems broken if we do it from insert mode
magnet:
    user.vim_normal_mode("f ")
    user.vim_normal_mode("x")
magnet back:
    user.vim_normal_mode("F ")
    user.vim_normal_mode("x")


show unsaved changes:
    user.vim_command_mode(":w !diff % -\n")

swap again:
    key(g &)

# XXX - should be switched to support any motion mode, but needs np
# which isn't supported yet
first <user.unmodified_key>:
    user.vim_normal_mode_np("^f{unmodified_key}")

    # XXX - should be switched to support any motion mode, but needs np
    # which isn't supported yet
last <user.unmodified_key>:
    user.vim_normal_mode_np("$F{unmodified_key}")

popup clear:
    user.vim_command_mode(":call popup_clear(1)")

yank funk: 
    user.vim_normal_mode("f(Byt(")
