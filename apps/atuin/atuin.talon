tag: user.atuin
-

atuin sync: "atuin sync\n"

# FIXME: This needs to be for when atuin TUI is open only eventually
# this is to augment "pick <number>", but with the ability to edit
tweak <number_small>:
    key("down:{number_small}")
    key("tab")

# FIXME: We should add more like, tweak <number_small> start, to auto pre-line, etc
