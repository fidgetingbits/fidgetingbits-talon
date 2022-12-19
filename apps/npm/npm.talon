tag: user.npm
-

node update: "npm update\n"
node global update: "npm -g update\n"
node install: "npm install "
node global install: "npm -g install "
node uninstall: "npm uninstall "
node global uninstall: "npm -g uninstall "
node list: "npm list\n"
node global list: "npm -g list\n"
node list depth <number_small>: "npm list --depth={number_small}\n"
node global list <number_small>: "npm -g list --depth={number_small}\n"
node config set prefix:
    insert("npm config set prefix ''")
    edit.left()
