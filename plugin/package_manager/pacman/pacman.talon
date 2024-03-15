tag: user.packager_pacman
-
pacman search <user.text>: "pacman -sS {text}"
pacman install <user.text>: "pacman -S {text}"
pacman make package: "makepkg -si\n"
