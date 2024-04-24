-
settings():
    ###
    # GUI
    ###
    # Adjust the scale of the imgui to my liking
    imgui.dark_mode = 1

    # Enable if you'd like the picker gui to automatically appear when explorer has focus
    user.file_manager_auto_show_pickers = 0

    # Set the max numbcer of command lines per page in help
    user.help_max_command_lines_per_page = 50

    # Set the max number of contexts display per page in help
    user.help_max_contexts_per_page = 40

    # where to save screen shots
    user.screenshot_folder = "~/images/screenshots/"

    # where to save replayed recordings for talon debugging
    user.saved_replay_recordings_directory = "~/talon/documents/conformer_problem_recordings/"

    ###
    # SPEECH
    ###

    # the default is now 300ms
    speech.timeout = 0.300
    speech.record_all = 1
    #speech.gain = 100
    speech.normalize = 1

    # Adjust how sensitive picking up commands are.
    # XXX what is the default?
    speech.threshold = 0.1

    ###
    # HISTORY
    ###

    # The number of lines of command history to display by default
    user.command_history_display = 3

    # The number of lines of command history to keep in total;
    # "command history more" to display all of them, "command history less" to restore
    user.command_history_size = 20

    # Automatically show the history size on talon startup
    user.command_history_auto = 1

    # Automatically show more history size
    user.command_history_auto_more = 1
    user.command_history_sticky = 1

    ###
    # KEYS
    ###

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

    ###
    # MOUSE
    ###

    # always turn on the mouse when we start talon
    user.mouse_enable_on_startup = 1

    # enables zoom mouse by default
    user.mouse_control_mouse_zoom = 0

    user.mouse_control_mouse = 1

    #stop continuous scroll/gaze scroll with a pop
    user.mouse_enable_pop_stops_scroll = 1

    # Enable pop click with 'control mouse' mode.
    # 0 = off
    # 1 = on with eyetracker but not zoom mouse mode
    # 2 = on but not with zoom mouse mode
    user.mouse_enable_pop_click = 1

    #hide cursor when mouse_wake is useful when using zoom mouse
    user.mouse_wake_hides_cursor = 0

    user.mouse_enable_zoom_auto_click = 0

    user.mouse_zoom_auto_click_timeout = 1.2

    # eye detection suspend settings
    #user.mouse_sleep_tracker_timeout_frames = 200
    #user.mouse_sleep_tracker_suspend_screen = 1
    #user.mouse_sleep_tracker_enter_sleep_mode = 1

    # When enabled, the 'Scroll Mouse' GUI will not be shown.
    user.mouse_hide_mouse_gui = 0

    # The default amount used when scrolling continuously
    user.mouse_continuous_scroll_amount = 80

    # The amount to scroll up/down (equivalent to mouse wheel on Windows by default)
    user.mouse_wheel_down_amount = 120

    ###
    # MOUSE GRID
    ###
    # gray
    user.full_mouse_grid_large_number_color = "CCCCCC"
    # white
    user.full_mouse_grid_small_letters_color = "FFFFFF"
    user.full_mouse_grid_superblock_background_color = "FF55FF"
    user.full_mouse_grid_superblock_stroke_color = "FFFFFF"
    user.full_mouse_grid_background_transparency = 30
    user.full_mouse_grid_label_transparency = 50
    user.full_mouse_grid_selector_transparency = 50
    user.full_mouse_grid_click_type_default = "drag"

    ###
    # DEBUGGER
    ###
    user.debug_default_architecture = "x64"
    user.debug_default_hexdump_count = 256

    ###
    # C
    ###
    user.use_stdint_datatypes = 1

    ###
    # Draft Editor
    ###
    user.draft_editor = "Code"
    # The number of lines of command history to keep in total;
    # "command history more" to display all of them, "command history less" to restore
    user.command_history_size = 50

    # Uncomment the below to insert text longer than 10 characters (customizable) by
    # pasting from the clipboard. This is often faster than typing.
    #user.paste_to_insert_threshold = 10

    # Uncomment the below to enable context-sensitive dictation. This determines
    # how to format (capitalize, space) dictation-mode speech by selecting &
    # copying surrounding text before inserting. This can be slow and may not
    # work in some applications. You may wish to enable this on a
    # per-application basis.
    # user.context_sensitive_dictation = 1

    # How to resize windows moved across physical screens (eg. via `snap next`).
    # Default is 'proportional', which preserves window size : screen size ratio.
    # 'size aware' keeps absolute window size the same, except full-height or
    # -width windows are resized to stay full-height/width.
    #user.window_snap_screen = "size aware"

    user.cursorless_settings_directory = "./fidgetingbits-talon/settings/cursorless-settings"
    # More explicit filename prefix for vscode, to improve accuracy of title matching
    user.vscode_title_filename_prefix = "filename:"

    # Uncomment the below line to add a directory (relative to the Talon user dir) with additional .snippet files
    # Changing this setting requires a restart of Talon
    # user.snippets_dir = "snippets"

    # My zsh-based auto completion stuff
    user.zsh_auto_completion = false
    user.justfile_auto_completion = false
    user.git_auto_completion = false
    user.package_manager_pinning = true
    # Doesn't work yet because it's needed to work outside of zsh as well
    user.path_manager_pinning = false

# uncomment tag to enable mouse grid
# tag(): user.mouse_grid_enabled

tag(): user.noise_quick_actions
tag(): user.record_replay

# Uncomment this to enable the curse yes/curse no commands (show hide mouse cursor). See issue #688.
tag(): user.mouse_cursor_commands_enable
#tag(): user.full_mouse_grid_enabled
#tag(): user.mouse_guide_enabled
#tag(): user.mouse_grid_enabled
tag(): user.shotbox_enabled
