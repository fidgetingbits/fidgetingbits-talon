tag: user.vim_fugitive
# NOTE: if you use the git versions of the commands in a terminal
# that's already inside of a git repo, then the terminal versions will override
# these ones
-

(fugitive|git) add (current|this) file: user.vim_command_mode(":G add %\n")
(fugitive|git) add everything: user.vim_command_mode(":G add -u\n")
(fugitive|git) blame: user.vim_command_mode(":Git blame\n")
(fugitive|git) browse: user.vim_command_mode(":G Browse\n")
(fugitive|git) commit: 
    user.vim_command_mode(":G commit\n")
    user.vim_set_insert_mode()
(fugitive|git) (delete|remove): user.vim_command_mode(":GDelete")
(fugitive|git) diff staged: user.vim_command_mode(":G! diff --staged\n")
(fugitive|git) diff: user.vim_command_mode(":Gdiffsplit\n")
(fugitive|git) vertical diff: user.vim_command_mode(":Gvdiffsplit!\n")
(fugitive|git) diff last: user.vim_command_mode(":Gdiff !~1\n")
(fugitive|git) fetch: user.vim_command_mode(":G fetch ")
(fugitive|git) force write: user.vim_command_mode(":Gwrite!")
(fugitive|git) grep: user.vim_command_mode(":G grep ")
(fugitive|git) log: user.vim_command_mode(":Gclog\n")
(fugitive|git) merge: user.vim_command_mode(":G fallmerge")
(fugitive|git) merge tool: user.vim_command_mode(":G mergetool")
(fugitive|git) move: user.vim_command_mode(":G Move ")
(fugitive|git) pull: user.vim_command_mode(":G pull ")
(fugitive|git) push: user.vim_command_mode(":G push ")
(fugitive|git) remove: user.vim_command_mode(":G Remove ")
(fugitive|git) rename: user.vim_command_mode(":G Rename ")
(fugitive|git) reset (current|reset) file: user.vim_command_mode(":G reset HEAD %\n")
(fugitive|git) split diff: user.vim_command_mode(":Gdiffsplit!")
(fugitive|git) status: user.vim_command_mode(":G\n")
(fugitive|git) write: user.vim_command_mode(":G write")
(fugitive|git) read: user.vim_command_mode(":Gread")

# XXX - they should be somewhere specific to knowing were inside of the
# diff window
# merge conflict resolution
keep (target|left): user.vim_command_mode(":diffget //2\n")
keep (merge|right): user.vim_command_mode(":diffget //3\n")
next hunk: user.vim_normal_mode_keys("] c")
last hunk: user.vim_normal_mode_keys("[ c")
