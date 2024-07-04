# This currently requires using a PR of mine to atuin
tag: user.atuin
win.title: /atuin/
-

# this is to augment "pick <number>", but with the ability to edit
tweak this: key("tab")
tweak <number_small>:
    key("down:{number_small}")
    key("tab")
