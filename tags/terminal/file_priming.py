from talon import Context, Module

mod = Module()
mod.list(
    "nix_way_template_languages",
    "Supported languages for the-nix-way flake dev-templates",
)

ctx = Context()
ctx.matches = r"""
os: linux
app: terminal
"""


@mod.capture(rule="file prime")
def file_prime(m) -> str:
    """Term for priming file from templates"""
    return str(m)


# https://github.com/the-nix-way/dev-templates
ctx.lists["user.nix_way_template_languages"] = {
    "bun": "bun",
    "c": "c-cpp",
    "clojure": "clojure",
    "c sharp": "csharp",
    "cue": "cue",
    "dhall": "dhall",
    "elixir": "elixir",
    "elm": "elm",
    "gleam": "gleam",
    "go": "go",
    "hashicorp": "hashi",
    "haxe": "haxe",
    "java": "java",
    "kotlin": "kotlin",
    "latex": "latex",
    "nickel": "nickel",
    "nim": "nim",
    "nix": "nix",
    "node": "node",
    "ocaml": "ocaml",
    "open policy agent": "opa",
    "php": "php",
    "proto buf": "protobuf",
    "pulumi": "pulumi",
    "purescript": "purescript",
    "python": "python",
    "r": "r",
    "ruby": "ruby",
    "rust": "rust",
    "scala": "scala",
    "shell": "shell",
    "swift": "swift",
    "vlang": "vlang",
    "zig": "zig",
}
