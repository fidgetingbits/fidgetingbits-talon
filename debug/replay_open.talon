# grammars that are only set when the picker window is open

mode: user.replay_picker_open
-

[replay] hide: user.replay_picker_hide()
(replay|pick) <number_small>:
    user.replay_picker_hide()
    user.replay_pick(number_small)
replay save <number_small>:
    user.replay_picker_hide()
    user.replay_save(number_small)
replay yank <number_small>:
    user.replay_picker_hide()
    user.replay_copy_name(number_small)
