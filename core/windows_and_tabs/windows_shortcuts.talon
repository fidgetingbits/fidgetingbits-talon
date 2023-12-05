coder: user.switcher_focus("code")
webby: user.switcher_focus("firefox")
# Focus browser and then switch to tab with name
# slacker: user.switcher_focus("firefox", "slack)

# this should just be a function
tweaker [<phrase>]$:
    user.vscode_open_workspace("fidgetingbits-talon (workspace)", phrase or "")

hail nix [<phrase>]$:
    user.vscode_open_workspace("nix-config (workspace)", phrase or "")
