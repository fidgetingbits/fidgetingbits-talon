tag: user.muslheap
-

tag(): user.heap_analysis

source muscle heap: "source musl-heap.py"
chunk info: "mchunkinfo "
chunk info clip:
    insert("mchunkinfo ")
    edit.paste()
    key(enter)
find slot: "mfindslot "
fine slot clip:
    insert("mfindslot ")
    edit.paste()
    key(enter)
magic: "mmagic\n"
heap info: "mheapinfo\n"

muscle debug path: "target:/usr/lib/debug/lib/ld-musl-x86_64.so.1.debug"
print meta: "p/x *(struct meta *) "
print meta clip:
    insert("p/x *(struct meta *) ")
    edit.paste()
    key(enter)
print meta {user.registers}:
    "i r ${registers}\n"
    "p/x *(struct meta *) ${registers}\n"

print malloc context:
    "p/x &__malloc_context\n"
    "p/x __malloc_context\n"

# NB: Using mgroup via my own symbol file rather than real struct group,
# due to gdb failing to find it because of duplication
print group:
    "p/x *(struct mgroup *) "
print group clip:
    insert("p/x *(struct mgroup *) ")
    edit.paste()
    key(enter)
