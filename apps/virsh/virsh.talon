os: linux
tag: user.virsh
-

# See https://libvirt.org/manpages/virsh.html

# Listing
virtual list running: insert("sudo virsh list\n")
virtual list all: insert("sudo virsh list --all\n")
virtual list inactive: insert("sudo virsh list --inactive\n")

# Network
virtual net [work] list: insert("sudo virsh net-list --all\n")
virtual net [work] leases: insert("sudo virsh net-dhcp-leases default\n")

# Running
virtual run console: insert("sudo virsh start --console ")
virtual start: insert("sudo virsh start ")
virtual (stop | shutdown): insert("sudo virsh shutdown ")
virtual (restart | reboot): insert("sudo virsh reboot ")
virtual destroy: insert("sudo virsh destroy ")

# Config
virtual edit config: "sudo virsh edit "
virtual dump network config:
    insert("virsh -c qemu:///system net-dumpxml default")

# VM management
virtual rename: "sudo virsh domrename old new"
virtual remove: "sudo virsh undefine "

# Disk management
virtual disk list: insert("sudo virsh domblklist ")
virtual disk resize <number>:
    user.insert_cursor("sudo qemu-img resize [|] +{number}G")

# Snapshots
virtual snapshot create otto: insert("sudo virsh snapshot-create ")
virtual snapshot list: insert("sudo virsh snapshot-list ")
virtual snapshot create:
    user.insert_cursor("sudo virsh snapshot-create-as [|] --name <name_here>")

# virt-clone

virtual clone: "sudo virt-clone --original oldname --auto-clone --name newname"
