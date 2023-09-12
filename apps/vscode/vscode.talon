app: vscode
-
tag(): user.find_and_replace
tag(): user.line_commands
tag(): user.multiple_cursors
tag(): user.snippets
tag(): user.splits
tag(): user.tabs

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

# Sidebar
bar (files|explore): user.vscode("workbench.view.explorer")
bar extensions: user.vscode("workbench.view.extensions")
bar outline: user.vscode("outline.focus")
bar run: user.vscode("workbench.view.debug")
bar search: user.vscode("workbench.view.search")
bar source: user.vscode("workbench.view.scm")
bar test: user.vscode("workbench.view.testing.focus")
bar switch: user.vscode("workbench.action.toggleSidebarVisibility")
(left|side) dog: user.vscode("workbench.action.toggleSidebarVisibility")
# Toggle Secondary Side Bar
right dog: key(ctrl-alt-b) 

view wider: user.vscode("workbench.action.increaseViewSize")
view thinner: user.vscode("workbench.action.decreaseViewSize")

# Splits
cross: user.split_next()

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
search (first|next): user.vscode("search.action.focusNextSearchResult")
search last: user.vscode("search.action.focusPreviousSearchResult")
search clear: user.vscode("search.action.clearSearchResults")
search editor: user.vscode("search.action.openInEditor")

# Panels
panel control: user.vscode("workbench.panel.repl.view.focus")
panel output: user.vscode("replaceworkbench.panel.output.focus")
(panel trouble|trouble show): user.vscode("workbench.panel.markers.view.focus")
(low dog|panel switch): user.vscode("workbench.action.togglePanel")
low dog off: user.vscode("workbench.action.closePanel")

(term show|panel terminal): user.vscode("workbench.action.terminal.focus")
(pan edit|editor): user.vscode("workbench.action.focusActiveEditorGroup")

# Settings
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

# Display
centered switch: user.vscode("workbench.action.toggleCenteredLayout")
fullscreen switch: user.vscode("workbench.action.toggleFullScreen")
theme switch: user.vscode("workbench.action.selectTheme")
wrap switch: user.vscode("editor.action.toggleWordWrap")
zen mode: user.vscode("workbench.action.toggleZenMode")

# Groups
focus group: user.vscode("workbench.action.toggleEditorWidths")
close group: user.vscode("workbench.action.closeEditorsInGroup")
(solo|one) group: user.vscode("workbench.action.closeEditorsInOtherGroups")

# File Commands
hunt files [<user.text>]:
    user.vscode("workbench.action.quickOpen")
    sleep(50ms)
    insert(text or "")
hunt files clip:
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
file (new|create sibling): user.vscode_and_wait("explorer.newFile")
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
file open folder: user.vscode("revealFileInOS")
file reveal: user.vscode("workbench.files.action.showActiveFileInExplorer")
disk:
    edit.save()
    sleep(150ms)
    user.vscode("hideSuggestWidget")
disk gentle: edit.save()
disk ugly: user.vscode("workbench.action.files.saveWithoutFormatting")

# Language Features
suggest show: user.vscode("editor.action.triggerSuggest")
hint show: user.vscode("editor.action.triggerParameterHints")
(def|definition) show: user.vscode("editor.action.revealDefinition")
(def|definition) peek: user.vscode("editor(.action.peekDefinition")
(def|definition) side: user.vscode("editor.action.revealDefinitionAside")
(jump ref|references show): user.vscode("editor.action.goToReferences")
(call|hierarchy) peek: user.vscode("editor.showCallHierarchy")
hunt (ref|references): user.vscode("references-view.find")
format that: user.vscode("editor.action.formatDocument")
format selection: user.vscode("editor.action.formatSelection")
imports fix: user.vscode("editor.action.organizeImports")
(trouble|problem) (next|show): user.vscode("editor.action.marker.nextInFiles")
(trouble|problem) last: user.vscode("editor.action.marker.prevInFiles")
(trouble|problem) fix: user.vscode("problems.action.showQuickFixes")
trouble bar: user.vscode("workbench.actions.view.problems")
trouble close: key(escape)
rename that: user.vscode("editor.action.rename")
refactor that: user.vscode("editor.action.refactor")
whitespace trim: user.vscode("editor.action.trimTrailingWhitespace")
language switch: user.vscode("workbench.action.editor.changeLanguageMode")
# refactor rename: user.vscode("editor.action.rename")
# refactor this: user.vscode("editor.action.refactor")

#code navigation
(go declaration | follow): user.vscode("editor.action.revealDefinition")
(jump|go) back: user.vscode("workbench.action.navigateBack")
go forward: user.vscode("workbench.action.navigateForward")
go (impl|implementation): user.vscode("editor.action.goToImplementation")
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


# Bookmarks. Requires Bookmarks plugin
hunt marks: user.vscode("workbench.view.extension.bookmarks")
(toggle mark|mark toggle): user.vscode("bookmarks.toggle")
mark next: user.vscode("bookmarks.jumpToNext")
mark last: user.vscode("bookmarks.jumpToPrevious")

close other tabs: user.vscode("workbench.action.closeOtherEditors")
close all tabs: user.vscode("workbench.action.closeAllEditors")
close tabs way right: user.vscode("workbench.action.closeEditorsToTheRight")
close tabs way left: user.vscode("workbench.action.closeEditorsToTheLeft")

# Folding
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

# Git / Github (not using verb-noun-adjective pattern, mirroring (term|terminal) commands.)
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
    sleep(100ms)
    insert("{user.git_conventional_commits}: ")
git commit undo: user.vscode("git.undoCommit")
git commit amend: user.vscode("git.commitStagedAmend")
git diff: user.vscode("git.openChange")
git fetch: user.vscode("git.fetch")
git fetch all: user.vscode("git.fetchAll")
git ignore: user.vscode("git.ignore")
git merge: user.vscode("git.merge")
git output: user.vscode("git.showOutput")
git pull: user.vscode("git.pullRebase")
git push: user.vscode("git.push")
git push focus: user.vscode("git.pushForce")
git rebase abort: user.vscode("git.rebaseAbort")
git reveal: user.vscode("git.revealInExplorer")
git revert: user.vscode("git.revertChange")
git stash: user.vscode("git.stash")
git stash pop: user.vscode("git.stashPop")
git status: user.vscode("workbench.scm.focus")
git stage: user.vscode("git.stage")
git stage all: user.vscode("git.stageAll")
git sync: user.vscode("git.sync")
git unstage: user.vscode("git.unstage")
git unstage all: user.vscode("git.unstageAll")
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
    insert('master')
git compare to main:
    user.vscode("gitlens.diffWithRevisionFrom")
    sleep(450ms)
    insert('main')
git compare:
    user.vscode("gitlens.diffWithRevisionFrom")
(hunt commits|git commit search): user.vscode("gitlens.showCommitSearch")
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
change next: key(alt-f5)
change last: key(shift-alt-f5)
stage this: user.vscode("git.stageChange")
# These are specific to being in the diff view only
# change stage: key(ctrl-k ctrl-alt-s)
# change unstage: key(ctrl-k ctrl-alt-n)
# change revert: key(ctrl-k ctrl-alt-r)

# Testing
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

# Debugging
break point: user.vscode("editor.debug.action.toggleBreakpoint")
step over: user.vscode("workbench.action.debug.stepOver")
debug step into: user.vscode("workbench.action.debug.stepInto")
debug step out [of]: user.vscode("workbench.action.debug.stepOut")
debug start: user.vscode("workbench.action.debug.start")
debug pause: user.vscode("workbench.action.debug.pause")
debug stopper: user.vscode("workbench.action.debug.stop")
debug continue: user.vscode("workbench.action.debug.continue")
debug restart: user.vscode("workbench.action.debug.restart")
debug console: user.vscode("workbench.debug.action.toggleRepl")
debug clean: user.vscode("workbench.debug.panel.action.clearReplAction")

# Terminal
(term|terminal) external: user.vscode("workbench.action.terminal.openNativeConsole")
(term|terminal) new: user.vscode("workbench.action.terminal.new")
(term|terminal) next: user.vscode("workbench.action.terminal.focusNext")
(term|terminal) last: user.vscode("workbench.action.terminal.focusPrevious")
(term|terminal) split: user.vscode("workbench.action.terminal.split")
(term|terminal) zoom: user.vscode("workbench.action.toggleMaximizedPanel")
(term|terminal) trash: user.vscode("workbench.action.terminal.kill")
(term|terminal) toggle: user.vscode_and_wait("workbench.action.terminal.toggleTerminal")
term dog: user.vscode_and_wait("workbench.action.terminal.toggleTerminal")
(term|terminal) scroll up: user.vscode("workbench.action.terminal.scrollUp")
(term|terminal) scroll down: user.vscode("workbench.action.terminal.scrollDown")
(term|terminal) <number_small>: user.vscode_terminal(number_small)

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

# this is specific to when the replace here prompt is open
replace all:
    key(ctrl-alt-enter)

hover show: user.vscode("editor.action.showHover")

join lines: user.vscode("editor.action.joinLines")

full screen: user.vscode("workbench.action.toggleFullScreen")

curse undo: user.vscode("cursorUndo")

select word: user.vscode("editor.action.addSelectionToNextFindMatch")
skip word: user.vscode("editor.action.moveSelectionToNextFindMatch")

# jupyter
cell next: user.vscode("notebook.focusNextEditor")
cell last: user.vscode("notebook.focusPreviousEditor")
cell run above: user.vscode("notebook.cell.executeCellsAbove")
cell run: user.vscode("notebook.cell.execute")

install local: user.vscode("workbench.extensions.action.installVSIX")

# copilot
pilot jest: user.vscode("editor.action.inlineSuggest.trigger")
previous|pilot next: user.vscode("editor.action.inlineSuggest.showNext")
pilot (last): user.vscode("editor.action.inlineSuggest.showPrevious")
pilot: user.vscode("editor.action.inlineSuggest.commit")
pilot word: user.vscode("editor.action.inlineSuggest.acceptNextWord")
pilot nope: user.vscode("editor.action.inlineSuggest.undo")
pilot cancel: user.vscode("editor.action.inlineSuggest.hide")
pilot generate: user.vscode("github.copilot.generate")
pilot pan next: user.vscode("github.copilot.nextPanelSuggestion")
pilot pan (previous|last): user.vscode("github.copilot.previousPanelSuggestion")
pilot [pan] (accept|commit): user.vscode("github.copilot.acceptPanelSuggestion")
[pilot] keep: key(tab)

# pokey 
sesh <user.show_list> [<user.text>] [halt]:
    user.vscode("workbench.action.openRecent")
    sleep(250ms)
    user.insert_formatted(text or "", "DASH_SEPARATED,ALL_LOWERCASE")
    sleep(250ms)
<user.teleport> sesh [<user.text>] [halt]:
    user.vscode("workbench.action.openRecent")
    sleep(250ms)
    user.insert_formatted(text or "", "DASH_SEPARATED,ALL_LOWERCASE")
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


# TODO: It would be good to close the panel on success with certain commits
task build: user.vscode("workbench.action.tasks.build")

(task build quiet|builder): 
    user.vscode("workbench.action.tasks.build")
    sleep(2s)
    user.vscode("workbench.action.closePanel")

copy command id:            user.copy_command_id()

break <user.cursorless_target>:
    user.cursorless_command("setSelectionBefore", cursorless_target)
    user.vscode("hideSuggestWidget")
    key("enter")

