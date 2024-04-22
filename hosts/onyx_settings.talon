hostname: onyx
-
settings():
    user.notify_use_notify_send = true
    # gnome-terminal
    user.terminal_app = "terminal"
    user.package_manager_default = "nix"

settings():
    ###
    # GUI
    ###
    imgui.scale = 2.5


tag(): user.gnome-shell
