os: linux
app: terminal
tag: user.make_commands
-

run make: "make -j`nproc`\n"
run make file: "make -f "
run make clean: "make clean\n"
