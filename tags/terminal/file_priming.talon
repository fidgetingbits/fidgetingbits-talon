os: linux
os: mac
app: terminal
-

envy flake init:
    insert("echo 'use flake' > .envrc\n")
    insert("git add flake.nix .envrc\n")
    insert("direnv allow\n")

initialize dev project {user.nix_way_template_languages}:
    insert('nix flake init --template "https://flakehub.com/f/the-nix-way/dev-templates/*#{nix_way_template_languages}"')
