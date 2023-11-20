app: firefox
-
tag(): browser
tag(): user.tabs
tag(): user.pages
#tag(): user.vimium

tab search:
    browser.focus_address()
    insert("% ")
tab search <user.text>$:
    browser.focus_address()
    insert("% {text}")
    key(down)
tab jump <user.text>$:
    browser.focus_address()
    insert("% {text}")
    sleep(500ms)
    key(down)
    sleep(500ms)
    key(enter)

outline that:
    browser.focus_address()
    key(home)
    insert("outline.com/")
    key(end enter)
archive that:
    browser.focus_address()
    key(home)
    insert("https://web.archive.org/web/*/")
    key(end enter)

(sidebar | panel) bookmarks: user.firefox_bookmarks_sidebar()
(sidebar | panel) history: user.firefox_history_sidebar()

side dog: key(f1)

# Automate tabbing through accepting an untrusted certificate
accept certificate:
    key(tab:2)
    key(enter)
    key(pgdown)
    # There seems to be a purposeful delay for this item to be clickable
    sleep(2s)
    key(tab:2)
    key(enter)
