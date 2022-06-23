# BluestacksWorldFlipperBot
A non-user friendly python programme for bluestacks automation 
of a game known as World Flipper. (for personal use)


![alt text](https://play-lh.googleusercontent.com/vMoDYU7ZuLOxFA_Q5BXGREAarZZOqPxMULIrndjgTbkkjDQjs2QrX4UYJ0Z3T6_yoQc=w240-h480-rw "World Flipper")

Code is horribly unoptimized, still working on it.

~~Use of pyautogui to read data on the bluestacks emulator,
therefore emulator has to be in foreground
and cannot be blocked by other windows.~~

~~Use of win32 libraries to interact with emulator directly,
thus this programme will not take control of your cursor
(for the mini) and or keyboard.~~

~~Do note that bluestacks custom controls
have to be setup before using this programme.~~

Now using ADB (Android Debug Bridge) to control and interact with the emulator (In this case being BlueStacks)

[This is how you enable ADB on BlueStacks](https://stackoverflow.com/questions/54317727/how-do-you-adb-to-bluestacks-4)

Rerun the program once if you encounter an error along the lines of "no device found"

This new version allows the emulator to run in the background without any interuption.
The ADB allows for a constant stream of screen-captures, which are then processed by open-cv, in order to understand and detect the flow of the game.

As of now, the program is limited to solely the "Auto-Bell" feature.

