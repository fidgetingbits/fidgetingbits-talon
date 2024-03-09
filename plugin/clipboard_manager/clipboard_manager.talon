tag: user.clipboard_manager
-

clippy:                     user.clipboard_manager_toggle()
clippy hide: user.clipboard_manager_hide()

paste <number_small> [and <number_small>]*:
    user.clipboard_manager_paste(number_small_list)
# FIXME: I don't handle oridnals yet?
paste <user.ordinals_small> [and <user.ordinals_small>]*:
    user.clipboard_manager_paste(ordinals_small_list)

paste special <number_small> [and <number_small>]*:
    user.clipboard_manager_paste(number_small_list, 1)
paste special <user.ordinals_small> [and <user.ordinals_small>]*:
    user.clipboard_manager_paste(ordinals_small_list, 1)

clippy remove <number_small> [and <number_small>]*:
    user.clipboard_manager_remove(number_small_list)
