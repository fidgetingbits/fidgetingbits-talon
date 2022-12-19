# a lot of this will have come from: https://stellaris.paradoxwikis.com/Hotkeys
app: stellaris
-
settings():
    user.stellaris_screen_resolution = "2560x1440"

# Loading screen
new game: key(n)
multiplayer: key(m)
load game: key(l)
show credits: key(c)
settings: key(s)
exit game: key(e)

###
# Main game window
###
pause: key(space)
close: key(escape)
# place the mouse on a benign location with no popups
(newt|neutral): user.stellaris_hover("neutral")
# next star
next: key(tab)
# previous star
last: key(shift-tab)
# go to home system
home: key(backspace)
help: key(alt-b)
focus: key(q)
# open galaxy map
map: key(e)
search: key(f)
faster: key(+)
slower: key(-)


# Bottom hot key bar
science: key(3)

# Outline bar
outline:
    user.stellaris_outliner()
# XXX - this will have to all be coordinates

# Top bar
<user.stellaris_topbar>:
    user.stellaris_hover_topbar("{stellaris_topbar}")
<user.stellaris_topbar> market:
    user.stellaris_click_topbar("{stellaris_topbar}")

alert:
    user.stellaris_hover_alert(1)
alert <number_small>:
    user.stellaris_hover_alert(number_small)

open: user.mouse_click(0, 1)
diss: user.mouse_click(1, 1)

###
# Camera
###
pan up: key(up)
pan left: key(left)
pan down: key(down)
pan right: key(right)
reset: key(r)

###
# Mouse
#
# We use more aggressive most shortcuts in game to reduce syllables
###

# single click
sip: user.mouse_click(0, 1)
# right click
rip: user.mouse_click(1, 1)
# double click
dip: user.mouse_click(0, 2)
# triple click
tip: user.mouse_click(0, 3)
track: user.mouse_toggle_control_mouse()
out: user.mouse_scroll_down()
in: user.mouse_scroll_up()
cancel: user.mouse_cancel_zoom_mouse()
show: user.mouse_show_cursor()
hide: user.mouse_hide_cursor()

###
# Left side bar
###
# Contacts
contacts: key(f1)
# Situation log
[situation] log: key(f2)
# Market
market: key(f3)
# Planets and sectors
sector: key(f4)
# Expansion planner
[expansion] planner: key(f5)
# Policies
policy: key(f6)
# Edicts
edict: key(f7)
# Traditions and relics
relic: key(f8)
# Ship designer
ships: key(f9)
# Fleet manager
fleet: key(f10)

###
# Starbase menu
###

# Shipyard
build: key(b)

###
# Numbered bottom bar
#
# NOTE: these are configurable so you need to use some sort of consistent
# default layout
###


###
# Custom stay tracking
###
#reset: user.stellaris_reset_state()
