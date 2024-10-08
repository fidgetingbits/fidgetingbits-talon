app: terminal
tag: user.rust_apps
-

<user.rustup>: "rustup "


<user.rustup> show: "rustup show\n"
<user.rustup> default: "rustup default\n"


<user.rustup> install: "rustup install"
<user.rustup> install {user.rust_toolchains}: "rustup install {user.rust_toolchains}"
<user.rustup> uninstall: "rustup uninstall"
<user.rustup> uninstall {user.rust_toolchains}: "rustup uninstall {user.rust_toolchains}"

<user.rustup> target add: "rustup target add "
<user.rustup> target add {user.rust_targets}: "rustup target add {rust_targets}\n"
<user.rustup> target remove: "rustup target remove "
<user.rustup> target remove {user.rust_targets}: "rustup target remove {rust_targets}\n"
<user.rustup> target list [installed]: "rustup target list --installed\n"
<user.rustup> target list all: "rustup target list \n"


<user.rustup> tool chain list [all]: "rustup toolchain list -v\n"

<user.rustup> component list all: "rustup component list\n"
<user.rustup> component list [installed]: "rustup component list --installed\n"
<user.rustup> component list search: "rustup component list | rg -i "
