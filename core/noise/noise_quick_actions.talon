tag: user.noise_quick_actions
-

quack on: user.pop_quick_action_set()
quack flip: user.pop_quick_action_set_last()
quack off: user.pop_quick_action_clear()

# TODO: hiss doesn't really work at the moment
[quick] action set hiss: user.hiss_quick_action_set()
[quick] action flip hiss: user.hiss_quick_action_set_last()
[quick] action clear hiss: user.hiss_quick_action_clear()
