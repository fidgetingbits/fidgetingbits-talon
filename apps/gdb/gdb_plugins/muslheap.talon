tag: user.muslheap
-

tag(): user.heap_analysis

chunk info: "mchunkinfo "
find slot: "mfindslot "
magic: "mmagic\n"
heap info: "mheapinfo\n"

muscle debug path: "target:/usr/lib/debug/lib/ld-musl-x86_64.so.1.debug"
print meta: "p/x *(struct meta *)"
print meta {user.registers}:
    "i r ${registers}\n"
    "p/x *(struct meta *)${registers}\n"

print malloc context:
    "p/x &__malloc_context\n"
    "p/x __malloc_context\n"
