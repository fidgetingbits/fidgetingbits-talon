from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = """
tag: user.gpg
"""


@mod.action_class
class GpgActions:
    def gpg_list_short_form_keys():
        """Lists all GPG keys in short form"""
        actions.insert(
            r"""gpg --list-keys --with-colons | awk -F: '/^pub:/ {keyid=$5} /^uid:/ {print "ID: " keyid, "Email: " $10}'"""
        )
