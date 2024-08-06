import json
import pathlib

from talon import Context, Module, actions, app, fs, imgui, settings, ui
from talon_init import TALON_HOME

mod = Module()
mod.mode("personal_info")
mod.setting(
    "personal_info_auto_select",
    type=int,
    default=1,
    desc="Auto select specified entry in json list, or none if 0",
)
mod.list("personal_info", desc="List of personal info populated by json file")
ctx = Context()


@mod.capture(rule="{user.personal_info}")
def personal_info(m) -> list:
    """Returns a personal_info name"""
    return m.personal_info


main_screen = ui.main_screen()

personal_info_list = []


def close_personal_info():
    gui.hide()
    actions.mode.disable("user.personal_info")


@imgui.open(y=0, x=main_screen.width / 2.6)
def gui(gui: imgui.GUI):
    global personal_info_list
    gui.text("Select an entry")
    gui.line()
    index = 1
    for word in personal_info_list:
        gui.text(f"Pick {index}: {word} ")
        index = index + 1

    if gui.button("Hide"):
        close_personal_info()


class PersonalInfo:
    db = None
    command_key_map = {}

    def __init__(self):
        # FIXME: make this path configurable
        self.personal_info_file = pathlib.Path(
            TALON_HOME, "user/private/misc/personal_info/personal_info.json"
        )
        self.update_commands()
        fs.watch(self.personal_info_file, self.__on_fs_change)

    def __on_fs_change(self, name, flags):
        print("updating personal info commands")
        self.update_commands()

    def update_commands(self):
        with open(self.personal_info_file) as f:
            self.db = json.loads(f.read())
            for key in self.db:
                self.command_key_map[" ".join(key.split("-"))] = key
        global ctx
        ctx.lists["user.personal_info"] = self.command_key_map


pi = PersonalInfo()


def raise_personal_info():
    actions.mode.enable("user.personal_info")
    gui.show()


@mod.action_class
class Actions:
    def personal_info_hide():
        """Hides the personal_info display"""
        close_personal_info()

    def personal_info(record: str):
        """Insert some info from the personal info database"""
        global pi
        global personal_info_list
        record_data = pi.db[record]
        if isinstance(record_data, list):
            if len(record_data) > 1:
                auto_index = settings.get("user.personal_info_auto_select")
                personal_info_list = record_data
                if auto_index <= len(record_data):
                    record_data = record_data[auto_index]
                else:
                    raise_personal_info()
            else:
                record_data = record_data[0]
        actions.insert(f"{record_data}")

    def personal_info_by_id(record: str, index: int):
        """Insert some info from the personal info database"""
        global pi
        global personal_info_list
        record_data = pi.db[record]
        if isinstance(record_data, list):
            if index - 1 > len(record_data):
                index = 0
            record_data = record_data[index - 1]
            actions.insert(f"{record_data}")
        else:
            actions.insert(f"{record_data}")

    def personal_info_select(number: int):
        """selects the personal_info by number"""
        if number <= len(personal_info_list) and number > 0:
            return personal_info_list[number - 1]

        error = "personal_info.py index {} is out of range (1-{})".format(
            number, len(personal_info_list)
        )
        app.notify(error)
        raise error

    def print_talon_version():
        """print the current talon version"""
        actions.insert(app.version)
