# Its note that this is not actual EMACS itself, but refers to the default
# command line editing mode enabled in most common linux shells like bash, zsh,
# is also used by lots of command line tools/interfaces, for example gdb
# command line interface.
#
# It more information about the commands can be found here:
# https://www.gnu.org/software/bash/manual/html_node/Command-Line-Editing.html
#
# The idea is that certain shell tools can assert the tag to ensure that the
# generic talon line editing commands will still work. Is also allows for
# things like zsh being configured in vi mode, but then using gdb with the more
# traditional emacs-style keyboard shortcuts
tag: user.readline
-

# readline.py should parse the key bindings in the currentl terminal and then automatically update the action

clear screen: key(ctrl-l)
line search: key(ctrl-r)
found it: key(ctrl-J)
punch it: key(ctrl-J enter)
abort: key(ctrl-g)

# FIXME(cursorless-neovim): This should eventually something we can use cursorless for on the cmdline
chuck word: user.delete_word_right()
chuck back: user.delete_word_left()
chuck line: edit.delete_line()
