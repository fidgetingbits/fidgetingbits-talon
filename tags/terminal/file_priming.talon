os: linux
os: mac
app: terminal
-

envy flake init:
    insert("echo 'use flake' > .envrc\n")
    insert("git add flake.nix .envrc\n")
    insert("direnv allow\n")
