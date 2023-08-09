tag: browser
-

# Open in a new tab
click new <user.rango_target>:
  user.rango_command_with_target("openInNewTab", rango_target)
click (stash|hidden) <user.rango_target>:
  user.rango_command_with_target("openInBackgroundTab", rango_target)

hint {user.rango_hint_styles}:
  user.rango_command_without_target("setHintStyle", user.rango_hint_styles)
hint weight {user.rango_hint_weights}:
  user.rango_command_without_target("setHintWeight", user.rango_hint_weights)

half up: user.rango_command_without_target("scrollUpPage", 0.5)
half down: user.rango_command_without_target("scrollDownPage", 0.5)

half left <user.rango_target>:
  user.rango_command_with_target("scrollLeftAtElement", rango_target, 0.5)
half right <user.rango_target>:
  user.rango_command_with_target("scrollRightAtElement", rango_target, 0.5)

parrot(tut):
  user.rango_command_without_target("toggleHints")