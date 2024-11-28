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

# FIXME: The following could all be abstracted with python list
# Ideally we want the last for serial attach commands to only work when we're actually on ooze
serial remote attach fang:
    "ssh ooze\n"
    # wait long enough for yubikey press
    sleep(2)
    "sudo screen /dev/ttyUSB0 9600\n"
serial remote attach flux:
    "ssh ooze\n"
    # wait long enough for yubikey press
    sleep(2)
    "sudo screen /dev/ttyUSB1 9600\n"
serial remote attach frog:
    "ssh ooze\n"
    # wait long enough for yubikey press
    sleep(2)
    "sudo screen /dev/ttyUSB2 9600\n"
serial remote attach furby:
    "ssh ooze\n"
    # wait long enough for yubikey press
    sleep(2)
    "sudo screen /dev/ttyUSB3 9600\n"

serial attach fang:
    "sudo screen /dev/ttyUSB0 9600\n"
serial attach flux:
    "sudo screen /dev/ttyUSB1 9600\n"
serial attach frog:
    "sudo screen /dev/ttyUSB2 9600\n"
serial attach furby:
    "sudo screen /dev/ttyUSB3 9600\n"
