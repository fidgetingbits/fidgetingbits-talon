-
settings():
    # if set and a list has more than one entry autos select the specified one
    # otherwise will use a gui selector by default
    user.personal_info_auto_select = 0
show my <user.personal_info>: user.personal_info(personal_info)
show my full name:
    user.personal_info("first-name")
    key(space)
    user.personal_info("last-name")
show my talon version: user.print_talon_version()

show my <user.ordinals> <user.personal_info>:
    user.personal_info_by_id(personal_info, ordinals)
