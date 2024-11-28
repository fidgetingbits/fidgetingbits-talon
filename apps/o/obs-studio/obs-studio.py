import glob
import os
import subprocess

from talon import Module, actions, settings

mod = Module()
mod.tag("obs_studio_global", desc="tag that's active if oba-studio is running")
mod.setting(
    "obs_recording_folder",
    type=str,
    default=None,
    desc="the default location to record files with obs-studio",
)
mod.setting(
    "obs_clip_folder",
    type=str,
    default=None,
    desc="the default location to save clipped viedo files",
)


@mod.action_class
class Actions:
    def obs_play_last_clip():
        """Plays the last recorded clip after putting talon to sleep"""
        folder = settings.get("user.obs_clip_folder")
        list_of_files = glob.glob(f"{folder}/*")
        latest_file = max(list_of_files, key=os.path.getctime)
        actions.speech.disable()
        # XXX - this should launch new app
        subprocess.Popen(["vlc", f"{latest_file}"])
        # XXX - re-wake talon
