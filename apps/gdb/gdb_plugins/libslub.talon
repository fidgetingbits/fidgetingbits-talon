tag: user.libslab
-

# libslab
slab help: "sbhelp\n"

# sbcache
slab cache help: "sbcache -h\n"
slab cache {user.slabs}: "sbcache -n {slabs} -M tag\n"

# sbinfo
slab info: "sbinfo\n"
slab info help: "sbinfo -h\n"

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

# sbslabdb
slab (D B|database) help: "sbslabdb -h\n"
