tag: user.zsh
-
tag(): user.zsh_cd_gitroot
tag(): user.zsh_folder_completion
tag(): user.zsh_zhooks
# Only enable terminal commands if we're actually inside a shell app (zsh)
# tag(): terminal

# XXX - should be generic shell command
# zsh commands
(source|reload) (zsh|shell) config: "source ~/.config/zsh/.zshrc\n"

# XXX - This functionality is disabled for now
#^<user.zsh_completion>:
#    insert(user.zsh_completion)
zsh dump (completion | completions): user.zsh_dump_completions()
zsh dump file (completion | completions): user.zsh_dump_file_completions()
zsh dump folder (completion | completions): user.zsh_dump_folder_completions()
zsh (dump | get) pid: insert("{user.zsh_get_pid()}")
zsh (update|refresh) key map: user.zle_update_keymap()

(key map show|bind key list): "bindkey\n"
key map find: "bindkey | grep "
key map show emacs: "bindkey -M emacs\n"
key map show vim: "bindkey -M vicmd\n"

# These depend on custom zsh functions (extraInit.zsh in nix-config), so don't put in commandline.talon
# These are fzf-based commands.
# fuzzy directory deep
pivot in: "fdd\n"
# fuzzy directory shallow
pivot shallow: "fds\n"
# fuzzy directory reverse
pivot out: "fdr\n"
