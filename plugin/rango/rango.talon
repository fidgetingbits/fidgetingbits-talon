tag: browser
-

# Note these are additional commands for the Rango extension. The defaults
# are also enabled in rango-talon folder.

settings: user.rango_start_with_direct_clicking = 0

# Open in a new tab
click new <user.rango_target>:
    user.rango_command_with_target("openInNewTab", rango_target)
click (stash | hidden) <user.rango_target>:
    user.rango_command_with_target("openInBackgroundTab", rango_target)

#hint {user.rango_hint_styles}:
#  user.rango_command_without_target("setHintStyle", user.rango_hint_styles)
#hint weight {user.rango_hint_weights}:
#  user.rango_command_without_target("setHintWeight", user.rango_hint_weights)

half up: user.rango_command_without_target("scrollUpPage", 0.5)
half down: user.rango_command_without_target("scrollDownPage", 0.5)

half left <user.rango_target>:
    user.rango_command_with_target("scrollLeftAtElement", rango_target, 0.5)
half right <user.rango_target>:
    user.rango_command_with_target("scrollRightAtElement", rango_target, 0.5)

# parrot(tut):

# Github issue #189
tabby close <user.rango_target>:
    user.rango_command_with_target("activateTab", rango_target)
    user.tab_close_wrapper()
    user.rango_command_without_target("toggleHints")

tabby <user.rango_target>: user.rango_command_with_target("activateTab", rango_target)

confetti: user.rango_command_without_target("toggleHints")
