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
beauty trace: "bbt\n"
lookup symbol: "bx "
continue a cursor: "cc\n"
