os: mac
and tag: terminal
-
tag(): user.service_manager
tag(): user.launchctl
tag(): user.tracing_dtruss

file open: "open "

host name set: "scutil --set HostName "
restart launch services:
    "sudo /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -kill -r -domain local -domain system -domain user\n"

(folder yank path | folder path copy | folder copy | folder yank):
    "pwd | tr -d \\\\n\\\\r | pbcopy\n"

file list user temp:
    "ls $(getconf DARWIN_USER_TEMP_DIR)\n"

echo user temp:
    "echo $(getconf DARWIN_USER_TEMP_DIR)\n"

# FIXME: This should move to log_manager
log show:
    "sudo log show\n"

log show help:
    "sudo log show --help\n"

log help:
    "sudo log --help\n"

log watch:
    "sudo log stream\n"

# These assume MacOS date, but it doesn't work for GNU date used by nix-darwin
# log show last hour:
#     "sudo log show --info --start \"$(date -u \"+%Y-%m-%d %H:%M:%S\" -v -1H)\"\n"
# log show last minute:
#     "sudo log show --info --start \"$(date -u \"+%Y-%m-%d %H:%M:%S\" -v -1M)\"\n"
# GNU version
log show last hour:
    "sudo log show --info --start \"$(date -u \"+%Y-%m-%d %H:%M:%S\" -d \"1 hour ago\")\"\n"
log show last minute:
    "sudo log show --info --start \"$(date -u \"+%Y-%m-%d %H:%M:%S\" -d \"1 minute ago\")\"\n"

log show today:
    "sudo log show --info --start \"$(date -u \"+%Y-%m-%d 00:00:00\")\"\n"
log show service events:
    user.insert_between("sudo log show --predicate 'eventMessage contains \"", "}\"' --info --start \"$(date -u \"+%Y-%m-%d 00:00:00\")\"\n")
log show service {user.service_names} events:
     'sudo log show --predicate \'eventMessage contains "{service_names}"\' --info --start "$(date -u \"+%Y-%m-%d 00:00:00\")"\n'

U S B list:
    "system_profiler SPUSBDataType\n"

launch log monitor:
    "open -a Console.app\n"

# NOTE: MacOS sed requires a `-i ''` prefix, which differs from GNU sed
file swap in place: user.insert_between("sed -i '' -i 's/", "/g' ")
