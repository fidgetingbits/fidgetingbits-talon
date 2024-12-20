import subprocess
import shutil
import os
from pathlib import Path

from talon import Context, Module, actions, resource

mod = Module()
ctx = Context()

mod.list("cargo_crates", desc="Install packages inside a Cargo.toml")
mod.list("cargo_workspace_packages", desc="Cargo workspace packages")


def cargo_crates():
    # tomlq '.["dependencies"] | keys[]' Cargo.toml
    if not shutil.which("tomlq"):
        print("WARNING: Missing tomlq")
        return []
    query = '.["dependencies"] | keys[]'
    return subprocess.check_output(
        ("tomlq", query, "Cargo.toml"), cwd=actions.user.get_cwd()
    ).decode("utf-8")


@ctx.dynamic_list("user.cargo_crates")
def user_cargo_crates(m) -> dict[str, str]:
    """A dynamic list of staged git files"""

    crates = cargo_crates()
    return actions.user.create_spoken_forms_from_list(crates)


def cargo_workspace_packages():
    # tomlq '.["workspace"]["members"][]' Cargo.toml
    if not shutil.which("tomlq"):
        print("WARNING: Missing tomlq")
        return []
    query = '.["workspace"]["members"][]'
    entries = subprocess.check_output(
        ("tomlq", query, "Cargo.toml"), cwd=actions.user.get_cwd()
    ).decode("utf-8")
    # "crates/foo" -> foo" -> foo
    return [entry.split(os.sep)[-1].strip('"') for entry in entries.splitlines()]


@ctx.dynamic_list("user.cargo_workspace_packages")
def user_cargo_workspace_packages(m) -> dict[str, str]:
    """A dynamic list of cargo workspace packages"""

    packages = cargo_workspace_packages()
    spoken = actions.user.create_spoken_forms_from_list(packages)
    return spoken

    # package = "--package {cargo_workspace_packages or ''}"
    # if cargo_workspace_packages: insert(package + " ")
    # if rust_crates: insert(rust_crates)


@mod.capture(rule="[package {user.cargo_workspace_packages}] {user.rust_crates}")
def rust_crates(m) -> str:
    """Return a Rust crate name with an optional package name"""
    prefix = ""
    if "cargo_workspace_packages" in m:
        prefix = f"--package {m.cargo_workspace_packages}"
    return prefix + m.rust_crates


@mod.capture(rule="[package {user.cargo_workspace_packages}] {user.rust_crates}")
def rust_local_crates(m) -> str:
    """Return a Rust crate name with an optional package name"""
    prefix = ""
    if "cargo_workspace_packages" in m:
        prefix = f"--package {m.cargo_workspace_packages}"
    return prefix + f"--path {m.rust_crates}"
