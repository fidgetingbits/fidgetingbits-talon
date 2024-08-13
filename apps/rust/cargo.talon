app: terminal
tag: user.rust_apps
-

cargo init: "cargo init "
cargo init (library | lib): "cargo init --lib "
cargo new: "cargo new "

cargo run: "cargo run\n"
cargo run help: "cargo run -- --help\n"
cargo run release: "cargo run --release\n"
cargo run with args: "cargo run -- "
cargo run release with args: "cargo run --release -- "

cargo add [dep] [package {user.cargo_workspace_packages}] [{user.rust_crates}]:
    insert("cargo add --package ")
    if cargo_workspace_packages: insert(cargo_workspace_packages + " ")
    if rust_crates: insert(rust_crates)
cargo add dev [dep] [package {user.cargo_workspace_packages}] [{user.rust_crates}]:
    insert("cargo add --dev ")
    if cargo_workspace_packages: insert(cargo_workspace_packages + " ")
    if rust_crates: insert(rust_crates)

cargo remove [dep] [package {user.cargo_workspace_packages}] [{user.rust_crates}]:
    insert("cargo remove --package ")
    if cargo_workspace_packages: insert(cargo_workspace_packages + " ")
    if rust_crates: insert(rust_crates)
cargo remove dev [dep] [package {user.cargo_workspace_packages}] [{user.rust_crates}]:
    insert("cargo remove --dev ")
    if cargo_workspace_packages: insert(cargo_workspace_packages + " ")
    if rust_crates: insert(rust_crates)

cargo install: "cargo install "
cargo install <user.text>: "cargo install {text}"
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

cargo tree: "cargo tree\n"
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
cargo tree dupe: "cargo tree --duplicate\n"

