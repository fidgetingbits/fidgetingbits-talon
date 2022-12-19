"""The point of this file is to help managed talon recordings by being able to
speak a command to automatically save the last recording in a preconfigured
directory, with the assumption that the recording had some sort of error in it
that you want to document and then provide to @aegis for analysis. It allows
you to save the most recent recording, as well as replay them so that you can
actually see whether or not what you thought was an error sounded like an error
to the recording. It also allows you to remove the last saved recording in the
event that you feel that it wasn't actually an error. because the number of
recordings that can happen change fairly quickly it also provides a gui
selector that allows you to choose from a list of the most recent recordings
and have one of those specifically save to the preconfigured directory."""
import os
import pathlib
import shutil
import subprocess

from talon import Context, Module, actions, app, clip, imgui, settings, ui
from talon_init import TALON_HOME

ctx = Context()
mod = Module()
mod.mode("replay_picker_open")

mod.tag(
    "record_replay", desc="a tag that will enable certain replay recording commands"
)

mod.setting(
    "saved_replay_recordings_directory",
    type=str,
    default=None,
    desc="Location that you can use to store saved recordings",
)
mod.setting(
    "replay_recordings_list_count",
    type=int,
    default=30,
    desc="The number of recordings to show in the replay recordings gui",
)
# NOTE: this is mostly useful if you're trying to update a text file with a
# list of recordings that you're going to provide an analysis for, otherwise it
# will be annoying
mod.setting(
    "replay_paste_name_on_save",
    type=bool,
    default=1,
    desc="If set paste the name of the file saved into the open window",
)

ctx.matches = r"""
tag: user.record_replay
"""


def check_settings(f):
    """Validate settings match the expectation of having the tags set"""

    def wrapper(*args):
        if settings.get("speech.record_all") != 1:
            app.notify("Recording appears to be disabled")
            return None
        if args[0].saved_recording_directory is None:
            if settings.get("user.saved_replay_recordings_directory") is None:
                print("!!! check_settings wrapper")
                app.notify("No replay recording folder configured")
                return None
            args[0].saved_recording_directory = pathlib.Path(
                settings.get("user.saved_replay_recordings_directory")
            ).expanduser()
        return f(*args)

    return wrapper


class _RecordingReplayer:
    """Manages recent recordings and make them available for replay"""

    def __init__(self):
        """Specify the number of default recording to list in the picker"""
        self.gui_open = False
        self.recordings_list = []
        self.count = 0
        self.recordings = pathlib.Path(TALON_HOME, "recordings/")
        self.last_saved_recording = None
        self.last_played_recording = None
        self.saved_recording_directory = None

    def last_recordings(self) -> list:
        """Checks the last number of recordings from the recording directory,
        :returns: a list of the most recent self.count recordings
        :rtype: List

        """

        if self.count == 0:
            self.count = settings.get("user.replay_recordings_list_count")
        list_of_files = sorted(
            [file for file in self.recordings.iterdir() if file.is_file()],
            key=os.path.getmtime,
        )

        file_count = len(list_of_files)
        if file_count < self.count:
            return list_of_files
        else:
            return list_of_files[file_count - self.count : file_count]

    @check_settings
    def play_last(self):
        """Play the last recording (before the replay command itself)"""
        last_recordings = self.last_recordings()
        last = last_recordings[-1:][0]
        self.play_file(last)

    @check_settings
    def play_last_saved(self):
        """Play the last saved recording"""
        if self.last_saved_recording is not None:
            self.play_file(self.last_saved_recording)
        else:
            app.notify("No recording saved? Nothing to play")

    @check_settings
    def play_last_played(self):
        """Play the last selected recording"""
        if self.last_played_recording is not None:
            self.play_file(self.last_played_recording)
        else:
            app.notify("No previous recording selected? Nothing to play")

    @check_settings
    def remove_last_saved(self):
        """Remove the last saved recording"""
        if self.last_saved_recording is not None:
            self.last_saved_recording.unlink(missing_ok=True)
            self.last_saved_recording = None
            app.notify(f"{self.last_saved_recording} removed")
        else:
            app.notify("No recording saved? Nothing removed")

    @check_settings
    def play_file(self, recording: pathlib.Path):
        """Play the recording file passed in."""
        actions.speech.disable()
        # TODO -  start using cubeb
        # mplayer broke do to some libssl error, so use vlc for now
        subprocess.run(
            ["vlc", "--play-and-exit", "--intf", "dummy", "--no-interact", recording]
        )
        self.last_played_recording = recording
        actions.speech.enable()

    @check_settings
    def save_last_played(self):
        """Save the last recording played"""
        if self.last_played_recording:
            self.save_file(self.last_played_recording)
            app.notify(f"{self.last_played_recording} saved")
        else:
            app.notify("No played recordings? Nothing saved")

    @check_settings
    def save_recording_by_index(self, index):
        """Save the recording into the defined folder"""
        if index == 0:
            self.recordings_list = self.last_recordings()
        file_name = pathlib.Path(self.recordings_list[index - 1])
        return self.save_file(file_name)

    def save_file(self, file_name: pathlib.Path):
        """Save a file to the recording directory"""
        if self.saved_recording_directory is None:
            return None
        shutil.copy(file_name, self.saved_recording_directory)
        self.last_saved_recording = self.saved_recording_directory.joinpath(
            file_name.name
        )

        return file_name.name


main_screen = ui.main_screen()
rr = _RecordingReplayer()


def close_replay_picker():
    global rr
    gui.hide()
    actions.mode.disable("user.replay_picker_open")
    rr.gui_open = False


@imgui.open(y=0, x=main_screen.width / 2.6)
def gui(gui: imgui.GUI):
    gui.line()
    gui.text("Commands:")
    gui.text("replay <number>")
    gui.text("replay save <number>")
    gui.text("replay yank <number>")
    gui.line()
    index = 1
    global rr
    # we do this because this code is called in a refresh loop, we don't want
    # the recordings list to change if the user issues another command
    if not rr.gui_open:
        rr.gui_open = True
        rr.recordings_list = rr.last_recordings()

    for path in rr.recordings_list:
        gui.text(f"{index}: {path.name} ")
        index = index + 1

    if gui.button("Hide"):
        close_replay_picker()


def raise_replay_picker():
    actions.mode.enable("user.replay_picker_open")
    gui.show()


@mod.action_class
class Actions:
    def replay_recording_choose():
        """Opens an UI for picking a recording to replay"""
        raise_replay_picker()

    def replay_picker_hide():
        """Hides the replay_picker display"""
        close_replay_picker()

    def replay_pick(choice: int):
        """Hides the replay_picker display"""
        global rr

        rr.play_file(rr.recordings_list[choice - 1])

    def replay_save(choice: int):
        """Save the selected recording to a preconfigured directory"""
        global rr
        file_name = rr.save_recording_by_index(choice)
        if not file_name:
            return
        if settings.get("user.replay_paste_name_on_save") != 0:
            clip.set_text(file_name)
            actions.user.insert_cursor_paste('"[|]":', "")

    def replay_save_last_played():
        """Insert some info from the last self.count recordings"""
        global rr
        file_name = rr.save_last_played()
        if not file_name:
            return
        if settings.get("user.replay_paste_name_on_save") != 0:
            clip.set_text(file_name)
            actions.user.insert_cursor_paste('"[|]":', "")

    def replay_save_last():
        """Save the last recording to a preconfigured directory"""
        global rr
        file_name = rr.save_recording_by_index(0)
        if not file_name:
            return
        # XXX - make this optional
        clip.set_text(file_name)

    def replay_copy_name(choice: int):
        """Copy the file name of the selected replay file"""
        global rr

        file_name = rr.recordings_list[choice - 1]
        if not file_name:
            return None
        pathlib.Path(file_name)
        clip.set_text(file_name.name)

    def replay_last_recording():
        """Insert some info from the last self.count recordings"""
        global rr
        rr.play_last()

    def replay_last_saved():
        """Insert some info from the last self.count recordings"""
        global rr
        rr.play_last_saved()

    def replay_remove_last_saved():
        """Remove the last saved recording"""
        global rr
        rr.remove_last_saved()

    def replay_last_played_recording():
        """Insert some info from the last self.count recordings"""
        global rr
        rr.play_last_played()
