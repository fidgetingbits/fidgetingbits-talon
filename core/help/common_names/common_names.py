import os
import pathlib

from talon import Context, Module

mod = Module()
mod.list("first_names", desc="Common first names")
mod.list("last_names", desc="Common first names")

cwd = os.path.dirname(os.path.realpath(__file__))
first_names_file = os.path.join(cwd, "first_names.csv")
last_names_file = os.path.join(cwd, "last_names.csv")

# These list should contain values you don't want to be published publicly.
# see the read me about keeping them private
private_first_names_file = pathlib.Path(__file__).parent.parent.joinpath(
    "../../../private/misc/common_names/private_first_names.csv"
)
private_last_names_file = pathlib.Path(__file__).parent.parent.joinpath(
    "../../../private/misc/common_names/private_last_names.csv"
)


def populate_list(name_list, file_name):
    with open(file_name) as f:
        for line in f:
            line = line.rstrip()
            if "," in line:
                sound, word = line.split(",")
                if word is None:
                    word = sound
            else:
                sound = word = line
            if line not in name_list.keys():
                name_list[sound] = word


first_names = {}
last_names = {}
populate_list(first_names, first_names_file)
populate_list(first_names, private_first_names_file)
populate_list(last_names, last_names_file)
populate_list(last_names, private_last_names_file)


ctx = Context()
ctx.lists["self.first_names"] = first_names
ctx.lists["self.last_names"] = last_names


@mod.capture(rule="{self.first_names}")
def first_name(m) -> str:
    "One first name"
    return m.first_names


@mod.capture(rule="{self.last_names}")
def last_name(m) -> str:
    "One last name"
    return m.last_names
