hostname: onyx
-
settings():
    user.notify_use_notify_send = true
    user.terminal_app = "gnome-terminal"
    user.package_manager_default = "nix"
    ###
    # GUI
    ###
    imgui.scale = 2.5


tag(): user.gnome-shell
