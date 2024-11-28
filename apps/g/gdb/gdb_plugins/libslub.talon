tag: user.libslub
-

K malloc <number>: "kmalloc-{number}"

slab help: "sbhelp\n"

# sbcache
slab cache help: "sbcache -h\n"
slab [cache] show {user.slabs}: "sbcache -n {slabs} -M tag\n"
slab [cache] show {user.slabs} main free:
    "sbcache --cpu 0 --show-lockless-freeshow --show-freeshow --main-slab -n {slabs}\n"
slab [cache] show {user.slabs} all free:
    "sbcache --cpu 0 --show-lockless-freeshow --show-freeshow -n {slabs}\n"
slab [cache] show {user.slabs} main (objects | chunks):
    "sbcache --cpu 0 --main-slab --show-region -n {slabs}\n"
slab [cache] show {user.slabs} all (objects | chunks):
    "sbcache --cpu 0 --show-region -n {slabs}\n"

# sbobject
slab object: "sbobject "
slab object clip:
    insert("sbobject ")
    edit.paste()
slab object {user.slabs} clip:
    insert("sbobject -n {slabs} ")
    edit.paste()
slab object help: "sbobject -h\n"

# sblist
slab list: "sblist\n"
slab list help: "sblist -h\n"
slab list pattern [<user.text>]:
    insert("sblist -p {user.formatted_text(text or '', 'NOOP')}")
slab list kay only: "sblist -k\n"

# sbprint
slab print help: "sbprint -h\n"

# sbsearch
slab search help: "sbsearch -h\n"

# sbcrosscache
slab cross cache help: "sbcrosscache -h\n"

# sbmeta
slab meta help: "sbmeta -h\n"
slab meta: "sbmeta "
slab meta verbose: "sbmeta -v "
slab meta config: "sbmeta config "
slab meta config help: "sbmeta config -h\n"
slab meta add: "sbmeta add "
slab meta [remove | delete]: "sbmeta del "
slab meta list: "sbmeta list\n"

# sbslabdb
slab (D B | database) help: "sbslabdb -h\n"
