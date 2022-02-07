# NOTE: these are command line commands, not shell-specific bindings
# see shell.talon for shell-specific keybindings
os: linux
mode: user.terminal
mode: command
and tag: terminal
-

###
# Shell-specific
#
# XXX - this should move to zsh
###
# unset this if you use `bindkey -v`
tag(): user.readline

###
# Packages
#
# These tags correspond to talon grammars you want to enable while you're
# running some terminal emulator on your system. See the associated talon
# files for information and links to what tools they are associated with.
###

#tag(): user.buku
tag(): user.yay
#tag(): user.apt
#tag(): user.ghidra_server
#tag(): user.nmcli
#tag(): user.taskwarrior
#tag(): user.timewarrior
tag(): user.make
#tag(): user.tmux
tag(): user.git
tag(): user.docker
tag(): user.service_manager
tag(): user.package_manager
tag(): user.timer_manager
tag(): user.systemd
tag(): user.pulse_audio
tag(): user.virsh
tag(): user.iptables
#tag(): user.npm
#tag(): user.meson
#tag(): user.kubectl


# Shell commands

run last [command]:
    key(up)
    key(enter)
run last script:
    insert("./")
    key(up)
    key(enter)
rerun <user.text>:
    key(ctrl-r)
    insert(text)
rerun list:
    key(ctrl-r)
rerun last command:
    key(! ! enter enter)
# XXX - it would be good to have overrides for words that are harder to say,
# like ssh, ex: see following tunnel word
rerun last <user.word>:
    key(!)
    insert(word)
    key(enter)
rerun last tunnel:
    key(!)
    insert("ssh\n")
    key(enter)

kill all:
    key(ctrl-c)

file list: "ls "
file bare list: "ls --no-icons "
file (list here|lisa): "ls -l\n"
file bare (list here|lisa): "ls -l --no-icons\n"
file size: "ls -lh "
file list long: "ls -al "
file (list long here|lily): "ls -al\n"
file list latest: "exa --sort latest --no-icons | tail -n1\n"
file list folders: "ls -d */\n"
file strings: "strings "
file (tail|follow): "tail -f "

# find command
file find all links: "find . -maxdepth 1 -type l  -ls\n"
file find all folders: "find . -maxdepth 1 -type d  -ls\n"
file fine all files: "find . -maxdepth 1 -type f  -ls\n"

# TODO - revisit the grammar for $() commands
call file latest: "$(exa --sort latest --no-icons | tail -n1)\n"

# TODO - somehow make this scriptable to print anything
file edit latest: "edit $(exa --sort latest --no-icons | tail -n1)\n"
file latest: "$(exa --sort latest --no-icons | tail -n1)"
file link: "ln -s "
file link force: "ln -sf "
file hard link: "ln "
file broken links:
    insert("find . -type l -exec sh -c 'file -b \"$1\" | grep -q ^broken' sh /{} \\; -print")
file find excluding with depth:
    user.insert_cursor("find . -mindepth 2 -maxdepth 2 -type d '!' -exec sh -c 'ls -1 \"{}\"|egrep -i -q \"^*.[|]$\"' ';' -print")
file find excluding:
    user.insert_cursor("find . -type d '!' -exec sh -c 'ls -1 \"{}\"|egrep -i -q \"^*.[|]$\"' ';' -print")
file move: "mv "
file open: "vim "
file touch: "touch "
file copy: "cp "
file deep copy: "cp -R "
file type: "file "
file show <user.text>: "cat {text}"
file show: "cat "
file edit: insert("edit ")
file edit here: insert("edit .\n")
file remove: "rm -I "
file safe remove all: "rm -i -- *"
file real remove: "/bin/rm -I "
file disk image copy: user.insert_cursor("dd bs=4M if=[|] of=/dev/sdX conv=fsync oflag=direct status=progress")
(file|folder) deep remove: "rm -rIf "
(file|folder) real deep remove: "/bin/rm -rIf "
file diff: "diff "
# find
file find: 
    user.insert_cursor("find . -name \"[|]\" 2>/dev/null")
# case insensitive fuzzy find
file fuzzy [find]:
    user.insert_cursor("find . -iname \"*[|]*\" 2>/dev/null")
file fuzzy [find] today:
    user.insert_cursor("find . -mtime -1 -name \"*[|]*\" 2>/dev/null")

file hash: "sha256sum "
file check sec: "checksec --file="
file locate: "locate "
file [full] path: "readlink -f "

file tree permission: "tree -pufid "


file edit read me: insert("edit README.md\n")
file edit make file: insert("edit Makefile\n")
file [disk] usage all: "du -sh *\n"
#file [disk] usage: "du -sh "

trash list: "trash-list\n"
trash restore: "trash-restore "
trash empty: "trash-empty "
file watch latest: "vlc $(exa --sort latest --no-icons | tail -n1)"

echo param <user.text>: 
    insert("echo ${")
    snake = user.formatted_text(text, "snake")
    upper = user.formatted_text(snake, "upper")
    insert(upper)
    insert("}")

# directory and files
pivot: "cd "
pivot clip:
    insert("cd ")
    edit.paste()
    key(enter)
pivot <user.paths>:
    edit.paste("cd {paths}\n")
    insert("ls\n")
# pivot up doesn't work with talon
pivot back: "cd ../\n"
pivot <number_small> back: 
    insert("cd ")
    insert(user.path_traverse(number_small))
    key(enter)
pivot home: "cd\n"
pivot next:
    insert("cd ")
    key(tab)
    sleep(100ms)
    key(enter)
    insert("ls\n")

pivot (last|flip): "cd -\n"
pivot latest: "cd $(exa --sort latest --no-icons | tail -n1)\n"


folder remove: "rmdir "
folder (create|new): "mkdir -p  "

# tree
file tree: "tree -f -L 2\n"
file tree more: "tree -f -L "
file tree long: "tree -f -L 2 -p\n"
file tree all: "tree -f -L 2 -a\n"
file tree folders: "tree -f -L 2 -d\n"
file tree depth <number_small>: "tree -f -L {number_small}\n"

folder pop: "popd\n"
# pwd | tr -d \\n\\r | xclip -sel clipboard
folder yank path: "pwd | tr -d \\\\n\\\\r | xclip -sel clipboard\n"

# permissions
file [change] mode: "chmod "
file make executable: "chmod +x "
file [change] ownership: "chown "
file [change] deep ownership: "chown -R $UID:$GID "

# file viewing
file less: "less "
now less [that]:
    edit.up()
    insert("| less\n")

clear [screen|page]: "clear\n"

# piping
pipe tea: "| tee "

# grepping

file rip: "rg -i "
file rip around: "rg -B2 -A2 -i "
file rip (exact|precise): "rg "
now rip:
    edit.up()
    insert("| rg -i ")

# even though rip is arguably better, we still want grep for remote terminals,
# etc
file grep: "grep -i "
file grep around: "grep -B2 -A2 -i "
now grep:
    edit.up()
    insert("| grep -i ")

# networking
net (interfaces|I P|address): "ip addr\n"
net (route|routes): "ip route\n"
net route add: user.insert_cursor("ip route add [|] dev ")
net route add tunnel: user.insert_cursor("ip route add [|] dev tun0")
net route (remove|delete|drop): "ip route del"
# XXX - We should switch these to use ss
net stat all: "netstat --sctp -anutp\n"
net [stat] (listen|listening) unix: "netstat --sctp -anutp\n"
net [stat] (listen|listening) T C P: "netstat --tcp -nlp\n"
net [stat] (listen|listening) U D P: "netstat --udp -nlp\n"
net [stat] (listen|listening) S C T P: "netstat --sctp -nlp\n"
net [stat] (listen|listening): "netstat -lnpt\n"
net [stat] (listen|listening) all: "netstat --sctp -lnput\n"
net trace: "traceroute "
net trace clip: 
    insert("traceroute")
    edit.paste()
    key(enter)
net ping: "ping "
net ping clip: 
    insert("ping")
    edit.paste()
    key(enter)
net cat: "nc -vv "
net connect <user.domains>: "nc -vv {domains} "
net cat listener: "nc -v -l -p "
net my I P: "dig +short myip.opendns.com @resolver1.opendns.com\n"
net port <user.ports>: "{ports}"
net dump: "tcpdump "

net bridge (list|show): "brctl show\n"


show hosts file: "cat /etc/hosts\n"
edit hosts file: "sudoedit /etc/hosts\n"
net (remote desktop|R D P): 
    user.insert_cursor("xfreerdp /timeout:90000 /size:1280x800 /v:[|] /u: /p:")

(generate see tags|tags generate): "ctags --recurse --exclude=.git --exclude=.pc *"
generate see scope database:
    insert('find . -name "*.c"')
    insert(' -o -name "*.cpp"')
    insert(' -o -name "*.h"')
    insert(' -o -name "*.hpp"')
    insert(' -o -name "*.py"')
    insert(' -o -name "*.s"')
    insert(' -o -name "*.asm"')
    insert('> cscope.files\n')
    insert("cscope -q -R -b -i cscope.files\n")

file head: "head "
file head <number_small>: "head -n {number_small} "
folder show: "pwd\n"

file trace: "strace -f "
file trace log: "strace -o trace.log -f "

lazy edit:
    insert("edit ")
    insert("$(find . -not -path '*/\\.git/*' -name \"**\")")
    key("left")
    key("left")
    key("left")

lazy edit <user.text>:
    insert("edit ")
    insert("$(find . -not -path '*/\\.git/*' -name \"*{text}*\")\n")

find <user.text> inside (python|pie) files:
    insert('$(find . -name \"*.py\") | xargs rg -i "{text}"\n')

find <user.text> inside (python|pie) files less:
    insert('$(find . -name \"*.py\") | xargs rg -i "{text}\" | less\n')

man page: "man "
so do: "sudo "
so do that: 
    edit.line_start()
    insert("sudo ")
    key(enter)
so do edit: "sudoedit "
d message: "dmesg"

# disk management
# NOTE - talon doesn't like the word disk with on MD431-II
(disk|drive) usage: "df -h\n"
(disk|drive) list: "lsblk -l\n"
(disk|drive) file systems: "lsblk -f\n"
(disk|drive) mounted: "mount\n"
(disk|drive) mount: "mount "
(disk|drive) unmount: "umount "
(disk|drive) key dump: "sudo cryptsetup luksDump /dev/"
(disk|drive) key add: "sudo cryptsetup luksAddKey --key-slot "
(disk|drive) F stab: "cat /etc/fstab\n"

# system configuration
sis cuddle: "sysctl "
sis cuddle set: "sysctl -w "

# extraction
file tar [ball] create: "tar -cvJf"
file [tar] extract: "tar -xvaf "
# https://github.com/facebook/zstd
file extract Z S T: "tar --use-compress-program=unzstd -xvf "
file unzip: "unzip "
file B unzip: "bunzip2 "
file seven extract: "7z x "
file seven list: "7z l "
tar ball list: "tar -tf "
(un zip|extract zip): "unzip "

# kernel modules
module list: "lsmod\n"
module search: "lsmod |rg -i"
module probe: "modprobe "
module remove: "rmmod "

run curl: "curl "
run double you get: "wget "
download: "wget "
download clip:
    insert("wget ")
    edit.paste()
    key(enter)

# because talent doesn't seem to like me saying ./
run script: "./"
run again:
    insert("./")
    key(up enter)
run vim: "vim "
run make: "make\n"
run see make: "cmake "
run configure make: "./configure && make\n"

sub command:
    insert("$()")
    key(left)

parameter:
    insert("${}")
    edit.left()


# bash convenience stuff
history show: "history\n"
extra that: "| xargs "

net man log: "journalctl -u NetworkManager --no-pager --lines 100\n"

core dump list: "coredumpctl\n"
core dump info: "coredumpctl info\n"
core dump dump: "coredumpctl dump\n"
core dump debug: "coredumpctl debug\n"

# ssh
# XXX - make texts actually query a series of names from the %h config
#(secure shell|tunnel) [<user.text>]: 
#    insert("ssh ")
#    insert(text or "")
tunnel last:
    key(ctrl-r)
    insert("ssh ")
    key(enter)
    key(enter)

secure shall key gen: "ssh-keygen -t ed25519\n"
secure copy [<user.text>]:
    insert("scp -r ")
    insert(text or "")
show authorized keys: "vi ~/.ssh/authorized_keys\n"
show pub keys: "cat ~/.ssh/*.pub\n"
edit authorized keys: "vi ~/.ssh/authorized_keys\n"
go secure shell config: "cd ~/.ssh\n"
# talon suddenly loves the word termini
#tunnel (terminate|termini):
tunnel terminate:
    key(enter ~ .)

# virtsh virtual console escape
(virtual pop|console escape): key("ctrl-]")

# process management
(process grep|pee grep): "pgrep "
process list: "ps -ef\n"
process filter list: "ps -ef | rg -i "
process top: "htop\n"
process fuzzy kill: "pkill {text}"
process fuzzy kill <user.text>: "pkill {text}"
process loop kill: 
    user.insert_cursor("for PID in $(ps -ef | grep [|] | grep -v grep | awk '{{print $2}}'); do kill -9 $PID 2>/dev/null; done")
process kill <number>: "kill -9 {number}"
process kill job <number>: "kill -9 %{number}"
process kill: "kill -9 "

system reboot: "sudo reboot -h now"

# hardware
system [list] memory: "lshw -short -C memory"
system [list] processor: "lscpu\n"
system [list] pee bus: "lspci\n"
system [list] yew bus: "lsusb\n"
system release: "cat /etc/lsb_release\n"

# debugging
debug server: "gdbserver "
debug remote server: "gdbserver --multi :9999\n"

errors redirect: "2>&1 "
errors ignore: "2>/dev/null"

###
# Wallpaper
###
wallpaper set: "feh --bg-scale "
wallpaper set latest: "feh --bg-scale $(find ~/images/wallpaper/ -name $(exa --sort latest --no-icons ~/images/wallpaper/ | tail -n1))\n"


###
# ELF file
###
elf header: "eu-readelf -h "
elf symbols: "eu-readelf -s "


###
# Python
###
(pie|python) new [virtual] (env|environment): "python -m venv env"
python module: "python -m "
python (activate|enter) [env|environment]: "source env/bin/activate\n"
python (deactivate|leave) [env|environment]: "deactivate\n"


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
# Namespaces
###

capability list: "capsh --print\n"

(unshare|namespace) root: "unshare -U -r\n"
(unshare|namespace) net: "unshare -n\n"

# XXX - add support for saying words and making them too upper
environment show: "echo $"

# Custom utility stuff
bat cache build: "bat cache --build\n"
