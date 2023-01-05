app: vim
and tag: user.markdown
-

# XXX - These needs to detect the current working directory in vim, so should
# just call of macro instead
# It would be nice if this was even more specific, but probably need to move it
# to vim to detect if I have build_sides.sh in the current folder
build slides: user.system_command_nb("./build_slides.sh\n")
build slides preview: user.system_command_nb("./build_slides.sh preview\n")
