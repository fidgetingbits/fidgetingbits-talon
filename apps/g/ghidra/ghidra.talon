os: linux
app: ghidra
-

new project: key(ctrl-n)
open project: key(ctrl-o)
close project: key(ctrl-w)
save project: key(ctrl-s)
exit ghidra: key(ctrl-q)

# automation

ghidra test: user.run_rpc_command("test", "foo")
