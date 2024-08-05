# I use tide to mean escaped
question [mark]: "?"
score: "_"
double dash: "--"

docky: '"""'
ticky: "'''"
gravy: "```"
quest E: "???"
sexy: "XXX"
bang E: "!!!"

(dot dot | dotdot): ".."
(ellipses | dotty): "..."
tickle: "''"
snipped code: "[SNIPPED]"
(spam | spamma): ", "
stacked: ": "
arrow: "->"
dub arrow: "=>"
new line: "\\n"
tide new line: "\\\\n"
carriage: "\\r"
tide carriage: "\\\\r"
line feed: "\\r\\n"
tide line feed: "\\\\r\\\\n"
end of file: "EOF"
dashing: "-- "
prompt: "❯"

# NOTE: You made this explicit because it kept conflicting with cursorless `round wrap ...`
[pair] rounder: user.insert_between("(", ")")
tide round: user.insert_between("\\(", "\\)")

[pair] (brackets | braces | curly): user.insert_between("{", "}")
tide (brackets | braces | curly): user.insert_between("\\{", "\\}")

[pair] squares: user.insert_between("[", "]")
tide (squares | list): user.insert_between("\\[", "\\]")

[pair] (angles | diamond): user.insert_between("<", ">")
tide (angles | diamond): user.insert_between("\\<", "\\>")

[pair] primus: user.insert_between("'", "'")
tide primus: user.insert_between("\\'", "\\'")

[pair] quotes: user.insert_between('"', '"')
tide quotes: user.insert_between('\\"', '\\"')

[pair] slashes: user.insert_between("/", "/")
tide slashes: user.insert_between("\\/", "\\/")

[pair] (graves | skis): user.insert_between("`", "`")
[pair] percents: user.insert_between("%", "%")
[pair] stacks: user.insert_between(":", ":")

# NOTE: purposely no edit.left()
[pair] ampers: "&&"

# Because of turbo fish from rust: ::<>
turbo: "::"

# FIXME(cursorless): Some of these should probably only be enabled if not in cursorless?
angles that:
    text = edit.selected_text()
    user.paste("<{text}>")
(squares) that:
    text = edit.selected_text()
    user.paste("[{text}]")
(braces) that:
    text = edit.selected_text()
    user.paste("{{{text}}}")
round that:
    text = edit.selected_text()
    user.paste("({text})")
percent that:
    text = edit.selected_text()
    user.paste("%{text}%")
quote that:
    text = edit.selected_text()
    user.paste("'{text}'")
(double quote | dub quote) that:
    text = edit.selected_text()
    user.paste('"{text}"')
(globby | glob line):
    insert("s///g")
    key(left:3)
(grave | back tick) that:
    text = edit.selected_text()
    user.paste("`{text}`")
