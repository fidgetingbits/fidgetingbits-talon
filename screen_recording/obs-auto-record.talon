# This is a custom set of rules to control a obs-studio script I wrote in order
# to automatically record all sessions, and splice interesting parts.

tag: user.obs_studio_global
-
settings():
    user.obs_recording_folder = "/home/aa/mount/oath/workflow/video_recording/automatic/"
    user.obs_clip_folder = "/home/aa/mount/oath/workflow/video_recording/snapshots/"

broadcast start:
    user.system_command("/home/aa/source/obs-cli/obs-cli.py --start-recording")
    app.notify("obs-studio recording started")
broadcast stop:
    user.system_command("/home/aa/source/obs-cli/obs-cli.py --stop-recording")
    app.notify("obs-studio recording stopped")
broadcast pause:
    user.system_command("/home/aa/source/obs-cli/obs-cli.py --pause-recording")
    app.notify("obs-studio recording paused")
broadcast resume:
    user.system_command("/home/aa/source/obs-cli/obs-cli.py --resume-recording")
    app.notify("obs-studio recording resumed")
broadcast save:
    user.system_command_nb("/home/aa/source/obs-cli/obs-cli.py --save-recording")
    app.notify("obs-studio old recording saved")

# splices by a default time amount
broadcast clip:
    user.system_command_nb("/home/aa/source/obs-cli/obs-cli.py --splice-recording")
broadcast clip <number_small> (minute|minutes):
    user.system_command_nb("/home/aa/source/obs-cli/obs-cli.py --splice-recording --splice-minutes {number_small}")

# XXX - buggy. killing window/screen keeps playing video
# This should launch a new app instead with launcher
broadcast replay clip:
    user.obs_play_last_clip()
