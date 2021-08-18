os: linux
tag: terminal
and tag: user.buku
-

# general options
bookmark help: "buku -h\n"
bookmark version: "buku -v\n"
bookmark new: "buku -a "
bookmark (auto add|that):
    insert("buku -a ")
    edit.paste()
    key(enter)
    insert("buku -w -1\n")
bookmark delete: "buku -d "

bookmark update: "buku -u "
bookmark edit: "buku -w "
bookmark edit last:
    insert("buku -w -1\n")

# edit options

# search options
bookmark search: "buku -s "
bookmark list: "oil\n"
