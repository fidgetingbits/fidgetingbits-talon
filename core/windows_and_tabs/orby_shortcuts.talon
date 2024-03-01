hostname: orby
-
hacker: user.switcher_focus_or_launch("wezterm")

# The following items assume you to have pinned a certain number of tabs to the browser, such that they will always
# remain the same order
(need teams|chatty):
    user.switcher_focus_or_launch("firefox")
    sleep(50ms)
    user.tab_jump(2)
    # user.tab_jump_name("Microsoft Teams")

(need mail | mailer):
    user.switcher_focus_or_launch("firefox")
    sleep(50ms)
    user.tab_jump(1)
    #user.tab_jump_name("Outlook")

need viva:
    user.switcher_focus_or_launch("firefox")
    sleep(50ms)
    user.tab_jump(3)
    # user.tab_jump_name("Viva")

(need secrets|secret):
    user.switcher_focus_or_launch("firefox")
    sleep(50ms)
    user.tab_jump(4)

(need slack|slacker):
    user.switcher_focus_or_launch("firefox")
    sleep(50ms)
    user.tab_jump(5)
