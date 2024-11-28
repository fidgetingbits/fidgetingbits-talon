app: terminal
tag: user.glab
-

gitlab help: "glab\n"
gitlab auth login [{user.gitlab_server}]:
    insert("glab auth login ")
    if gitlab_server: insert("--hostname {gitlab_server}")
    key(enter)
gitlab auth status: "glab auth status\n"

# projects
#  archive:     Get an archive of the repository.
#  clone:       Clone a GitLab repository/project
#  contributors: Get repository contributors list.
#  create:      Create a new GitLab project/repository.
#  delete:      Delete an existing repository on GitLab.
#  fork:        Create a fork of a GitLab repository
#  list:        Get list of repositories.
#  mirror:      Mirror a project/repository to the specified location using pull or push method.
#  search:      Search for GitLab repositories and projects by name
#  transfer:    Transfer a repository to a new namespace.
#  view:        View a project/repositorsty

gitlab project help: "glab project\n"
gitlab project list [{user.gitlab_server}]:
    if gitlab_server: insert("GITLAB_HOST=https://{gitlab_server} ")
    insert("glab project list -P 100")
gitlab project list help: "glab project list --help\n"
gitlab project list all [{user.gitlab_server}]:
    if gitlab_server: insert("GITLAB_HOST=https://{gitlab_server} ")
    insert("glab project list -P 100 --all")
gitlab project create help: "glab project create --help\n"
gitlab project (create | new) public: "glab project create -P "
gitlab project (create | new) [private]: "glab project create -p "
gitlab project search: "glab project search "
gitlab project search help: "glab project search --help\n"
gitlab project view [{user.gitlab_server}] [{user.gitlab_namespace}]:
    edit.delete_line()
    insert("PAGER=cat glab project view ")
    insert(user.gitlab_server or "")
    insert(gitlab_namespace or "")
gitlab project {user.gitlab_namespace} (create|new): "glab project create -p -g {gitlab_namespace} "

gitlab group list [{user.gitlab_server}]:
    if gitlab_server: insert("GITLAB_HOST=https://{gitlab_server} ")
    insert("glab api groups | jq -r '.[].name'")

# issue
gitlab issue list help: "glab issue list --help\n"
gitlab issue list [{user.gitlab_server}]:
    if gitlab_server: insert("GITLAB_HOST=https://{gitlab_server} ")
    insert("glab issue list")

gitlab put {user.gitlab_server}: "{gitlab_server}"
gitlab put host var {user.gitlab_server}: insert("GITLAB_HOST=https://{gitlab_server}")
