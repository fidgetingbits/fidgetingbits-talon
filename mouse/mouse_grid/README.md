This is the "full mouse grid". It fills the screen with fields that can be reached with two letters and a number.

__To activate it, put this in whatever talon file you use for settings:__

`tag(): user.full_mouse_grid_enabled`

![](https://gist.githubusercontent.com/timo/b3429ede632f0eb9cac0eb142746dc3b/raw/ebf6185ded98d1ff960047c351d45c6618906891/screenshot.png)

![](https://gist.githubusercontent.com/timo/b3429ede632f0eb9cac0eb142746dc3b/raw/1bbb642824ba7a8dcb2c5d1710460bd7ecd28c0e/screenshot.png)

then use these voice commands:

* `alphabet soup` to show the grid
* `alphabet win` to put the grid over the active window
* `alphabet screen <number>` to put the grid over a different screen from the first one

When the screen is showing you can select fields using your alphabet words and a number for the field:

* `cap whale one` selects field CW in the top left field
* `one drum gust` selects field DG in the top left field
* `three vest near` selects field VN in whatever field has number 3

There are some commands to customize what the grid looks like:

* `alphabet rulers` turns on "rulers" that show the letters on the top and bottom as well as left and right, useful mostly for `alphabet win`
* `alphabet checkers` hides or shows every other field so you can see more of the screen content

Future plans:

* allow refining the target position more by adding another number (a la numpad / M grid)
* allow refining the target position with points-of-compass names
* allow refining even more closely with something like "plus" or "minus"
* make the superblock that contains the mouse cursor when the grid is brought up the "default" so the number doesn't have to be said

Possible ideas:

* configure look even more with voice commands; colors, transparency, etc
* make size of fields configurable with voice commands as well

# Tara's Additions:


Full mouse grid now has a special mode that excludes all other commands except for the commands in full_mouse_grid_open while the mouse grid is open.  

It is possible to put talon to sleep, and the mouse_grid commands will be disabled while talon is asleep and return to full_mouse_grid mode when Talon is reawakened.  

Many of the coloring settigs have been extracted to the file full_mouse_settings.talon.  The colors for various items in the full mouse grid can be reset using RGB hexadecimal colors. 

The colors currently look like this: 

![image](https://user-images.githubusercontent.com/1163925/114628783-0abdfb80-9c7d-11eb-9a47-d9a492aa5e09.png)

Instead of saying the commands as a sequence of numbers, there are commands added so that 

1. you can say a single number, pause and see that a certain superblock is selected,
2.  then say a single letter, and pause while all rows with that letter are highlighted, 
3. and say the final letter to select the coordinate that is in both the highlighted superblock and highlighted row.  

the image below shows superblock 6 selected, and row N highlighted.  

![image](https://user-images.githubusercontent.com/1163925/114629052-861fad00-9c7d-11eb-84ad-42369379879d.png)

It is possible to change your mind and select a different superblock, but it is not currently possible to select a different letter row without starting over. 
