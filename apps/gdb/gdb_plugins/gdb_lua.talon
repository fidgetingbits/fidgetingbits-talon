app: gdb
-

# for using https://github.com/xjdrew/lua-gdb

lua table: "p/x *(Table *) "
lua table clip:
    insert("p/x *(Table *) ")
    sleep(0.1)
    edit.paste()
    key(enter)

lua raw table:
    insert("p/rx *(Table *) ")
lua raw table clip:
    insert("p/rx *(Table *) ")
    edit.paste()
    key(enter)

lua value: "p/x *(TValue *) "
lua value clip:
    insert("p/x *(TValue *) ")
    edit.paste()
    key(enter)

lua raw value:
    insert("p/rx *(TValue *) ")
lua raw value clip:
    insert("p/rx *(TValue *) ")
    edit.paste()
    key(enter)

lua string: "p/x *(TString *) "
lua string clip:
    insert("p/x *(TString *) ")
    edit.paste()
    key(enter)

lua raw string:
    insert("p/rx *(TString *) ")
lua raw string clip:
    insert("p/rx *(TString *) ")
    edit.paste()
    key(enter)

lua L closure: "p/x *(LClosure *) "
lua L closure clip:
    insert("p/x *(LClosure *) ")
    edit.paste()

lua L raw closure:
    insert("p/rx *(LClosure *) ")
lua L raw closure clip:
    insert("p/rx *(LClosure *) ")
    edit.paste()
    key(enter)


lua C closure: "p/x *(CClosure *) "
lua C closure clip:
    insert("p/x *(CClosure *) ")
    edit.paste()
    key(enter)

lua C raw closure:
    insert("p/rx *(CClosure *) ")
lua C raw closure clip:
    insert("p/rx *(CClosure *) ")
    edit.paste()
    key(enter)

lua state: "p/x *(lua_State *) "
lua state clip:
    insert("p/x *(lua_State *) ")
    edit.paste()

lua coroutines: "luacoroutines\n"
lua stack: "luastack "
lua trace back: "luatraceback "
lua get local: "luagetlocal "

print type table: "ptype Table\n"

print type value: "ptype TValue\n"
