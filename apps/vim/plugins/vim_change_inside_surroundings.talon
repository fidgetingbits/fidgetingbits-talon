tag: user.vim_change_inside_surroundings
-

# XXX - i'm using 'this' right now to avoid conflicting with the support in vim.py
(change inside this | shimmer):
    user.vim_command_mode(':exe ":ChangeInsideSurrounding"\n')
(change around this | shammer):
    user.vim_command_mode(':exe ":ChangeAroundSurrounding"\n')
