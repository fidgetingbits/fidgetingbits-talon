<!-- vim-markdown-toc GFM -->

* [Fidgeting Bits Talon Repo](#fidgeting-bits-talon-repo)
    * [WARNING](#warning)
    * [Dependencies](#dependencies)

<!-- vim-markdown-toc -->

# Fidgeting Bits Talon Repo

Please read the WARNING section before you use this repo, as using some of
the stuff I have may break your talon experience as I only test this repo on my
own environment, and you should avoid reporting these problems to aegis or
talon, without first validating that a repo like
[knausj_talon](https://github.com/knausj85/knausj_talon) works properly first.

The main feature I added that most people come to this repo for is vim support.
See `apps/vim/` for more details.

This repo is meant to be used on Linux and is only tested on Arch. It requires
some non-standard python libraries in the talon virtual environment.

NOTE: As of 2022 I plan to start to deviate more and more from the main
knausj_talon layout and files. I hope to take some inspiration and borrow some
code from [AndreasArvidsson](https://github.dev/AndreasArvidsson/andreas-talon)
and [wenkokke](https://github.com/wenkokke/talon-user) which I think are a lot
cleaner layouts generally.

XXX - add a link to the script I use to launch talon.

This repo is developed around beta version of Talon so may result in errors
related to functionality. I recommend paying for beta on
[patreon](https://www.patreon.com/join/lunixbochs?) if you can.

In general I try to keep adding the core features from knausj_talon repo, but
this has become increasingly difficult lately due to other obligations.

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
