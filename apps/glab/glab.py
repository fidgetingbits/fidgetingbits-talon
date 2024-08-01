from talon import Context, Module


ctx = Context()
mod = Module()

mod.list("gitlab_namespace", desc="Project namespaces in GitLab.")

# Add your own GitLab namespaces here, or override the defaults in your private glab files
ctx.lists["user.gitlab_namespace"] = {}
