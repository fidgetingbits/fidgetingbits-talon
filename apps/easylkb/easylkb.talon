tag: user.easylkb
-

# TODO: add a version to make it easy to dictate the kernel versions by number
[easy] kernel set build version: "KERN_VER="
[easy] kernel show build version: "echo KERN_VER=$KERN_VER\n"

[easy] kernel build all: user.insert_between("./easylkb.py -k", "-a")
[easy] kernel auto build all: user.insert_between("./easylkb.py -k$KERN_VER -a\n")

# TODO: add a version to make it easy to dictate the kernel versions by number
[easy] kernel run: user.insert_between("./easylkb.py -k", "-r")
