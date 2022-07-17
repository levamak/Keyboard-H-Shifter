# Keyboard-H-Shifter
This app was created for Assetto Corsa(and perhaps other sim racing games) to simulate H-Shifter input using keyboard

To use this app you need to install vJoy first (https://sourceforge.net/projects/vjoystick/)
After installing and opening vJoy, modify the amount of buttons to be more or equal to 9. Now open 'H-Shifter for AC.exe' found in the archive.
Change the vJoy Device in the app to the one which is currently enabled(open vJoy to see which devices are enabled, default is 1).
In the app, you can change the gears(1-7,R for Reverse, N for Neutral) to any alphanumerical buttons(A-Z, 0-9 and `, -, =). The gears correspond to the specific vJoy buttons: 1st gear - '1', 2nd gear - '2', ... , 7th gear - '7', Reverse - '8', Neutral - '9'. After choosing preferable settings, press 'start' and go to Assetto Corsa.
Now you can change the controls in AC to keyboard keys.
If you want to stop simulating vJoy buttons, press 'End' in the app.

# How does it work?
Using tidzo's library pyvjoy(https://github.com/tidzo/pyvjoy) we can modify the state of vJoy buttons, and with the help of 'pynput' we can bind those commands to keyboard buttons. The way that it works is that once you click the 'gear' button on your keyboard, it will simulate a continuos press of a vJoy device button. Example: by pressing '1' with default settings in the app you will simulate '1' button in the vJoy and it will not release itself until you press another gear or neutral, which releases all the buttons.
NOTE: if you want to run and build it yourself, you have to extract the 'dont_steal_this.ico' from the rar file and place it in the same folder with main.py in order for it to work
