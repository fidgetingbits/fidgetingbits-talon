from talon import Context, Module


ctx = Context()
mod = Module()

mod.list("gitlab_namespace", desc="Project namespaces in GitLab.")
mod.list("gitlab_server", desc="GitLab servers.")

# Add your own GitLab namespaces here, or override the defaults in your private glab files
ctx.lists["user.gitlab_namespace"] = {}

# Add your own GitLab servers here, or override the defaults in your private glab files
ctx.lists["user.gitlab_server"] = {
    "gitlab": "https://gitlab.com/",
}
