from urllib.parse import urlparse

from talon import Context, Module, actions, clip

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: browser
"""


def is_url(url):
    try:
        # Valid if url successfully parsed
        result = urlparse(url)
        # and contains both scheme (e.g. http) and netloc (e.g. github.com)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


@mod.action_class
class Actions:
    def browsers_go_clip():
        """Go to the URL in the clipboard"""


@ctx.action_class("browser")
class BrowserActions:
    def address():
        # Split title by space, check each token and token[1: -1] (it might be in brackets) for valid url.
        # Prioritize last one if multiple are valid, return empty string if none is valid.
        tokens = (
            url[1:-1] if not is_url(url) else url
            for url in reversed(actions.win.title().split(" "))
        )
        return next((url for url in tokens if is_url(url)), "")


@ctx.action_class("user")
class UserActions:
    def browsers_go_clip():
        """Go to the URL in the clipboard"""
        actions.browser.focus_address()
        actions.sleep("50ms")
        actions.insert(clip.text())
        actions.key("enter")
