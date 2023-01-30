tag: user.zsh
-
tag(): user.zsh_cd_gitroot
tag(): user.zsh_folder_completion

# XXX - should be generic shell command
# zsh commands
reload shell config: "source ~/.zshrc\n"

# XXX - This functionality is disabled for now
#^<user.zsh_completion>:
#    insert(user.zsh_completion)
zsh dump (completion|completions):
    user.zsh_dump_completions()
zsh file dump (completion|completions):
    user.zsh_file_dump_completions()
zsh folder dump (completion|completions):
    user.zsh_folder_dump_completions()
zsh (dump|get) pid:
    insert("{user.zsh_get_pid()}")
