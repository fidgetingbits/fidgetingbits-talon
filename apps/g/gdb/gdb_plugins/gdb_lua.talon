app: gdb
-

[print] lua {user.lua_structs}:
    edit.delete_line()
    user.gdb_print_typed_pointer("", lua_structs, false)

[print] lua raw {user.lua_structs}:
    edit.delete_line()
    user.gdb_print_typed_pointer("", lua_structs, true)

[print] lua {user.lua_structs} {user.registers}:
    edit.delete_line()
    register = "${registers}"
    user.gdb_print_typed_pointer(register, lua_structs, false)

[print] lua raw {user.lua_structs} {user.registers}:
    edit.delete_line()
    register = "${registers}"
    user.gdb_print_typed_pointer(register, lua_structs, true)

[print] lua {user.lua_structs} clip:
    edit.delete_line()
    user.gdb_print_typed_pointer(clip.text(), lua_structs, false)
    key(enter)

[print] lua raw {user.lua_structs} clip:
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

lua table array clip:
    insert("p/x (*(Table *) ")
    edit.paste()
    insert(")->array\n")
    insert("p/x (*(Table *) ")
    edit.paste()
    insert(")->sizearray\n")

dump table array clip:
    edit.delete_line()
    insert("p/x ")
    edit.paste()
    key(enter)

    insert("p/x (*(Table *)$$0)->array\n")
    insert("p/x (*(Table *)$$1)->sizearray\n")
    # FIXME: This requires pwndbg for now
    insert("hexdump $$1 $$0\n")
