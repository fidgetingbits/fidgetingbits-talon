tag: user.vim_fugitive
# NOTE: if you use the git versions of the commands in a terminal
# that's already inside of a git repo, then the terminal versions will override
# these ones
-

# File management
(fugitive|git) add (current|this) file: user.vim_command_mode(':exe ":G add %"\n')
(fugitive|git) add everything: user.vim_command_mode(':exe ":G add -u"\n')
(fugitive|git) blame: user.vim_command_mode(':exe ":Git blame"\n')
(fugitive|git) browse: user.vim_command_mode(':exe ":G Browse"\n')
(fugitive|git) commit: 
    user.vim_command_mode(':exe ":G commit"\n')
    user.vim_set_insert_mode()
(fugitive|git) (delete|remove): user.vim_command_mode(":GDelete")

# Diffing
(fugitive|git) diff staged: user.vim_command_mode(':exe ":G! diff --staged"\n')
(fugitive|git) diff: user.vim_command_mode(':exe ":Gdiffsplit"\n')
(fugitive|git) [(vertical|pillar)] split diff:
    user.vim_command_mode(':exe ":Gvdiffsplit!"\n')
(fugitive|git) [(vertical|pillar)] diff split: 
    user.vim_command_mode(':exe ":Gvdiffsplit!"\n')
(fugitive|git) (horizontal|river) diff: user.vim_command_mode(':exe ":Gdiffsplit!"\n')
(fugitive|git) diff last: user.vim_command_mode(':exe ":Gdiff !~1"\n')

# Unsorted
(fugitive|git) fetch: user.vim_command_mode(":G fetch ")
(fugitive|git) force write: user.vim_command_mode(":Gwrite!")
(fugitive|git) grep: user.vim_command_mode(":G grep ")
(fugitive|git) log: user.vim_command_mode(':exe ":Gclog"\n')
(fugitive|git) merge: user.vim_command_mode(":G fallmerge")
(fugitive|git) merge tool: user.vim_command_mode(":G mergetool")
(fugitive|git) move: user.vim_command_mode(":G Move ")
(fugitive|git) pull: user.vim_command_mode(":G pull ")
(fugitive|git) push: user.vim_command_mode(":G push ")
(fugitive|git) remove: user.vim_command_mode(":G Remove ")
(fugitive|git) rename: user.vim_command_mode(":G Rename ")
(fugitive|git) reset (current|reset) file: user.vim_command_mode(':exe ":G reset HEAD %"\n')
(fugitive|git) status: user.vim_command_mode(':exe ":G"\n')
(fugitive|git) write: user.vim_command_mode(":G write")
(fugitive|git) read: user.vim_command_mode(":Gread")

# XXX - they should be somewhere specific to knowing were inside of the
# diff window
# merge conflict resolution
keep (target|left): user.vim_command_mode(':exe ":diffget //2"\n')
keep (merge|right): user.vim_command_mode(':exe ":diffget //3"\n')
diff update: user.vim_command_mode(':exe ":diffupdate"\n')
hunk next: user.vim_normal_mode_keys("] c")
hunk (back|last): user.vim_normal_mode_keys("[ c")

# Merging

# This is a fairly specific set of commands. It assumes that you have ran `:G
# mergetool` and you have one split open up top with the file you're editing, in
# and only the quick list on the bottom.
conflict start:
    user.vim_command_mode(':exe ":G mergetool"\n')
    user.vim_command_mode(':exe ":Gvdiffsplit!"\n')
    # XXX - maybe add a search for the next merge conflict?

# assumes you're already in a gvdiffsplit layout
# XXX - we shouldn't technically need any of these sleeps, so we need to figure
# out why... there must be a bug in my API or something
conflict next:
    # close all tabs
    user.vim_command_mode(':exe ":only"\n')
    # re-open quick list
    user.vim_command_mode(':exe ":cw"\n')
    # go to next quick list entry
    user.vim_command_mode(':exe ":cn"\n')
    # open the next diff
    user.vim_command_mode(':exe ":Gvdiffsplit!"\n')
    # XXX - maybe add a search for the next merge conflict?

