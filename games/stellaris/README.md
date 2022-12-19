<!-- vim-markdown-toc GFM -->

- [Stellaris Talon support development notes](#stellaris-talon-support-development-notes)
- [Resources](#resources)
  - [Basic environment setup](#basic-environment-setup)
  - [High level overview of requirements](#high-level-overview-of-requirements)
  - [Talon set up](#talon-set-up)
  - [Mouse additions](#mouse-additions)
    - [Most coordinate capturing](#most-coordinate-capturing)

<!-- vim-markdown-toc -->

# Stellaris Talon support development notes

Into this document describes the process of trying to add support for playing
stellas on steam using talon under linux. The entire development process in
testing processes all being done with talon voice beta and eye tracking using a
tobii 4c

# Resources

[Hot keys](https://stellaris.paradoxwikis.com/Hotkeys)

## Basic environment setup

Tools used: - nvim - talon beta - vim wiki for documentation - stellaris on linux

Recommended talon functionality

talon functionality that had to be added

## High level overview of requirements

- ability to hover mouse automatically at a coordinate or after clicking with
  eyes
- ability to auto click certain notifications based on coordinates
  - ability to record mouse coordinates
  -
- ability to remove all common command mode commands to reduce error rate

## Talon set up

Created a directory under `games/stellaris/`

Added a new `app.name` entry into `application_matches.py`

created a stellaris dev session and vim

Created a game mode with more aggressive command disabling than then command
mode,but with the ability to switch back to command mode or dictation mode.

started working on loading screen for basic testing

## Mouse additions

- add the ability to hover the cursor at a given location, without clicking
- add the ability to record cursor locations into a list
- add the ability to record cursor locations into the clipboard

### Most coordinate capturing

set up a jason file to capture the coordinates first specific screen
resolution. need to categorize all of the different areas on the screen with a
specific name that can be looked up generically within talon
