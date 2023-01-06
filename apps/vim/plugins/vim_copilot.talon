tag: user.vim_copilot
-

# XXX - I don't know why this ends up not actually accepting, so just falling
# back to use tab for now
#pilot: user.vim_command_mode(":call copilot#Accept(\"\")\n")
([co] pilot|keep): key("ctrl-j")
copilot disable: user.vim_command_mode(":Copilot disable\n")
copilot enable: user.vim_command_mode(":Copilot enable\n")
copilot status: user.vim_command_mode(":Copilot status\n")
copilot panel: user.vim_command_mode(":Copilot panel\n")
copilot version: user.vim_command_mode(":Copilot version\n")
copilot suggest:
    user.vim_command_mode(':execute "normal \\<Plug>(copilot-suggest)"\n')
copilot dismiss:
    user.vim_command_mode(':execute "normal \\<Plug>(copilot-dismiss)"\n')
copilot next:
    user.vim_command_mode(':execute "normal \\<Plug>(copilot-next)"\n')
copilot (last | previous | prev):
    user.vim_command_mode(':execute "normal \\<Plug>(copilot-previous)"\n')
# purposefully don't have new lines at the end of these commands
copilot setup: user.vim_command_mode(":Copilot setup")
copilot sign out: user.vim_command_mode(":Copilot signout")

