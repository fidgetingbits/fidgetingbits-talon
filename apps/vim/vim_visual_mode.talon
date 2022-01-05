tag: user.vim_visual_mode
-

swap (selected|highlighted):
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
reswap (selected|highlighted):
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(50ms)
    key(up)

deleted selected empty lines:
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(50ms)
    insert("g/^$/d\\j")

prefix with <user.unmodified_key>:
    insert(":")
    # leave time for vim to populate '<,'>
    sleep(50ms)
    insert("s/^/{unmodified_key}/g\n")

    # XXX - maybe make this work another modes
yank with numb:
    # NOTE - xclip struggles with we use @+ directly, we indirect through @n
    # this turns @n into a scratch register. XXX - we may want to document
    # this eventually
    user.vim_command_mode_exterm(":redir @n | silent! :'<,'>number | redir END | let @+=@n\n")

# XXX - we could add something with motions, so we search for something
# selected via motion
search that:
    insert("y/\\V")
    key(ctrl-r)
    insert("=escape(@\",'/\\')")
    key("enter:2")


(shift|indent) right: insert(">")
(shift|indent) left: insert("<")


(dup|duplicate) line: 
    insert("Y")
    insert("p")
