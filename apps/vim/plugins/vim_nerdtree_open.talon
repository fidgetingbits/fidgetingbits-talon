tag: user.vim_nerdtree
win.title: /NERD_tree/
-
# XXX - lot of these should just to override the same functions I used for vim

change root: key(C)
close parent: key(x)
close all children: key(X)
folder refresh: key(r)
folder root refresh: key(R)
[folder] root up: key(u)
[folder] root up day: key(U)

# file node mappings
node open <number_small>$:
    insert(":{number_small}\n")
    key(o)
node recursive open: key(O)
node open: key(o)
node [open] [in] split: key(i)
node [open] [in] vertical [split]: key(s)

# directory node mappings
node close <number_small>$:
    insert(":{number_small}\n")
    key(o)
node close parent: key(x)
node close all: key(X)
folder edit: key(e)

# filesystem mappings
nerd menu: key(m)

# menu-based actions
(file | node) (add | new): "ma"
folder (add | new):
    insert("ma/")
    edit.left()
(node | file) (remove | delete): "md"
(node | file) (move | rename): "mm"
(node | file) list: "ml"
(node | file) copy: "mc"

# tree navigation mappings
[folder] go root: key(P)
[folder] go parent: key(p)
[folder] go first: key(K)
[folder] go last: key(J)

# tree filtering mappings
[file] show hidden [files]: key(I)

# other mappings
[nerd] quick help: key(?)
nerd close: key(q)
