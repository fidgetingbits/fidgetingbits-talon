# Precision Mouse Guide Instructions

This is a very precise voice-controlled mouse scrip for Talon, which creates a voice-controlled mouse that can be used on Windows, macOS, and Linux.

To get this to work, put mouse_guide.talon and mouse_guide.py into the user directory of your Talon home folder, ~/.talon/user on Linux and Mac or %APPDATA%\Talon\user on Windows.

You can do this either by copying these files directly, or with a shell command.

> git clone https://github.com/tararoys/mouse_guide.git

When you turn on talon, a crosshair guide will appear on your mouse. The crosshairs will have hash marks.

You can use the commands

> mouse 10 down

to move the mouse down ten units.

You can use the commad

> mouse 10 major down

To move the command down ten major hash marks on the crosshairs.

You can also combine commands: for example,

> Mouse 10 major up 30 major right

to move the command up and to the right in a diagonal.

To toggle the crosshairs on and off, say

> mouse guide
