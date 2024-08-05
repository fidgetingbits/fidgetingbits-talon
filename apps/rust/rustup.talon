app: terminal
tag: user.rust_apps
-

<user.rustup>: "rustup "

<user.rustup> show: "rustup show\n"

<user.rustup> install: "rustup install"
<user.rustup> install {user.rust_toolchains}: "rustup install {user.rust_toolchains}"

<user.rustup> target add: "rustup target add "
<user.rustup> target add {user.rust_targets}: "rustup target add {rust_targets}\n"
<user.rustup> target list: "rustup target list\n"
<user.rustup> target list installed: "rustup target list --installed\n"

<user.rustup> component list: "rustup component list\n"
<user.rustup> component list search: "rustup component list | grep "
