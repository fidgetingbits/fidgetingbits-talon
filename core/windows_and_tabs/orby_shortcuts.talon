hostname: orby
-
hacker: user.switcher_focus("terminal")

focus teams:
    user.switcher_focus("firefox")
    sleep(50ms)
    user.tab_jump(2)
    # user.tab_jump_name("Microsoft Teams")

mailer:
    user.switcher_focus("firefox")
    sleep(50ms)
    user.tab_jump(1)
    #user.tab_jump_name("Outlook")

focus viva:
    user.switcher_focus("firefox")
    sleep(50ms)
    user.tab_jump(3)
    # user.tab_jump_name("Viva")
