# -1 because we are repeating, so the initial command counts as one
repeat <user.ordinals>: core.repeat_command(ordinals - 1)
<user.ordinals_small>: core.repeat_command(ordinals_small - 1)
parrot(palate_click):
    # app.notify("Palate Click")
    core.repeat_command(1)
(repeat that | twice): core.repeat_command(1)
repeat <number_small> times: core.repeat_command(number_small)
