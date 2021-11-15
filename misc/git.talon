tag: terminal
and tag: user.git
-
# Standard commands
git add patch: "git add . -p\n"
git add: "git add "
git add (changed|everything): "git add -u\n"
git bisect: "git bisect "
git blame: "git blame "
git branch: "git branch "
git branch (remove|delete): "git branch -d "
git branch force (remove|delete): "git branch -D "
git branch remote: "git branch --remote\n"
git branch <user.text>: "git branch {text}"
git checkout: "git checkout "
git checkout master: "git checkout master\n"
git checkout file master: "git checkout master --"
git checkout main: "git checkout main\n"
git checkout dev: "git checkout dev\n"
git checkout <user.text>: "git checkout {text}"
git checkout <number_small> before clip: 
    insert("git checkout ")
    edit.paste()
    key("^:{number_small}")
    key(enter)
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
git clean everything: "git clean -dfx"
# XXX - should use text or
git commit message <user.text>: "git commit -m '{text}'"
git commit message: 
    insert("git commit -m ''")
    edit.left()
git commit: "git commit\n"
git commit amend: "git commit --amend "
git diff (colour|color) words: "git diff --color-words "
git diff: "git diff "
git diff cached: "git diff --cached\n"
git fetch: "git fetch\n"
git fetch and rebase: "git fetch && git rebase\n"
git fetch prune: "git fetch --prune\n"
git fetch all: "git fetch --all\n"
# XXX - These are a little misleading for the simplicity of seeing. Maybe "fetch
# pull.. ?"
git fetch <number>: "git fetch origin pull/{number}/head:"
git fetch upstream <number>: "git fetch upstream pull/{number}/head:"
#git fetch <user.text>: "git fetch {text}"
git ignore changes: "git update-index --assume-unchanged "
git in it: "git init\n"
git list files: "git ls-files\n"
git list modified: "git ls-files -m\n"
git list tracked: "git ls-files -r master --name-only\n"
git list ignored: "git ls-files . --ignored --exclude-standard --others\n"
git list untracked: "git ls-files . --ignored --exclude-standard --others\n"
git log all: "git log\n"
git log all changes: "git log -c\n"
git log: "git log -5\n"
git log files: "git log --name-status -5\n"
git log files <number>: "git log --name-status -{number}\n"
git log changes: "git log -c "
git merge: "git merge "
git merge <user.text>:"git merge {text}"
git move: "git mv "
git new branch: "git checkout -b "
git pull: "git pull"
git pull origin: "git pull origin "
git pull rebase: "git pull --rebase "
git pull fast forward: "git pull --ff-only\n"
git pull <user.text>: "git pull {text} "
git push: "git push\n"
git push origin: "git push origin "
git push up stream origin: "git push -u origin"
git push <user.text>: "git push {text} "
git push tags: "git push --tags\n"
git rebase: "git rebase "
# NOTE - we don't use abort in the command because it conflicts with
# abort.talon
git rebase cancel: "git rebase --abort\n"
git rebase continue: "git rebase --continue\n"
git rebase skip: "git rebase --skip"
git remove: "git rm "
git remove cached: "git rm --cached"
git (remove|delete) remote branch: "git push --delete origin "
git remove remote origin: "git remote rm origin"
git reset: "git reset "
git reset soft: "git reset --soft "
git reset hard: "git reset --hard "
git restore: "git restore "
git restore staged: "git restore --staged "
git restore source: "git restore --source="
get remote set origin: "git remote set-url origin "
git remote show origin: "git remote show origin\n"
git remote: "git remote "
git remote add: "git remote add "
git remote add upstream: "git remote add upstream "
git remote remove: "git remote remove "
git remote show origin: "git remote show origin\n"
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
git stash pop: "git stash pop\n"
git stash: "git stash\n"
git stash apply: "git stash apply\n"
git stash list: "git stash list\n"
git stash show: "git stash show"
git status: "git status --untracked-files=no\n"
git status full: "git status\n"
git status staged: "git status --short | grep '^[MARCD]'\n"
git sub tree: "git subtree "
git switch: "git switch -"
git switch branch: "git switch -c"
git switch [<user.text>]: "git switch {user.formatted_text(text or '', 'DASH_SEPARATED')}"
git switch master: "git switch master "
git switch main: "git switch main "
git switch detached: "git switch --detach "
git (switch create | new branch) [<user.text>]:
  "git switch -c {user.formatted_text(text or '', 'DASH_SEPARATED')}"
git switch orphan: "git switch --orphan "
git [sub] module add:  "git submodule add "
git [sub] module status: "git submodule status\n"
git [sub] module status recurse: "git submodule status --recursive\n"
git [sub] module sink: "git submodule sync\n"
git [sub] module update: "git submodule update --init --recursive --remote"
git module references: "git ls-files --stage | grep 160000\n"
git tag: "git tag "
git tag list: "git tag\n"
git tag list specific: 
    insert('git tag -l ""')
    edit.left()
git tag add: 
    user.insert_cursor('git tag -a v[|] -m ""')
git tag remove: "git tag -d "
git tag remove remote: "git push origin --delete "

# Convenience
git edit config: "git config --local -e\n"

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
