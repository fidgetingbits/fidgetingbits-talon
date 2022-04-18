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

# XXX - See generic_terminal.talon for some basics as well.
tag(): user.generic_unix_shell


# Shell commands

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

file list <user.folder_paths>: "ls {folder_paths}\n"

file list bare exact: "ls --no-icons "
file list bare: "ls -l --no-icons\n"
file size: "ls -lh "
file list exact: "ls -l"
file list long exact: "ls -al "
file list with paths: 'ls --sort changed --no-icons -d - "$PWD"/*'
file list latest: "exa --sort changed --no-icons | tail -n1\n"
file list last <number>: "exa --sort changed --no-icons | tail -n{number}\n"
file list folders: "ls -d */\n"
file list (runnable|executable): "find . -type f -executable\n"
file strings: "strings "
file (tail|follow): "tail -f "
file line count: "wc -l "
file list <user.letter>: 'find . -maxdepth 1 -name "{letter}*" -ls\n'
file list fuzzy {user.file_extension}: "ls *{file_extension}\n"
file list {user.file_extension} files: "ls *{file_extension}\n"

# find command
file find all links: "find . -maxdepth 1 -type l  -ls\n"
file find all folders: "find . -maxdepth 1 -type d  -ls\n"
file fine all files: "find . -maxdepth 1 -type f  -ls\n"

# TODO - revisit the grammar for $() commands
call file latest: "$(exa --sort changed --no-icons | tail -n1)\n"

# TODO - somehow make this scriptable to print anything
file edit latest: "edit $(exa --sort changed --no-icons | tail -n1)\n"
file latest: "$(exa --sort changed --no-icons | tail -n1)"
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
file P D F: "evince "
file touch: "touch "
file copy: "cp -d "
file copy latest <user.folder_paths>: user.paste("cp $(ls --sort changed --no-icons -d {folder_paths}/* | tail -n1) .")
file (deep copy|copy deep): "cp -dR "
file (file|info|type): "file "
file show <user.text>: "cat {text}"
file show: "cat "
file edit: insert("edit ")
file edit here: insert("edit .\n")
file (delete|remove): "rm -I "
file safe remove all: "rm -i -- *"
file real remove: "/bin/rm -I "
file disk image copy: user.insert_cursor("dd bs=4M if=[|] of=/dev/sdX conv=fsync oflag=direct status=progress")
(file|folder) deep remove: "rm -rIf "
(file|folder) real deep remove: "/bin/rm -rIf "
file diff: "diff "
# find
file find:
    user.insert_cursor("find . -name \"[|]\" 2>/dev/null")
file find file:
    user.insert_cursor("find . -type f -name \"[|]\" 2>/dev/null")
file find folder:
    user.insert_cursor("find . -type d -name \"[|]\" 2>/dev/null")
# case insensitive fuzzy find
file fuzzy find:
    user.insert_cursor("find . -iname \"*[|]*\" 2>/dev/null")
file fuzzy find today:
    user.insert_cursor("find . -mtime -1 -name \"*[|]*\" 2>/dev/null")
file fuzzy find at clip:
    insert("find ")
    edit.paste()
    user.insert_cursor(" -iname \"*[|]*\" 2>/dev/null")
file hash: "sha256sum "
file check sec: "checksec --file="
file locate: "locate "
file [full] path: "readlink -f "

loop for file: insert("for FILE in $(exa --no-icons); do echo ${{FILE}}; done")

file tree permission: "tree -pufid "

folder tree permissions: user.insert_cursor('FILE=[|]; until [ "$FILE" = "/" ]; do ls -lda $FILE; FILE=`dirname $FILE` done')

file edit read me: insert("edit README.md\n")
file edit make file: insert("edit Makefile\n")
file [disk] usage all: "du -sh *\n"
#file [disk] usage: "du -sh "

trash list: "trash-list\n"
trash restore: "trash-restore "
trash empty: "trash-empty "
file watch latest: "vlc $(exa --sort changed --no-icons | tail -n1)"

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
pivot <user.folder_paths>:
    user.paste("cd {folder_paths}\n")
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
pivot latest: "cd $(exa --sort changed --no-icons | tail -n1)\n"


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

# piping
tea that: "| tee "

# grepping

rip that: " | rg -i "
file rip: "rg -i "
file rip exclude: "rg -i -g \\!"
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
so do with (env|environment): "sudo -E "
so do sue: "sudo su\n"
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
file tar [ball] list: "tar -tf "
file tar [ball] create: "tar -cvJf"
file [tar] [ball] extract: "tar -xvaf "
file [tar] [ball] extract deb: "ar x "
# https://github.com/facebook/zstd
file extract Z S T: "tar --use-compress-program=unzstd -xvf "
#favor 7z because it supports newer decryption mechanisms
#file unzip: "unzip "
file B unzip: "bunzip2 "
file (unzip|seven extract): "7z x "
file (seven|zip) list: "7z l "
file zip folder: "zip -rP changepassword output.zip "
file create encrypted (zip|archive): "zip -P changepassword output.zip "

# kernel modules
module list: "lsmod\n"
module search: "lsmod |rg -i"
module probe: "modprobe "
module remove: "rmmod "

run curl: "curl "
run double you get: "wget "
[file] download: "wget "
[file] download clip:
    insert("wget ")
    edit.paste()
    key(enter)
[file] download ignore cert: "wget --no-check-certificate "

# because talent doesn't seem to like me saying ./
run script: "./"
run again:
    insert("./")
    key(up enter)
run vim: "vim "
run make: "make\n"
run clean and make: "make clean && make\n"
run make clean: "make clean\n"
run see make: "cmake "
run configure make: "./configure && bear -- make\n"
run auto jen make: "./autogen.sh && ./configure && bear -- make\n"

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
    sleep(500ms)
    insert("^ssh ")
    key(enter)
    key(enter)
tunnel copy last:
    key(ctrl-r)
    sleep(500ms)
    insert("^scp ")
    key(enter)
    key(enter)

secure shall key gen: "ssh-keygen -t ed25519\n"
(tunnel|secure) copy [<user.text>]:
    insert("scp -r ")
    insert(text or "")
show authorized keys: "vi ~/.ssh/authorized_keys\n"
show pub keys: "cat ~/.ssh/*.pub\n"
edit authorized keys: "vi ~/.ssh/authorized_keys\n"
go secure shell config: "cd ~/.ssh\n"
# talon suddenly loves the word termini
#tunnel (terminate|termini):
tunnel (pop|terminate):
    key(enter ~ .)

# virtsh virtual console escape
(virtual pop|console escape): key("ctrl-]")

# process management
(process grep|pee grep): "pgrep "
process list: "ps -ef\n"
process find: "ps -ef | rg -i "
process tree: "pstree\n"
process top: "htop\n"
process fuzzy kill: "pkill "
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
system release: "cat /etc/lsb-release\n"

# debugging
run (debug script|debugger): "gdb -x debug.gdb\n"
run debug server: "gdbserver "
run debug remote server: "gdbserver --multi :9999\n"

errors redirect: "2>&1 "
errors ignore: "2>/dev/null"

###
# images
###
file image: "feh "
wallpaper set: "feh --bg-scale "
wallpaper set latest: "feh --bg-scale $(find ~/images/wallpaper/ -name $(exa --sort changed --no-icons ~/images/wallpaper/ | tail -n1))\n"


###
# ELF file
###
file elf header: "eu-readelf -h "
file elf symbols: "eu-readelf -s "


###
# Python
###
(pie|python) new [virtual] (env|environment): "python -m venv env"
python module: "python -m "
python (activate|enter) [env|environment]: "source env/bin/activate\n"
python (deactivate|leave) [env|environment]: "deactivate\n"

python three eight env: "virtualenv -p python3.8 py38"
python three nine env: "virtualenv -p python3.9 py39"


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
# Version stuff
###
(cis|system) I D: "id\n"
(cis|system) user: "whoami\n"
(cis|system) (version|kernel): "uname -a\n"
(cis|system) show release: "cat /etc/lsb-release\n"

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

file P D F compress: "gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf"
file P D F strip pages: "gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf -dFirstPage=1 -dLastPage=1 input.pdf"
file P D F scale: 'cpdf -scale-page "0.5 0.5" in.pdf -o out.pdf'

###
# Limits
###

limits show all: "ulimit -a\n"
limits show files: "ulimit -f\n"
limits show processes: "ulimit -u\n"
limits show stack: "ulimit -s\n"
limits show core: "ulimit -c\n"

###
# Sorting
###
file sort column [<user.number_string>]:
    insert("sort -k ")
    insert(number_string or "")

run B P F trace:
    user.insert_cursor("sudo BPFTRACE_PERF_RB_PAGES=256 bpftrace [|].bt | tee trace.log")

code Q L resolve: "codeql resolve languages\n"

###
# Kernel
###
kernel generate tags: "python scripts/clang-tools/gen_compile_commands.py"
run pa hole: "pahole "

###
# Development
###

(generate compile commands|run bear make): "bear -- make"
file build: "gcc "
file build clip:
    insert("gcc ")
    edit.paste()
    insert(" -o ")

clipboard as Q R code: "xclip -o -s c | qrencode -o - | feh --force-aliasing -ZF -"

###
# udev
###

you dev admin: "udevadm "
run wiggly: "weggli '{}'"

bytes disassemble: 
  insert("rasm2 -d ''")
  key(left)
