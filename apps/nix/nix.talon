tag: terminal
and tag: user.nix_cli
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
    "nix-build -E 'with import <nixpkgs> {{}}; pkgs.callPackage ./default.nix {{}}'"

# FIXME: Move this to private, since I use a private path
nix old build nix package:
    insert("cd ~/dev/nix/nixpkgs\n")
    user.insert_between("nix-build -I nixpkgs=$PWD -E 'with import <nixpkgs> {}; callPackage ./pkgs/by-name/", " {}'")

nix build with paths:
    user.insert_between("nix build nixpkgs#", "--print-out-paths --no-link")

# Flake build commands
nix build: "nix build "
nix build (this|now): "nix build .\n"
nix build log: "nix build -L "
nix build impure: "nix build --impure "
nix build with paths:
    user.insert_between("nix build nixpkgs#", "--print-out-paths --no-link")
nix build debug: " nix build --verbose --debug --print-build-logs\n"

nix flake check: "nix flake check\n"
nix flake update: "nix flake update\n"

nix (dev|develop) [flake]: "nix develop\n"

nix eval: "nix-instantiate --eval "
nix strict eval: "nix-instantiate --eval --strict "
nix eval local package:
    "nix-instantiate --eval -E 'with import <nixpkgs> {{}}; pkgs.callPackage ./default.nix {{}}'"
nix strict eval local package:
    "nix-instantiate --eval --strict -E 'with import <nixpkgs> {{}}; pkgs.callPackage ./default.nix {{}}'"
nix instantiate: "nix-instantiate -A "

run nix repl: "nix repl\n"

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

nix run impure: "nix run --impure\n"
nix run here: "nix run\n"
nix format: "nix fmt\n"

nix flake check all: "nix flake check --all-systems\n"

# Stuff useful for hacking on nixpkgs
nix export packages: "export NIXPKGS=$PWD"
nix search local: "nix-env -f $NIXPKGS -qaP '*'"
nix build local: "nix-build $NIXPKGS -A "

# NixOS Installation Commands
nix O S enter: "nixos-enter\n"

nix shell with:
    "nix shell nixpkgs#"

nix shell command with:
    user.insert_between("nix shell nixpkgs#", " --command ")
