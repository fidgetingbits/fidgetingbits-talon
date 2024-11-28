tag: user.launchctl
-

service load help: "launchctl load -h\n"
# -w auto enables onload
service load: "launchctl load -w "
service bootstrap:
    "sudo launchctl bootstrap "
service load clip:
    insert("launchctl load -w ")
    edit.paste()
    key(enter)
service unload: "launchctl unload "
service unload clip:
    insert("launchctl load -w ")
    edit.paste()
    key(enter)
service boot out: "sudo launchctl bootout "
