tag: terminal
-

json query [<user.zsh_file_completion>]:
    insert("jq . ")
    insert(zsh_file_completion or "")
json query clip:
    insert("jq . ")
    edit.paste()
    key(enter)
json length [<user.zsh_file_completion>]:
    insert("jq '. | length' ")
    insert(zsh_file_completion or "")
json length nested [<user.zsh_file_completion>]:
    file = zsh_file_completion or ""
    user.insert_between("jq '.", " | length' {file}")
