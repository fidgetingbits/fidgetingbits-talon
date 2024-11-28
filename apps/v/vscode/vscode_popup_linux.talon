app: vscode
and win.title: /Visual Studio Code/
and os: linux
-
# TODO: We should be able to use a screen reader to query the contents of the
# window and determine that it's actually the specific popup

# This is indicative of a pop up window, which in my case is most commonly the
# do you want to save dialogue, which has some specific keyboard shortcuts
save: key("alt-s")
don't save: key("alt-n")
cancel: key("alt-c")
