tag: terminal
-

# NOTE: I favor `fd` over `find` for most cases. `fd` is faster,  has a simpler syntax, and honors `.gitignore` by
# default. If you need to use find, use the "find old" version. It is handy to keep both versions here in case inside of
# an ssh shell that doesn't have it

file find:
    user.insert_between('fd ', ' 2>/dev/null')
file old find:
    user.insert_between('find . -name "', '" 2>/dev/null')
file find clip:
    insert("find . -name ")
    user.paste_without_new_lines()
    key(enter)
file find file clip:
    insert("find . -type f -name ")
    user.paste_without_new_lines()
    key(enter)
file find file [<user.word>]:
    user.insert_between('find . -type f -name ""', '"" 2>/dev/null')
    insert(word or "")
file find folder clip:
    insert("find . -type d -name ")
    user.paste_without_new_lines()
    key(enter)
file find folder [<user.word>]:
    user.insert_between('find . -type d -name ""', '"" 2>/dev/null')
    insert(word or "")
# case insensitive fuzzy find
file fuzzy find [<user.word>]:
    user.insert_between('fd --glob "*', '*" 2>/dev/null')
    insert(word or "")
file old fuzzy find [<user.word>]:
    user.insert_between('find . -iname "*', '*" 2>/dev/null')
    insert(word or "")
file fuzzy hash:
    user.insert_between('find . -path "*", "*" -exec sha256sum {{}} \\; 2>/dev/null')

file fuzzy find depth <number> [<user.word>]:
    user.insert_between('find . -maxdepth {number} -iname "*", "*" 2>/dev/null')
    insert(word or "")
(file fuzzy find folder | folder fuzzy find) [<user.word>]:
    user.insert_between('find . -type d -iname "*", "*" 2>/dev/null')
    insert(word or "")
(file fuzzy find folder | folder fuzzy find) depth <number> [<user.word>]:
    user.insert_between('find . -maxdepth {number} -type d -iname "*", "*" 2>/dev/null')
    insert(word or "")
file fuzzy find today [<user.word>]:
    user.insert_between('find . -mtime -1 -name "*", "*" 2>/dev/null')
    insert(word or "")
file fuzzy find (at|in) clip:
    insert("find ")
    user.paste_without_new_lines()
    user.insert_between(' -iname "*", "*" 2>/dev/null')

file find all links:
     insert("find . -maxdepth 1 -type l  -ls\n")
file find all folders:
     insert("find . -maxdepth 1 -type d  -ls\n")
file find all files:
     insert("find . -maxdepth 1 -type f  -ls\n")

file find (all | type) {user.file_extension}:
    'fd --type f  --glob "*{file_extension}"\n'
file old find (all | type) {user.file_extension}:
    'find . -type f  -name "*{file_extension}"\n'
file find excluding with depth:
    user.insert_between("find . -mindepth 2 -maxdepth 2 -type d '!' -exec sh -c 'ls -1 \"{}\"|egrep -i -q \"^*.", "$\"' ';' -print")
file find excluding:
    user.insert_between("find . -type d '!' -exec sh -c 'ls -1 \"{}\"|egrep -i -q \"^*.", "$\"' ';' -print")
