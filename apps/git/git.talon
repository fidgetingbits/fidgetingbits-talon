tag: terminal
and tag: user.git
-

# Standard commands
<user.git> add patch: "git add . -p\n"
<user.git> add: "git add "
<user.git> add force: "git add -f "
<user.git> add (all | changed | everything):
    edit.delete_line()
    insert("git add -u\n")
<user.git> add <user.zsh_path_completion>:
    "git add {zsh_path_completion}\n"

<user.git> bisect: "git bisect "

<user.git> blame: "git blame "

<user.git> branch: "git branch "
<user.git> branch help: "git branch --help\n"
<user.git> branch list [all]:
    edit.delete_line()
    insert("git branch -a\n")
<user.git> branch list remote:
    edit.delete_line()
    insert("git branch -r\n")
<user.git> branch list local:
    edit.delete_line()
    insert("git branch\n")
<user.git> branch (remove | delete): "git branch -d "
<user.git> branch (remove | delete) force: "git branch -D "
<user.git> branch remove remote: "git push origin --delete "
<user.git> branch remove remote clip:
    "git push origin --delete "
    edit.paste()
<user.git> branch remote: "git branch --remote\n"
<user.git> branch (rename | move): "git branch -m "
<user.git> branch <user.text>: "git branch {text}"

<user.git> checkout: "git checkout "
<user.git> checkout {user.git_branches}:
    edit.paste()
    insert("git checkout {git_branches}\n")
<user.git> checkout file {user.git_branches}:
    edit.paste()
    insert("git checkout {git_branches} -- ")
<user.git> checkout upstream (main | men):
    edit.delete_line()
    insert("git checkout upstream/main\n")
<user.git> checkout <number_small> before clip:
    insert("git checkout ")
    edit.paste()
    key("^:{number_small}")
    key(enter)
<user.git> checkout clip:
    edit.delete_line()
    insert("git checkout ")
    edit.paste()
    key(enter)

<user.git> check ignore: "git check-ignore -v "

<user.git> cherry pick: "git cherry-pick "
<user.git> cherry pick continue: "git cherry-pick --continue "
<user.git> cherry pick (cancel|quit): "git cherry-pick --quit "
<user.git> cherry pick skip: "git cherry-pick --skip "

<user.git> clone: "git clone "
<user.git> clone clip:
    edit.delete_line()
    insert("git clone ")
    edit.paste()
    key(enter)
<user.git> clone depth <number>: "git clone --depth {number} "
<user.git> clone depth <number> clip:
    edit.delete_line()
    insert("git clone --depth {number} ")
    edit.paste()
    key(enter)
# Leave \n out for confirmation since the operation is destructive

<user.git> clean: "git clean"
<user.git> clean everything: "git clean -dfx"
<user.git> clean untracked: "git clean -fd"

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
<user.git> re (commit|calm):
    'git status -s | grep -e "^MM" | cut -d" " -f2- | xargs git add\n'
    key(ctrl-r)
    sleep(500ms)
    "git commit -m\n"
    key(enter)

<user.git> diff (colour | color) words: "git diff --color-words "
<user.git> diff: "git diff "
<user.git> diff cached: "git diff --cached\n"
<user.git> diff staged: "git diff --staged\n"
<user.git> diff {user.git_branches}: "git diff {git_branches}  \n"
<user.git> diff tool: "git difftool -d\n"
<user.git> diff tool cached: "git difftool --cached -d\n"
<user.git> diff names only: "git diff --name-only "

<user.git> fetch: "git fetch\n"
(git fetch and rebase|G base): "git fetch && git rebase\n"

<user.git> fetch prune: "git fetch --prune\n"
<user.git> fetch all: "git fetch --all\n"
<user.git> fetch upstream: "git fetch upstream\n"
<user.git> fetch (pull | P R) <number>: "git fetch origin pull/{number}/head:"
<user.git> fetch upstream (pull | P R) <number>: "git fetch upstream pull/{number}/head:"

#git fetch <user.text>: "git fetch {text}"
<user.git> filter branch: "git filter-branch --subdirectory-filter"

<user.git> garbage collect aggressive: "git gc --aggressive"

<user.git> ignore changes: "git update-index --assume-unchanged "

<user.git> in it: "git init\n"

<user.git> list files: "git ls-files\n"
<user.git> list modified: "git ls-files -m\n"
<user.git> list tracked {user.git_branches}: "git ls-files -r git_branches --name-only\n"
<user.git> list ignored: "git ls-files . --ignored --exclude-standard --others\n"
<user.git> list untracked: "git ls-files . --ignored --exclude-standard --others\n"

<user.git> show hook folder: "git rev-parse --git-path hooks\n"

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
<user.git> log added files: "git log --diff-filter=A --summary\n"
<user.git> log added files only: "git log --diff-filter=A --summary | grep create\n"
<user.git> log removed files: "git log --diff-filter=D --summary\n"
<user.git> log removed files only: "git log --diff-filter=D --summary | grep delete\n"

<user.git> merge base: "git merge-base "
<user.git> merge base {user.git_branches}: "git merge-base {git_branches} HEAD"
<user.git> merge (cancel|quit): "git merge --quit\n"
<user.git> merge pull request: user.insert_between("git pull origin pull/", "/head:")
<user.git> merge pull request <number>: "git pull origin pull/{number}/head:"
<user.git> merge upstream pull request:
    user.insert_between("git pull upstream pull/", "/head:")
<user.git> merge upstream pull request <number>: "git pull upstream pull/{number}/head:"
<user.git> merge: "git merge "
<user.git> merge {user.git_branches}: "git merge {git_branches}"
<user.git> merge ours: "git merge -X ours "
<user.git> merge theirs: "git merge -X theirs "
<user.git> merge clip:
    insert("git merge ")
    edit.paste()
<user.git> merge tool: "git mergetool\n"

<user.git> move: "git mv "

<user.git> new branch: "git checkout -b "

<user.git> prune: "git prune"
<user.git> remote prune origin: "git remote prune origin\n"

<user.git> pull: "git pull"
<user.git> pull origin: "git pull origin "
<user.git> pull rebase: "git pull --rebase "
<user.git> pull fast forward: "git pull --ff-only\n"
<user.git> pull <user.text>: "git pull {} "

<user.git> push: "git push\n"
<user.git> push origin: "git push origin "
<user.git> push up stream origin: "git push -u origin "
<user.git> push <user.text>: "git push {} "
<user.git> push tags: "git push --tags\n"

<user.git> rebase: "git rebase "
<user.git> rebase now: "git rebase\n"
# FIXME: add auto population of upstream branches
<user.git> rebase upstream main: "git rebase upstream/main\n"
<user.git> rebase upstream master: "git rebase upstream/master\n"
<user.git> rebase upstream dev: "git rebase upstream/dev\n"
<user.git> rebase upstream <user.text>: "git rebase upstream/{text}"
<user.git> rebase upstream: "git rebase upstream "
# NOTE - we don't use abort in the command because it conflicts with
# abort.talon
<user.git> rebase (cancel|quit): "git rebase --quit\n"
# GIT_EDITOR=true will keep the existing commit message
<user.git> rebase continue: "GIT_EDITOR=true git rebase --continue\n"
<user.git> rebase continue edit: "git rebase --continue\n"
<user.git> rebase skip: "git rebase --skip"

<user.git_remotes> remove [<user.zsh_path_completion>]:
    insert("git rm ")
    insert(zsh_path_completion or "")
<user.git> remove cached: "git rm --cached"
<user.git> (remove | delete) remote branch: "git push --delete origin "
<user.git> remove remote origin: "git remote rm origin"

<user.git> reset: "git reset "
<user.git> reset soft: "git reset --soft "
<user.git> reset soft head: "git reset --soft HEAD~1"
<user.git> reset soft head <number_small>: "git reset --soft HEAD~{number_small}"
# git reset hard: "git reset --hard "
<user.git> reset hard: "git stash -u "
# FIXME: See about a way to do something stash-equivalent so we don't really just lose everything
# git reset hard head: "git reset --hard HEAD~1"
 #git reset hard head <number_small>: "git reset --hard HEAD~{number_small}"
# These two are useful for mass commit squashing
<user.git> reset [merge] base {user.git_branches}: "git reset --soft $(git merge-base {git_branches} HEAD)"


<user.git> restore: "git "
<user.git>restore [<user.zsh_path_completion>]:
    insert("git restore ")
    insert(zsh_path_completion or "")
<user.git> restore staged: "git restore --staged "
<user.git> restore staged [<user.zsh_path_completion>]:
    insert("git restore --staged ")
    insert(zsh_path_completion or "")
# Purposefully no \n because it is destructive
<user.git> restore all: "git restore --source=HEAD :/"
get restore staged all: "git restore --staged :/\n"
<user.git> restore source: "git restore --source="
# This allows you to remove file(s) from HEAD^ and then git commit --amend
<user.git> restore commited file:  "git restore -s@^ -S -- "
get remote set origin: "git remote set-url origin "

<user.git> remote: "git remote "
<user.git> remote add [<user.git_remotes>]:
    insert("git remote add ")
    insert(git_remotes or "")
# FIXME: Confirm these aren't needed after using the above action
<user.git> remote add origin: "git remote add origin "
<user.git> remote add upstream: "git remote add upstream "
<user.git> remote list: "git remote -v\n"
<user.git> remote set url: "git remote set-url "
<user.git> remote remove: "git remote remove "
<user.git> remote rename: "git remote rename "
<user.git> [remote] show [remote] origin: "git remote show origin\n"

<user.git> revert: "git revert "
<user.git> revert clip:
    insert("git revert ")
    edit.paste()

<user.git> show: "git show "
<user.git> show clip:
    insert("git show ")
    edit.paste()
    key(enter)
<user.git> show (code | change): "git show -c"
<user.git> show (code | change) clip:
    insert("git show -c")
    edit.paste()
    key(enter)
<user.git> show (head | last): "git show -c HEAD\n"
<user.git> show (head | last) [minus] <number>: "git show -c HEAD~{number}\n"
<user.git> change head to main:
    "git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main\n"
get stash help: "git stash --help\n"
<user.git> stash pop: "git stash pop\n"
<user.git> stash: "git stash\n"
<user.git> stash rebase:
    "git stash -m 'Talon auto stash'\n"
    "git fetch && git rebase\n"
    "git stash pop\n"
<user.git> stash push: user.insert_between("git stash push -m '", "'")
<user.git> stash apply: "git stash apply\n"
<user.git> stash list: "git stash list\n"
<user.git> stash show: "git stash show"

<user.git> (status|stat): "git status --untracked-files=no\n"
<user.git> (status|stat) (all | full | everything): "git status\n"
<user.git> (status|stat) staged: "git status --short | grep '^[MARCD]'\n"

<user.git> sub tree: "git subtree "
<user.git> switch: "git switch "
<user.git> switch {user.git_branches}: "git switch {git_branches}"
<user.git> switch detached: "git switch --detach "
<user.git> (switch create | new branch) [<user.text>]:
    "git switch -c {user.formatted_text(text or '', 'DASH_SEPARATED')}"
<user.git> switch orphan: "git switch --orphan "
<user.git> switch clip:
    insert("git switch ")
    edit.paste()
    key(enter)

<user.git> [sub] module add: "git submodule add "
<user.git> [sub] module status: "git submodule status\n"
<user.git> [sub] module status recurse: "git submodule status --recursive\n"
<user.git> [sub] module sink: "git submodule sync\n"
<user.git> [sub] module update: "git submodule update --init --recursive --remote"
<user.git> module references: "git ls-files --stage | grep 160000\n"
<user.git> tag: "git tag "
<user.git> tag list: "git --no-pager tag\n"
<user.git> tag list specific:
    insert('git tag -l ""')
    edit.left()
<user.git> tag add: user.insert_between('git tag -a v", " -m ""')
<user.git> tag remove: "git tag -d "
<user.git> tag remove remote: "git push origin --delete "

# XXX - revisit this with sublists for ones I want to always run with \n, as
#git {user.git_command} [<user.git_arguments>]:
#    args = git_arguments or ""
#    "git {git_command}{args} "
#git commit [<user.git_arguments>] message [<user.prose>]:
#    args = git_arguments or ""
#    message = prose or ""
#    user.insert_between("git commit{args} --message '{message}", "'")
<user.git> stash [push] [<user.git_arguments>] message [<user.prose>]:
    args = git_arguments or ""
    message = prose or ""
    user.insert_between('git stash push{args} --message "{message}', '"')

# Optimistic execution for frequently used commands that are harmless (don't
# change repository or index state).
# XXX - revisit as I'm just favouring my old stuff for now
#git status$: "git status\n"
<user.git> add patch$: "git add --patch"
# git add patch all: "git add --patch\n"
#git show head$: "git show HEAD\n"
#git diff: "git diff\n"
#git diff (cached | cashed)$: "git diff --cached\n"

# Convenience
<user.git> clone clipboard:
    insert("git clone ")
    edit.paste()
    key(enter)
<user.git> diff highlighted:
    edit.copy()
    insert("git diff ")
    edit.paste()
    key(enter)
<user.git> diff clipboard:
    insert("git diff ")
    edit.paste()
    key(enter)

<user.git> add highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    key(enter)
<user.git> add clipboard:
    insert("git add ")
    edit.paste()
    key(enter)

<user.git> commit highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    insert("\ngit commit\n")

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
