app: terminal
tag: user.glab
-

gitlab help: "glab\n"
gitlab auth login: "glab auth login\n"

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
gitlab project list: "glab project list\n"
gitlab project create help: "glab project create --help\n"
gitlab project (create | new) public: "glab project create -P "
gitlab project (create | new) [private]: "glab project create -p "
gitlab project search: "glab search "
gitlab project search help: "glab search --help\n"

# issue
gitlab issue list help: "glab issue list --help\n"
gitlab issue list: "glab issue list\n"
