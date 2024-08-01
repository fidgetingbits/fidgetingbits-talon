coder: user.switcher_focus_or_launch("code")
webby: user.switcher_focus_or_launch("firefox")
# Focus browser and then switch to tab with name
# slacker: user.switcher_focus("firefox", "slack)

# this should use a function that adds workspace?

# FIXME: This should use a dynamic list to inside of ~/.config/code-workspaces/
pop talon$:
    user.vscode_open_workspace("fidgetingbits-talon (workspace)")

pop nix [config] $:
    user.vscode_open_workspace("nix-config (workspace)")

pop cursorless $:
    user.vscode_open_workspace("fidgetingbits-cursorless (workspace)")

pop nix secrets:
    user.vscode_open_workspace("nix-secrets (workspace)")

pop nix vim [flake]:
    user.vscode_open_workspace("nixvim-flake (workspace)")

pop neovim talon:
    user.vscode_open_workspace("neovim-talon (workspace)")

pop wiki:
    user.vscode_open_workspace("wiki (workspace)")
