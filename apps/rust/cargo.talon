tag: user.rust_apps
-

cargo init:
    "cargo init "
cargo new:
    "cargo new "
cargo run:
    "cargo run\n"
cargo run release:
    "cargo run --release\n"
cargo add:
    "cargo add "
cargo add {user.rust_crates}:
    "cargo add {rust_crates}\n"
cargo remove:
    "cargo remove "
cargo install:
    "cargo install "
cargo uninstall:
    "cargo uninstall "
cargo run with args:
    "cargo run -- "
cargo run release with arg:
    "cargo run --release -- "
cargo build:
    "cargo build\n"
cargo build release:
    "cargo build --release\n"
cargo build (all|workspace):
    "cargo build --workspace\n"
# TODO: It would be nice to automatically derive valid packages
cargo build package:
    "cargo build --package "
cargo build package <user.text>:
    "cargo build --package {text}"
cargo test:
    "cargo test\n"
cargo check:
    "cargo check\n"
cargo clean:
    "cargo clean\n"
rustup:
    "rustup "
