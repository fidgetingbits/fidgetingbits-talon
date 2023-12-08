os: mac
and mode: command
and tag: terminal
-

host name set: "scutil --set HostName "
restart launch services:
    "sudo /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -kill -r -domain local -domain system -domain user\n"

(folder yank path | folder path copy | folder copy | folder yank):
    "pwd | tr -d \\\\n\\\\r | pbcopy\n"

file list user temp:
    "ls $(getconf DARWIN_USER_TEMP_DIR)\n"
