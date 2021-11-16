-
# NOTE: Other files also declare settings, see mouse/mouse.talon, etc
settings():
    # Adjust the scale of the imgui to my liking
    imgui.scale = 1.3
    imgui.dark_mode = 1

    # Enable if you'd like the picker gui to automatically appear when explorer has focus
    user.file_manager_auto_show_pickers = 0

    # Set the max number of command lines per page in help
    user.help_max_command_lines_per_page = 50

    # Set the max number of contexts display per page in help
    user.help_max_contexts_per_page = 40


    # where to save screen shots
    user.screenshot_folder = "/home/aa/images/screenshots/"
    # where to save replayed recordings for talon debugging
    user.saved_replay_recordings_directory = "~/talon/documents/conformer_problem_recordings/"
    # the default is now 300ms
    speech.timeout = 0.150
    speech.record_all = 1
    #speech.gain = 100
    speech.normalize = 1

    # Adjust how sensitive picking up commands are.
    # XXX what is the default?
    speech.threshold = 0.1

    # Mouse grid and friends put the number one on the bottom left (vs on the top left)
    user.grids_put_one_bottom_left = 1
    # The number of lines of command history to display by default
    user.command_history_display = 3
    # The number of lines of command history to keep in total;
    # "command history more" to display all of them, "command history less" to restore
    user.command_history_size = 20

    # Uncomment the below to enable context=sensitive dictation. This determines
    # how to format (capitalize, space) dictation=mode speech by selecting &
    # copying surrounding text before inserting. This can be slow and may not
    # work in some applications. You may wish to enable this on a
    # per=application basis.
    # user.context_sensitive_dictation = 1

    # XXX = ?
    key_wait = 1
    # how long to wait between key presses
    insert_wait = 5



# uncomment tag to enable mouse grid
# tag(): user.mouse_grid_enabled

tag(): user.i3wm
tag(): user.noise_quick_actions
tag(): user.record_replay
