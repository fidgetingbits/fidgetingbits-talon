tag: user.vim_insert_mode
tag: user.vim_normal_mode
-

# Generally this file won't be used for too much, as most things work okay inside of all
# motion modes. However, there are some things that are only useful in insert and
# normal, for instance the initial selection of a treesitter node, where subsequent
# selections will pivot to using visual mode.

<user.vim_normal_counted_motion_keys>:
    user.vim_any_motion_mode_key("{vim_normal_counted_motion_keys}")
<user.vim_normal_counted_action>:
    user.vim_any_motion_mode("{vim_normal_counted_action}")
<user.vim_normal_counted_actions_keys>:
    user.vim_any_motion_mode_key("{vim_normal_counted_actions_keys}")
<user.vim_counted_motion_command_with_ordinals>:
    user.vim_any_motion_mode("{vim_counted_motion_command_with_ordinals}")

<user.vim_normal_counted_motion_command>:
    user.vim_any_motion_mode("{vim_normal_counted_motion_command}")

# TODO: It would be nicer if we could pull out the key binding or call the actual trees
# it are command itself, but I didn't see it in the key map list in telescope so delaying
# for now
(node select | take node): user.vim_normal_mode_np("gnn")
# NOTE: I'm keeping this separate just as a note that this is to prevent me from
# mistakenly use the visual mode version... but it may be that I just start using this
# all the time
node grow: user.vim_normal_mode_np("gnn")
