# BlockComPi
A Block of a Computer of a Raspberry Pi phone
Components needed to build:

 Raspberry Pi 2
 Raspberry Pi Camera Module
 Adafruit PiTFT 2.8 resistive
 Adafruit FONA 2G (could use 3G but have to modify the design a bit)
 Earphones with Mic
 5V boost converter
 2000mah or so battery from phone
 Buttons,  Female Headers, Diode
 Wires and a PCB to connect everything together
 White Acrylic Case with PLA filament from 3Doodler to connect the pieces together 
 Wooden Back Plate
 Black Stylus (Nintendo DS)
Buzzer (For Notifications) (connects through expansion port)

Software:

Based on Raspbian Jessie
Crappily Coded in Python
Uses PyGame, with PiTFT Rotated 180
garthvh's menu_8button.py is under no license, and has been adapted into PitftGraphicLib.py for easier use with PyGame in my code
No Bitmaps or images used
Note that virtual keyboard, licensed under the GNU GPL, is included, used, and has not been modified.
The Main Menu, Notifcentral.py, has a Notifications  and Service system and an App drawer which layout apps as in App.py
Can actually Receive and send Phone Calls and SMS through Notifications and Service System
The Apps included are, Phone, Messages (just something that sends Messages), Contacts, Camera, X11 and Tab Mode.
The ones coded my me are Phone (just a dialer ), Messages (just something that sends Messages), Contacts (stores contacts in config file
The Camera app actually adafruit pi cam software , which is included under BSD license
X11 shows the X Server with Matchbox Desktop Environment on PiTFT, while Tab Mode actually shows the full Raspbian Desktop through the main TV Output, HDMI or Composite
Download code Here (Note that you cannot run commands from the script, and have to copy and paste the commands )( install dependencies to run adafruit-pi-cam yourself)
What it can do:

Modular (Anything Major like the PiTFT, Camera, Pi, FONA etc. can be removed and replaced)(Small components like the buttons can be easily desoldered)
Expandable (All unused GPIO can be used through the female header connectors, I2C is also available)(4 Full USB ports)
Can be used in other projects (eg. Upcoming Home Automation System)
Full power of Command Line and X11 Linux (Programming)
Portable use (But battery is not that good and would be best used as a UPS)
Can Receive and send Phone Calls and SMS through embedded Earpiece
Why build This: Why not?

Too Lazy to create a setup guide and video.

Pictures here
