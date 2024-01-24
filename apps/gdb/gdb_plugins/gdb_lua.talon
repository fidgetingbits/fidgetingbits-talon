tag: user.gdb
-

# for using https://github.com/xjdrew/lua-gdb

lua table: "p/x *(Table *)"
lua table clip:
    insert("p/x *(Table *)")
    edit.paste()

lua raw table:
    insert("disable pretty-printer")
    insert("p/x *(Table *)")
lua raw table clipboard:
    insert("disable pretty-printer")
    insert("p/x *(Table *)")
    edit.paste()
    key(enter)
    insert("enable pretty-printer")

lua value: "p/x *(TValue *)"
lua value clip:
    insert("p/x *(TValue *)")
    edit.paste()
    key(enter)

lua raw value:
    insert("disable pretty-printer")
    insert("p/x *(TValue *)")
lua raw value clip:
    insert("disable pretty-printer")
    insert("p/x *(TValue *)")
    edit.paste()
    key(enter)
    insert("enable pretty-printer")

lua string: "p/x *(TString *)"
lua string clip:
    insert("p/x *(TString *)")
    edit.paste()
    key(enter)

lua raw string:
    insert("disable pretty-printer")
    insert("p/x *(TString *)")
lua raw string clip:
    insert("disable pretty-printer")
    insert("p/x *(TString *)")
    edit.paste()
    key(enter)
    insert("enable pretty-printer")

lua L closure: "p/x *(LClosure *)"
lua L closure clip:
    insert("p/x *(LClosure *)")
    edit.paste()

lua L raw closure:
    insert("disable pretty-printer")
    insert("p/x *(LClosure *)")
lua L raw closure clip:
    insert("disable pretty-printer")
    insert("p/x *(LClosure *)")
    edit.paste()
    key(enter)
    insert("enable pretty-printer")


lua C closure: "p/x *(CClosure *)"
lua C closure clip:
    insert("p/x *(CClosure *)")
    edit.paste()
    key(enter)

lua C raw closure:
    insert("disable pretty-printer")
    insert("p/x *(CClosure *)")
lua C raw closure clip:
    insert("disable pretty-printer")
    insert("p/x *(CClosure *)")
    edit.paste()
    key(enter)
    insert("enable pretty-printer")

lua state: "p/x *(lua_State *)"
lua state clip:
    insert("p/x *(lua_State *)")
    edit.paste()

lua coroutines: "luacoroutines\n"
lua stack: "luastack "
lua trace back: "luatraceback "
lua get local: "luagetlocal "
