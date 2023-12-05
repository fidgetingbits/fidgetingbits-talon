hostname: orby
-
hacker: user.switcher_focus("terminal")

# The following items assume you to have pinned a certain number of tabs to the browser, such that they will always
# remain the same order
focus teams:
    user.switcher_focus("firefox")
    sleep(50ms)
    user.tab_jump(2)
    # user.tab_jump_name("Microsoft Teams")

(focus mail|mailer):
    user.switcher_focus("firefox")
    sleep(50ms)
    user.tab_jump(1)
    #user.tab_jump_name("Outlook")

focus viva:
    user.switcher_focus("firefox")
    sleep(50ms)
    user.tab_jump(3)
    # user.tab_jump_name("Viva")
