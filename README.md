<!-- vim-markdown-toc GFM -->

* [Fidgeting Bits Talon Repo](#fidgeting-bits-talon-repo)
    * [WARNING](#warning)
    * [Dependencies](#dependencies)
        * [Monkey Patching](#monkey-patching)
    * [Hardware](#hardware)
    * [Setup](#setup)
    * [Recommendations](#recommendations)
    * [Pull requests](#pull-requests)
    * [Syncing with knausj_talon](#syncing-with-knausj_talon)

<!-- vim-markdown-toc -->

# Fidgeting Bits Talon Repo 

Please read the WARNING section before you use this repo, as using some of
the stuff I have may break your talon experience as I only test this repo on my
own environment, and you should avoid reporting these problems to aegis or
talon, without first validating that a repo like
[knausj_talon[](https://github.com/knausj85/knausj_talon) works properly first.

The main difference between this repo and knausj_talon is my fairly extensive
vim support. I also sometimes have custom functionality that I haven't had time
to create pull requests for, or that otherwise isn't sufficiently generic to be
able to provide to everyone to use.

This repo is meant to be used on Linux and is only tested on Arch.  It requires
some non-standard python libraries in the talon virtual environment.

This is also developed around beta version of Talon so may result in errors
related to functionality.

In general I try to keep things compatible with the knausj_talon repo, and also
try to contribute back generic parts when I have time. 

## WARNING

I only test this repository on my own system. Although other people are using
it, they may have similar environments to me. It's very possible that you will
run into problems using this repository that aren't actually problems with
talon, in which case you should investigate using knausj_talon first, before
reporting the problems on slack too ease the support load on others.

## Dependencies

My working environment is largely centered around:
* arch linux
* i3-gaps
* dunst
* rofi
* kitty
* neovim
* firefox
* Tobii 5

It is possible I tweak things that end up only working on this environment, and
break on either Linux systems. That said, if you run into a problem using my
repo I'm more than happy to fix it to make it more generic, I just don't do
this type of proactive testing on my own due to lack of time.

### Monkey Patching

There are a few features that I don't like the way they work on i3, so I choose
to monkey patch them. These patches may break on your system, in you need to
test a different repo first if you run into problems, before assuming its
a talon problem.

Currently the list of [monkey
patches](https://github.com/fidgetingbits/knausj_talon/blob/master/monkey/monkey_patching.py)
are:

* [notify-send.sh](https://github.com/vlevit/notify-send.sh) - Use dunst for notifications instead of Qt
* [i3-msg](https://build.i3wm.org/docs/i3-msg.html) - Allows window focusing on i3

## Hardware

This is the hardware I'm using as of 2021. I rarely use a keyboard, but I do
have them available when I need them.

Microphones:
- Primary: DPA d:fine 4188 and DPA d:vice interface.
- Secondary: Sennheiser MD 431 II and Focusrite Scarlet Solo

Keyboards:
- Primary: Gergoplex with 12g khalhi switches.
- Secondary: [Ergodox Ez Glow](https://ergodox-ez.com/pages/ergodox-ez-keyboard) with 60g cherry brown mx switches.

Eye Tracker:
- Desktop: Tobii 4c
- Laptop: Tobii 5

Monitors:
- Desktop: Dual 27" monitors, with the right monitor having the eye tracker and webcam. 


Foot pedal:
- [Stinky board](https://web.archive.org/web/20160531205704/http://stinkyboard.com/)

Mouse:
- Primary: [Corsair SCIMITAR RGB](https://www.corsair.com/us/en/Categories/Products/Gaming-Mice/SCIMITAR-RGB-Optical-MOBA-MMO-Gaming-Mouse/p/CH-9000091-NA)
- Secondary: [Logitech Trackman Marble](https://www.logitech.com/assets/51557/bossa-trackman-marble.pdf)

## Setup

NOTE: This is out of date, I'm not sure what's required at the moment.

In order to run talon on Arch I had to install the follow
dependencies:

* skia-sharp
* qt5-base ?

## Recommendations

Although not Talon specific, I recommend using
[howdy](https://wiki.archlinux.org/title/Howdy) if you are using Linux. It
makes things like logging in and sudo authentication a lot more seamless.

## Pull requests

Even though I use this repo mostly for personal stuff, I'm happy to take pull
requests from people that find issues specifically in my changes that don't
directly applied to knausj_talon.

## Syncing with knausj_talon

<<<<<<< HEAD
I generally try to keep in sync with knausj_talon every couple of weeks, but
sometimes this can go as long as a few months, which can sometimes make things
like updating talon unstable.
=======
`command air` to press `command-a` and select all.

`control shift command 4` to press ` ctrl-shift-cmd-4` to trigger the screenshot application. Then try `escape` to exit the screenshot application. Please note the order of the modifiers doesn't matter.


Any combination of the modifiers, symbols, alphabet, numbers and function keys can be executed via voice to execute shorcuts. Out of the box, only the modifier keys (command, shift, alt, super) cannot be triggered by themselves.

### Symbols
Some symbols are defined in keys.py, so you can say e.g. `control colon` to press those keys.
https://github.com/knausj85/knausj_talon/blob/master/code/keys.py#L93

Some other symbols are defined here:
https://github.com/knausj85/knausj_talon/blob/master/text/symbols.talon

### Formatters
`format help` will display the available formatters with examples of the output.

Try using formatters by saying e.g. `snake hello world`, which will insert hello_world

Multiple formatters can be used together, e.g. `dubstring snake hello world`. This will insert "hello_world"

Formatters (snake, dubstring) are defined here
https://github.com/knausj85/knausj_talon/blob/master/code/formatters.py#L146

All formatter-related commands are defined here
https://github.com/knausj85/knausj_talon/blob/master/misc/formatters.talon#L2


### Mouse commands
See https://github.com/knausj85/knausj_talon/blob/master/misc/mouse.talon

### Generic editor
https://github.com/knausj85/knausj_talon/blob/master/text/generic_editor.talon#L7

These generic commands are global. Commands such as `go word left` will work in any text box.

### Repeating commands
For repeating commands, useful voice commands are defined here:
https://github.com/knausj85/knausj_talon/blob/ced46aee4b59e6ec5e8545bb01434e27792c830e/misc/repeater.talon#L2

Try saying e.g. `go up fifth` will go up five lines.
Try saying e.g. `select up third` to hit `shift-up` three times to select some lines in a text field.

### Window management
Global window managment commands are defined here:
https://github.com/knausj85/knausj_talon/blob/master/misc/window_management.talon#L1

`running list` will toggle a GUI list of words you can say to switch to running applications.
`focus chrome` will focus the chrome application.
`launch music` will launch the music application. Note this is currently only implemented on Mac OS X.

### Screenshot commands

https://github.com/knausj85/knausj_talon/blob/master/misc/screenshot.talon

### Programming Languages

Specific programming languages may be activated by voice commands, or via title tracking.

Activating languages via commands will enable the commands globally, e.g. they'll work in any application. This will also disable the title tracking method (code.language in .talon files) until the "clear language modes" voice command is used.

The commands for enabling languages are defined here:
https://github.com/knausj85/knausj_talon/blob/master/modes/language_modes.talon

By default, title tracking activates coding languages in supported applications such as VSCode, Visual Studio (requires plugin), and Notepad++.

To enable title tracking for your application:
1. The active filename (including extension) must be included in the editor's title
2. Implement the required Talon-defined `filename` action to correctly extract the filename from the programs's title. See https://github.com/knausj85/knausj_talon/blob/8fc3ca75874398806b42d972c28dad91f1399653/apps/vscode/vscode.py#L109 for an example.

Python, C#, Talon and javascript language support is currently broken up into several tags in an attempt to define a common grammar where possible between languages. Each tag is defined by a .talon file, which defines the voice commands, and a Python file which declares the actions that should be implemented by each concrete language implementation to support those voice commands. Currently, the tags which are available are:

• `lang/tags/comment_block.{talon,py}`         - block comments (e.g., C++'s `/* */`)
• `lang/tags/comment_documentation.{talon,py}` - documentation comments (e.g., Java's `/** */`)
• `lang/tags/comment_line.{talon,py}`          - line comments (e.g., Python's `#`)
• `lang/tags/data_null.{talon,py}`             - null & null checks (e.g., Python's `None`)
• `lang/tags/data_bool.{talon,py}`             - booleans (e.g., Haskell's `True`)
• `lang/tags/functions.{talon,py}`             - functions and definitions
• `lang/tags/functions_gui.{talon,py}`         - graphical helper for common functions
• `lang/tags/imperative.{talon,py}`            - statements (e.g., `if`, `while`, `switch`)
• `lang/tags/libraries.{talon,py}`             - libraries and imports
• `lang/tags/libraries_gui.{talon,py}`         - graphical helper for common libraries
• `lang/tags/object_oriented.{talon,py}`       - objects and classes (e.g., `this`)
• `lang/tags/operators_array.{talon,py}`       - array operators (e.g., Ruby's `x[0]`)
• `lang/tags/operators_assignment.{talon,py}`  - assignment operators (e.g., C++'s `x += 5`)
• `lang/tags/operators_bitwise.{talon,py}`     - bitwise operators (e.g., C's `x >> 1`)
• `lang/tags/operators_lambda.{talon,py}`      - anonymous functions (e.g., JavaScript's `x => x + 1`)
• `lang/tags/operators_math.{talon,py}`        - numeric, comparison, and logical operators
• `lang/tags/operators_pointer.{talon,py}`     - pointer operators (e.g., C's `&x`)

The support for the language-specific implementations of actions are then located in:

• `lang/{your-language}/{your-language}.py`

To start support for a new language, ensure the appropriate extension is added to the [`extension_lang_map` in `code.py`](https://github.com/knausj85/knausj_talon/blob/12229e932d9d3de85fa2f9d9a7c4f31ed6b6445b/code/code.py#L32).
Then create the following files:

• `lang/{your-language}/{your-language}.py`
• `lang/{your-language}/{your-language}.talon`

Activate the appropriate tags in `{your-language}.talon` and implement the corresponding actions in `{your-language}.py`, following existing language implementations.
If you wish to add additional voice commands for your language, put those in `{your-language}.talon`.
You may also want to add a force command to `language_modes.talon`.

## File Manager commands
For the following file manager commands to work, your file manager must display the full folder path in the title bar. https://github.com/knausj85/knausj_talon/blob/baa323fcd34d8a1124658a425abe8eed59cf2ee5/apps/file_manager.talon


For Mac OS X's Finder, run this command in terminal to display the full path in the title.

```
defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES
```

For Windows Explorer, follow these directions
https://www.howtogeek.com/121218/beginner-how-to-make-explorer-always-show-the-full-path-in-windows-8/

For the Windows command line, the `refresh title` command will force the title to the current directory, and all directory commands (`follow 1`) will automatically update the title.

Notes:

• Both Windows Explorer and Finder hide certain files and folder by default, so it's often best to use the imgui to list the options before issuing commands.

• If there no hidden files or folders, and the items are displayed in alphabetical order, you can typically issue the `follow <number>`, `file <number>` and `open <number>` commands based on the displayed order.

To implement support for a new program, you need to implement the relevant file manager actions for your application and assert the user.file_manager tag.
- There are a number of example implementations in the repository. Finder is a good example to copy and customize to your application as needed.
https://github.com/knausj85/knausj_talon/blob/5eae0b6a8f2269f24265e77feddbcc4bcf437c36/apps/mac/finder/finder.py#L16

## Terminal commands

Many terminal programs are supported out of the box, but you may not want all the commands enabled.

To disable various commandsets in your terminal, find the relevant talon file and enable/disable the tags for command sets as appropriate.

```
tag(): user.file_manager
tag(): user.git
tag(): user.kubectl
tag(): user.tabs
```

For instance, kubectl commands (kubernetes) aren't relevant to everyone.


## Jetbrains commands

For Jetbrains commands to work you must install https://plugins.jetbrains.com/plugin/10504-voice-code-idea
into each editor.

## Settings

Several options are configurable via a single settings file out of the box. Any setting can be made context specific as needed (e.g., per-OS, per-app, etc).

https://github.com/knausj85/knausj_talon/blob/master/settings.talon


```
#adjust the scale of the imgui to my liking
imgui.scale = 1.3
# enable if you'd like the picker gui to automatically appear when explorer has focus
user.file_manager_auto_show_pickers = 0
#set the max number of command lines per page in help
user.help_max_command_lines_per_page = 50
# set the max number of contexts display per page in help
user.help_max_contexts_per_page = 20
# The default amount used when scrolling continuously
user.mouse_continuous_scroll_amount = 80
#stop continuous scroll/gaze scroll with a pop
user.mouse_enable_pop_stops_scroll = 1
#enable pop click with 'control mouse' mode
user.mouse_enable_pop_click = 1
#When enabled, the 'Scroll Mouse' GUI will not be shown.
user.mouse_hide_mouse_gui = 0
#hide cursor when mouse_wake is called to enable zoom mouse
user.mouse_wake_hides_cursor = 0
#the amount to scroll up/down (equivalent to mouse wheel on Windows by default)
user.mouse_wheel_down_amount = 120
```

The most commonly adjusted settings are probably

• `imgui.scale` to improve the visibility of all imgui-based windows (help, history, etc). This is simply a scale factor, 1.3 = 130%.

• `user.help_max_command_lines_per_page` and `user.help_max_contexts_per_page` to ensure all help information is visible.

• `user.mouse_wheel_down_amount` and `user.mouse_continuous_scroll_amount` for adjusting the scroll amounts for the various scroll commands.


# Collaborators

This repository is now officially a team effort. The following contributors have direct access:
- @dwiel
- @fidgetingbits
- @knausj85
- @rntz
- @splondike
- @pokey

Collaborators will reply to issues and pull requests as time and health permits. Please be patient.

## Guidelines for collaborators

1. Collaborators prioritize their health and their personal/professional needs first. Their time commitment to this effort is limited.
2. For "minor" fixes and improvements/bugs/new apps, collaborators are free to contribute without any review
3. For "significant" new development and refactors, collaborators should seek appropriate input and reviews from each-other. Collaborators are encouraged to open a discussion before committing their time to any major effort.

# Contributing

Anyone is welcome to submit PRs and report issues.

## Guidelines for contributions

- Any addition to the global grammar will be scrutinized a bit more thoroughly. The more specific a new context, the less scrutiny that is typically applied.

- New grammars should follow the [subject][verb] standard where-ever possible.

- For Mac OS X, the bundle id should be used for defining app contexts, rather than the name.

- For Windows, both the friendly app name and exe name should be used for defining app contexts when they are different. For some people, the MUICache breaks.

- For new web apps, ensure the domain is used to minimize potential mismatches
https://github.com/knausj85/knausj_talon/blob/master/apps/web/window_titles.md

- New applications should support the appropriate 'generic' grammars where possible

```
generic_browser.talon
find_and_replace.talon
line_commands.talon
multiple_cursors.talon
generic_snippets.talon
splits.talon
tabs.talon
generic_terminal.talon
```

- New programming languages should support the appropriate 'generic' grammars where possible, see above.

## Automated tests

There are a number of automated tests in the repository which are run outside of the Talon environment. To run them make sure you have the `pytest` python package installed. You can then just run the `pytest` command from the repository root to execute all the tests.

# Talon documentation
For official documentation on Talon's API and features, please visit https://talonvoice.com/docs/.

For community-generated documentation on Talon, please visit https://talon.wiki/
>>>>>>> 4a376d1ece8b60728f71120ef3e7dd10c3ba34e6
