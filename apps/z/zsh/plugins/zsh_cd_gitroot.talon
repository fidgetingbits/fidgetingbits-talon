tag: user.zsh_cd_gitroot
-

<user.go> [project] [git] root:
    edit.delete_line()
    insert("cd-gitroot\n")
<user.go> [project] (next|parent|grand) [git] root:
    edit.delete_line()
    insert("cd-gitroot && ../ && cd-gitroot\n")
