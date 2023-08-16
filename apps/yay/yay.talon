os: linux
tag: user.packager_yay
-
package fetch build: "yay --getpkgbuild "

make local package: "makepkg -si\n"