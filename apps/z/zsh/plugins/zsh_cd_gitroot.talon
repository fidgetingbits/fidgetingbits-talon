tag: user.zsh_cd_gitroot
-

<user.go> [project] [git] root:
    edit.delete_line()
    insert("cd-gitroot\n")
<user.go> [project] [git] (next|parent|grand) root:
    edit.delete_line()
    insert("cd-gitroot && ../ && cd-gitroot\n")
