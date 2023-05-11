-
path <user.paths>: user.paste("{paths}")
path escaped <user.paths>: user.paste(user.escape_path("{paths}"))

path dev loop <number>: "/dev/loop{number}"
path dev loop <number> part <number>: "/dev/loop{number_1}p{number_2}"