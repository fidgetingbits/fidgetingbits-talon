app: nm-applet
-

# Deal with the NetworkManager 2FA pop-up when we need to enter/confirm 2FA
# code
net man two factor:
    key(tab)
    key(space)
    key(tab:3)
    key(right)
    key(backspace:6)
    user.system_command("i3-msg 'focus floating'")
    # can now speak the 2FA code

reveal:
    key(tab)
    key(space)
    key(tab:3)
    key(right)
