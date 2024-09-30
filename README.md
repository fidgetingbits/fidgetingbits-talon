# fidgetingbits' Talon Repo

- [fidgetingbits' Talon Repo](#fidgetingbits-talon-repo)
  - [Interesting features](#interesting-features)
  - [Other stuff](#other-stuff)
  - [Deprecated Features](#deprecated-features)
  - [WARNING](#warning)
  - [Dependencies](#dependencies)
    - [Monkey Patching](#monkey-patching)
  - [Hardware](#hardware)
  - [Recommendations](#recommendations)
  - [Pull requests](#pull-requests)

Please read the WARNING section before you use this repo, as using some of
the stuff I have may break your talon experience as I only test this repo on my
own environment, and you should avoid reporting these problems to aegis or
talon, without first validating that a repo like
[community](https://github.com/talonhub/community) works properly first.

This repo is fairly thoroughly tested on both Linux (i3wm and Gnome) and Mac (Sonoma). Linux functionality was
originally built for Arch Linux, but now is only ever tested on NixOS.

I use the beta version of Talon so this may result in errors related to
functionality if you aren't using it. I highly recommend paying for beta on
[patreon](https://www.patreon.com/join/lunixbochs?) if you can.

In general I try to keep merging the core features from knausj_talon repo, but
sometimes it might be months behind.

## Interesting features

Following in the steps of [Andreas Arvidsson](https://github.com/AndreasArvidsson/andreas-talon) the following is a list
of interesting things you will find in is repo that you can take/reuse, that hasn't been added to community yet. I'd
love to add most of it, but have never found the time.

- _types support_ - I have language tab support for types that I use to help me dictate rust/C types more easily
- _package manager support_ -
- _zle_ -
- _tag pinning_ -
- _vscode plugin scope_ -
- _service manager support_ -

## Other stuff

- _vim support_ - The main feature most people were using was my vim support. This is now split between
   [neovim-talon](https://github.com/hands-free-vim/neovim-talon/tree/main) and my own
   [talon-vim](https://github.com/fidgetingbits/talon-vim) repo, where neovim-talon occasionally lifts parts from..
- _systemd user services_ - I use a systemd user service and watchdog to launch Talon on login, and also restart it if
  it stalls. See [here](https://gist.github.com/fidgetingbits/a9c9d4786dd28c0f5224071280edfb66)
- _talon-python-command-server_ - Talon file-based [RPC server](https://github.com/fidgetingbits/talon-python-command-server)
- _talon-shotbox_ - A [screenshot tool](https://github.com/fidgetingbits/talon-shotbox) that allows you to select
  regions of screen by voice. A bit rough around the edges, but usable. Inspired by flameshot on Linux.

## Deprecated Features

- _run_talon.sh_ A [script](https://gist.github.com/fidgetingbits/cfc1699da2e8a60533db6c4cfdf390c3) I use to run talon that auto-restarts on stalls. (NOTE: I not longer use this since moving to NixOS)

## WARNING

I only test this repository on my own system. Although other people are using
it, they may have similar environments to me. It's very possible that you will
run into problems using this repository that aren't actually problems with
talon, in which case you should investigate using knausj_talon first, before
reporting the problems on slack to ease the support load on others.

## Dependencies

My working environment is largely centered around:

- arch linux
- i3-gaps
- dunst
- rofi
- kitty
- neovim
- firefox
- Tobii 5

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

- [notify-send.sh](https://github.com/vlevit/notify-send.sh) - Use dunst for notifications instead of Qt
- [i3-msg](https://build.i3wm.org/docs/i3-msg.html) - Allows window focusing on i3

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

- Primary: [Logitech G903 Lightspeed](https://www.logitechg.com/en-us/products/gaming-mice/g903-hero-wireless-gaming-mouse.910-005670.html)
  - This is great if you need an ambidextrous backup mouse
- Secondary: [Logitech Trackman Marble](https://www.logitech.com/assets/51557/bossa-trackman-marble.pdf)

## Recommendations

Although not Talon specific, I recommend using
[howdy](https://wiki.archlinux.org/title/Howdy) if you are using Linux. It
makes things like logging in and sudo authentication a lot more seamless.

## Pull requests

Even though I use this repo mostly for personal stuff, I'm happy to take pull
requests from people that find issues specifically in my changes that don't
directly applied to knausj_talon.
