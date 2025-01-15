app: terminal
-

screen detach:
    key(ctrl-a)
    key(d)

screen list:
    "screen -ls\n"

screen kill all detached:
    "sudo screen -ls | grep Detached | cut -d. -f1 | awk '{{print $1}}' | xargs sudo kill\n"


# FIXME: add lists for baud rates and serial interfaces
screen serial [num <number_small>] (ninety six | fortinet):
    insert("sudo screen /dev/ttyUSB")
    insert(number_small or "0")
    insert(" 9600\n")

screen serial [num <number_small>] eleven:
    insert("sudo screen /dev/ttyUSB")
    insert(number_small or "0")
    insert(" 115200\n")

serial list:
    "ls /dev/ttyUSB*\n"
