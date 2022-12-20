#defines the commands that sleep/wake Talon
mode: command
mode: dictation
-
settings():
    user.sleep_word = "drowse"

drowse: user.talon_sleep()
