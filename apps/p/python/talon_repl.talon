# XXX
tag: user.talon_repl
-

new pretty printer:
    insert("import pprint\n")
    insert("pp = pprint.PrettyPrinter()\n")
pretty print:
    insert("pp.pprint()")
    key(left)
