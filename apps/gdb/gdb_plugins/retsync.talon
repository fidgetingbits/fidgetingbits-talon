tag: user.retsync
-

sync help: "synchelp\n"
sync on: "sync\n"
sync off: "syncoff\n"

sync symbol: "rln "
sync symbol clip:
    insert("rln ")
    edit.paste()
    key(enter)

sync comment: "cmt "
sync patch: "patch "
beauty trace: "idb init\nbbt\n"
# beauty trace: "bbt\n"
lookup symbol: "bx "
continue a cursor: "cc\n"

sync D B list: "idblist\n"
sync (mod|module) list: "modlist\n"
sync (mod|module) info: "curmod\n"
