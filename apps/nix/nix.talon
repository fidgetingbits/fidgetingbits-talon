tag: terminal
and tag: user.nix_cli
-

# Edit some derivation that already exists in nixpkgs
nix edit package: "nix edit nixpkgs#"

nix build: "nix build"
nix build with paths: user.insert_between("nix build nixpkgs#", "--print-out-paths --no-link")

# Use public nix index database (updated weekly) to find package location
nix remote index: "nix run github:mic92/nix-index-database "
# Use nix index database locally
nix locate: "nix-locate "
