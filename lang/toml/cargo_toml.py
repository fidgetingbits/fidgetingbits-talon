from talon import Context, Module, actions, settings

mod = Module()
mod.list("cargo_toml_keys", desc="List of common Cargo.toml table keys")
mod.list("cargo_toml_tables", desc="List of common Cargo.toml table names")
mod.list("cargo_toml_arrays", desc="List of common Cargo.toml array-of-table names")


ctx = Context()
ctx.matches = r"""
code.language: toml
title: /Cargo.toml/
"""


cargo_toml_tables = dict()
for name in [
    "package",
    "dependencies",
    "dev-dependencies",
    "build-dependencies",
    "lib",
    "badges",
    "features",
    "lints",
    "patch",
    "replace",
    "profile",
    "workspace",
]:
    cargo_toml_tables = name
ctx.lists["self.cargo_toml_tables"] = cargo_toml_tables

cargo_toml_keys = dict()
for name in [
    "name",
    "version",
    "authors",
    "edition",
    "description",
    "license",
    "repository",
    "homepage",
    "documentation",
    "readme",
    "keywords",
    "categories",
    "workspace members",
    "exclude",
    "include",
    "publish",
    "metadata",
    "default-run",
    "features",
    "dependencies",
    "dev dependencies",
    "build dependencies",
    "target",
    "patch",
    "replace",
    "profile",
    "badges",
    "lib",
    "bin",
    "example",
    "test",
    "bench",
    "doctest",
    "build",
    "doc",
    "bench",
    "check",
    "test",
    "run",
    "bench",
    "bench",
    "release",
    "debug",
    "panic",
    "incremental",
    "rpath",
    "lto",
    "codegen units",
]:
    cargo_toml_keys = name
ctx.lists["self.cargo_toml_keys"] = cargo_toml_keys
ctx.lists["self.cargo_toml_arrays"] = {
    "bin": "bin",
}
