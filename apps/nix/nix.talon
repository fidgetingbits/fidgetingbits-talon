tag: terminal
and tag: user.nix_cli
-

# Special words
nix pack: "'<nixpkgs>'"

# Edit some derivation that already exists in nixpkgs
nix edit package: "nix edit nixpkgs#"

nix build: "nix build"
nix build with paths:
    user.insert_between("nix build nixpkgs#", "--print-out-paths --no-link")

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



# Flakes Commands
nix build flake: "nix build"
nix build flake with paths: user.insert_between("nix build nixpkgs#", "--print-out-paths --no-link")

nix flake check: "nix flake check\n"
nix flake update: "nix flake update\n"

nix develop [flake]: "nix develop\n"
