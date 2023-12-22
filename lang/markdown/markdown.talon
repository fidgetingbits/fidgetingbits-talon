code.language: markdown
-

(level | heading | header) one:
    edit.line_start()
    "# "
(level | heading | header) two:
    edit.line_start()
    "## "
(level | heading | header) three:
    edit.line_start()
    "### "
(level | heading | header) four:
    edit.line_start()
    "#### "
(level | heading | header) five:
    edit.line_start()
    "##### "
(level | heading | header) six:
    edit.line_start()
    "###### "

list [one]:
    edit.line_start()
    "- "
list two:
    edit.line_start()
    "    - "
list three:
    edit.line_start()
    "        - "
list four:
    edit.line_start()
    "            - "
list five:
    edit.line_start()
    "                - "
list six:
    edit.line_start()
    "                    - "

lang {user.markdown_code_block_language}: "{user.markdown_code_block_language}"
code block {user.markdown_code_block_language}:
    "```{markdown_code_block_language}"
    sleep(200ms)
    key(enter:2)
    insert("```")
    key(enter)
    key(up:2)

empty code block:
    insert("```")
    sleep(200ms)
    key(enter:2)
    insert("```")
    key(enter)
    key(up:2)

gravy {user.markdown_code_block_language}: insert("```{markdown_code_block_language}")

# NOTE: We purposefully pre insert the closing ``` so that we can avoid auto
# tabbing from potentially pasted code
# IMPORTANT: longer sleep to allow for pasting seems to be required on some systems
code block {user.markdown_code_block_language} clip:
    "```{markdown_code_block_language}"
    sleep(200ms)
    key(enter:2)
    insert("```")
    key(enter)
    key(up:2)
    edit.paste()
    sleep(200ms)
    key(down:2)

code block clip:
    insert("```")
    sleep(200ms)
    key(enter:2)
    insert("```")
    key(enter)
    key(up:2)
    edit.paste()
    sleep(200ms)
    key(down:2)
    # XXX - would be nice if this had something like the ability to then find
    # the next set of ```

put link:
    "[]()"
    key(left:3)

put task: "- [ ] "
pour task:
    edit.line_end()
    edit.line_insert_down()
    "- [ ] "
drink task:
    edit.line_start()
    edit.line_insert_up()
    "- [ ] "

put list path: user.insert_between("- `", "`: ")
pour list path:
    edit.line_end()
    edit.line_insert_down()
    user.insert_between("- `", "`: ")

make list:
    edit.line_start()
    "- "
