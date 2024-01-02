os: mac
and tag: terminal
-
tag(): user.service_manager
tag(): user.launchctl
tag(): user.tracing_dtruss

host name set: "scutil --set HostName "
restart launch services:
    "sudo /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -kill -r -domain local -domain system -domain user\n"

(folder yank path | folder path copy | folder copy | folder yank):
    "pwd | tr -d \\\\n\\\\r | pbcopy\n"

file list user temp:
    "ls $(getconf DARWIN_USER_TEMP_DIR)\n"

echo user temp:
    "echo $(getconf DARWIN_USER_TEMP_DIR)\n"

log show:
    "sudo log show\n"

# show the logs from today
log show service {user.service_names} events:
     'sudo log show --predicate \'eventMessage contains "{service_names}"\' --info --start "$(date -u \"+%Y-%m-%d 00:00:00\")"\n'
