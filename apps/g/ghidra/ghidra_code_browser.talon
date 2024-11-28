app: ghidra
win.title: /^CodeBrowser/
-

file open: key(ctrl-o)

rename: key(l)
rename <user.text>:
    key(l)
    sleep(50ms)
    insert(text)
    # key(enter)
