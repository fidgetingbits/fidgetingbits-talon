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

I generally try to keep in sync with knausj_talon every couple of weeks, but
sometimes this can go as long as a few months, which can sometimes make things
like updating talon unstable.
