#app: windbg_preview
mode: user.windbg
-

toggle just in time debugging:
    key(alt-f)
    sleep(500ms)
    key(s)
    sleep(200ms)
    key(tab)
    # hit home because it's smart and saves the last setting location
    key(home)
    key(down:3)
    key(tab)
    key(down:4)
    # this delay is so you can see what the old setting was...
    sleep(1s)
    key(enter)
    sleep(500ms)
    key(tab:2)
    key(enter)
    sleep(200ms)
    key(alt-f4)
    sleep(500ms)
    key(escape)
