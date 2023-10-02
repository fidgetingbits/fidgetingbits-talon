# See https://github.com/vimwiki/vimwiki/
tag: user.vim_wiki
# In general calls need to use something like this: `:execute "normal
# \<Plug>NiceCenterCursor"`, since the wiki relies on `<leader>`. You can see
# the mappings with `:nmap` or similar.
# XXX - consider switching to `key` instead of wiki
-

###
# Global Vim Wiki Commands - Callable even when outside a wiki
###

# Main wiki commands
go wiki: user.vim_command_mode_exterm(':execute "normal \\<Plug>VimwikiIndex"\n')
go work wiki: user.vim_normal_mode(':VimwikiIndex 2"\n')

go wiki tabbed:
    user.vim_command_mode_exterm(':execute "normal \\<Plug>VimwikiTabIndex"\n')
go wiki <number_small>:
    user.vim_command_mode_exterm(':execute "normal <C-U>call vimwiki#diary#make_note({number_small})"\n')
list wikis: user.vim_command_mode_exterm(':execute "normal \\<Plug>VimwikiUISelect"\n')
# XXX
# wiki rename <number_small>:
#     user.vim_command_mode_exterm(':execute "normal <C-U>call vimwiki#diary#make_note({number_small})"\n')
# wiki delete <number_small>:
#     user.vim_command_mode_exterm(':execute "normal <C-U>call vimwiki#diary#make_note({number_small})"\n')

# Diary Commands
go diary: user.vim_command_mode_exterm(':execute "normal \\<Plug>VimwikiDiaryIndex"\n')
go work diary: user.vim_normal_mode(":VimwikiDiaryIndex 2\n")
diary new:
    user.vim_command_mode_exterm(':execute "normal \\<Plug>VimwikiMakeDiaryNote"\n')
diary new tab:
    user.vim_command_mode_exterm(':execute "normal \\<Plug>VimwikiTabMakeDiaryNote"\n')
diary last:
    user.vim_command_mode_exterm(':execute "normal \\<Plug>VimwikiMakeYesterdayDiaryNote"\n')
diary next:
    user.vim_command_mode_exterm(':execute "normal \\<Plug>VimwikiMakeTomorrowDiaryNote"\n')

wiki help: user.vim_command_mode_exterm(":help vimwiki\n")
wiki help commands: user.vim_command_mode_exterm(":help vimwiki-commands\n")
