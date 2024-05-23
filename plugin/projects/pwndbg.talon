user.working_folder: ~/dev/pwndbg
-

run muscle tests:
    edit.delete_line()
    insert("nix build .#pwndbg-dev; ./tests.sh --nix musl\n")
