-
path <user.paths>: user.paste("{paths}")
path escaped <user.paths>: user.paste(user.escape_path("{paths}"))
# TODO: this may be best suited for something like file_management.talon
pivot <user.folder_paths>:
    user.paste("cd {folder_paths}")
    key(enter)
