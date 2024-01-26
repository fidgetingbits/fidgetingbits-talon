os: linux
and tag: terminal
os: mac
and tag: terminal
-

prime env R C:
    insert("echo 'use flake' > .envrc\n")
    insert("git add flake.nix .envrc\n)
    insert("direnv allow\n")
