tag: user.clipboard_manager
-

clippy:      user.clipboard_manager_toggle()
clippy hide: user.clipboard_manager_hide()

(clippy bring|paste) <number_small> [and <number_small>]*:
    user.clipboard_manager_paste(number_small_list)
# FIXME: I don't handle oridnals yet?
(clippy bring|paste)  <user.ordinals_small> [and <user.ordinals_small>]*:
    user.clipboard_manager_paste(ordinals_small_list)
(clippy bring|paste)  <number_small> [and <number_small>]*:
    user.clipboard_manager_paste(number_small_list, 1)
(clippy bring|paste) <user.ordinals_small> [and <user.ordinals_small>]*:
    user.clipboard_manager_paste(ordinals_small_list, 1)

# FIXME: What is the point of this?
clippy copy <number_small> [and <number_small>]*:
    user.clipboard_manager_copy(number_small_list)

clippy chuck <number_small> [and <number_small>]*:
    user.clipboard_manager_remove(number_small_list)

clippy enable:
    user.clipboard_manager_enable()

clippy disable:
    user.clipboard_manager_disable()

# Purposefully a bit harder to say, as it deletes all entries
clippy flush all:
    user.clipboard_manager_clear_all()
