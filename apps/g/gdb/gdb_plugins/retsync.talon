tag: user.retsync
-

sink help: "synchelp\n"
sink on: "sync\n"
sink off: "syncoff\n"

sink symbol: "rln "
sink symbol clip:
    insert("rln ")
    edit.paste()
    key(enter)

sink comment: "cmt "
sink patch: "patch "
# beauty trace: "idb init\nbbt\n"
beauty trace: "bbt\n"
lookup symbol: "bx "
continue a cursor: "cc\n"

sink [I] D B list: "idblist\n"
sink (mod | module) list: "modlist\n"
sink (mod | module) info: "curmod\n"
