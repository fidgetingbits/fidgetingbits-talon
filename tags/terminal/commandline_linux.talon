# NOTE: these are command line commands, not shell-specific bindings
# see shell.talon for shell-specific keybindings
os: linux
and tag: terminal
-

tag(): user.service_manager
tag(): user.timer_manager
tag(): user.systemd
tag(): user.pulse_audio
tag(): user.iptables
tag(): user.nftables
tag(): user.coredumpctl
tag(): user.yay
#tag(): user.aptb
tag(): user.nmcli
tag(): user.package_manager

file hash: "sha256sum "
file hash five twelve: "sha512sum "
file hash M D five: "md5sum "
file hash shaw one: "sha1sum "
file hash blake two: "b2sum "
file hash <user.zsh_file_completion>: "sha256sum {zsh_file_completion}"

file tree permission: "tree -pufid "

trash list: "trash-list\n"
trash restore: "trash-restore "
trash empty: "trash-empty "

net (interfaces | I P | address) [show]: "ip addr\n"
net flush: "ip addr flush dev "
net show: "ip addr show "
net [address] (set | add [ip]): "ip addr add "
net [address] (remove | delete) [ip]: "ip addr del "

net (route | routes) [list]: "ip route\n"
net (route | routes) six [list]: "ip -6 route\n"
net route add: user.insert_cursor("ip route add [|] dev ")
net route add tunnel: user.insert_cursor("ip route add [|] dev tun0")
net route (remove | delete | drop): "ip route del "
# XXX - We should switch these to use ss
net stat all: "ss --sctp -anutp\n"
net [stat] (listen | listening) unix: "ss --sctp -anutp\n"
net [stat] (listen | listening) T C P: "ss --tcp -nlp\n"
net [stat] (listen | listening) U D P: "ss --udp -nlp\n"
net [stat] (listen | listening) S C T P: "ss --sctp -nlp\n"
net [stat] (listen | listening): "ss -lnpt\n"
net [stat] (listen | listening) all: "ss --sctp -lnput\n"

net [dev | device] up: user.insert_cursor("ip link set dev [|] up")
net [dev | device] down: user.insert_cursor("ip link set dev [|] down")

file trace: "strace -f "
file trace log: "strace -o trace.log -f "

(disk | drive) key dump: "sudo cryptsetup luksDump /dev/"
(disk | drive) key add: "sudo cryptsetup luksAddKey --key-slot "

file change attributes: "chattr "
(file | folder) make immutable: "chattr +i "
(file | folder) drop immutable: "chattr +i "
file make append only: "chattr +a "
file drop append only: "chattr -a "

# kernel modules
module list: "lsmod\n"
module search: "lsmod |rg -i"
module probe: "modprobe "
module remove: "rmmod "

net man log: "journalctl -u NetworkManager --no-pager --lines 100\n"

process tree: "pstree\n"

# hardware
system [list] memory: "lshw -short -C memory"
system [list] processor: "lscpu\n"
system [list] (P C I | pee) bus: "lspci\n"
system [list] (yew bus | U S B): "lsusb\n"
system release: "cat /etc/lsb-release\n"

###
# images
###
file image: "feh "
file image meta: "identify -verbose "
wallpaper set: "feh --bg-scale "
wallpaper set latest:
    "feh --bg-scale $(find ~/images/wallpaper/ -name $(exa --sort changed --no-icons ~/images/wallpaper/ | tail -n1))\n"

###
# Screen recording
###
screen record: insert("recordmydesktop")

###
# X11 stuff
###
screen dimensions: "xdpyinfo | grep dimensions\n"
screen resolution: "xdpyinfo | awk '/dimensions/{{print $2}}'\n"

###
# Arch Linux
# https://wiki.archlinux.org/index.php/Arch_Build_System#Retrieve_PKGBUILD_source_using_Git
###
arch source check out: "asp checkout "
arch source export: "asp export "

###
# Kernel Tracing
###
kernel trace on: "echo 1 > /sys/kernel/tracing/tracing_on\n"
kernel trace off: "echo 0 > /sys/kernel/tracing/tracing_on\n"
kernel trace show: "cat /sys/kernel/tracing/trace\n"
kernel trace functions: "echo function > /sys/kernel/tracing/current_tracer\n"
# XXX -we may want this to shut off tracing first?

###
# Namespaces
###

capability list: "capsh --print\n"

(unshare | namespace) root: "unshare -U -r\n"
(unshare | namespace) net: "unshare -n\n"

###
# Kernel
###
kernel generate tags: "python scripts/clang-tools/gen_compile_commands.py"
run pa hole: "pahole "

run B P F trace:
    user.insert_cursor("sudo BPFTRACE_PERF_RB_PAGES=256 bpftrace [|].bt | tee trace.log")

clipboard as Q R code: "xclip -o -s c | qrencode -o - | feh --force-aliasing -ZF -"

###
# udev
###

you dev admin: "udevadm "
you dev reload: "sudo udevadm control --reload-rules && sudo udevadm trigger"

###
# keyctl
###

key cuttle version: "keyctl --version\n"
key cuttle list user: "keyctl list @u\n"
key cuttle list process: "keyctl list @p\n"
key cuttle list session: "keyctl list @s\n"
key cuttle clear session: "keyctl clear @s\n"

###
# dpkg
###
deb install: "dpkg -i"

###
# Monitors
###
display list: "polybar --list-monitors\n"
camera list: "v4l2-ctl --list-devices\n"

cron tab list user: "crontab -l -u "

volume scan: "lvscan\n"

###
# cpu debugging
###
show cpu frequencies: "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq\n"
show cpu governors: "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor\n"
show cpu max frequencies: "cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_max_freq\n"
show cpu min frequencies: "cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_min_freq\n"
set all governors:
    "echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor\n"

loop setup help: "losetup --help\n"
loop setup attach: "losetup -f "
loop setup part attach: "losetup -fP "
loop setup list: "losetup -a\n"
loop setup detach: "losetup -d "

###
# ELF
###
file patch interpreter: "patchelf --set-interpreter /usr/lib64/ld-linux-x86-64.so.2 "

# TODO: Need to move to host specific interface names
net add name server:
    user.insert_between("echo 'nameserver ", "' | sudo /sbin/resolvconf -a net1")
net (delete | deli) name server:
    user.insert_between("echo 'nameserver ", "' | sudo /sbin/resolvconf -d net1")
net resolve config: "/sbin/resolvconf "
net resolve config help: "/sbin/resolvconf -h\n"
net restart: "sudo systemctl restart NetworkManager\n"
# systemd-resolved specific
[net] (name server | D N S) list: "resolvectl status\n"
