app: terminal
tag: user.nix_cli
-

# TODO:
# - This should be tied to nix3 tag, and the other to non-flake
# - Need to breakup the old commands

# Special words
nix packages: "'<nixpkgs>'"

# Edit some derivation that already exists in nixpkgs
nix edit package: "nix edit nixpkgs#"

# Use public nix index database (updated weekly) to find package location
nix remote index: "nix run github:mic92/nix-index-database "
# Use nix index database locally
nix locate: "nix-locate "

# Store
nix store help: "nix-store --help\n"
nix store query dependencies: "nix-store --query --references "
# When playing with a local result, it would be nice to just throw on a 'result' command, and have it auto-complete

# Build
nix old build help: "nix-build --help\n"
nix old build: "nix-build "
nix old build standard: "nix-build '<nixpkgs>' -A "
nix old build local package:
    "nix-build -E 'with import <nixpkgs> {{ config = {{ allowUnfree = true;}}; }}; pkgs.callPackage ./package.nix {{}}'"

# FIXME: Move this to private, since I use a private path
nix old build nix package:
    insert("cd ~/dev/nix/nixpkgs\n")
    user.insert_between("nix-build -I nixpkgs=$PWD -E 'with import <nixpkgs> {{}}; callPackage ./pkgs/by-name/", " {{}}'")

# Flake build commands
nix build: "nix build "
nix build (this|now): "nix build .\n"
nix build (this|now) impure: "nix build --impure .\n"
nix build show traces: "nix build --show-trace "

nix build log: "nix build -L "
nix build impure: "nix build --impure "
nix build with paths:
    user.insert_between("nix build nixpkgs#", "--print-out-paths --no-link")
nix build debug: " nix build --verbose --debug --print-build-logs\n"
nix build output {user.flake_outputs}: "nix build {flake_outputs}\n"
nix build package:
    "nix build --impure --expr 'with import <nixpkgs> {{ config = {{ allowUnfree = true; }}; }}; pkgs.callPackage ./package.nix {{}}'"

nix flake check: "nix flake check\n"
nix flake update: "nix flake update\n"
nix flake meta data: "nix flake metadata\n"
nix flake show: "nix flake show\n"
# nix flake lock update: "nix flake lock --update-input "
nix flake list inputs: "nix flake metadata --json | jq -r '.locks.nodes.root.inputs | keys[]'\n"
nix flake lock update {user.flake_inputs}: "nix flake lock --update-input {flake_inputs}\n"

nix (dev|develop) [flake]: "nix develop\n"

nix eval: "nix-instantiate --eval "
nix strict eval: "nix-instantiate --eval --strict "
nix eval local package:
    "nix-instantiate --eval -E 'with import <nixpkgs> {{}}; pkgs.callPackage ./default.nix {{}}'"
nix strict eval local package:
    "nix-instantiate --eval --strict -E 'with import <nixpkgs> {{}}; pkgs.callPackage ./default.nix {{}}'"
nix instantiate: "nix-instantiate -A "


nix tree: "nix-tree\n"

# Garbage Collection
nix collect [garbage]: "nix-collect-garbage\n"
nix collect help: "nix-collect-garbage --help\n"
nix collect profiles: "nix-collect-garbage --delete-older-than 7d"
nix collect all profiles: "nix-collect-garbage -d"

nix list generations: "nix-env --list-generations\n"

nix show (drive|derivation): "nix derivation show "
nix show (drive|derivation) clip:
    insert("nix derivation show")
    edit.paste()
    key(enter)

nix profile install: "nix profile install nixpkgs#"
nix profile remove: "nix profile remove "
nix profile list: "nix profile list"

nix run: "nix run "
nix run impure: "nix run --impure "
nix run impure here: "nix run --impure .\n"
nix run here: "nix run .\n"
nix run this impure: "nix run --impure .\n"
nix run this: "nix run .\n"
nix format: "nix fmt\n"


nix flake check all: "nix flake check --all-systems\n"

# Stuff useful for hacking on nixpkgs
nix export packages: "export NIXPKGS=$PWD"
nix search local: "nix-env -f $NIXPKGS -qaP '*'"
nix build local: "nix-build $NIXPKGS -A "

# NixOS Installation Commands
nix O S enter: "nixos-enter\n"

nix shell with [<user.text>]:
    insert('nix shell nixpkgs#{text or ""}')

nix shell command with:
    user.insert_between("nix shell nixpkgs#", " --command ")

nix [store] show dependencies: "nix-store -q --references"

[run] nix repl: "nix repl\n"
[run] nix repl with flake packages: "nix repl --extra-experimental-features 'flakes repl-flake' nixpkgs\n"
[run] nix repl with packages: "nix repl --expr 'import <nixpkgs>{}'\n"

nix repl evaluate: "nix repl --eval "

nix eval with packages: user.insert_between("nix eval --impure --expr '(let pkgs = import <nixpkgs>{}; in ", ")'")

nix log: "nix log "
nix log clip:
    insert("PAGER=cat nix log ")
    user.paste_without_new_lines()
    key(enter)

# Personal alias
nix log last: "nix-log-last\n"
