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
virtual (stop|shutdown): insert("sudo virsh shutdown ")
virtual (restart|reboot): insert("sudo virsh reboot ")

# Config
virtual dump config: insert("virsh -c qemu:///system net-dumpxml default")

# Disk management

virtual disk list: insert("sudo virsh domblklist ")

virtual disk resize <number>: user.insert_cursor("sudo qemu-img resize [|] +{number}G")

virtual snapshot create otto: insert("$ virsh snapshot-create ")
virtual snapshot list: insert("$ virsh snapshot-list ")
virtual snapshot create: user.insert_cursor("virsh snapshot-create-as [|] --name <name_here>")

# XXX - This doesn't actually work because we need to detect that we're running
# insideof a virsh console, so need to add support
# pop out of the virtual console
virtual pop: key(ctrl+])
