-
path <user.paths>: "{paths}"
path escaped <user.paths>: insert(user.escape_path("{paths}"))
# TODO: this may be best suited for something like file_management.talon
pivot <user.folder_paths>: "cd {folder_paths}\n"
