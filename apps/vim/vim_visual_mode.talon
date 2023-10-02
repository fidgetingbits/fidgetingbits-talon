tag: user.vim_visual_mode
-

# A more limited number of actions that differ from the ones that we can use in normal
# and insert mode
{user.vim_visual_actions}: key(vim_visual_actions)
# TODO: This needs to be turned into an actual action so that we can deal with a
# variable number
{user.vim_visual_counted_actions}: key(vim_visual_counted_actions)
swap (selected | highlighted):
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(50ms)
    insert("s///g")
    key(left)
    key(left)
    key(left)

sort selected:
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(100ms)
    insert("sort\n")

unique selected:
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(100ms)
    insert("sort u\n")

    # assumes visual mode
reswap (selected | highlighted):
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(50ms)
    key(up)

deleted selected empty lines:
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(50ms)
    insert("g/^$/d\\j")

delete from selected:
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(50ms)
    user.insert_between("g/", "/d\\j")

prefix with <user.unmodified_key>:
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(50ms)
    insert("s/^/{unmodified_key}/g\n")

# XXX - maybe make this work another modes
# copy with line numbers
(yank | copy) with [line] (numb | numbers):
    # NOTE - xclip struggles with we use @+ directly, we indirect through @n
    # this turns @n into a scratch register. XXX - we may want to document
    # this eventually
    user.vim_command_mode(":redir @n | silent! :'<,'>number | redir END | let @+=@n\n")

# XXX - we could add something with motions, so we search for something
# selected via motion
search that:
    insert("y/\\V")
    key(ctrl-r)
    insert("=escape(@\",'/\\')")
    key("enter:2")

(shift | indent) right: insert(">")
(shift | indent) left: insert("<")

(dup | duplicate) line:
    insert("Y")
    insert("p")

yank line: insert("Y")

push: user.vim_normal_mode_np("$a")

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

# Convert a number to hex
convert to hex: user.vim_command_mode(':%s/\\d\\+/\\=printf("0x%04x", submatch(0))')

# Subtract hex
# https://www.reddit.com/r/vim/comments/emtwgz/add_subtract_multiply_or_divide_a_value_to_each/
# Only works on the last number in a line
subtract that: insert(":s/\\d\\+$/\\=submatch(0)-")

subtract that clip:
    insert(":s/\\d\\+$/\\=submatch(0)-")
    edit.paste()

# this should only be enabled within python
sort by dick value: insert(":!sort -t ':' -k 2\n")

##
# treesitter
##
node grow: key("g r n")
node shrink: key("g r m")
node scope: key("g r c")

# These are from https://github.com/echasnovski/mini.nvim
move up: key("alt-k")
move down: key("alt-j")
move left: key("alt-h")
move right: key("alt-l")
