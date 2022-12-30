tag: user.vboxmanage
-

V box help: "vboxmanage\n"
V box version: "vboxmanage -V\n"
V box list: "vboxmanage list vms\n"

# modifyvm
V box modify: "vboxmanage modifyvm "
V box modify help: "vboxmanage modifyvm\n"
V box modify nat proxy on: user.insert_between("vboxmanage modifyvm ", " --natdnsproxy1 on")

# natnetwork
V box nat network help: "vboxmanage natnetwork\n"
V box nat network list: "vboxmanage natnetwork list\n"
