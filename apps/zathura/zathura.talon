app: zathura
-
settings():
    key_wait = 2
    insert_wait = 2

tag(): user.pages
tag(): user.zoom


# FIXME(bookmarks): This should be it's own tag type
bookmark: ":bmark "
bookmark delete: ":bdelete "
bookmark list:
    insert(":")
    sleep(50ms)
    insert("blist \n")

# FIXME(zathura): These should be navigation?
half: key(ctrl-d)
half up: key(ctrl-u)
jump back: key(ctrl-o)
jump next: key(ctrl-i)
search: "/"


# FIXME(marks): This should be it's own tag type (different from bookmark)
mark set <number>: "m{number}"
mark set <user.letter>: "m{user.letter}"
mark <number>: "'{number}"
mark <user.letter>: "'{user.letter}"
