tag: terminal
and tag: user.git
-

# Standard commands
git add patch: "git add . -p\n"
git add: "git add "
git add force: "git add -f "
git add (all | changed | everything):
    edit.delete_line()
    insert("git add -u\n")
git bisect: "git bisect "
git blame: "git blame "
git branch: "git branch "
git branch help: "git branch --help\n"
git branch list [all]:
    edit.delete_line()
    insert("git branch -a\n")
git branch list remote:
    edit.delete_line()
    insert("git branch -r\n")
git branch list local:
    edit.delete_line()
    insert("git branch\n")
git branch (remove | delete): "git branch -d "
git branch (remove | delete) force: "git branch -D "
git branch remove remote: "git push origin --delete "
git branch remove remote clip:
    "git push origin --delete "
    edit.paste()
git branch remote: "git branch --remote\n"
git branch (rename | move): "git branch -m "
git branch <user.text>: "git branch {text}"
git checkout: "git checkout "
git checkout {user.git_branches}:
    edit.paste()
    insert("git checkout {git_branches}\n")
git checkout file {user.git_branches}:
    edit.paste()
    insert("git checkout {git_branches} -- ")
git checkout upstream (main | men):
    edit.delete_line()
    insert("git checkout upstream/main\n")
git checkout <number_small> before clip:
    insert("git checkout ")
    edit.paste()
    key("^:{number_small}")
    key(enter)
git checkout clip:
    edit.delete_line()
    insert("git checkout ")
    edit.paste()
    key(enter)
git check ignore: "git check-ignore -v "
git cherry pick: "git cherry-pick "
git cherry pick continue: "git cherry-pick --continue "
git cherry pick (cancel|quit): "git cherry-pick --quit "
git cherry pick skip: "git cherry-pick --skip "
git clone: "git clone "
git clone clip:
    edit.delete_line()
    insert("git clone ")
    edit.paste()
    key(enter)
git clone depth <number>: "git clone --depth {number} "
git clone depth <number> clip:
    edit.delete_line()
    insert("git clone --depth {number} ")
    edit.paste()
    key(enter)
# Leave \n out for confirmation since the operation is destructive
git clean: "git clean"
git clean everything: "git clean -dfx"
git clean untracked: "git clean -fd"

<user.git> (commit|calm) [message] <user.text>:
    edit.delete_line()
    insert("git commit -m \"{text or ''}")
<user.git> (commit|calm) [message] {user.git_conventional_commits}:
    edit.delete_line()
    user.insert_between('git commit -m "{git_conventional_commits}: ', '"')
# git commit [message] {user.git_conventional_commits} <user.word>:
#     edit.delete_line()
#     insert(user.insert_between('git commit -m "{git_conventional_commits}({word}): ', '"'))
<user.git> (commit|calm) [message] {user.git_conventional_commits} <user.text>:
    edit.delete_line()
    user.insert_between('git commit -m "{git_conventional_commits}: {text}', '"')
<user.git> (commit|calm) [message]:
    edit.delete_line()
    user.insert_between('git commit -m "', '"')
<user.git> (commit|calm) empty:
    edit.delete_line()
    insert("git commit\n")
<user.git> (commit|calm) amend: "git commit --amend "
<user.git> (commit|calm) amend no edit: "git commit --amend --no-edit\n"
<user.git> (commit|calm) no verify: "git commit -n"
<user.git> (commit|calm) existing: "git commit -a\n"

# git commit automation convenience
<user.git> (commit|calm) all {user.git_conventional_commits}:
    "git add -u\n"
    user.insert_between('git commit -m "{git_conventional_commits}: ', '"')
# Two useful commands when commit fails due to pre commit hook
<user.git> (commit|calm) again:
    key(ctrl-r)
    "git commit\n"
git re commit [modified | staged]:
    'git status -s | grep -e "^MM" | cut -d" " -f2- | xargs git add\n'
    key(ctrl-r)
    sleep(500ms)
    "git commit -m\n"
    key(enter)

git diff (colour | color) words: "git diff --color-words "
git diff: "git diff "
git diff cached: "git diff --cached\n"
git diff staged: "git diff --staged\n"
git diff {user.git_branches}: "git diff {git_branches}  \n"
git diff tool: "git difftool -d\n"
git diff tool cached: "git difftool --cached -d\n"
git diff names only: "git diff --name-only "

git fetch: "git fetch\n"
(git fetch and rebase|G base): "git fetch && git rebase\n"

git fetch prune: "git fetch --prune\n"
git fetch all: "git fetch --all\n"
git garbage collect aggressive: "git gc --aggressive"
git fetch upstream: "git fetch upstream\n"
git fetch (pull | P R) <number>: "git fetch origin pull/{number}/head:"
git fetch upstream (pull | P R) <number>: "git fetch upstream pull/{number}/head:"
#git fetch <user.text>: "git fetch {text}"
git filter branch: "git filter-branch --subdirectory-filter"
git ignore changes: "git update-index --assume-unchanged "
git in it: "git init\n"
git list files: "git ls-files\n"
git list modified: "git ls-files -m\n"
git list tracked {user.git_branches}: "git ls-files -r git_branches --name-only\n"
git list ignored: "git ls-files . --ignored --exclude-standard --others\n"
git list untracked: "git ls-files . --ignored --exclude-standard --others\n"
git show hook folder: "git rev-parse --git-path hooks\n"

<user.git> log all: "git log\n"
<user.git> log all pretty: "git log --pretty=oneline\n"
<user.git> log all changes: "git log -c\n"
<user.git> log: "git log -5\n"
<user.git> log pretty: "git log -5 --pretty=oneline\n"
<user.git> log graph: "git log -5 --graph --pretty=oneline\n"
<user.git> log graph all: "git log --graph --pretty=oneline\n"
<user.git> log find upstream P R: user.insert_between('git log --pretty=oneline --grep="#', '" upstream/main')
<user.git> log diff: "git log -p -5\n"
<user.git> log reverse: "git log -5 --reverse\n"
<user.git> log <number>: "git log -{number}\n"
<user.git> log diff <number>: "git log -p -{number}\n"
<user.git> log files: "git log --name-status -5\n"
<user.git> log files <number>: "git log --name-status -{number}\n"
<user.git> log [changes | code]: "git log -c "
<user.git> log clip:
    insert("git log -1 -c ")
    edit.paste()


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

git merge base: "git merge-base "
git merge base {user.git_branches}: "git merge-base {git_branches} HEAD"

git merge (cancel|quit): "git merge --quit\n"

git merge pull request: user.insert_between("git pull origin pull/", "/head:")
git merge pull request <number>: "git pull origin pull/{number}/head:"
git merge upstream pull request:
    user.insert_between("git pull upstream pull/", "/head:")
git merge upstream pull request <number>: "git pull upstream pull/{number}/head:"

git merge: "git merge "
git merge {user.git_branches}: "git merge {git_branches}"
git merge ours: "git merge -X ours "
git merge theirs: "git merge -X theirs "
git merge clip:
    insert("git merge ")
    edit.paste()
git merge tool: "git mergetool\n"
git move: "git mv "
git new branch: "git checkout -b "
git prune: "git prune"
git remote prune origin: "git remote prune origin\n"

git pull: "git pull"
git pull origin: "git pull origin "
git pull rebase: "git pull --rebase "
git pull fast forward: "git pull --ff-only\n"
git pull <user.text>: "git pull {} "

(git|G) push: "git push\n"
(git|G) push origin: "git push origin "
(git|G) push up stream origin: "git push -u origin "
(git|G) push <user.text>: "git push {} "
(git|G) push tags: "git push --tags\n"

git rebase: "git rebase "
git rebase now: "git rebase\n"
# FIXME: add auto population of upstream branches
git rebase upstream main: "git rebase upstream/main\n"
git rebase upstream master: "git rebase upstream/master\n"
git rebase upstream dev: "git rebase upstream/dev\n"
git rebase upstream <user.text>: "git rebase upstream/{text}"
git rebase upstream: "git rebase upstream "
# NOTE - we don't use abort in the command because it conflicts with
# abort.talon
git rebase (cancel|quit): "git rebase --quit\n"
# GIT_EDITOR=true will keep the existing commit message
git rebase continue: "GIT_EDITOR=true git rebase --continue\n"
git rebase continue edit: "git rebase --continue\n"
git rebase skip: "git rebase --skip"
git remove: "git rm "
git remove cached: "git rm --cached"
git (remove | delete) remote branch: "git push --delete origin "
git remove remote origin: "git remote rm origin"
git reset: "git reset "
git reset soft: "git reset --soft "
git reset soft head: "git reset --soft HEAD~1"
git reset soft head <number_small>: "git reset --soft HEAD~{number_small}"
# git reset hard: "git reset --hard "
git reset hard: "git stash -u "
# FIXME: See about a way to do something stash-equivalent so we don't really just lose everything
# git reset hard head: "git reset --hard HEAD~1"
 #git reset hard head <number_small>: "git reset --hard HEAD~{number_small}"

# These two are useful for mass commit squashing
git reset [merge] base {user.git_branches}: "git reset --soft $(git merge-base {git_branches} HEAD)"


git restore: "git restore "
# Purposefully no \n because it is destructive
git restore all: "git restore --source=HEAD :/"
git restore staged: "git restore --staged "
get restore staged all: "git restore --staged :/\n"
git restore source: "git restore --source="
# This allows you to remove file(s) from HEAD^ and then git commit --amend
git restore commited file:  "git restore -s@^ -S -- "
get remote set origin: "git remote set-url origin "
git remote: "git remote "
git remote add: "git remote add "
git remote add origin: "git remote add origin "
git remote add upstream: "git remote add upstream "
git remote list: "git remote -v\n"
git remote set url: "git remote set-url "
git remote remove: "git remote remove "
git remote rename: "git remote rename "
git [remote] show [remote] origin: "git remote show origin\n"
git revert: "git revert "
git revert clip:
    insert("git revert ")
    edit.paste()
git show: "git show "
git show clip:
    insert("git show ")
    edit.paste()
    key(enter)
git show (code | change): "git show -c"
git show (code | change) clip:
    insert("git show -c")
    edit.paste()
    key(enter)
git show (head | last): "git show -c HEAD\n"
git show (head | last) [minus] <number>: "git show -c HEAD~{number}\n"
git change head to main:
    "git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main\n"
get stash help: "git stash --help\n"
git stash pop: "git stash pop\n"
git stash: "git stash\n"
git stash rebase:
    "git stash -m 'Talon auto stash'\n"
    "git fetch && git rebase\n"
    "git stash pop\n"
git stash push: user.insert_between("git stash push -m '", "'")
git stash apply: "git stash apply\n"
git stash list: "git stash list\n"
git stash show: "git stash show"

(git status|G stat): "git status --untracked-files=no\n"
(git status|G stat) (all | full | everything): "git status\n"
(git status|G stat) staged: "git status --short | grep '^[MARCD]'\n"

git sub tree: "git subtree "
git switch: "git switch "
git switch {user.git_branches}: "git switch {git_branches}"
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
git tag add: user.insert_between('git tag -a v", " -m ""')
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
    user.insert_between('git stash push{args} --message "{message}', '"')

# Optimistic execution for frequently used commands that are harmless (don't
# change repository or index state).
# XXX - revisit as I'm just favouring my old stuff for now
#git status$: "git status\n"
git add patch$: "git add --patch"
# git add patch all: "git add --patch\n"
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
    insert("\ngit commit\n")

git dump completions:
    user.git_dump_completions()

# git commit automation convenience
<user.git> calm flake:
    insert("git add flake.lock\n")
    insert("git commit -m 'chore: update flake.lock'\n")
    # because prettier always tweaks the lock file
    insert("git add flake.lock\n")
    insert("git commit -m 'chore: update flake.lock'\n")

<user.git> calm lists:
    insert("git add -u\n")
    insert("git status --untracked-files=no\n")
    insert("git commit -m 'chore: update lists'")

# Personal convenience scripts
<user.git> smart rebase:
    "git-smart-rebase\n"
