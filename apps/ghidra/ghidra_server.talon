os: linux
tag: terminal
and tag: user.ghidra_server
-

# ghidraSvr
(ghidra|hydra) server status: "server/ghidraSvr status\n"
(ghidra|hydra) server stop: "server/ghidraSvr stop\n"
(ghidra|hydra) server start: "server/ghidraSvr start\n"
(ghidra|hydra) server install: "server/ghidraSvr install\n"
(ghidra|hydra) server restart: "server/ghidraSvr restart\n"
(ghidra|hydra) server: "server/ghidraSvr "

# svrAdmin
(ghidra|hydra) admin: "server/svrAdmin "
(ghidra|hydra) list (repo|repositories): "server/svrAdmin -list\n"
(ghidra|hydra) list user access: "server/svrAdmin -list -users\n"
(ghidra|hydra) list users: "server/svrAdmin -users\n"
(ghidra|hydra) add user: "server/svrAdmin -add "
(ghidra|hydra) remove user: "server/svrAdmin -remove "
(ghidra|hydra) reset password: "server/svrAdmin -reset "

# misc
(ghidra|hydra) edit config: "vi server/server.conf\n"
# NOTE: you will have to edit this path to match your repo directory
(ghidra|hydra) edit log: "vi ../repo/server.log\n"
