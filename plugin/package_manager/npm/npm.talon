app: terminal
tag: user.nodejs
tag: user.packager_node
-

node search: user.nodejs_package_search()
node install <user.text>: user.nodejs_package_install_by_name(text or "")
node install local: user.nodejs_package_local_install()
node remove: user.nodejs_package_remove()
node remove local: user.nodejs_package_local_remove()
node update [<user.text>]: user.nodejs_package_update(text or "")


# node config set prefix:
#     insert(f"{user.nodejs_packager()} config set prefix ''")
#     edit.left()
# node list depth <number_small>: insert(f"{user.nodejs_packager()} list --depth={number_small}\n")
node run {user.nodejs_scripts}:
    user.nodejs_packager()
    insert(" run {user.nodejs_scripts}")
