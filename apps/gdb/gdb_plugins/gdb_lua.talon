app: gdb
-

lua {user.lua_structs}:
    edit.delete_line()
    user.gdb_print_typed_pointer("", lua_structs, false)

lua raw {user.lua_structs}:
    edit.delete_line()
    user.gdb_print_typed_pointer("", lua_structs, true)

lua {user.lua_structs} {user.registers}:
    edit.delete_line()
    register = "${registers}"
    user.gdb_print_typed_pointer(register, lua_structs, false)

lua raw {user.lua_structs} {user.registers}:
    edit.delete_line()
    register = "${registers}"
    user.gdb_print_typed_pointer(register, lua_structs, true)

lua {user.lua_structs} clip:
    edit.delete_line()
    user.gdb_print_typed_pointer(clip.text(), lua_structs, false)
    key(enter)

lua raw {user.lua_structs} clip:
    edit.delete_line()
    user.gdb_print_typed_pointer(clip.text(), lua_structs, true)
    key(enter)
print type {user.lua_structs}:
    edit.delete_line()
    "ptype {lua_structs}\n"

# Specific to https://github.com/xjdrew/lua-gdb
lua coroutines: "luacoroutines\n"
lua stack: "luastack "
lua trace back: "luatraceback "
lua get local: "luagetlocal "

dump table array clip:
    edit.delete_line()
    insert(f"p/x ")
    edit.paste()
    key(enter)

    insert("p/x (*(Table *)$$0)->array\n")
    insert("p/x (*(Table *)$$1)->sizearray\n")
    # FIXME: This requires pwndbg for now
    insert("hexdump $$1 $$0\n")
