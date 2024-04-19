tag: user.ssh
-

ssh dump hosts: user.ssh_dump_hosts_list()

# ssh
# XXX - make texts actually query a series of names from the %h config
#(secure shell|tunnel) [<user.text>]:
#    insert("ssh ")
#    insert(text or "")
# tunnel {user.ssh_hosts}: insert("ssh {ssh_hosts}\n")
tunnel [to|host] {user.ssh_hosts}: insert("ssh {ssh_hosts}")
tunnel no (pass|password) {user.ssh_hosts}: insert("ssh -o PreferredAuthentications=publickey {ssh_hosts}")
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


tunnel local proxy <number> {user.ssh_hosts}: user.insert_between("ssh -L {number}", ":localhost:{number} {ssh_hosts}")
tunnel local proxy {user.ports} {user.ssh_hosts}: user.insert_between("ssh -L {ports}", ":localhost:{ports} {ssh_hosts}")

(S S H | secure shell | tunnel) key (gen | generate):
    "ssh-keygen -o -a 256 -t ed25519\n"
tunnel key fingerprint:
    user.insert_between("ssh-keygen -lf ~/.ssh/", ".pub\n")
(tunnel | secure) copy [<user.text>]:
    insert("scp -r ")
    insert(text or "")
tunnel copy from {user.ssh_hosts}: insert("scp -r {ssh_hosts}:")
tunnel copy to {user.ssh_hosts}: user.insert_between("scp -r ", " {ssh_hosts}:")
[tunnel] show authorized keys: "cat ~/.ssh/authorized_keys\n"
[tunnel] show pub keys: "cat ~/.ssh/*.pub\n"
edit authorized keys: "edit ~/.ssh/authorized_keys\n"
go secure shell config: "cd ~/.ssh\n"
tunnel (pop | terminate): key(enter ~ .)

tunnel key copy {user.ssh_keys} [{user.ssh_hosts}]: "ssh-copy-id -i {ssh_keys} {ssh_hosts or ''}"

tunnel control check {user.ssh_keys}: "ssh -O check {ssh_hosts or ''}"
tunnel control exit {user.ssh_keys}: "ssh -O exit {ssh_hosts or ''}"
tunnel control stop {user.ssh_keys}: "ssh -O stop {ssh_hosts or ''}"
tunnel control cancel {user.ssh_keys}: "ssh -O cancel {ssh_hosts or ''}"
tunnel control forward {user.ssh_keys}: "ssh -O forward {ssh_hosts or ''}"

# FIXME: Add an option with ssh hosts to target
tunnel (gen|generate) age key:
    user.insert_between("nix shell nixpkgs#ssh-to-age.out -c sh -c 'ssh-keyscan -p 10022 -t ssh-ed25519 ", " 2>&1 | rg ssh-ed25519 | cut -f2- -d\" \" | ssh-to-age'")
