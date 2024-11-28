tag: terminal
user.working_folder: ~/dev/nix/nixpkgs
-

ghidra bump deps: "$(nix-build -A ghidra.mitmCache.updateScript)"
