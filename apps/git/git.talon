tag: terminal
and tag: user.git
-
# Standard commands
git add patch: "git add . -p\n"
git add: "git add "
git add force: "git add -f "
git add (changed | everything): "git add -u\n"
git bisect: "git bisect "
git blame: "git blame "
git branch: "git branch "
git branch list: "git branch -a\n"
git branch (remove | delete): "git branch -d "
git branch force (remove | delete): "git branch -D "
git branch remote: "git branch --remote\n"
git branch <user.text>: "git branch {text}"
git checkout: "git checkout "
git checkout master: "git checkout master\n"
git checkout file master: "git checkout master --"
git checkout (main | men): "git checkout main\n"
git checkout dev: "git checkout dev\n"
git checkout <user.text>: "git checkout {text}"
git checkout <number_small> before clip:
    insert("git checkout ")
    edit.paste()
    key("^:{number_small}")
    key(enter)
git checkout clip:
    insert("git checkout ")
    edit.paste()
    key(enter)
git check ignore: "git check-ignore -v "
git cherry pick: "git cherry-pick "
git cherry pick continue: "git cherry-pick --continue "
git cherry pick abort: "git cherry-pick --abort "
git cherry pick skip: "git cherry-pick --skip "
git clone: "git clone "
git clone clip:
    insert("git clone ")
    edit.paste()
    key(enter)
# Leave \n out for confirmation since the operation is destructive
git clean: "git clean"
git clean everything: "git clean -dfx"
git clean FD: "git clean -fd"
# TODO: The should use sentence to match conventional commit standard
git commit message <user.text>: "git commit -m \"{text}\""
git commit message {user.git_conventional_commits}:
    user.insert_between("git commit -m \"{git_conventional_commits}: ", "\"")
git commit message {user.git_conventional_commits} <user.word>:
    user.insert_between("git commit -m \"{git_conventional_commits}({word}): ", "\"")
git commit message: user.insert_between("git commit -m \"", "\"")
git commit: "git commit\n"
git commit amend: "git commit --amend "
git commit no verify: "git commit -n"
git commit existing: "git commit -a\n"
git diff (colour | color) words: "git diff --color-words "
git diff: "git diff "
git diff cached: "git diff --cached\n"
git diff staged: "git diff --staged\n"
git diff main: "git diff main\n"
git diff tool: "git difftool -d\n"
git diff tool cached: "git difftool --cached -d\n"
git fetch: "git fetch\n"
git fetch and rebase: "git fetch && git rebase\n"
git fetch prune: "git fetch --prune\n"
git fetch all: "git fetch --all\n"
git garbage collect aggressive: "git gc --aggressive"
# XXX - These are a little misleading for the simplicity of seeing. Maybe "fetch
# pull.. ?"
git fetch <number>: "git fetch origin pull/{number}/head:"
git fetch upstream <number>: "git fetch upstream pull/{number}/head:"
#git fetch <user.text>: "git fetch {text}"
git filter branch: "git filter-branch --subdirectory-filter"
git ignore changes: "git update-index --assume-unchanged "
git in it: "git init\n"
git list files: "git ls-files\n"
git list modified: "git ls-files -m\n"
git list tracked: "git ls-files -r main --name-only\n"
git list ignored: "git ls-files . --ignored --exclude-standard --others\n"
git list untracked: "git ls-files . --ignored --exclude-standard --others\n"
git show hook folder: "git rev-parse --git-path hooks\n"
git log all: "git log\n"
git log all changes: "git log -c\n"
git log: "git log -5\n"
git log reverse: "git log -5 --reverse\n"
git log <number>: "git log -{number}\n"
git log files: "git log --name-status -5\n"
git log files <number>: "git log --name-status -{number}\n"
git log [changes | code]: "git log -c "
git log clip:
    insert("git log -1 -c ")
    edit.paste()
    key(enter)

# diff-filter
#--diff-filter=[(A|C|D|M|R|T|U|X|B)…​[*]]
#
#    Select only files that are Added (A), Copied (C), Deleted (D), Modified (M), Renamed (R), have their type (i.e. regular file, symlink, submodule, …​) changed (T), are Unmerged (U), are Unknown (X), or have had their pairing Broken (B). Any combination of the filter characters (including none) can be used. When * (All-or-none) is added to the combination, all paths are selected if there is any file that matches other criteria in the comparison; if there is no file that matches other criteria, nothing is selected.
#
#    Also, these upper-case letters can be downcased to exclude. E.g. --diff-filter=ad excludes added and deleted paths.
#
#    Note that not all diffs can feature all types. For instance, copied and renamed entries cannot appear if detection for those types is disabled.
#
git log added files: "git log --diff-filter=A --summary\n"
git log added files only: "git log --diff-filter=A --summary | grep create\n"
git log removed files: "git log --diff-filter=D --summary\n"
git log removed files only: "git log --diff-filter=D --summary | grep delete\n"

git merge: "git merge "
git merge <user.text>: "git merge {text}"
git merge clip:
    insert("git merge ")
    edit.paste()
git merge tool: "git mergetool\n"
git move: "git mv "
git new branch: "git checkout -b "
git prune: "git prune"
git pull: "git pull"
git pull origin: "git pull origin "
git pull rebase: "git pull --rebase "
git pull fast forward: "git pull --ff-only\n"
git pull <user.text>: "git pull {text} "
git push: "git push\n"
git push origin: "git push origin "
git push up stream origin: "git push -u origin "
git push <user.text>: "git push {text} "
git push tags: "git push --tags\n"
git rebase: "git rebase "
git rebase now: "git rebase\n"
# NOTE - we don't use abort in the command because it conflicts with
# abort.talon
git rebase cancel: "git rebase --abort\n"
git rebase continue: "git rebase --continue\n"
git rebase skip: "git rebase --skip"
git remove: "git rm "
git remove cached: "git rm --cached"
git (remove | delete) remote branch: "git push --delete origin "
git remove remote origin: "git remote rm origin"
git reset: "git reset "
git reset soft: "git reset --soft "
git reset soft head: "git reset --soft HEAD~1"
git reset soft head <number_small>: "git reset --soft HEAD~{number_small}"
git reset hard: "git reset --hard "
git reset hard head: "git reset --hard HEAD~1"
git reset hard head <number_small>: "git reset --hard HEAD~{number_small}"
git restore: "git restore "
git restore staged: "git restore --staged "
git restore source: "git restore --source="
get remote set origin: "git remote set-url origin "
git remote: "git remote "
git remote add: "git remote add "
git remote list: "git remote -v\n"
git remote set url: "git remote set-url "
git remote add upstream: "git remote add upstream "
git remote remove: "git remote remove "
git [remote] show origin: "git remote show origin\n"
git show: "git show "
git show clip:
    insert("git show ")
    edit.paste()
    key(enter)
git show change: "git show -c"
git show change clip:
    insert("git show -c")
    edit.paste()
    key(enter)
git show head: "git show -c HEAD\n"
git change head to main:
    "git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main\n"
git stash pop: "git stash pop\n"
git stash: "git stash\n"
git stash push: user.insert_between("git stash push -m '", "'")
git stash apply: "git stash apply\n"
git stash list: "git stash list\n"
git stash show: "git stash show"
git status: "git status --untracked-files=no\n"
git status (all | full): "git status\n"
git status staged: "git status --short | grep '^[MARCD]'\n"
git sub tree: "git subtree "
git switch: "git switch "
git switch branch: "git switch -c"
git switch [<user.text>]:
    "git switch {user.formatted_text(text or '', 'DASH_SEPARATED')}"
git switch master: "git switch master "
git switch main: "git switch main "
git switch develop: "git switch develop "
git switch detached: "git switch --detach "
git (switch create | new branch) [<user.text>]:
    "git switch -c {user.formatted_text(text or '', 'DASH_SEPARATED')}"
git switch orphan: "git switch --orphan "
git switch clip:
    insert("git switch ")
    edit.paste()
    key(enter)

git [sub] module add: "git submodule add "
git [sub] module status: "git submodule status\n"
git [sub] module status recurse: "git submodule status --recursive\n"
git [sub] module sink: "git submodule sync\n"
git [sub] module update: "git submodule update --init --recursive --remote"
git module references: "git ls-files --stage | grep 160000\n"
git tag: "git tag "
git tag list: "git --no-pager tag\n"
git tag list specific:
    insert('git tag -l ""')
    edit.left()
git tag add: user.insert_cursor('git tag -a v[|] -m ""')
git tag remove: "git tag -d "
git tag remove remote: "git push origin --delete "

# XXX - revisit this with sublists for ones I want to always run with \n, as
#git {user.git_command} [<user.git_arguments>]:
#    args = git_arguments or ""
#    "git {git_command}{args} "
#git commit [<user.git_arguments>] message [<user.prose>]:
#    args = git_arguments or ""
#    message = prose or ""
#    user.insert_between("git commit{args} --message '{message}", "'")
git stash [push] [<user.git_arguments>] message [<user.prose>]:
    args = git_arguments or ""
    message = prose or ""
    user.insert_between("git stash push{args} --message '{message}", "'")

# Optimistic execution for frequently used commands that are harmless (don't
# change repository or index state).
# XXX - revisit as I'm just favouring my old stuff for now
#git status$: "git status\n"
#git add patch$: "git add --patch\n"
#git show head$: "git show HEAD\n"
#git diff: "git diff\n"
#git diff (cached | cashed)$: "git diff --cached\n"

# Convenience
git clone clipboard:
    insert("git clone ")
    edit.paste()
    key(enter)
git diff highlighted:
    edit.copy()
    insert("git diff ")
    edit.paste()
    key(enter)
git diff clipboard:
    insert("git diff ")
    edit.paste()
    key(enter)
git add highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    key(enter)
git add clipboard:
    insert("git add ")
    edit.paste()
    key(enter)
git commit highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    insert("\ngit commitit tag\n")
