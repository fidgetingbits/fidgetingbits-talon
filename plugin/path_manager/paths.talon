file name {user.common_files}: insert("{common_files}")
path <user.paths>: insert("{paths}")
path escaped <user.paths>: insert(user.escape_path("{paths}"))
path dev loop <number>: "/dev/loop{number}"
path dev loop <number> part <number>: "/dev/loop{number_1}p{number_2}"

path windows <user.windows_paths>: insert("{windows_paths}")

