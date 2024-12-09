app: terminal
tag: user.rust_apps
-

cargo help: "cargo --help\n"
cargo init: "cargo init "
cargo init (library | lib): "cargo init --lib "

cargo new: "cargo new "
cargo new (library | lib): "cargo new --lib "

cargo update: "cargo update\n"

cargo run: "cargo run\n"
cargo run help: "cargo run -- --help\n"
cargo run release: "cargo run --release\n"
cargo run with args: "cargo run -- "
cargo run release with args: "cargo run --release -- "

# cargo add [--dev] [--package <package>] <crate>
cargo add [dep] [<user.rust_crates>]:
    insert("cargo add {rust_crates or ''}")
cargo add dev [dep] [<user.rust_crates>]:
    insert("cargo add --dev {rust_crates or ''}")
cargo add [dep] clip:
    insert("cargo add ")
    edit.paste()
cargo add dev [dep] clip:
    insert("cargo add --dev ")
    edit.paste()

# cargo add [--package <package>] --path <path>
cargo add [dep] local crate [<user.rust_local_crates>]:
    insert(f"cargo add {rust_local_crates or '--path '}")
cargo add dev local crate [dep] [<user.rust_local_crates>]:
    insert("cargo add --dev {rust_local_crates or '--path '}")

# cargo remove [--dev] [--package <package>] <crate>
cargo remove [dep] [<user.rust_crates>]:
    insert("cargo remove {rust_crates or ''}")
cargo remove dev [dep] [<user.rust_crates>]:
    insert("cargo remove --dev {rust_crates or ''}"))
cargo remove [dep] clip:
    insert("cargo remove ")
    edit.paste()
cargo remove dev [dep] clip:
    insert("cargo remove --dev ")
    edit.paste()

cargo install: "cargo install "
cargo install <user.text>: "cargo install {text}"
cargo install clip:
    insert("cargo install ")
    edit.paste()
cargo uninstall: "cargo uninstall "

cargo build: "cargo build\n"
cargo build with output: "cargo -vv build\n"
cargo build release: "cargo build --release\n"
cargo build all release: "cargo build --all --release\n"
cargo build release with output: "cargo -vv build --release\n"
cargo build (all | workspace): "cargo build --workspace\n"
cargo build package {user.cargo_workspace_packages}: "cargo build --package {cargo_workspace_packages}\n"
cargo build bin: "cargo build --bin "
cargo build lib: "cargo build --lib\n"

cargo test: "cargo test\n"
cargo test no capture: "cargo test -- --nocapture\n"
cargo test ignored: "cargo test -- --ignored\n"
cargo test ignored no capture: "cargo test -- --ignored --nocapture\n"

cargo check: "cargo check\n"
cargo clippy: "cargo clippy\n"

cargo doc: "cargo doc\n"

cargo clean: "cargo clean\n"
cargo clean package: "cargo clean --package "
cargo clean release: "cargo clean --release\n"
cargo clean release package: "cargo clean --release --package "

# These are command specific to cross, but to make it a little bit saner, I use cargo cross
cargo cross: "cross "
cargo cross windows: "cross build --target x86_64-pc-windows-gnu\n"
cargo cross windows release: "cross build --target x86_64-pc-windows-gnu --release\n"
cargo cross mac: "cross build --target x86_64-apple-darwin\n"
cargo cross mac release: "cross build --target x86_64-apple-darwin --release\n"
cargo cross linux: "cross build --target x86_64-unknown-linux-gnu\n"
cargo cross linux release: "cross build --target x86_64-unknown-linux-gnu --release\n"

cargo tree: "cargo tree\n"
cargo tree depth <number>: "cargo tree --depth {number}\n"
cargo tree dupe: "cargo tree --duplicate\n"


cargo flush locks: "rm -rf ~/.cargo/registry/index/* ~/.cargo/.package-cache"
