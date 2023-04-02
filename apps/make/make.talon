os: linux
tag: terminal
and tag: user.make_commands
-

run make: "make -j`nproc`\n"
run make file: "make -f "
run make clean: "make clean\n"
