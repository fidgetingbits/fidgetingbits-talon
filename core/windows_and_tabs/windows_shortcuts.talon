coder: user.switcher_focus_or_launch("code")
webby: user.switcher_focus_or_launch("firefox")
# Focus browser and then switch to tab with name
# slacker: user.switcher_focus("firefox", "slack)

# this should just be a function

# FIXME: This should use a dynamic list to inside of ~/.config/code-workspaces/
pop talon [<phrase>]$:
    user.vscode_open_workspace("fidgetingbits-talon (workspace)", phrase or "")

pop nix [<phrase>]$:
    user.vscode_open_workspace("nix-config (workspace)", phrase or "")

pop cursorless [<phrase>]$:
    user.vscode_open_workspace("fidgetingbits-cursorless (workspace)", phrase or "")

pop nix secrets:
    user.vscode_open_workspace("nix-secrets (workspace)")

pop neovim talon:
    user.vscode_open_workspace("neovim-talon (workspace)")

pop wiki:
    user.vscode_open_workspace("wiki (workspace)")
