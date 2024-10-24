# NOTE: these are command line commands, not shell-specific bindings
# see shell.talon for shell-specific keybindings
not os: windows
and tag: terminal
-
tag(): user.line_commands

###
# Packages
#
# These tags correspond to talon grammars you want to enable while you're
# running some terminal emulator on your system. See the associated talon
# files for information and links to what tools they are associated with.
###
tag(): user.package_manager

#tag(): user.buku
tag(): user.ssh
#tag(): user.ghidra_server
#tag(): user.taskwarrior
#tag(): user.timewarrior
tag(): user.make_commands
tag(): user.just_commands
#tag(): user.tmux
tag(): user.git
tag(): user.docker
tag(): user.podman
tag(): user.virsh
tag(): user.yarn
tag(): user.nodejs
#tag(): user.meson
#tag(): user.kubectl
tag(): user.vboxmanage
tag(): user.glab
tag(): user.rust_apps
tag(): user.gpg
tag(): user.nix_cli
tag(): user.poetry
# XXX - See generic_terminal.talon for some basics as well.
tag(): user.generic_unix_shell
tag(): user.unix_utilities
tag(): user.aws_cli
tag(): user.s3fs
tag(): user.direnv
tag(): user.ykman
tag(): user.btrfs
tag(): user.qcow2
tag(): user.borg
tag(): user.atuin
tag(): user.cyberpower-pdu
tag(): user.pip

# Shell commands

# Also see unix_utilities.{py,talon} for run commands
run last script:
    insert("./")
    key(up)
    key(enter)
recall [<user.text>]:
    key(ctrl-r)
    insert(text or "")
re force <user.text>:
    key(ctrl-r)
    insert(text)
    key(enter)
recall last [command]:
    edit.delete_line()
    key(! ! enter enter)
# atuin_open.talon for other tweak commands
tweak last:
    key(up)


# XXX - it would be good to have overrides for words that are harder to say,
# like ssh, ex: see following tunnel word
recall last <user.word>:
    key(!)
    insert(word)
    #this is pretty dangerous...
    #key(enter)
recall last tunnel:
    key(!)
    insert("ssh\n")
    key(enter)


kill all: key(ctrl-c)

(file | folder) name <user.zsh_path_completion>: "{user.zsh_path_completion}"
file list (<user.zsh_path_completions> | <user.folder_paths>):
    path = zsh_path_completion or folder_paths
    "ls {path} \n"
file list long (<user.zsh_path_completions> | <user.folder_paths>):
    path = zsh_path_completion or folder_paths
    "ls -l {path} \n"
file list local <user.zsh_file_completions>: "ls {zsh_file_completions} \n"
file list global <user.folder_paths>: "ls {folder_paths} \n"
file list bare exact: "ls "
file list bare: "ls -l \n"
file size: "ls -lh "
file list (size | bytes): "ls -lB "
file list exact: "ls -l "
file list long exact: "ls -al "
file list with paths: 'ls --sort changed -d - "$PWD"/*'
file list latest: "eza --sort changed | tail -n1\n"
file list today: 'find . -maxdepth 1 -newermt "$(date +%D)"\n'
file list deep: "fd .\n"
file list names: "ls -1 --icons=never\n"
file list clip:
    "ls "
    user.paste_without_new_lines()
    key(enter)

# I can't always rely on -newermt, since an old file might get extracted from from an archive, in the timestamp is
# actually quite old. This allows me to give it the actual local birthdate of the file
file list [last] <number> minutes:
    'find . -maxdepth 1 -type f -exec bash -c \'cur=$(date "+%s"); birth=$(stat -c %W "{{}}"); delta=$((cur - (60*{number}))); if [ $birth -ge $delta ]; then echo "{{}}"; fi\' \\;\n'
file move [last] <number> minutes:
    'find . -maxdepth 1 -type f -exec bash -c \'cur=$(date "+%s"); birth=$(stat -c %W "{{}}"); delta=$((cur - (60*{number}))); if [ $birth -ge $delta ]; then echo "{{}}"; fi\' \\; | xargs mv -t '
file list (last | latest) <number>: "eza --sort changed | tail -n{number}\n"
file list count: "ls -1 | wc -l\n"

folder list latest: "eza -D --sort changed | tail -n1\n"
folder list (last | latest) <number>: "eza -D --sort changed | tail -n{number}\n"
folder list: "eza -D -l\n"
folder list dead symlinks here: "find -L . -maxdepth 1 -type l\n"
folder list dead symlinks: user.insert_between("find -L ", " -maxdepth 1 -type l\n")
folder delete dead symlinks here: "find -L . -maxdepth 1 -type l -delete\n"

file list (folders | directories): "ls -d */\n"
file list (folders | directories) long: "ls -ld */\n"
file list (runnable | executable): "find . -type f -executable\n"
file strings: "strings "
file (tail | follow) [<user.zsh_file_completions>]:
    insert("tail -f ")
    insert(zsh_file_completions or "")
file (count lines | line count): "wc -l "
file list <user.letter>: 'find . -maxdepth 1 -name "{letter}*" -ls\n'
file fuzzy list <user.text>: 'find . -maxdepth 1 -name "*{text}*" -ls\n'
file list {user.file_extension} files: "ls *{file_extension}\n"
file list hidden: "ls -ld .?*\n"
# XXX - it would be nice if these were coloured like regular ls sometimes
file list hidden files: 'find . -maxdepth 1 -not -type d -name ".*" -printf "%f\\n"\n'
file list hidden folders:
    'find . -maxdepth 1 -not -type f -name ".*" -printf "%f\\n"\n'
file list long [sym] links:
    'find . -maxdepth 1 -type l -printf "%f\\n" | xargs ls -l \n'
file list [sym] links: 'find . -maxdepth 1 -type l -printf "%f\\n"\n'

# TODO - revisit the grammar for $() commands
call file latest: "$(eza --sort changed | tail -n1)\n"
[sub] file latest: "$(eza --sort changed | tail -n1) "

file link: "ln -s "
file link force: "ln -sf "
file link force clip:
    insert("ln -sf ")
    edit.paste()
    # key(enter)
file hard link: "ln "
file broken links:
    insert("find . -type l -exec sh -c 'file -b \"$1\" | grep -q ^broken' sh /{} \\; -print")

file (move | rename):
    "mv "
file (move | rename) <user.zsh_file_completions>:
    insert("mv {zsh_file_completions} ")
file move files: user.insert_between("find . -maxdepth 1 -type f -exec mv {} ", " \\;")
file P D F: "evince "
file (touch|new): "touch "
[file] (touch | create|new) {user.common_files}: "touch {common_files}\n"
file touch pair {user.common_extension_pairs}:
    user.insert_between("touch ", ".{{{common_extension_pairs}}}")
file name (<user.zsh_file_completions> | {user.common_files}):
    file = zsh_file_completions or common_files
    insert("{file}")
file global name {user.common_files}: "{common_files}"
file local name <user.zsh_file_completions>: "{zsh_file_completions}"

file copy [<user.zsh_file_completions>]:
    insert("cp -d ")
    insert(zsh_file_completions or "")
file recopy: "!cp\n"
file copy latest <user.folder_paths>:
    user.paste("cp $(ls --sort changed -d {folder_paths}/* | tail -n1) .")
(file | folder) (deep copy | copy deep) [<user.zsh_folder_completions>]:
    insert("cp -dR ")
    insert(zsh_folder_completions or "")
file (file | info | type) [<user.zsh_file_completions>]:
    insert("file -L ")
    insert(zsh_file_completions or "")
file (file | info | type) clip:
    insert("file -L ")
    user.paste_without_new_lines()
    key(enter)

file fuzzy file (here|<user.zsh_folder_completion>):
    path = zsh_folder_completion or "."
    insert("file -L {path}/*\n")

file fuzzy file clip:
    insert("file -L ")
    user.paste_without_new_lines()
    insert("/*\n")


file show: "cat "
# assuming you are using bat
file show plain: "cat -p "
file show max width: "cut -c-120 "
file show max width <number>: "cut -c-{number} "
file show clip:
    "cat "
    user.paste_without_new_lines()
file show (<user.zsh_file_completions> | <user.word>):
    file = zsh_file_completions or word
    insert("cat {file}")

file edit:
    edit.delete_line()
    insert("edit ")
file edit <user.zsh_file_completions>: insert("edit {zsh_file_completions}")
file edit latest: "edit $(eza --sort changed | tail -n1)\n"
file edit here: insert("edit .\n")

file code: "code "
file code new: "code -n "
file code add folder: "code -a "
file code here: "code .\n"
code install extension: "code --install-extension "

file (delete | remove): "rm -I "
# TODO: It might be nice to automatically escape the file name in this case
file (delete | remove) [<user.zsh_file_completions>]:
    insert("rm -I ")
    insert(zsh_file_completions or "")
file safe (delete | remove) all: "rm -i -- *"
file real (delete | remove): "command rm -I "
(file | folder) deep remove: "rm -rIf "
(file | folder) real deep remove: "command rm -rIf "
file diff: "diff "

file check sec: "checksec --file="
file locate: "locate "
file locate clip:
    "locate "
    user.paste_without_new_lines()
run update paths: "sudo updatedb\n"
file [full] path: "readlink -f "


file cut first line: "tail -n +2 "
file cut <number> (lines|line): "tail -n+{number+1} "
file cut last <number> (lines|line): "head -n -{number} "
file cut last line: "head -n -1 "

# dd
file disk image copy:
    user.insert_between("dd bs=4M if=", " of=/dev/sdX conv=fsync oflag=direct status=progress")
file read <number> bytes: user.insert_between("dd bs=1 count={number} if=", " of=")
file read <number> bytes at offset <number>:
    user.insert_between("dd bs=1 count={number_1} skip={number_2} if=", " of=")

loop for file: user.insert_between("for FILE in $(command ls); do ", "echo ${{FILE}}; done")

folder tree permissions:
    user.insert_between('FILE=", "; until [ "$FILE" = "/" ]; do ls -lda $FILE; FILE=`dirname $FILE` done')

(file sizes|disk usage) (all|here): "du -Lsh *\n"
(file sizes|disk usage) <user.zsh_folder_completion>:
    insert("du -Lsh {zsh_folder_completion}/*\n")
#file [disk] usage: "du -sh "


file watch latest: "vlc $(eza --sort changed | tail -n1)"
file play audio: "vlc --play-and-exit --intf dummy --no-interact"

# This uses an actual dynamic list
echo [param] {user.runtime_environment_variables}:
    insert("echo ${{{runtime_environment_variables}}}")
    key(enter)

# echo [param] ({user.environment_variables}|<user.text>):
#     insert("echo ${")
#     snake = user.formatted_text(environment_variables or text, "snake")
#     upper = user.formatted_text(snake, "upper")
#     insert(upper)
#     insert("}")
#     key(enter)

# FIXME: Maybe tweak these to use an action, since lots of dupe
# Split a variable into a list based on specified symbol (or ':')
echo split [<user.symbol_key>] ({user.environment_variables}|<user.text>):
    insert("echo ${")
    snake = user.formated_text(environment_variables or text, "SNAKE_CASE")
    upper = user.formatted_text(snake, "UPPER")
    insert(upper)
    insert("} | tr '")
    insert(symbol_key or ":")
    insert("' '\\n'")
    key(enter)

# directory and files
<user.go>: "cd "
<user.go> (only | first):
    edit.delete_line()
    "cd *\n"
<user.go> clip:
    edit.delete_line()
    insert("cd ")
    user.paste_without_new_lines()
    key(enter)
# NOTE: I don't auto ls here because zsh is setup to automatically do it for me
# FIXME: This should get moved to a zsh specific file
<user.go> (<user.zsh_path_completion> | <user.folder_paths>):
    edit.delete_line()
    path = zsh_path_completion or folder_paths
    user.paste("cd {path}")
    key(enter)
<user.go> global <user.folder_paths>:
    edit.delete_line()
    user.paste("cd {folder_paths}")
    key(enter)
<user.go> local <user.zsh_path_completion>:
    edit.delete_line()
    user.paste("cd {zsh_path_completion}\n")
# <user.go> up doesn't work with talon
<user.go> back:
    edit.delete_line()
    "cd ../\n"
<user.go> real:
    edit.delete_line()
    "cd -P .\n"
<user.go> real back:
    edit.delete_line()
    "cd -P ..\n"
<user.go> <number_small> back:
    edit.delete_line()
    insert("cd ")
    insert(user.path_traverse(number_small))
    key(enter)
<user.go> home:
    edit.delete_line()
    "cd\n"
<user.go> next:
    edit.delete_line()
    insert("cd ")
    key(tab)
    sleep(100ms)
    key(enter)
    # insert("ls\n")
<user.go> deep [<user.text>]:
    edit.delete_line()
    insert("cd $(fd -t d . | fzf --reverse)\n")
    insert(text or "")
# don't honour .gitignore
<user.go> (all|hiddeni) deep [<user.text>]:
    edit.delete_line()
    insert("cd $(fd -I -t d . | fzf --reverse)\n")
    insert(text or "")

(<user.go> | folder) (last | flip): "cd -\n"
<user.go> latest:
    edit.delete_line()
    insert("cd $(eza --sort changed | tail -n1)\n")

# zoxide
oxy <user.text>:
    edit.delete_line()
    insert("z {text}\n")
oxy fuzzy <user.text>:
    edit.delete_line()
    insert("zi {text}\n")

folder (remove | delete): "rmdir "
folder (create | new) [<user.text>]:
    insert("mkdir -p ")
    pathing = user.formatted_text(text, "pathing")
    insert(pathing)


# XXX - It would be nice to make the depth configurable
# flat tree
file [flat] tree: "fd . -d 2\n"
file [flat] tree follow: "fd . -d 2 -L\n"
file [flat] tree follow <user.zsh_symlink_completion>: "fd . '{zsh_symlink_completion}' -d 2 -L\n"
file [flat] tree <user.folder_paths>: "fd . -d 2 '{folder_paths}'\n"
file [flat] tree <user.zsh_folder_completion>: "fd . -d 2 '{zsh_folder_completion}'\n"
file [flat] tree more: "fd . -d "
file [flat] tree long: "fd . -d 2 -l\n"
file [flat] tree all: "fd . -d 2 -I\n"
file [flat] tree folders: "fd . -d 2 -t d\n"
file [flat] tree [depth] <number_small>: "fd . -d {number_small}\n"
file [flat] tree clip [depth <number_small>]:
    "fd . -d {number_small or 2} "
    user.paste_without_new_lines()
    key(enter)

file deep tree: "eza --tree --git-ignore\n"

folder pop: "popd\n"
# pwd | tr -d \\n\\r | xclip -sel clipboard

# permissions
file [change] mode: "chmod "
file (mark | make) (exec | executable): "chmod +x "
[file] change owner: "chown "
[file] change owner me: "chown $UID:$GID "
[file] change deep owner: "chown -R "
[file] change deep owner me: "chown -R $UID:$GID "
sudo [file] change owner: "sudo chown "
sudo [file] change owner me:
    user.insert_between("sudo bash -c 'chown $SUDO_UID:$SUDO_GID ", "'")
sudo [file] change deep owner: "sudo chown -R "
sudo [file] change deep owner me:
    user.insert_between("sudo bash -c 'chown -R $SUDO_UID:$SUDO_GID ", "'")

now command that:
    edit.up()
    edit.line_start()
    insert("command ")
    edit.line_end()
# file viewing
less that:
    edit.line_end()
    insert("| less")
file less: "less "
less last:
    edit.up()
    insert("| less\n")

# piping
tea that: " | tee "

# grepping

rip that: " | rg -i "
file rip: "rg -i "
file rip hidden: "rg -i --hidden"
file rip binary: "rg -i --binary"
file rip clip:
    insert("rg -i ")
    user.paste_without_new_lines()
    key(enter)
file rip exclude: "rg -i -g \\!"
file rip around: "rg -B2 -A2 -i "
file rip (exact | precise): "rg "
file rip [git] conflicts:
    "rg --no-messages --no-line-number --no-filename -e '^<<<<<<< ' -e '^=======$' -e '>>>>>>>$'\n"
rip last:
    edit.up()
    insert("| rg -i ")

# even though rip is arguably better, we still want grep for remote terminals,
# etc
file grep: "grep -i "
file grep around: "grep -B2 -A2 -i "
grep last:
    edit.up()
    insert("| grep -i ")

# networking

net trace: "traceroute "
net trace <user.domains>: "traceroute {domains}\n"
net trace clip:
    insert("traceroute")
    edit.paste()
    key(enter)
net ping: "ping "
net ping <user.domains>: "ping {domains}\n"
net ping clip:
    insert("ping ")
    edit.paste()
    key(enter)

net (cat|connect) [<user.domains>] [(<user.ports>|<number>)]:
    insert("nc ")
    insert(domains or "")
    key(space)
    insert(ports or "")
    insert(number  or "")
net connect <user.domains>: "nc {domains} "
net cat listener: "nc -v -l -p "
net cat listen [on] <number>:
    user.bind_nc_listener(number)
    key(enter)
net cat listen [on] <number> pipe from file:
    user.bind_nc_listener(number)
    insert(" < ")
#NOTE: saying `to file` next to the number will cause it to be interpreted as a number
net cat listen [on] <number> pipe to file:
    user.bind_nc_listener(number)
    insert(" > ")
net cat copy file to: user.insert_between("nc -v ", "<")
net my I P: "dig +short myip.opendns.com @resolver1.opendns.com\n"
net port <user.ports>: "{ports}"
net dump: "tcpdump "


show hosts file: "cat /etc/hosts\n"

net (remote desktop | R D P):
    user.insert_between("xfreerdp /timeout:90000 /size:1280x800 /v:", " /u: /p:")

run see tags: "ctags --recurse --exclude=.git --exclude=.pc *"
run see scope database:
    insert('find . -name "*.c"')
    insert(' -o -name "*.cpp"')
    insert(' -o -name "*.h"')
    insert(' -o -name "*.hpp"')
    insert(' -o -name "*.py"')
    insert(' -o -name "*.s"')
    insert(' -o -name "*.asm"')
    insert("> cscope.files\n")
    insert("cscope -q -R -b -i cscope.files\n")

file head: "head "
head [<number_small>] this:
    insert("| head -n {number_small or 10} ")
head [<number_small>] last:
    edit.up()
    insert("| head -n {number_small or 10} ")
file head <number_small>: "head -n {number_small} "
folder show: "pwd\n"

lazy edit:
    insert("edit ")
    insert("$(find . -not -path '*/\\.git/*' -name \"**\")")
    key("left")
    key("left")
    key("left")

lazy edit <user.text>:
    insert("edit ")
    insert("$(find . -not -path '*/\\.git/*' -name \"*{text}*\")\n")

find <user.text> inside (python | pie) files:
    insert('$(find . -name "*.py") | xargs rg -i "{text}"\n')

find <user.text> inside (python | pie) files less:
    insert('$(find . -name "*.py") | xargs rg -i "{text}" | less\n')

man page: "man "
so do: "sudo "
so do with (env | environment): "sudo -E "
so do sue: "sudo su\n"
so do tea: "sudo tee "
so do tee append: "sudo tee -a "
so do that:
    edit.line_start()
    insert("sudo ")
    key(enter)
time that:
    edit.line_start()
    insert("time ")
    key(enter)
so do edit: "sudoedit "
so do edit <user.paths>: "sudoedit {paths}\n"

run d message: "sudo dmesg --color --reltime\n"
run d message samba: "sudo dmesg --color --reltime | rg CIFS\n"

# tar extraction
# TODO: Should add the version with zsh completion
(file tar [ball] | tar file) list: "tar -tf "
(file tar [ball] | tar file) (add | append): "tar -rf "
(file tar [ball] | tar file) update: "tar -uf "
(file tar [ball] | tar file) create: "tar -cvJf "
(file tar [ball] | tar file) (delete | remove): "tar --delete -f "

file [tar] [ball] extract: "tar -xvaf "

# other file format extraction
file [tar] [ball] extract deb: "ar x "
# https://github.com/facebook/zstd
file extract Z S T: "tar --use-compress-program=unzstd -xvf "
file extract C P I O: "cpio -idmv "
file unzip C P I O: user.insert_between("gzip -cd ", " | cpio -idmv")
# Commonly found in boot partitions
# TODO: This should be tweaked with a copy that uses fake root for device nodes
file extract root F S:
    "mkdir rootfs 2>/dev/null; cd rootfs; gzip -cd ../rootfs.gz | cpio -idmv"
file B unzip: "bunzip2 "
file (gun zip | unzip | seven extract): "7z x "
file (seven | zip) list: "7z l "
file G zip: "gzip "
file zip folder: "TMP_PASS=$(genpasswd); echo password: $TMP_PASS; 7z a -r -p$TMP_PASS output.7z "
file create encrypted (zip | archive): "TMP_PASS=$(genpasswd); echo password: $TMP_PASS; 7z -p $TMP_PASS output.7z "

run curl: "curl "
(file | web) (download | get): "wget "
(file | web) (download | get) clip:
    insert("wget ")
    user.paste_without_new_lines()
    key(enter)
(file | web) (download | get) ignore cert: "wget --no-check-certificate "

(run script | file run): "./"
(run script | file run) {user.executable_files}: "./{executable_files}"

run again:
    insert("./")
    key(up enter)
run vim: "vim "
run make: "make\n"
run make install: "make install\n"
run clean and make: "make clean && make\n"
run make clean: "make clean\n"
run make debug: "make debug\n"
run make kasan: "make kasan\n"
run make release: "make release\n"
run see make: "cmake "
run configure make: "./configure && bear -- make\n"
run configure help: "./configure --help\n"
run auto jen make: "./autogen.sh && ./configure && bear -- make\n"

sub command:
    insert("$()")
    key(left)

parameter:
    insert("${}")
    edit.left()

# bash convenience stuff
history show: "history\n"
history search: "history | rg -i"
history search <user.text>: "history | rg -i {text}"
(X args | extra) this: "| xargs "
(X args | extra) last:
    edit.up()
    insert("| xargs ")


# virtsh virtual console escape
(virtual pop | console escape): key("ctrl-]")

deja <user.text>: "!{text}\t"

# process management
(process grep | pee grep): "pgrep "
process list: "ps -ef\n"
process (rip | search | find): "ps -ef | rg -i "
process (rip | search | find) <user.text>: "ps -ef | rg -i {text}"
process forest: "ps -aef --forest\n"
process top: "htop\n"
process fuzzy kill: "pkill "
process fuzzy kill <user.text>: "pkill {text}"
process fuzzy kill pid: user.insert_between("pgrep ", " | xargs kill -9")
process loop kill:
    user.insert_between("for PID in $(ps -ef | grep ", " | grep -v grep | awk '{{print $2}}'); do kill -9 $PID 2>/dev/null; done")
process kill <number>: "kill -9 {number}"
[process] kill job <number>: "kill -9 %{number}"
process kill: "kill -9 "
process sudo kill: "sudo kill -9 "
process kill all: "killall "
process kill all <user.word>: "killall {word}"
job list: "jobs\n"
job kill <number>: "kill -9 %{number}"

system reboot [now]: "sudo reboot -h now"
system shutdown [now]: "sudo shutdown -h now"

# debugging
file debug: "gdb "
run G D B: "gdb -q\n"
file debug with command: "gdb -ex "
file arm debug: "arm-none-eabi-gdb "
file arm sixty forty bug: "aarch64-linux-gnu-gdb "
debug file {user.executable_files}: "gdb {executable_files}\n"

run (debug script | debugger): "gdb -x debug.gdb\n"
run arm (debug script | debugger): "arm-none-eabi-gdb -x debug.gdb\n"
run debug server: "gdbserver "
run debug remote server: "gdbserver --multi :9999\n"
run debug remote server [on] port <number>: "gdbserver --multi :{number}\n"

errors redirect: "2>&1 "
errors ignore: "2>/dev/null"

###
# ELF file
###
[file] elf [read] header: "readelf -h "
[file] elf [read] symbols: "readelf -s "
[file] elf [read] (program headers | sections): "readelf -l "
[file] elf dependencies: "readelf -d "
[file] elf debug info: user.insert_between("readelf -w", "| head -15")
[file] strip: "strip --strip-all "
[file] elf extract (debug | symbols): "objcopy --only-keep-debug "
[file] elf read got: "readelf -r "
[file] elf read P L T: "objdump -d -s -j .plt -j .got.plt "
[file] elf exports: user.insert_between("nm -D --demangle ", "| rg ' T '")

###
# Version stuff
###
(cis | system) I D: "id\n"
(cis | system) user: "whoami\n"
(cis | system) (name | version | kernel): "uname -a\n"


###
# Environment variables
###

able list: "env\n"
able (find|grep|rip) [<user.text>]:
    insert("env|rg -i ")
    snake = user.formatted_text(text or "", "ALL_CAPS,SNAKE_CASE")

    insert(snake)
able find strict [<user.text>]:
    insert("env|rg ")
    snake = user.formatted_text(text or "", "ALL_CAPS,SNAKE_CASE")
    insert(snake)
able show: "echo $"
able prefix <user.text>:
    edit.line_start()
    snake = user.formatted_text(text or "", "ALL_CAPS,SNAKE_CASE")
    insert(snake)
    insert("=")
able set {user.environment_variables}: "export {environment_variables}="
able put {user.environment_variables}: "${{{environment_variables}}}"

# Custom utility stuff
bat cache build: "bat cache --build\n"

file P D F compress:
    "gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf"
file P D F strip pages:
    "gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf -dFirstPage=1 -dLastPage=1 input.pdf"
file P D F scale: 'cpdf -scale-page "0.5 0.5" in.pdf -o out.pdf'
file P D F cut pages:
    user.insert_between("qpdf input.pdf --pages . 1,", "3-r1 -- output.pdf")

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

code Q L resolve: "codeql resolve languages\n"

###
# Development
###

(generate compile commands | run bear make): "bear -- make"
file build: "gcc "
file build clip:
    insert("gcc ")
    edit.paste()
    insert(" -o ")

run wiggly: "weggli '{}'"

bytes disassemble:
    insert("rasm2 -d ''")
    key(left)

module load N F tables: "unshare -U -r -n -- iptables -L \n"

print hex as decimal: "printf '%d\\n', 0x"
print decimal as hex: "printf '0x%x\\n', "

while true loop: "while true; do ; done"

file swap in place: "sed -i s///g "
file swap many in place: 'find . -name "" | xargs sed -i s///g'
file swap many see: 'find . -name "*.[ch]" | xargs sed -i -e s///g'
file swap many pie: 'find . -name "*.py" | xargs sed -i -e s///g'

###
# screen/tmux
###

mux list: "screen -list\n"
mux attach now: "screen -x\n"
mux next [window]: key(ctrl-a n)
mux prev [window]: key(ctrl-a p)


###
# XML
###
X M L lint: "xmllint --format "

###
# crontab
###
cron tab list: "crontab -l\n"
cron tab (delete | remove): "crontab -i -r "

###
# cross-compiled tools
###
arm L D D:
    user.insert_between("/usr/arm-linux-gnueabi/bin/readelf -d ", " | rg NEEDED")
arm readelf: "/usr/arm-linux-gnueabi/bin/readelf "

file hex dump: "hexdump -C "
file hex dump <number> bytes: "hexdump -C -n {number} "
file hex dump <number> bytes at offset <number>:
    "hexdump -C -n {number_1} -s {number_2} "

file bin walk: "binwalk -Me "
file un squash: "unsquashfs "

run I D: "id\n"

file dependencies: "ldd "

G D B version: "gdb --version\n"

disk part list: "fdisk -l "

# bash helpers
print hex: "printf '0x%x\\n' "

screen serial (ninety six | fortinet): "sudo screen /dev/ttyUSB0 9600\n"
screen serial eleven: "sudo screen /dev/ttyUSB0 115200\n"

# TODO: This should be moved to its own tag based thing probably
pre commit run: "pre-commit run --all-files\n"
pre commit auto update: "pre-commit autoupdate\n"
pre commit install: "pre-commit install\n"
pre commit uninstall: "pre-commit uninstall\n"
pre commit generate config: "pre-commit sample-config > .pre-commit-config.yaml\n"

edit read me: "edit README.md\n"

user add group: "sudo usermod -aG "
run talon event log: 'echo "events.tail()"|~/.talon/bin/repl\n'
run tail talon log: "tail -f ~/.talon/talon.log\n"

[file] R P M extract: user.insert_between("rpm2cpio ./", " | cpio -idmv")
# If errors about bad numbers above, try some combo of decompression
[file] R P M decompress extract:
    user.insert_between("rpm2cpio ./", "| 7z e -si | cpio -idmv")
pipe to C P I O: "| cpio -idmv"

mime type list: "handlr list\n"
mime type show: "file --mime-type"


file show row <number>: "sed -n '{number}p' "
file chunk row <number>: "sed -i '{number}d' "

(run|file) which: "which "
(run|file) where: "type -a "

folder sync: "rsync -avz "
folder sync here: "rsync -avz . "

(cert|certificate) show: "openssl x509 -in "
(cert|certificate) show expiry: "openssl x509 -enddate -noout -in "

code here: "code .\n"

re run <number>: "!{number}\n"
# re run last: "!!\n"

# My convenience commands on nix boxen
repo sync: "update-core-repos\n"

draw extract [<user.zsh_file_completion>]:
    insert("drawio-export-all.py ")
    insert(zsh_file_completion or "")

folder make temp: "mktemp -d\n"

# FIXME: It might be nice to have some helper function that allows you to automatically put the given commands inside of
# a sub call...
(gen|generate) (pass|password): "genpasswd\n"
sub (gen|generate) (pass|password): "$(genpasswd)"


now paginate [width <user.number_string> call <user.number_string>]:
    insert("| pr -tw")
    insert(number_string_1 or "100")
    insert(" --columns ")
    insert(number_string_2 or "3")

file U U decode [<user.zsh_file_completion>]:
    insert("uudecode ")
    insert(zsh_file_completion or "")

file U U encode [<user.zsh_file_completion>]:
    insert("uuencode ")
    insert(zsh_file_completion or "")

link tree [<user.text>]:
    user.insert_between("linktree $(which {text or ''}", ")")

link tree clip:
    insert("linktree $(which ")
    edit.paste()
    insert(")\n")

P E bear: "PE-bear"

run wine shell:
    edit.delete_line()
    insert("WINEDEBUG=-all wine64 cmd\n")

run wine command:
    edit.delete_line()
    user.insert_between("WINEDEBUG=-all wine64 cmd /c \"", "\"")

run zsh:
    edit.delete_line()
    insert("zsh\n")
