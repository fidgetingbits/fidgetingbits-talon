# select from a list with the keyboard
<user.dropdown>: key(return)

# NOTE: This is zero-indexed purposefully
<user.dropdown> [down] <number_small>:
    key("down:{number_small}")
    sleep(200ms)
    key(return)
<user.dropdown> up <number_small>:
    key("up:{number_small}")
    sleep(200ms)
    key(return)
