# NOTE: If you want to use i3wm you must enable the tag settings.talon. i.e.: `tag(): user.i3wm`
os: linux
tag: user.i3wm
-

##
# Workspaces
##
portal <number_small>:
    user.bash_command_quiet("i3-msg workspace number {number_small}")
portal flip: user.bash_command_quiet("i3-msg workspace back_and_forth")
portal right: user.bash_command_quiet("i3-msg workspace next")
portal left: user.bash_command_quiet("i3-msg workspace prev")

##
# Windows
##
(win | window) left: user.bash_command_quiet("i3-msg focus left")
(win | window) right: user.bash_command_quiet("i3-msg focus right")
(win | window) (north | up): user.bash_command_quiet("i3-msg focus up")
(win | window) (south | down): user.bash_command_quiet("i3-msg focus down")
(win | window) kill: user.bash_command_quiet("i3-msg kill")
(win | window) (stack | stacking): user.bash_command_quiet("i3-msg layout stacking")
(win | window) default: user.bash_command_quiet("i3-msg layout toggle split")
(win | window) tabbed: user.bash_command_quiet("i3-msg layout tabbed")
(win | window) flip:
    user.bash_command_quiet("/home/aa/scripts/i3/i3-focus-last.py --switch")
(win | window) focus <number_small>:
    user.bash_command_quiet("/home/aa/scripts/i3/i3-nth_window_in_workspace.py $(i3-msg -t get_workspaces | jq -r '.[] | select(.focused==true).name') {number_small-1}")
(win | window) focus parent: user.bash_command_quiet("i3-msg focus parent")
(win | window) focus child: user.bash_command_quiet("i3-msg focus child")

[(win | window)] full screen: user.bash_command_quiet("i3-msg fullscreen")
[(win | window)] floating toggle: user.bash_command_quiet("i3-msg floating toggle")
[(win | window)] floating focus: user.bash_command_quiet("i3-msg focus mode_toggle")
(win | window) center: user.bash_command_quiet("i3-msg move position center")
(win | window) move left: user.bash_command_quiet("i3-msg move left")
(win | window) move <number> left:
    user.bash_command_quiet("i3-msg move left {number} px")
(win | window) move right: user.bash_command_quiet("i3-msg move right")
(win | window) move <number> right:
    user.bash_command_quiet("i3-msg move right {number} px")
(win | window) move up: user.bash_command_quiet("i3-msg move up")
(win | window) move <number> up: user.bash_command_quiet("i3-msg move up {number} px")
(win | window) move down: user.bash_command_quiet("i3-msg move down")
(win | window) move <number> down:
    user.bash_command_quiet("i3-msg move down {number} px")
(win | window) resize: user.bash_command_quiet('i3-msg mode "resize"')
(win | window) horizontal: user.bash_command_quiet("i3-msg split h")
(win | window) vertical: user.bash_command_quiet("i3-msg split v")

(win | window) grow [<number>]: user.i3wm_window_grow(number or 1)
(win | window) shrink [<number>]: user.i3wm_window_shrink(number or 1)
# NOTE: these commands often conflict with split versions, which is why they
# don't have win version
window taller [<number>]: user.i3wm_window_adjust_height_up(number or 50)
window shorter [<number>]: user.i3wm_window_adjust_height_down(number or 50)
window (wider | fatter) [<number>]: user.i3wm_window_adjust_width_out(number or 50)
window (thinner | skinnier) [<number>]: user.i3wm_window_adjust_width_in(number or 50)

horizontal (shell | terminal):
    user.bash_command_quiet("i3-msg split h")
    user.i3wm_shell()

vertical (shell | terminal):
    user.bash_command_quiet("i3-msg split v")
    user.i3wm_shell()

shuffle <number_small>:
    user.bash_command_quiet("i3-msg move container to workspace number {number_small}")
shuffle (parent | all) <number_small>:
    user.bash_command_quiet("i3-msg focus parent")
    user.bash_command_quiet("i3-msg move container to workspace {number_small}")
shuffle flip:
    user.bash_command_quiet("i3-msg move container to workspace back_and_forth")
shuffle left: user.bash_command_quiet("i3-msg move left")
shuffle right: user.bash_command_quiet("i3-msg move right")
shuffle (up | north): user.bash_command_quiet("i3-msg move up")
shuffle (down | south): user.bash_command_quiet("i3-msg move down")

# move a (win|window) to a workspace and follow it there
# NOTE: Moved away from follow due to usage of follow in cursorless that would
# sometimes talon would confuse. Example: follow <target> where a grey hat is on a number
shuffle go <number_small>:
    user.bash_command_quiet("i3-msg move container to workspace {number_small}")
    user.bash_command_quiet("i3-msg workspace {number_small}")

# multi-monitor commands
# NOTE: these are flipped on purpose, because I have to trick the talon monitor
# orientation to ensure that eye tracking works on multiple monitors
shuffle screen left: user.bash_command_quiet("i3-msg move container to output right")
shuffle screen right: user.bash_command_quiet("i3-msg move container to output left")

[(win | window)] unmake scratch: user.bash_command_quiet("i3-msg move scratchpad")
# This should become configurable, since the dimensions are specific to my setup
[(win | window)] make scratch:
    user.bash_command_quiet("i3-msg move scratchpad; i3-msg scratchpad show; i3-msg resize set 2270 2150; i3-msg move position center;")
[(show | hide)] scratch: user.bash_command_quiet("i3-msg scratchpad show")
next scratch:
    user.bash_command_quiet("i3-msg scratchpad show")
    user.bash_command_quiet("i3-msg scratchpad show")

# these rely on the user settings for the mod key. see i3wm.py Actions class
launch: user.i3wm_launch()
launch <user.text>:
    user.i3wm_launch()
    sleep(100ms)
    insert("{text}")
screen lock: user.i3wm_lock()

term me: user.i3wm_shell()
new test term: user.i3wm_testing_shell()

new scratch (shell | window):
    user.i3wm_shell()
    sleep(100ms)
    user.bash_command_quiet("i3-msg move scratchpad")
    user.bash_command_quiet("i3-msg scratchpad show")
    user.i3wm_window_grow(5)

##
# Configuration
##
i three reload: user.bash_command_quiet("i3-msg reload")
i three restart: user.bash_command_quiet("i3-msg restart")

##
# Marks
##
(win | window) mark <user.word>: user.bash_command_quiet("i3-msg mark {word}")
(win | window) clear marks: user.bash_command_quiet("i3-msg unmark")
(win | window) focus [mark] <user.word>:
    user.bash_command_quiet('i3-msg [con_mark="{word}"] focus')
(win | window) focus alert: user.bash_command_quiet("i3-msg [urgent=latest] focus")
(win | window) show marks:
    user.bash_command_quiet_nb("bash -c \"notify-send.sh -- '$(python /home/aa/scripts/i3/i3-print-window-marks.py)'\"")
