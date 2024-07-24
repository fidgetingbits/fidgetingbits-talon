
-
# There's no identifier for the pop up on gnome, so unfortunately these have to be completely global atm

# Deal with the NetworkManager 2FA pop-up when we need to enter/confirm 2FA
# code
net man two factor:
    key(ctrl-shift-f10)
    sleep(200ms)
    key(down)
    key(enter)
    key(backspace:6)

net man reveal:
    key(ctrl-shift-f10)
    sleep(200ms)
    key(enter)
