app: terminal
tag: user.ssh
-

ssh dump hosts: user.ssh_dump_hosts_list()

# ssh
# XXX - make texts actually query a series of names from the %h config
#(secure shell|<user.ssh>) [<user.text>]:
#    insert("ssh ")
#    insert(text or "")
# <user.ssh> {user.ssh_hosts}: insert("ssh {ssh_hosts}\n")
<user.ssh> [to|host] {user.ssh_hosts}: insert("ssh {ssh_hosts}")
<user.ssh> no (pass|password) {user.ssh_hosts}: insert("ssh -o PreferredAuthentications=publickey {ssh_hosts}")
<user.ssh> last:
    key(ctrl-r)
    sleep(500ms)
    insert("^ssh ")
    key(enter)
    key(enter)
<user.ssh> copy last:
    key(ctrl-r)
    sleep(500ms)
    insert("^scp ")
    key(enter)
    key(enter)


<user.ssh> local proxy <number> {user.ssh_hosts}: user.insert_between("ssh -L {number}", ":localhost:{number} {ssh_hosts}")
<user.ssh> local proxy {user.ports} {user.ssh_hosts}: user.insert_between("ssh -L {ports}", ":localhost:{ports} {ssh_hosts}")

<user.ssh> key (gen | generate):
    "ssh-keygen -o -a 256 -t ed25519\n"
<user.ssh> key fingerprint:
    user.insert_between("ssh-keygen -lf ~/.ssh/", ".pub\n")
(<user.ssh> | secure) copy [<user.text>]:
    insert("scp -r ")
    insert(text or "")
<user.ssh> copy from {user.ssh_hosts}: insert("scp -r {ssh_hosts}:")
<user.ssh> copy to {user.ssh_hosts}: user.insert_between("scp -r ", " {ssh_hosts}:")
[<user.ssh>] show authorized keys: "cat ~/.ssh/authorized_keys\n"
[<user.ssh>] show pub keys: "cat ~/.ssh/*.pub\n"
edit authorized keys: "edit ~/.ssh/authorized_keys\n"
go secure shell config: "cd ~/.ssh\n"
<user.ssh> (pop | terminate): key(enter ~ .)

<user.ssh> key copy {user.ssh_keys} [{user.ssh_hosts}]: "ssh-copy-id -i {ssh_keys} {ssh_hosts or ''}"

<user.ssh> control check {user.ssh_hosts}: "ssh -O check {ssh_hosts or ''}"
<user.ssh> control exit {user.ssh_hosts}: "ssh -O exit {ssh_hosts or ''}"
<user.ssh> control stop {user.ssh_hosts}: "ssh -O stop {ssh_hosts or ''}"
<user.ssh> control cancel {user.ssh_hosts}: "ssh -O cancel {ssh_hosts or ''}"
<user.ssh> control forward {user.ssh_hosts}: "ssh -O forward {ssh_hosts or ''}"

# FIXME: Add an option with ssh hosts to target
<user.ssh> (gen|generate) age key:
    user.insert_between("nix shell nixpkgs#ssh-to-age.out -c sh -c 'ssh-keyscan -p 10022 -t ssh-ed25519 ", " 2>&1 | rg ssh-ed25519 | cut -f2- -d\" \" | ssh-to-age'")
