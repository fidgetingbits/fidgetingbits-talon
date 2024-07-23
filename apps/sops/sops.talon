app: terminal
-
# FIXME: We could have a scope that actually tests whether or not the command is present, which fires in additional to
# being in the terminal. This is especially suited to nix

sops [<user.zsh_file_completion>]:
    insert("sops ")
    insert(zsh_file_completion or "")
