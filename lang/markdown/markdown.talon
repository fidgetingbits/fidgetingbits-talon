tag: user.markdown
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

{user.markdown_code_block_language} block:
    "```{markdown_code_block_language}"
    key(enter:2)
    "```"
    key(up)

link:
    "[]()"
    key(left:3)


code block:
    insert("```\n\n")
    insert("```\n")
    key(up:2)

code block python:
    insert("```python\n\n")
    insert("```\n")
    key(up:2)

code block see:
    insert("```cpp\n\n")
    insert("```\n")
    key(up:2)

gravy see: insert("```cpp")

code block bash:
    insert("```bash\n\n")
    insert("```\n")
    key(up:2)

code block clip:
    insert("```\n\n")
    insert("```\n")
    key(up:2)
    edit.paste()
    # XXX - would be nice if this had something like the ability to then find
    # the next set of ```

paste as code:
    insert("```\n\n")
    insert("```\n")
    key(up:2)
    edit.paste()

paste as bash code:
    insert("```bash\n\n")
    insert("```\n")
    key(up:2)
    edit.paste()

paste as see code:
    insert("```cpp\n\n")
    insert("```\n")
    key(up:2)
    edit.paste()

paste as python code:
    insert("```python\n\n")
    insert("```\n")
    key(up:2)
    edit.paste()

link clip: user.insert_cursor_paste("[[|]](", ")")

#link selected:
#    edit.cut()
#    key([)
#    user.insert_cursor_paste("[[|]](", ")")
#    edit.paste()

# XXX - turn the word under the cursor into a link
# link this:

put task: "- [ ] "
pour task:
    edit.line_end()
    edit.line_insert_down()
    "- [ ] "