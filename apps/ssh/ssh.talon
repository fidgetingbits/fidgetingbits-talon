tag: user.ssh
-

ssh dump hosts: user.ssh_dump_hosts_list()

# ssh
# XXX - make texts actually query a series of names from the %h config
#(secure shell|tunnel) [<user.text>]:
#    insert("ssh ")
#    insert(text or "")
tunnel {user.ssh_hosts}: insert("ssh {ssh_hosts}\n")
tunnel host {user.ssh_hosts}: insert("ssh {ssh_hosts}")
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

# 8384

tunnel local proxy <number> {user.ssh_hosts}: user.insert_between("ssh -L {number}", ":localhost:{number} {ssh_hosts}")
tunnel local proxy {user.ports} {user.ssh_hosts}: user.insert_between("ssh -L {ports}", ":localhost:{ports} {ssh_hosts}")

(S S H | secure shell | tunnel) key (gen | generate):
    "ssh-keygen -o -a 256 -t ed25519\n"
(tunnel | secure) copy [<user.text>]:
    insert("scp -r ")
    insert(text or "")
tunnel copy from {user.ssh_hosts}: insert("scp -r {ssh_hosts}:")
tunnel copy to {user.ssh_hosts}: user.insert_between("scp -r ", " {ssh_hosts}:")
[tunnel] show authorized keys: "vi ~/.ssh/authorized_keys\n"
[tunnel] show pub keys: "cat ~/.ssh/*.pub\n"
edit authorized keys: "vi ~/.ssh/authorized_keys\n"
go secure shell config: "cd ~/.ssh\n"
# talon suddenly loves the word termini
#tunnel (terminate|termini):
tunnel (pop | terminate): key(enter ~ .)
