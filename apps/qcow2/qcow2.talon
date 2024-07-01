app: terminal
tag: user.qcow2
-

queue cow resize: "qemu-img resize "
queue cow resize <number> (gigs|gigabytes):
    user.insert_between("qemu-img resize ", " {number}G")
queue cow resize <user.zsh_file_completion> <number> (gigs|gigabytes):
    "qemu-img resize {zsh_file_completion} {number}G"
