# NOTE: If you want to use i3wm you must enable the tag settings.talon. i.e.: `tag(): user.i3wm`
os: linux
tag: user.i3wm
-

##
# Workspaces
##
portal <number_small>: user.system_command("i3-msg workspace number {number_small}")
portal flip: user.system_command("i3-msg workspace back_and_forth")
portal right: user.system_command("i3-msg workspace next")
portal left: user.system_command("i3-msg workspace prev")

##
# Windows
##
(win | window) left: user.system_command("i3-msg focus left")
(win | window) right: user.system_command("i3-msg focus right")
(win | window) up: user.system_command("i3-msg focus up")
(win | window) down: user.system_command("i3-msg focus down")
(win | window) kill: user.system_command("i3-msg kill")
(win | window) (stack|stacking): user.system_command("i3-msg layout stacking")
(win | window) default: user.system_command("i3-msg layout toggle split")
(win | window) tabbed: user.system_command("i3-msg layout tabbed")
(win | window) flip:
    user.system_command("/home/aa/scripts/i3/i3-focus-last.py --switch")
(win | window) focus <number_small>:
    user.system_command("/home/aa/scripts/i3/i3-nth_window_in_workspace.py $(i3-msg -t get_workspaces | jq -r '.[] | select(.focused==true).name') {number_small-1}")
(win | window) focus parent: user.system_command("i3-msg focus parent")
(win | window) focus child: user.system_command("i3-msg focus child")

[(win | window)] full screen: user.system_command("i3-msg fullscreen")
[(win | window)] floating toggle: user.system_command("i3-msg floating toggle")
[(win | window)] floating focus:
    user.system_command("i3-msg focus mode_toggle")
(win | window) center: user.system_command("i3-msg move position center")
(win | window) move left: user.system_command("i3-msg move left")
(win | window) move <number> left:
    user.system_command("i3-msg move left {number} px")
(win | window) move right: user.system_command("i3-msg move right")
(win | window) move <number> right:
    user.system_command("i3-msg move right {number} px")
(win | window) move up: user.system_command("i3-msg move up")
(win | window) move <number> up:
    user.system_command("i3-msg move up {number} px")
(win | window) move down: user.system_command("i3-msg move down")
(win | window) move <number> down:
    user.system_command("i3-msg move down {number} px")
(win | window) resize: user.system_command('i3-msg mode "resize"')
(win | window) horizontal: user.system_command("i3-msg split h")
(win | window) vertical: user.system_command("i3-msg split v")

(win | window) [<number>] grow: user.i3wm_window_grow(number or 1)
(win | window) [<number>] shrink: user.i3wm_window_shrink(number or 1)
# NOTE: these commands often conflict with split versions, which is why they
# don't have win version
window [<number>] taller: user.i3wm_window_adjust_height_up(number or 50)
window [<number>] shorter: user.i3wm_window_adjust_height_down(number or 50)
window [<number>] (wider|fatter): user.i3wm_window_adjust_width_out(number or 50)
window [<number>] (thinner|skinnier): user.i3wm_window_adjust_width_in(number or 50)

horizontal (shell | terminal):
    user.system_command("i3-msg split h")
    user.i3wm_shell()

vertical (shell | terminal):
    user.system_command("i3-msg split v")
    user.i3wm_shell()

shuffle <number_small>:
    user.system_command("i3-msg move container to workspace number {number_small}")
shuffle (parent | all) <number_small>:
    user.system_command("i3-msg focus parent")
    user.system_command("i3-msg move container to workspace {number_small}")
shuffle flip:
    user.system_command("i3-msg move container to workspace back_and_forth")
shuffle left: user.system_command("i3-msg move left")
shuffle right: user.system_command("i3-msg move right")
shuffle up: user.system_command("i3-msg move up")
shuffle down: user.system_command("i3-msg move down")

# move a (win|window) to a workspace and follow it there
follow <number_small>:
    user.system_command("i3-msg move container to workspace {number_small}")
    user.system_command("i3-msg workspace {number_small}")

# multi-monitor commands
# NOTE: these are flipped on purpose, because I have to trick the talon monitor
# orientation to ensure that eye tracking works on multiple monitors
shuffle screen left:
    user.system_command("i3-msg move container to output right")
shuffle screen right:
    user.system_command("i3-msg move container to output left")

[(win | window)] make scratch: user.system_command("i3-msg move scratchpad")
[(show | hide)] scratch: user.system_command("i3-msg scratchpad show")
next scratch:
    user.system_command("i3-msg scratchpad show")
    user.system_command("i3-msg scratchpad show")

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
    user.system_command("i3-msg move scratchpad")
    user.system_command("i3-msg scratchpad show")
    user.i3wm_window_grow(5)

##
# Configuration
##
i three reload: user.system_command("i3-msg reload")
i three restart: user.system_command("i3-msg restart")

##
# Marks
##
(win | window) mark <user.word>: user.system_command("i3-msg mark {word}")
(win | window) clear marks: user.system_command("i3-msg unmark")
(win | window) focus [mark] <user.word>:
    user.system_command('i3-msg [con_mark="{word}"] focus')
(win | window) focus alert: user.system_command("i3-msg [urgent=latest] focus")
(win | window) show marks:
    user.system_command_nb("bash -c \"notify-send.sh -- '$(python /home/aa/scripts/i3/i3-print-window-marks.py)'\"")
