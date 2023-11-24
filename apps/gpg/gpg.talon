tag: terminal
and tag: user.gpg
-

# Helpful gpg commands

G P G list long: "gpg --list-keys --fingerprint\n"
G P G list:
    user.gpg_list_short_form_keys()
    key(enter)
G P G list secret [keys]: "gpg --list-secret-keys\n"
G P G search:
    user.gpg_list_short_form_keys()
    insert(" | rg -i")
G P G search clip:
    user.gpg_list_short_form_keys()
    insert(" | rg -i ")
    edit.paste()
    key(enter)
G P G search global [keys]: "gpg --search-keys "
G P G export [key]: "gpg --export -a "
G P G import [key]: "gpg --import "

file encrypt with key:
    user.insert_between("gpg -v --trust-model always -e -r ", " file\n")
file encrypt with clip:
    insert("gpg -v --trust-model always -e -r ")
    edit.paste()
    insert(" ")
file decrypt: "gpg <file>\n"
