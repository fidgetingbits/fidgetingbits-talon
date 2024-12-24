app: vscode
-
tag(): user.find_and_replace
tag(): user.line_commands
tag(): user.multiple_cursors
tag(): user.splits
tag(): user.tabs
tag(): user.plugins

settings():
    key_wait = 2

# Useful references:
# maciejklimek: https://github.com/maciejklimek/knausj_talon/blob/b09e3331/apps/vscode/vscode.talon
# pokey:
# andreas:

window reload: user.vscode("workbench.action.reloadWindow")
window close: user.vscode("workbench.action.closeWindow")
#multiple_cursor.py support end

please [<user.text>]:
    user.vscode("workbench.action.showCommands")
    insert(user.text or "")

go view [<user.text>]:
    user.vscode("workbench.action.openView")
    insert(user.text or "")

# Sidebar
#
bar (files | explore): user.vscode("workbench.view.explorer")
bar extensions: user.vscode("workbench.view.extensions")
bar outline: user.vscode("outline.focus")
bar run: user.vscode("workbench.view.debug")
bar search: user.vscode("workbench.view.search")
bar source: user.vscode("workbench.view.scm")
bar test: user.vscode("workbench.view.testing.focus")
bar switch: user.vscode("workbench.action.toggleSidebarVisibility")
bar [focus] tabs: user.vscode("andreas.tabs.focus")
bar terminal: user.vscode("workbench.action.terminal.focus")
bar cursorless: user.vscode("workbench.view.extension.cursorless")
bar chat: user.vscode("workbench.panel.chat.view.copilot.focus")
(left | side) dog: user.vscode("workbench.action.toggleSidebarVisibility")
# Toggle Secondary Side Bar
# right dog: key(ctrl-alt-b)

# NOTE: If you're in the code panel, The highlight order is as follows:
# 1. Bottom bar (repo, branch, etc) - No context switch: Name starts west vscode.talon
# 2. Side bar view selector (file view, search, cursorless) - Name starts with ● vscode.talon
# 3. Side bar item (interact with currently viewed side bar contents) - Name contains focused view name
# FIXME: It would be nice to have commands tied to the current view
bar next: user.vscode("workbench.action.focusNextPart")
bar last: user.vscode("workbench.action.focusPreviousPart")

view wider: user.vscode("workbench.action.increaseViewSize")
view thinner: user.vscode("workbench.action.decreaseViewSize")

#
# Splits
#
cross: user.split_next()

#
# Search
#

# Symbol search
hunt symbols [<user.text>]:
    user.vscode("workbench.action.gotoSymbol")
    sleep(50ms)
    insert(text or "")

hunt all symbols [<user.text>]:
    user.vscode("workbench.action.showAllSymbols")
    sleep(50ms)
    insert(text or "")

# If you open the search panel (via hunt code) this allows you to jump between the results
search (first | next): user.vscode("search.action.focusNextSearchResult")
search last: user.vscode("search.action.focusPreviousSearchResult")
search clear: user.vscode("search.action.clearSearchResults")
search editor: user.vscode("search.action.openInEditor")

#
# Panels
#
panel control: user.vscode("workbench.panel.repl.view.focus")
panel output: user.vscode("replaceworkbench.panel.output.focus")
(panel trouble | trouble show): user.vscode("workbench.panel.markers.view.focus")
(low dog | panel switch): user.vscode("workbench.action.togglePanel")
low dog off: user.vscode("workbench.action.closePanel")

(term show | panel terminal): user.vscode("workbench.action.terminal.focus")
(pan edit | editor): user.vscode("workbench.action.focusActiveEditorGroup")

#
# Settings
#
show settings: user.vscode("workbench.action.openGlobalSettings")
show settings json: user.vscode("workbench.action.openSettingsJson")
show settings folder: user.vscode("workbench.action.openFolderSettings")
show settings folder json: user.vscode("workbench.action.openFolderSettingsFile")
show settings workspace: user.vscode("workbench.action.openWorkspaceSettings")
show settings workspace json: user.vscode("workbench.action.openWorkspaceSettingsFile")
show shortcuts: user.vscode("workbench.action.openGlobalKeybindings")
show shortcuts json: user.vscode("workbench.action.openGlobalKeybindingsFile")
show key bindings: user.vscode("workbench.action.openDefaultKeybindingsFile")
show snippets: user.vscode("workbench.action.openSnippets")

# VSCode Snippets
snip (last | previous): user.vscode("jumpToPrevSnippetPlaceholder")
snip next: user.vscode("jumpToNextSnippetPlaceholder")

# Display
#
centered switch: user.vscode("workbench.action.toggleCenteredLayout")
fullscreen switch: user.vscode("workbench.action.toggleFullScreen")
theme switch: user.vscode("workbench.action.selectTheme")
wrap switch: user.vscode("editor.action.toggleWordWrap")
zen mode: user.vscode("workbench.action.toggleZenMode")

#
# Groups
#
focus group: user.vscode("workbench.action.toggleEditorWidths")
close group: user.vscode("workbench.action.closeEditorsInGroup")
(solo | one) group: user.vscode("workbench.action.closeEditorsInOtherGroups")

# File Commands
hunt (file | files) [<user.text>]:
    user.vscode("workbench.action.quickOpen")
    sleep(50ms)
    insert(text or "")
hunt (file | files) clip:
    user.vscode("workbench.action.quickOpen")
    sleep(50ms)
    edit.paste()
# TODO: Possible telescope replacement to do something like hunt in file:
# https://marketplace.visualstudio.com/items?itemName=shibayu36.search-in-current-file
# https://marketplace.visualstudio.com/items?itemName=jpcrs.binocular
file copy name: user.vscode("fileutils.copyFileName")
file copy path: user.vscode("copyFilePath")
file copy local [path]: user.vscode("copyRelativeFilePath")
file copy relative: user.vscode("copyRelativeFilePath")
file copy link: user.vscode("gitlens.copyRemoteFileUrlToClipboard")
file (new | create sibling): user.vscode_and_wait("explorer.newFile")
file create: user.vscode("workbench.action.files.newUntitledFile")
file create relative: user.vscode("fileutils.newFile")
file create root: user.vscode("fileutils.newFileAtRoot")
file duplicate: user.vscode("fileutils.duplicateFile")
file rename:
    user.vscode("fileutils.renameFile")
    sleep(150ms)
file move:
    user.vscode("fileutils.moveFile")
    sleep(150ms)
file clone:
    user.vscode("fileutils.duplicateFile")
    sleep(150ms)
file delete:
    user.vscode("fileutils.removeFile")
    sleep(150ms)
# Opens folder of current file
file open current folder: user.vscode("revealFileInOS")
file reveal: user.vscode("workbench.files.action.showActiveFileInExplorer")
folder open: user.vscode("workbench.action.files.openFolder")
folder open clip:
    user.vscode("workbench.action.files.openFolder")
    sleep(150ms)
    # Likely *nix only
    key('/')
    edit.paste()

# Saving
disk:
    edit.save()
    sleep(150ms)
    user.vscode("hideSuggestWidget")
# TODO: This could probably be an edit command
disk as: user.vscode("workbench.action.files.saveAs")
disk gentle: edit.save()
disk ugly: user.vscode("workbench.action.files.saveWithoutFormatting")
disk all: user.vscode("workbench.action.files.saveAll")

#
# Workspaces
#

workspace save: user.vscode("workbench.action.saveWorkspaceAs")
workspace open: user.vscode("workbench.action.openWorkspace")
workspace close: user.vscode("workbench.action.closeWorkspace")
workspace folder newr: user.vscode("workbench.action.addRootFolder")
workspace remove folder: user.vscode("workbench.action.removeRootFolder")
workspace configure trust: user.vscode("workbench.trust.manage")

#
# File Management
#
folder root new: user.vscode("workbench.action.addRootFolder")
folder [relative] new: user.vscode("explorer.newFolder")
folder collapse: user.vscode("workbench.files.action.collapseExplorerFolders")

#
# Programming Language Features
#
suggest show: user.vscode("editor.action.triggerSuggest")
hint show: user.vscode("editor.action.triggerParameterHints")
(def | definition) show: user.vscode("editor.action.revealDefinition")
(def | definition) peek: user.vscode("editor(.action.peekDefinition")
(def | definition) side: user.vscode("editor.action.revealDefinitionAside")
(jump ref | references show): user.vscode("editor.action.goToReferences")
(call | hierarchy) peek: user.vscode("editor.showCallHierarchy")
hunt (ref | references): user.vscode("references-view.find")
format that: user.vscode("editor.action.formatDocument")
format selection: user.vscode("editor.action.formatSelection")
imports fix: user.vscode("editor.action.organizeImports")
(trouble | problem) (next | show): user.vscode("editor.action.marker.nextInFiles")
(trouble | problem) last: user.vscode("editor.action.marker.prevInFiles")
(trouble | problem) fix: user.vscode("editor.action.quickFix")
trouble bar: user.vscode("workbench.actions.view.problems")
trouble close: key(escape)
rename that: user.vscode("editor.action.rename")
refactor that: user.vscode("editor.action.refactor")
whitespace trim: user.vscode("editor.action.trimTrailingWhitespace")
language switch: user.vscode("workbench.action.editor.changeLanguageMode")
# refactor rename: user.vscode("editor.action.rename")
# refactor this: user.vscode("editor.action.refactor")

#
# Code Navigation
#
(go declaration | follow): user.vscode("editor.action.revealDefinition")
(jump | go) back: user.vscode("workbench.action.navigateBack")
go forward: user.vscode("workbench.action.navigateForward")
go (impl | implementation): user.vscode("editor.action.goToImplementation")
go type: user.vscode("editor.action.goToTypeDefinition")
go usage: user.vscode("references-view.find")
go recent [<user.text>]:
    user.vscode("workbench.action.openRecent")
    sleep(50ms)
    insert(text or "")
    sleep(250ms)
go edit: user.vscode("workbench.action.navigateToLastEditLocation")
go remotes: user.vscode("gitlens.views.remotes.focus")
go branches: user.vscode("gitlens.views.branches.focus")
go commits: user.vscode("gitlens.views.commits.focus")

#
# Bookmarks. Requires Bookmarks plugin
#
hunt marks: user.vscode("workbench.view.extension.bookmarks")
(toggle mark | mark toggle): user.vscode("bookmarks.toggle")
mark next: user.vscode("bookmarks.jumpToNext")
mark last: user.vscode("bookmarks.jumpToPrevious")

(close other tabs|tabby scorch): user.vscode("workbench.action.closeOtherEditors")
close all tabs: user.vscode("workbench.action.closeAllEditors")
close tabs way right: user.vscode("workbench.action.closeEditorsToTheRight")
close tabs way left: user.vscode("workbench.action.closeEditorsToTheLeft")

#
# Folding
#
fold that: user.vscode("editor.fold")
unfold that: user.vscode("editor.unfold")
fold those: user.vscode("editor.foldAllMarkerRegions")
unfold those: user.vscode("editor.unfoldRecursively")
fold all: user.vscode("editor.foldAll")
unfold all: user.vscode("editor.unfoldAll")
fold comments: user.vscode("editor.foldAllBlockComments")
fold one: user.vscode("editor.foldLevel1")
fold two: user.vscode("editor.foldLevel2")
fold three: user.vscode("editor.foldLevel3")
fold four: user.vscode("editor.foldLevel4")
fold five: user.vscode("editor.foldLevel5")
fold six: user.vscode("editor.foldLevel6")
fold seven: user.vscode("editor.foldLevel7")

#
# Git / Github (not using verb-noun-adjective pattern, mirroring (term|terminal) commands.)
#
git branch: user.vscode("git.branchFrom")
git branch this: user.vscode("git.branch")
git checkout [<user.text>]:
    user.vscode("git.checkout")
    sleep(50ms)
    insert(text or "")
git commit [<user.text>]:
    user.vscode("git.commitStaged")
    sleep(100ms)
    user.insert_formatted(text or "", "CAPITALIZE_FIRST_WORD")
git commit {user.git_conventional_commits}:
    user.vscode("git.commitStaged")
    sleep(100ms)
    insert("{user.git_conventional_commits}: ")
git commit undo: user.vscode("git.undoCommit")
git commit amend: user.vscode("git.commitStagedAmend")

#To focus on the commit message box in the source control side tab
# FIXME: The actual underlying focusing should become of function, since I use it elsewhere
git quick commit:
    user.vscode("workbench.view.scm")
    sleep(50ms)
    user.vscode("workbench.scm.focus")
    sleep(50ms)
    user.vscode("list.focusFirst")
    sleep(50ms)
    user.vscode("list.focusDown")
    sleep(50ms)
    key(tab)

git quick commit {user.git_conventional_commits}:
    user.vscode("workbench.view.scm")
    sleep(50ms)
    user.vscode("workbench.scm.focus")
    sleep(50ms)
    user.vscode("list.focusFirst")
    sleep(50ms)
    user.vscode("list.focusDown")
    sleep(50ms)
    key(tab)
    sleep(100ms)
    insert("{user.git_conventional_commits}: ")

# To focus the second commit message box in the source control assuming you use
# multiple repos (ex: public and private talon)
# FIXME: It would be nice if you could just specify the number...
git quick commit other:
    user.vscode("workbench.view.scm")
    sleep(50ms)
    user.vscode("workbench.scm.focus")
    sleep(50ms)
    user.vscode("list.focusLast")
    sleep(50ms)
    user.vscode("list.focusUp")
    sleep(50ms)
    key(tab)

git quick commit other {user.git_conventional_commits}:
    user.vscode("workbench.view.scm")
    sleep(50ms)
    user.vscode("workbench.scm.focus")
    sleep(50ms)
    user.vscode("list.focusLast")
    sleep(50ms)
    user.vscode("list.focusUp")
    sleep(50ms)
    key(tab)
    sleep(100ms)
    insert("{user.git_conventional_commits}: ")

git diff: user.vscode("git.openChange")
git fetch: user.vscode("git.fetch")
git fetch all: user.vscode("git.fetchAll")
git ignore: user.vscode("git.ignore")
git merge: user.vscode("git.merge")
git output: user.vscode("git.showOutput")
git pull: user.vscode("git.pullRebase")
git push: user.vscode("git.push")
git push first:
    user.vscode("git.push")
    sleep(150ms)
    key(enter)
git push second:
    user.vscode("git.push")
    sleep(150ms)
    key(down)
    key(enter)
git push force: user.vscode("git.pushForce")
git rebase abort: user.vscode("git.rebaseAbort")
git reveal: user.vscode("git.revealInExplorer")
git revert: user.vscode("git.revertChange")
git stash: user.vscode("git.stash")
git stash pop: user.vscode("git.stashPop")
(git status | bar git): user.vscode("workbench.scm.focus")
git stage: user.vscode("git.stage")
git stage and close:
    user.vscode("git.stage")
    sleep(150ms)
    user.vscode("workbench.action.closeActiveEditor")
git stage all: user.vscode("git.stageAll")
git sync: user.vscode("git.sync")
git unstage: user.vscode("git.unstage")
git unstage all: user.vscode("git.unstageAll")
git discard file: user.vscode("git.clean")
pull request: user.vscode("pr.create")

# GitLens
git branches: user.vscode("gitlens.views.branches.focus")
# git file history: user.vscode("gitlens.views.fileHistory.focus")
# TODO: Probably change this, just taking from somebody else
dock open: user.vscode("gitlens.openWorkingFile")
git blame: user.vscode("gitlens.toggleFileBlameInDiffLeft")
git blame toggle: user.vscode("gitlens.toggleLineBlame")
# TODO: Make this use common branch names list
git compare to master:
    user.vscode("gitlens.diffWithRevisionFrom")
    sleep(450ms)
    insert("master")
git compare to main:
    user.vscode("gitlens.diffWithRevisionFrom")
    sleep(450ms)
    insert("main")
git compare: user.vscode("gitlens.diffWithRevisionFrom")
git compare to clip:
    user.vscode("gitlens.diffWithRevisionFrom")
    sleep(450ms)
    edit.paste()
(hunt commits | git commit search): user.vscode("gitlens.showCommitSearch")
git commit details: user.vscode("gitlens.showQuickCommitFileDetails")
git branch history: user.vscode("gitlens.showQuickRepoHistory")
git file history: user.vscode("gitlens.showQuickFileHistory")
git summary: user.vscode("gitlens.showQuickRepoStatus")
# TODO: Need to check what these do
git blame switch: user.vscode("gitlens.toggleLineBlame")
git lens switch: user.vscode("gitlens.toggleCodeLens")
git zen switch: user.vscode("gitlens.toggleZenMode")
git review switch: user.vscode("gitlens.toggleReviewMode")

# Use keyboard shortcuts because VSCode relies on when clause contexts to choose the appropriate
# action: https://code.visualstudio.com/api/references/when-clause-contexts
change next: user.vscode("workbench.action.editor.nextChange")
change last: user.vscode("workbench.action.editor.previousChange")
(diff|hunk) next: user.vscode("workbench.action.compareEditor.nextChange")
(diff|hunk) last: user.vscode("workbench.action.compareEditor.previousChange")

stage this: user.vscode("git.stageChange")
stage hunk: user.vscode("git.diff.stageHunk")
stage last:
    user.vscode("workbench.action.compareEditor.previousChange")
    user.vscode("git.diff.stageHunk")

stage next:
    user.vscode("workbench.action.compareEditor.nextChange")
    user.vscode("git.diff.stageHunk")
stage selected: user.vscode("git.stageSelectedRanges")
# These are specific to being in the diff view only
# change stage: key(ctrl-k ctrl-alt-s)
# change unstage: key(ctrl-k ctrl-alt-n)
# change revert: key(ctrl-k ctrl-alt-r)

#
# Merge Conflicts
#
[merge] reject all [theirs]: user.vscode("merge-conflict.accept.all-current")
[merge] (accept|keep) all [ours]: user.vscode("merge-conflict.accept.all-incoming")
[merge] (accept|keep) both all: user.vscode("merge-conflict.accept.all-both")
[merge] (accept|keep) (ours | current): user.vscode("merge-conflict.accept.current")
[merge] reject [(theirs | incoming)]:
    user.vscode("merge-conflict.accept.current")
    user.vscode("merge-conflict.next")
[merge] (accept|keep) (theirs | incoming): user.vscode("merge-conflict.accept.incoming")
# FIXME: Add a cursorless variation for selecting stuff
[merge] (accept|keep) (selection | that): user.vscode("merge-conflict.accept.selection")
[merge] (accept|keep) both: user.vscode("merge-conflict.accept.both")
(merge | conflict) next: user.vscode("merge-conflict.next")
(merge | conflict) last: user.vscode("merge-conflict.previous")
merge compare: user.vscode("merge-conflict.compare")

#
# Testing
#
test run: user.vscode("testing.runAtCursor")
test run file: user.vscode("testing.runCurrentFile")
test run all: user.vscode("testing.runAll")
test run failed: user.vscode("testing.reRunFailTests")
test run last: user.vscode("testing.reRunLastRun")

test debug: user.vscode("testing.debugAtCursor")
test debug file: user.vscode("testing.debugCurrentFile")
test debug all: user.vscode("testing.debugAll")
test debug failed: user.vscode("testing.debugFailTests")
test debug last: user.vscode("testing.debugLastRun")

test cancel: user.vscode("testing.cancelRun")

#
# Debugging
#
break point: user.vscode("editor.debug.action.toggleBreakpoint")
[(debug|bug)] step over: user.vscode("workbench.action.debug.stepOver")
[(debug|bug)] step into: user.vscode("workbench.action.debug.stepInto")
[(debug|bug)] step out [of]: user.vscode("workbench.action.debug.stepOut")
(debug|bug) start: user.vscode("workbench.action.debug.start")
(debug|bug) pause: user.vscode("workbench.action.debug.pause")
(debug|bug) stop: user.vscode("workbench.action.debug.stop")
(debug|bug) continue: user.vscode("workbench.action.debug.continue")
(debug|bug) restart: user.vscode("workbench.action.debug.restart")
(debug|bug) console: user.vscode("workbench.debug.action.toggleRepl")
(debug|bug) clean: user.vscode("workbench.debug.panel.action.clearReplAction")
# Select specific run config
(debug|bug) run config: user.vscode("workbench.action.debug.selectandstart")

# These should be project specific
(debug|bug) run neovim:
    user.vscode("workbench.action.debug.selectandstart")
    sleep(1)
    insert("Neovim: Run")
    key(enter)
    sleep(1)
    # Pops up a terminal
    user.snap_window_to_position("bottom")
    user.switcher_focus("code")
    sleep(1)
    user.attach_node_and_continue()

# These should be project specific
(debug|bug) test neovim:
    user.vscode("workbench.action.debug.selectandstart")
    sleep(1)
    insert("Neovim: Test")
    key(enter)
    sleep(1)
    # Pops up a terminal
    user.snap_window_to_position("bottom")

debug start node:
    user.vscode("workbench.action.debug.start")
    sleep(1)
    user.attach_node_and_continue()

debug node:
    user.attach_node_and_continue()

#
# Terminal
#
(term | terminal) external: user.vscode("workbench.action.terminal.openNativeConsole")
(term | terminal) new: user.vscode("workbench.action.terminal.new")
(term | terminal) next: user.vscode("workbench.action.terminal.focusNext")
(term | terminal) last: user.vscode("workbench.action.terminal.focusPrevious")
(term | terminal) split: user.vscode("workbench.action.terminal.split")
(term | terminal) zoom: user.vscode("workbench.action.toggleMaximizedPanel")
(term | terminal) trash: user.vscode("workbench.action.terminal.kill")
(term | terminal) toggle:
    user.vscode_and_wait("workbench.action.terminal.toggleTerminal")
term dog: user.vscode_and_wait("workbench.action.terminal.toggleTerminal")
(term | terminal) scroll up: user.vscode("workbench.action.terminal.scrollUp")
(term | terminal) scroll down: user.vscode("workbench.action.terminal.scrollDown")
(term | terminal) <number_small>: user.vscode_terminal(number_small)

#
# Lower Panel
#
# Some duplication with above, but I don't always work on it as a terminal
low zoom: user.vscode("workbench.action.toggleMaximizedPanel")

task run [<user.text>]:
    user.vscode("workbench.action.tasks.runTask")
    insert(user.text or "")
#TODO: should this be added to linecommands?
copy line down: user.vscode("editor.action.copyLinesDownAction")
copy line up: user.vscode("editor.action.copyLinesUpAction")

#Expand/Shrink AST Selection
select less: user.vscode("editor.action.smartSelect.shrink")
select (more | this): user.vscode("editor.action.smartSelect.expand")

minimap: user.vscode("editor.action.toggleMinimap")
maximize: user.vscode("workbench.action.minimizeOtherEditors")
restore: user.vscode("workbench.action.evenEditorWidths")

#breadcrumb
select breadcrumb: user.vscode("breadcrumbs.focusAndSelect")
# Use `alt-left` and `alt-right` to navigate the bread crumb

# Toast notifications
toast: user.vscode("notifications.focusToasts")
# Accepts whatever the default highlighted button is
toast yes: user.vscode("notification.acceptPrimaryAction")
toast next: user.vscode("notification.focusNextToast")
toast prev: user.vscode("notification.focusPreviousToast")
toast first: user.vscode("notification.focusFirstToast")
toast last: user.vscode("notification.focusLastToast")
toast show: user.vscode("notification.showList")
toast close: user.vscode("notification.hideList")
toast clear: user.vscode("notification.clear")
toast clear all: user.vscode("notification.clearAll")
toast shrink: user.vscode("notification.collapse")
toast grow: user.vscode("notification.expand")

hover show: user.vscode("editor.action.showHover")

join lines: user.vscode("editor.action.joinLines")

full screen: user.vscode("workbench.action.toggleFullScreen")

curse undo: user.vscode("cursorUndo")
curse redo: user.vscode("cursorRedo")
# Reduce cursors back to one without moving back to where we were
curse one: user.vscode("removeSecondaryCursors")

select word: user.vscode("editor.action.addSelectionToNextFindMatch")
skip word: user.vscode("editor.action.moveSelectionToNextFindMatch")

#
# Jupyter
#
cell next: user.vscode("notebook.focusNextEditor")
cell last: user.vscode("notebook.focusPreviousEditor")
cell run above: user.vscode("notebook.cell.executeCellsAbove")
cell run: user.vscode("notebook.cell.execute")

install local: user.vscode("workbench.extensions.action.installVSIX")



# pokey
sesh <user.show_list> [<user.text>] [halt]:
    user.vscode("workbench.action.openRecent")
    sleep(250ms)
    user.insert_formatted(text or "", "DASH_SEPARATED,ALL_LOWERCASE")
    sleep(250ms)

<user.teleport> sesh <user.text> [halt]:
    user.vscode("workbench.action.openRecent")
    sleep(250ms)
    # NB: I had workspace to avoid some file name conflicts, eg cursorless_todo.md
    user.insert_formatted("{text}", "DASH_SEPARATED,ALL_LOWERCASE")
    insert(" workspace")
    key(enter)
    sleep(250ms)

<user.teleport> sesh [halt]:
    user.vscode("workbench.action.openRecent")
    sleep(250ms)
    key(enter)
    sleep(250ms)

new sesh [<user.text>]:
    user.vscode("workbench.action.newWindow")
    sleep(3s)
    user.vscode("workbench.action.openRecent")
    sleep(250ms)
    insert(text or "")
    sleep(250ms)

<user.show_list> win [<user.text>]:
    user.vscode("workbench.action.switchWindow")
    sleep(250ms)
    insert(text or "")
    sleep(250ms)
<user.teleport> win [<user.text>]:
    user.vscode("workbench.action.switchWindow")
    sleep(50ms)
    insert(text or "")
    key(enter)
    sleep(250ms)

replace here:
    user.replace("")
    key(alt-l)

# vim muscle memory
lights out: key(escape)
matching: user.vscode("editor.action.jumpToBracket")
squeak:
    edit.save()
    sleep(150ms)
    app.tab_close()

# Refresh the contents of a file
file refresh: user.vscode("workbench.action.files.revert")
file new window: user.vscode("workbench.action.files.showOpenedFileInNewWindow")
file open: user.vscode("workbench.action.files.openFile")
hunt recent: user.vscode("workbench.action.openRecent")

# rust-analyzer
file open cargo: user.vscode("rust-analyzer.cargo.openCargoToml")

#
# Tasks
#

# TODO: It would be good to close the panel on success with certain commits
task build: user.vscode("workbench.action.tasks.build")
task recall:
    user.vscode("workbench.action.tasks.runTask")
    sleep(50ms)
    key(enter)
task run [<user.text>]:
    user.vscode("workbench.action.tasks.runTask")
    sleep(50ms)
    insert(text or "")
(task run go | runner) <user.text>:
    user.vscode("workbench.action.tasks.runTask")
    sleep(50ms)
    insert("{text}\n")
(task build quiet | builder):
    user.vscode("workbench.action.tasks.build")
    sleep(2s)
    user.vscode("workbench.action.closePanel")

copy command id: user.copy_command_id()

break <user.cursorless_target>:
    user.cursorless_command("setSelectionBefore", cursorless_target)
    user.vscode("hideSuggestWidget")
    key("enter")

{user.search_engine} hunt <user.cursorless_target>$:
    user.cursorless_command("copyToClipboard", cursorless_target)
    user.search_with_search_engine(search_engine, clip.text())


# andreas-talon
tabby {self.letter} [{self.letter}]:
    user.vscode("andreas.focusTab", "{letter_1}{letter_2 or ''}")

tabby close {self.letter} [{self.letter}]:
    user.vscode("andreas.focusTab", "{letter_1}{letter_2 or ''}")
    sleep(150ms)
    user.vscode("workbench.action.closeActiveEditor")

# remote-ssh
tunnel open: user.vscode("opensshremotes.openEmptyWindow")

#
# Snippets
#

next: user.vscode_and_wait("jumpToNextSnippetPlaceholder")
snip last: user.vscode("jumpToPrevSnippetPlaceholder")
skip:
    key("backspace")
    user.vscode("jumpToNextSnippetPlaceholder")

# Pedal
deck(pedal_left):
    key("pageup")
    print("deck page up")
deck(pedal_right):
    key("pagedown")
    print("deck page down")

deck(pedal_middle):
    edit.save()
    print("deck save")

# direnv extensionl
envy allow: user.vscode("direnv.loadEnvrc")
envy open: user.vscode("direnv.open")
envy create: user.vscode("direnv.create")
envy reload: user.vscode("direnv.reload")
envy reset: user.vscode("direnv.reset")

# alternate files
<user.teleport> alter: user.vscode("alternate.alternateFile")
make alter: user.vscode("alternate.createAlternateFile")
split alter: user.vscode("alternate.alternateFileInSplit")

# indentation
convert file to tabs: user.vscode("editor.action.indentationToTabs")
convert file to spaces: user.vscode("editor.action.indentationToSpaces")

toggle markdown: user.vscode("markdownlint.toggleLinting")
toggle (spelling|spell): user.vscode("cSpell.toggleVisible")

fix select: user.vscode("editor.action.autoFix")
fix this:
    user.vscode("editor.action.autoFix")
    sleep(150ms)
    key(enter)
