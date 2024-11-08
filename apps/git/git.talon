app: terminal
tag: user.git
-

<user.git> version:
    edit.delete_line()
    "git --version\n"

# Standard commands
<user.git> add patch:
    edit.delete_line()
    "git add . -p\n"
<user.git> add:
    edit.delete_line()
    "git add "
<user.git> add force:
    edit.delete_line()
    "git add -f "
<user.git> add (all | changed | everything):
    edit.delete_line()
    insert("git add -u\n")
<user.git> add intend (all  | everything):
    edit.delete_line()
    insert("git add --intent-to-add .\n")
# <user.git> add <user.zsh_path_completion>:
#     "git add {zsh_path_completion}"
<user.git> add <user.git_modified_files>:
    edit.delete_line()
    "git add {git_modified_files}"
# FIXME: This should be wrapped in some sort of generic path capture that supports base
<user.git> add base [<number>] <user.git_modified_files>:
    edit.delete_line()
    insert("git add ")
    index = number or -1
    insert(user.path_folder(git_modified_files, index))

<user.git> add untracked <user.git_untracked_files>:
    edit.delete_line()
    "git add {git_untracked_files}"
<user.git> add untracked everything:
   edit.delete_line()
    "git add .\n"
<user.git> add file type {user.file_extension}:
    edit.delete_line()
    "git add **/*{file_extension}"

<user.git> bisect:
    edit.delete_line()
    "git bisect "

<user.git> blame:
    edit.delete_line()
    "git blame "

<user.git> branch:
    edit.delete_line()
    "git branch "
<user.git> branch help:
    edit.delete_line()
    "git branch --help\n"
<user.git> branch list [all]:
    edit.delete_line()
    insert("git branch -a\n")
<user.git> branch list remote:
    edit.delete_line()
    insert("git branch -r\n")
<user.git> branch list local:

    edit.delete_line()
    insert("git branch\n")
<user.git> branch (remove | delete):
    edit.delete_line()
    "git branch -d "
<user.git> branch (remove | delete) force:
    edit.delete_line()
    "git branch -D "
<user.git> branch remove remote:
    edit.delete_line()
    "git push origin --delete "
<user.git> branch remove remote clip:
    edit.delete_line()
    "git push origin --delete "
    edit.paste()
<user.git> branch (remove | delete) <user.git_branches>:
    edit.delete_line()
    "git branch -d {git_branches}"
<user.git> branch (remove | delete) force <user.git_branches>:
    edit.delete_line()
    "git branch -D {git_branches}"
<user.git> branch remote:
    edit.delete_line()
    "git branch --remote\n"
<user.git> branch (rename | move):
    edit.delete_line()
    "git branch -m "

<user.git> checkout:
    edit.delete_line()
    "git checkout "
<user.git> checkout <user.git_branch>:
    edit.delete_line()
    insert("git checkout {git_branch}\n")
<user.git> checkout file <user.git_branch>:
    edit.delete_line()
    insert("git checkout {git_branch} -- ")
<user.git> checkout <user.git_tag>:
    edit.delete_line()
    "git checkout {git_tag}"
<user.git> checkout upstream (main | men):
    edit.delete_line()
    insert("git checkout upstream/main\n")
<user.git> checkout <number_small> before clip:
    edit.delete_line()
    insert("git checkout ")
    edit.paste()
    key("^:{number_small}")
    key(enter)
<user.git> checkout clip:
    edit.delete_line()
    insert("git checkout ")
    edit.paste()
    key(enter)

<user.git> check ignore:
    edit.delete_line()
    "git check-ignore -v "

<user.git> cherry pick:
    edit.delete_line()
    "git cherry-pick "
<user.git> cherry pick continue:
    edit.delete_line()
    "git cherry-pick --continue "
<user.git> cherry pick (cancel|quit):
    edit.delete_line()
    "git cherry-pick --quit "
<user.git> cherry pick skip:
    edit.delete_line()
    "git cherry-pick --skip "

<user.git> clone:
    edit.delete_line()
    "git clone "
<user.git> clone clip:
    edit.delete_line()
    insert("git clone ")
    edit.paste()
    key(enter)
<user.git> clone depth <number>:
    edit.delete_line()
    "git clone --depth {number} "
<user.git> clone depth <number> clip:
    edit.delete_line()
    insert("git clone --depth {number} ")
    edit.paste()
    key(enter)
# Leave \n out for confirmation since the operation is destructive

<user.git> clean:
    edit.delete_line()
    "git clean"
<user.git> clean everything:
    edit.delete_line()
    "git clean -dfx"
<user.git> clean untracked:
    edit.delete_line()
    "git clean -fd"

# <user.git> (commit|calm) [message] <user.text>:
#     edit.delete_line()
#     insert("git commit -m \"{text or ''}")
<user.git> (commit|calm) [message] <user.git_conventional_commits>:

    edit.delete_line()
    user.insert_between('git commit -m "{git_conventional_commits}', '"')
# git commit [message] {user.git_conventional_commits} <user.word>:
#     edit.delete_line()
#     insert(user.insert_between('git commit -m "{git_conventional_commits}({word}): ', '"'))
<user.git> (commit|calm) [message] <user.git_conventional_commits> <user.text>:
    edit.delete_line()
    user.insert_between('git commit -m "{git_conventional_commits}{text}', '"')
<user.git> (commit|calm) [message]:
    edit.delete_line()
    user.insert_between('git commit -m "', '"')
<user.git> (commit|calm) empty:
    edit.delete_line()
    insert("git commit\n")
<user.git> (commit|calm) amend:
    edit.delete_line()
    "git commit --amend "
<user.git> (commit|calm) amend no edit:
    edit.delete_line()
    "git commit --amend --no-edit\n"
<user.git> (commit|calm) no verify:
    edit.delete_line()
    "git commit -n"
<user.git> (commit|calm) existing:
    edit.delete_line()
    "git commit -a\n"
# git commit automation convenience
<user.git> (commit|calm) all {user.git_conventional_commits}:
    edit.delete_line()
    "git add -u\n"
    user.insert_between('git commit -m "{git_conventional_commits}: ', '"')
# Two useful commands when commit fails due to pre commit hook
<user.git> (commit|calm) again:
    edit.delete_line()
    key(ctrl-r)
    "git commit\n"
<user.git> (commit|calm) clip:
    edit.delete_line()
    user.insert_between('git commit -m "', '"')
    edit.paste()
    key(enter)
<user.git> re (commit|calm):
    edit.delete_line()
    'git status -s | grep -e "^MM" | cut -d" " -f2- | xargs git add\n'
    key(ctrl-r)
    sleep(500ms)
    "git commit -m\n"
    key(enter)


<user.git> config:
    edit.delete_line()
    "git config "
<user.git> config list:
    edit.delete_line()
    "git config --list\n"
<user.git> module ignore untracked [{user.git_submodule}]:
    edit.delete_line()
    # FIXME: It would be ideal if we could find the path to get module on the fly so this doesn't have to be from the root
    user.insert_between('git config -f .gitmodules submodule.', '.ignore untracked')
    insert(git_submodule or "")

##
# diff
##
<user.git> diff (colour | color) words:
    edit.delete_line()
    "git diff --color-words "
# REMINDER: This exists instead of a optional [<user.git_modified_files>] because sometimes I literally want to say
# git diff and just end up with git diff with no arguments yet
<user.git> (doll|diff all):
    edit.delete_line()
    "git diff\n"
<user.git> diff <user.git_modified_files>:
    edit.delete_line()
    insert("git diff ")
    insert(git_modified_files)
<user.git> diff cached:
    edit.delete_line()
    "git diff --cached\n"
<user.git> diff staged [<user.git_staged_files>]:
    edit.delete_line()
    insert("git diff --staged ")
    insert(git_staged_files or "")
<user.git> (stall|diff staged all):
    edit.delete_line()
    "git diff --staged\n"
<user.git> diff branch <user.git_branch>:
    edit.delete_line()
    "git diff {git_branch}\n"
<user.git> diff tag <user.git_tag>:
    edit.delete_line()
    "git diff {git_tag}\n"

<user.git> diff tool:
    edit.delete_line()
    "git difftool -d\n"
<user.git> diff tool cached:
    edit.delete_line()
    "git difftool --cached -d\n"
<user.git> diff names only:
    edit.delete_line()
    "git diff --name-only "
<user.git> diff status:
    edit.delete_line()
    "git diff --name-status "
<user.git> diff status <user.git_branch>:
    edit.delete_line()
    "git diff --name-status {git_branch}\n"


<user.git> fetch:
    edit.delete_line()
    "git fetch\n"
(git fetch and rebase|G base):
    edit.delete_line()
    "git fetch && git rebase\n"

<user.git> fetch prune:
    edit.delete_line()
    "git fetch --prune\n"
<user.git> fetch all:
    edit.delete_line()
    "git fetch --all\n"
<user.git> fetch <user.git_remote>:
    edit.delete_line()
    "git fetch {git_remote}\n"


<user.git> fetch (pull [request]| P R) <number>:
    edit.delete_line()
    "git fetch origin pull/{number}/head:"
<user.git> fetch (pull [request]| P R) clip:
    edit.delete_line()
    insert("git fetch origin pull/")
    edit.paste()
    insert("/head:")
<user.git> fetch <user.git_remote> (pull [request]| P R) <number>:
    edit.delete_line()
    "git fetch {git_remote} pull/{number}/head:"
<user.git> fetch <user.git_remote> (pull [request]| P R) clip:
    edit.delete_line()
    insert("git fetch {git_remote} pull/")
    edit.paste()
    insert("/head:")


#git fetch <user.text>: "git fetch {text}"
<user.git> filter branch:
    edit.delete_line()
    "git filter-branch --subdirectory-filter"

<user.git> garbage collect aggressive:
    edit.delete_line()
    "git gc --aggressive"

<user.git> ignore changes:
    edit.delete_line()
    "git update-index --assume-unchanged "

<user.git> in it:
    edit.delete_line()
    "git init\n"

<user.git> list files:
    edit.delete_line()
    "git ls-files\n"
<user.git> list modified:
    edit.delete_line()
    "git ls-files -m\n"
<user.git> list tracked <user.git_branch>:
    edit.delete_line()
    "git ls-files -r {git_branch} --name-only\n"
<user.git> list ignored:
    edit.delete_line()
    "git ls-files . --ignored --exclude-standard --others\n"
<user.git> list untracked:
    edit.delete_line()
    "git ls-files . --ignored --exclude-standard --others\n"

<user.git> show hook folder:
    edit.delete_line()
    "git rev-parse --git-path hooks\n"

<user.git> log all:
    edit.delete_line()
    "git log\n"
<user.git> log all pretty:
    edit.delete_line()
    "git log --pretty=oneline\n"
<user.git> log all changes:
    edit.delete_line()
    "git log -c\n"
<user.git> log:
    edit.delete_line()
    "git log -5\n"
<user.git> log pretty:
    edit.delete_line()
    "git log -5 --pretty=oneline\n"
<user.git> log graph:
    edit.delete_line()
    "git log -5 --graph --pretty=oneline\n"
<user.git> log graph all:
    edit.delete_line()
    "git log --graph --pretty=oneline\n"
<user.git> log find upstream P R:
    edit.delete_line()
    user.insert_between('git log --pretty=oneline --grep="#', '" upstream/main')
<user.git> log diff:
    edit.delete_line()
    "git log -p -5\n"
<user.git> log reverse:
    edit.delete_line()
    "git log -5 --reverse\n"
<user.git> log <number>:
    edit.delete_line()
    "git log -{number}\n"
<user.git> log diff <number>:
    edit.delete_line()
    "git log -p -{number}\n"
<user.git> log files:
    edit.delete_line()
    "git log --name-status -5\n"
<user.git> log files <number>:
    edit.delete_line()
    "git log --name-status -{number}\n"
<user.git> log [changes | code]:
    edit.delete_line()
    "git log -c "
<user.git> log clip:

    edit.delete_line()
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
<user.git> log added files:
    edit.delete_line()
    "git log --diff-filter=A --summary\n"
<user.git> log added files only:
    edit.delete_line()
    "git log --diff-filter=A --summary | grep create\n"
<user.git> log removed files:
    edit.delete_line()
    "git log --diff-filter=D --summary\n"
<user.git> log removed files only:
    edit.delete_line()
    "git log --diff-filter=D --summary | grep delete\n"

<user.git> merge base:
    edit.delete_line()
    "git merge-base "
<user.git> merge base <user.git_branch>:
    edit.delete_line()
    "git merge-base {git_branch} HEAD"
<user.git> merge (cancel|quit):
    edit.delete_line()
    "git merge --quit\n"
<user.git> merge pull request:
    edit.delete_line()
    user.insert_between("git pull origin pull/", "/head:")
<user.git> merge pull request <number>:
    edit.delete_line()
    "git pull origin pull/{number}/head:"
<user.git> merge upstream pull request:
    edit.delete_line()
    user.insert_between("git pull upstream pull/", "/head:")
<user.git> merge upstream pull request <number>:
    edit.delete_line()
    "git pull upstream pull/{number}/head:"
<user.git> merge:
    edit.delete_line()
    "git merge "
<user.git> merge <user.git_branch>:
    edit.delete_line()
    "git merge {git_branch}"
<user.git> merge ours:
    edit.delete_line()
    "git merge -X ours "
<user.git> merge theirs:
    edit.delete_line()
    "git merge -X theirs "
<user.git> merge clip:
    edit.delete_line()
    insert("git merge ")
    edit.paste()
<user.git> merge tool:
    edit.delete_line()
    "git mergetool\n"

<user.git> move:
    edit.delete_line()
    "git mv "

<user.git> new branch:
    edit.delete_line()
    "git checkout -b "

<user.git> prune:
    edit.delete_line()
    "git prune"
<user.git> remote prune <user.git_remote>:
    edit.delete_line()
    "git remote prune {git_remote}\n"

<user.git> pull:
    edit.delete_line()
    "git pull"
<user.git> pull <user.git_remote>:
    edit.delete_line()
    "git pull {git_remote} "
<user.git> pull rebase:
    edit.delete_line()
    "git pull --rebase "
<user.git> pull fast forward:
    edit.delete_line()
    "git pull --ff-only\n"

<user.git> push:
    edit.delete_line()
    "git push\n"
<user.git> force push:
    edit.delete_line()
    "git push --force-with-lease"
<user.git> push <user.git_remote>:
    edit.delete_line()
    "git push {git_remote} "
<user.git> push mirror [<user.git_remote>]:
    edit.delete_line()
    insert("git push --mirror ")
    insert(git_remote or "")

<user.git> push [to] up stream <user.git_remote> [<user.git_branch>]:
    edit.delete_line()
    insert("git push -u {git_remote} ")
    insert(git_branch or "")
<user.git> push tags:
    edit.delete_line()
    "git push --tags\n"

<user.git> rebase:
    edit.delete_line()
    "git rebase "
<user.git> rebase now:
    edit.delete_line()
    "git rebase\n"
# FIXME: add auto population of upstream branches
<user.git> rebase upstream main:
    edit.delete_line()
    "git rebase upstream/main\n"
<user.git> rebase upstream master:
    edit.delete_line()
    "git rebase upstream/master\n"
<user.git> rebase upstream dev:
    edit.delete_line()
    "git rebase upstream/dev\n"
<user.git> rebase upstream <user.text>:
    edit.delete_line()
    "git rebase upstream/{text}"
<user.git> rebase upstream:
    edit.delete_line()
    "git rebase upstream "
# NOTE - we don't use abort in the command because it conflicts with
# abort.talon
<user.git> rebase (cancel|quit):
    edit.delete_line()
    "git rebase --quit\n"
# GIT_EDITOR=true will keep the existing commit message
<user.git> rebase continue:
    edit.delete_line()
    "GIT_EDITOR=true git rebase --continue\n"
<user.git> rebase continue edit:
    edit.delete_line()
    "git rebase --continue\n"
<user.git> rebase skip:
    edit.delete_line()
    "git rebase --skip"

<user.git> remove [(<user.git_modified_files>|<user.zsh_path_completions>)]:
    edit.delete_line()
    insert("git rm ")
    optional = zsh_path_completions or git_modified_files
    insert(optional or "")
<user.git> remove cached:
    edit.delete_line()
    "git rm --cached"
<user.git> (remove | delete) remote branch:
    edit.delete_line()
    "git push --delete origin "
<user.git> remove remote origin:
    edit.delete_line()
    "git remote rm origin"

<user.git> reset:
    edit.delete_line()
    "git reset "
<user.git> reset soft:
    edit.delete_line()
    "git reset --soft "
<user.git> reset soft head:
    edit.delete_line()
    "git reset --soft HEAD~1"
<user.git> reset soft head <number_small>:
    edit.delete_line()
    "git reset --soft HEAD~{number_small}"
# git reset hard: "git reset --hard "
<user.git> reset hard:
    edit.delete_line()
    "git stash -u "
# FIXME: See about a way to do something stash-equivalent so we don't really just lose everything
# git reset hard head: "git reset --hard HEAD~1"
 #git reset hard head <number_small>: "git reset --hard HEAD~{number_small}"
# These two are useful for mass commit squashing
<user.git> reset [merge] base <user.git_branch>:
    edit.delete_line()
    "git reset --soft $(git merge-base {git_branch} HEAD)"

<user.git> restore:
    edit.delete_line()
    "git restore "
<user.git> restore [<user.git_modified_files>]:
    edit.delete_line()
    insert("git restore ")
    insert(git_modified_files or "")
<user.git> restore staged:
    edit.delete_line()
    "git restore --staged "
<user.git> restore staged <user.git_staged_files>:
    edit.delete_line()
    insert("git restore --staged {git_staged_files}")

# Purposefully no \n because it is destructive
<user.git> restore all:
    edit.delete_line()
    "git restore --source=HEAD :/"
get restore staged all:
    edit.delete_line()
    "git restore --staged :/\n"
<user.git> restore source:
    edit.delete_line()
    "git restore --source="
# This allows you to remove file(s) from HEAD^ and then git commit --amend
<user.git> restore commited file:
    edit.delete_line()
    "git restore -s@^ -S -- "
get remote set origin:
    edit.delete_line()
    "git remote set-url origin "

<user.git> remote:
    edit.delete_line()
    "git remote "
<user.git> remote add [<user.text>]:
    edit.delete_line()
    insert("git remote add ")
    insert(text or "")
<user.git> remote add origin:
    edit.delete_line()
    "git remote add origin "
<user.git> remote add upstream:
    edit.delete_line()
    "git remote add upstream "
<user.git> remote list:
    edit.delete_line()
    "git remote -v\n"
<user.git> remote set url:
    edit.delete_line()
    "git remote set-url "
<user.git> remote (remove|delete) [<user.git_remotes>]:
    edit.delete_line()
    insert("git remote rm ")
    insert(git_remotes or "")
<user.git> remote rename [<user.git_remote>]:
    edit.delete_line()
    insert("git remote rename ")
    insert(git_remote or "")
<user.git> [remote] show [remote] <user.git_remote>:
    edit.delete_line()
    "git remote show {git_remote}\n"

<user.git> revert:
    edit.delete_line()
    "git revert "
<user.git> revert clip:
    edit.delete_line()
    insert("git revert ")
    edit.paste()

<user.git> show:
    edit.delete_line()
    "git show "
<user.git> show clip:
    edit.delete_line()
    insert("git show ")
    edit.paste()
    key(enter)
<user.git> show (code | change):
    edit.delete_line()
    "git show -c"
<user.git> show (code | change) clip:
    edit.delete_line()
    insert("git show -c")
    edit.paste()
    key(enter)
<user.git> show (head | last):
    edit.delete_line()
    "git show -c HEAD\n"
<user.git> show (head | last) [minus] <number>:
    edit.delete_line()
    "git show -c HEAD~{number}\n"
<user.git> show names:
    edit.delete_line()
    "git show --name-status "
<user.git> show names clip:
    edit.delete_line()
    insert("git show --name-status ")
    edit.paste()
    key(enter)
<user.git> show names (head | last):
    edit.delete_line()
    "git show --name-status HEAD\n"
<user.git> show names (head | last) [minus] <number>:
    edit.delete_line()
    "git show --name-status HEAD~{number}\n"

<user.git> change head to main:
    edit.delete_line()
    "git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main\n"
<user.git> stash help:
    edit.delete_line()
    "git stash --help\n"
<user.git> stash pop:
    edit.delete_line()
    "git stash pop\n"
<user.git> stash:
    edit.delete_line()
    "git stash\n"
# This will stash untracked files as well
<user.git> stash everything:
    edit.delete_line()
    "git stash -u\n"
<user.git> stash rebase:
    edit.delete_line()
    "git stash -m 'Talon auto stash'\n"
    "git fetch && git rebase\n"
    "git stash pop\n"
<user.git> stash push:
    edit.delete_line()
    user.insert_between("git stash push -m '", "'")
<user.git> stash apply:
    edit.delete_line()
    "git stash apply\n"
<user.git> stash list:
    edit.delete_line()
    "git stash list\n"
<user.git> stash show:
    edit.delete_line()
    "git stash show "
<user.git> stash drop:
    edit.delete_line()
    "git stash drop "

<user.git> (status|stat) long:
    edit.delete_line()
    "git status --untracked-files=no\n"
<user.git> (status|stat) [sum]:
    edit.delete_line()
    "git status -s --untracked-files=no\n"
<user.git> (status|stat) (all | full | everything):
    edit.delete_line()
    "git status\n"
<user.git> (status|stat) [sum] (all | full | everything):
    edit.delete_line()
    "git status -s\n"
<user.git> (status|stat) staged:
    edit.delete_line()
    "git status -s | grep '^[MARCD]'\n"

<user.git> sub tree:
    edit.delete_line()
    "git subtree "
<user.git> switch:
    edit.delete_line()
    "git switch "
<user.git> switch <user.git_branch>:
    edit.delete_line()
    "git switch {git_branch}"
<user.git> switch detached:
    edit.delete_line()
    "git switch --detach "
<user.git> (switch create | new branch) [<user.text>]:
    edit.delete_line()
    "git switch -c {user.formatted_text(text or '', 'DASH_SEPARATED')}"
<user.git> switch orphan:
    edit.delete_line()
    "git switch --orphan "
<user.git> switch clip:
    edit.delete_line()
    insert("git switch ")
    edit.paste()
    key(enter)

<user.git> [sub] module add:
    edit.delete_line()
    "git submodule add "
<user.git> [sub] module add clip:
    edit.delete_line()
    insert("git submodule add ")
    edit.paste()
<user.git> [sub] module delete:
    edit.delete_line()
    "git rm  "
<user.git> [sub] module status:
    edit.delete_line()
    "git submodule status\n"
<user.git> [sub] module status recurse:
    edit.delete_line()
    "git submodule status --recursive\n"
<user.git> [sub] module sink:
    edit.delete_line()
    "git submodule sync\n"
<user.git> [sub] module update:
    edit.delete_line()
    "git submodule update --init --recursive --remote --progress"
<user.git> [sub] module update shallow:
    edit.delete_line()
    "git submodule update --init --recursive --remote --progress --depth 1"
<user.git> [sub] module set U R L:
    edit.delete_line()
    "git submodule set-url "
<user.git> [sub] module list:
    edit.delete_line()
    'git ls-files --stage | grep "^160000 "\n'

<user.git> tag:
    edit.delete_line()
    "git tag "
<user.git> tag list:
    edit.delete_line()
    "git --no-pager tag\n"
<user.git> tag list specific:
    edit.delete_line()
    insert('git tag -l ""')
    edit.left()
<user.git> tag add:
    edit.delete_line()
    user.insert_between('git tag -a v", " -m ""')
<user.git> tag remove:
    edit.delete_line()
    "git tag -d "
<user.git> tag remove remote:
    edit.delete_line()
    "git push origin --delete "

# XXX - revisit this with sublists for ones I want to always run with \n, as
#git {user.git_command} [<user.git_arguments>]:
#    args = git_arguments or ""
#    "git {git_command}{args} "
#git commit [<user.git_arguments>] message [<user.prose>]:
#    args = git_arguments or ""
#    message = prose or ""
#    user.insert_between("git commit{args} --message '{message}", "'")
<user.git> stash [push] [<user.git_arguments>] message [<user.prose>]:
    edit.delete_line()
    args = git_arguments or ""
    message = prose or ""
    user.insert_between('git stash push{args} --message "{message}', '"')

<user.git> add patch$:
    edit.delete_line()
    "git add --patch"

# Convenience
<user.git> diff highlighted:
    edit.copy()
    edit.delete_line()
    insert("git diff ")
    edit.paste()
    key(enter)
<user.git> diff clip:
    edit.delete_line()
    insert("git diff ")
    edit.paste()
    key(enter)

<user.git> add highlighted:
    edit.copy()
    edit.delete_line()
    insert("git add ")
    edit.paste()
    key(enter)
<user.git> add clip:
    edit.delete_line()
    insert("git add ")
    edit.paste()
    key(enter)

<user.git> commit highlighted:
    edit.copy()
    edit.delete_line()
    insert("git add ")
    edit.paste()
    insert("\ngit commit\n")

# git commit automation convenience
<user.git> calm flake:
    edit.delete_line()
    insert("git add flake.lock\n")
    insert("git commit -m 'chore: update flake.lock'\n")
    # because prettier always tweaks the lock file
    insert("git add flake.lock\n")
    insert("git commit -m 'chore: update flake.lock'\n")

<user.git> calm lists:
    edit.delete_line()
    insert("git add -u\n")
    insert("git status --untracked-files=no\n")
    insert("git commit -m 'chore: update lists'")

# Personal convenience scripts
<user.git> smart rebase:
    edit.delete_line()
    "git-smart-rebase\n"

<user.git> undo amend:
    edit.delete_line()
    # ᕙ(◕ل͜◕)ᕗ
    # https://stackoverflow.com/questions/1459150/how-to-undo-git-commit-amend-done-instead-of-git-commit
    "git reset --soft HEAD@{1}"
