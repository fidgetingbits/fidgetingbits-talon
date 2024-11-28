tag: terminal
and tag: user.gnome-shell
-

gnome extensions help: "gnome-extensions --help\n"
gnome extensions list: "gnome-extensions list\n"
# FIXME: add a dynamic list
gnome extensions info {user.gnome_extensions}:
    insert("gnome-extensions info {gnome_extensions}\n")

