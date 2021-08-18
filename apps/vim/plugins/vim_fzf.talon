tag: user.vim_fzf
-

# ripgrep through files under current directory
ripple: user.vim_command_mode_exterm(":Rg\n")
ripple clip: 
    user.vim_command_mode_exterm(":Rg\n")
    edit.paste()
# XXX - this should behave differently depending on if it's a selection in
# visual mode, etc
ripple this: 
    user.vim_command_mode_exterm("yiw") 
    user.vim_command_mode_exterm(":Rg\n")
    edit.paste()


fuzz buffer commits: user.vim_command_mode_exterm(":BCommit\n")

# Lines across current buffer
fuzz (buffer lines|here): user.vim_command_mode_exterm(":BLines\n")
lizzie: user.vim_command_mode_exterm(":BLines\n")

fuzz buffer tags: user.vim_command_mode_exterm(":BTags\n")

# Open buffers
buzzle: user.vim_command_mode_exterm(":Buffers\n")


fuzz code search: user.vim_command_mode_exterm(":Ag\n")
fuzz colors: user.vim_command_mode_exterm(":Colors\n")
fuzz command history: user.vim_command_mode_exterm(":History:\n")
fuzz commands: user.vim_command_mode_exterm(":Commands\n")
fuzz commits: user.vim_command_mode_exterm(":Commit\n")
fuzz file types: user.vim_command_mode_exterm(":Filetypes\n")

# Files under current directory

fizzle: user.vim_command_mode_exterm(":Files\n")

fuzz git files: user.vim_command_mode_exterm(":GFiles\n")
fuzz git status: user.vim_command_mode_exterm(":GFiles?\n")
fuzz help tags: user.vim_command_mode_exterm(":Helptags\n")
fuzz history: user.vim_command_mode_exterm(":History\n")

# Lines across all open buffers
fuzz lines: user.vim_command_mode_exterm(":Lines\n")
fuzz locate: user.vim_command_mode_exterm(":Locate ")
fuzz maps: user.vim_command_mode_exterm(":Maps\n")
fuzz marks: user.vim_command_mode_exterm(":Marks\n")
fuzz search history: user.vim_command_mode_exterm(":History/\n")
fuzz snippets: user.vim_command_mode_exterm(":Snippets\n")
fuzz tags: user.vim_command_mode_exterm(":Tags\n")
(fuzz windows|wizard): user.vim_command_mode_exterm(":Windows\n")
