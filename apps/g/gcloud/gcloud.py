from talon import Context, Module


ctx = Context()
mod = Module()

mod.list("gcloud_buckets", desc="Buckets in gcloud.")

# Add your own GCloud namespaces here, or override the defaults in your private glab files
ctx.lists["user.gcloud_buckets"] = {}
