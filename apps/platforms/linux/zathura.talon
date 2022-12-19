app: zathura
-

settings():
    key_wait = 2
    insert_wait = 2
bookmark: ":bmark "
bookmark delete: ":bdelete "

bookmark list:
    insert(":")
    sleep(50ms)
    insert("blist \n")
go <number>: "{number}G"
go first: "gg"
go last: "G"
half: key(ctrl-d)
half up: key(ctrl-u)
jump back: key(ctrl-o)
jump next: key(ctrl-i)
search: "/"
page next: "J"
page back: "K"
zoom in: "shift-+"
zoom out: "+"
mark set <number>: "m{number}"
mark set <user.letter>: "m{user.letter}"
mark <number>: "'{number}"
mark <user.letter>: "'{user.letter}"
