surf to {user.website}: user.open_url(website)
surf to clip: user.open_url(clip.text())
{user.search_engine} hunt <user.text>$:
    user.search_with_search_engine(search_engine, user.text)
{user.search_engine} (that | this):
    text = edit.selected_text()
    user.search_with_search_engine(search_engine, text)
{user.search_engine} clip: user.search_with_search_engine(search_engine, clip.text())
web site {user.website}: insert(website)
