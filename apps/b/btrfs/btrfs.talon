app: terminal
tag: user.btrfs
-

butter [sub] volume list: "btrfs subvolume list "
butter [sub] volume list clip:
    insert("btrfs subvolume list ")
    edit.paste()
    key(enter)
butter [sub] volume delete: "btrfs subvolume delete "
butter [sub] volume create: "btrfs subvolume create "

butter [sub] volume snapshot: "btrfs subvolume snapshot "
butter [sub] volume find new: "btrfs subvolume find-new "
