question [mark]: "?"
score: "_"
double dash: "--"
triple quote: '"""'
triple tick: "'''"
gravy: "```"
# NOTE: riddle conflict with a rizzle, middle, etc
triple question: "???"
sexy: "XXX"
triple bang: "!!!"
(dot dot | dotdot): ".."
(ellipses | dotty): "..."
snipped code: "[SNIPPED]"
(comma and | spamma): ", "
arrow: "->"
dub arrow: "=>"
new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
end of file: "EOF"

empty (string | quotes): user.insert_between('"', '"')
empty escaped (string | quotes): user.insert_between('\\"', '\\"')
empty ticks: user.insert_between("'", "'")
empty escaped ticks: user.insert_between("\\'", "\\'")
empty round: user.insert_between("(", ")")
empty (square | list): user.insert_between("[", "]")
empty (bracket | braces): user.insert_between("{", "}")
empty percent: user.insert_between("%", "%")
empty coals: user.insert_between(":", ":")

[pair] (round): user.insert_between("(", ")")
escaped round: user.insert_between("\\(", "\\)")
escaped slashes: user.insert_between("\\/", "\\/")
[pair] (brackets | braces): user.insert_between("{", "}")
[pair] (square | squares): user.insert_between("[", "]")
[pair] angles: user.insert_between("<", ">")
[pair] graves: user.insert_between("`", "`")
[pair] percents: user.insert_between("%", "%")
[pair] ticks: user.insert_between("'", "'")
[pair] quotes: user.insert_between('"', '"')
[pair] slashes: user.insert_between("/", "/")
# NOTE: purposely no edit.left()
[pair] ampers: "&&"

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
