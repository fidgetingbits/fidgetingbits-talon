tag: terminal
and tag: user.nix_cli
-

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
nix build help: "nix-build --help\n"
nix build: "nix-build "
nix build standard: "nix-build '<nixpkgs>' -A "
nix build with paths:
    user.insert_between("nix build nixpkgs#", "--print-out-paths --no-link")
nix build local package:
    "nix-build -E 'with import <nixpkgs> {{}}; pkgs.callPackage ./default.nix {{}}'"

# Flakes Commands
nix build flake: "nix build"
nix build flake with paths:
    user.insert_between("nix build nixpkgs#", "--print-out-paths --no-link")

nix flake check: "nix flake check\n"
nix flake update: "nix flake update\n"

nix develop [flake]: "nix develop\n"

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
