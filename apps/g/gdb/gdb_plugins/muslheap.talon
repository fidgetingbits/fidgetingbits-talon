tag: user.muslheap
-

tag(): user.heap_analysis

M map threshold: "0x1ffec"

# FIXME: Might be cleaner to make this all a capture now that it's got 3 ways.
muscle {user.mallocng_structs}:
    edit.delete_line()
    user.gdb_print_typed_pointer("", mallocng_structs, false)

muscle raw {user.mallocng_structs}:
    edit.delete_line()
    user.gdb_print_typed_pointer("", mallocng_structs, true)

muscle {user.mallocng_structs} {user.registers}:
    edit.delete_line()
    register = "${registers}"
    user.gdb_print_typed_pointer(register, mallocng_structs, false)

muscle raw {user.mallocng_structs} {user.registers}:
    edit.delete_line()
    register = "${registers}"
    user.gdb_print_typed_pointer(register, mallocng_structs, true)


muscle {user.mallocng_structs} clip:
    edit.delete_line()
    user.gdb_print_typed_pointer(clip.text(), mallocng_structs, false)
    key(enter)

muscle raw {user.mallocng_structs} clip:
    edit.delete_line()
    user.gdb_print_typed_pointer(clip.text(), mallocng_structs, true)
    key(enter)

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


print malloc context:
    "p/x &__malloc_context\n"
    "p/x __malloc_context\n"
