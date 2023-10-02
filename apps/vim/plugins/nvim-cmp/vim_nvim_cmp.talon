tag: user.vim_nvim_cmp
and tag: user.vim_insert_mode
-
# This is technically a nvim-cmp specific command
# they should probably also tie into something that uses pumvisible()
close: key('ctrl-e')
keep:
    # NOTE: This purposefully overlaps with copilot keep, so you would need to configure
    # it with a fall back function in nvim-cmp
    key('ctrl-j')
next: key('ctrl-n')
prev: key('ctrl-p')
(suggest | complete | pleat): key('ctrl-space')
