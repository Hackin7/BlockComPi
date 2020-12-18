# BlockComPi
A Block of a Computer of a Raspberry Pi phone 

Phone going to be useless by 2017

## Overview
Thought of what to do with your Raspberry Pi? During Mid 2015, I decided to use a Raspberry Pi 2, and mainly some other components to build a Raspberry Pi Phone, mainly because i had an Adafruit FONA 2G that is going to be outdated in 2017. This design is partially based on the PiPhone, because i also conveniently had a PiTFT 2.8 , so I couldn't use this TyPhone Design.

Components needed to build:

1. Raspberry Pi 2
1. Raspberry Pi Camera Module
1. Adafruit PiTFT 2.8 resistive
1. Adafruit FONA 2G (could use 3G but have to modify the design a bit)
1. Earphones with Mic
1. 5V boost converter 
1. 2000mah or so battery from phone
1. Buttons,  Female Headers, Diode
1. Wires and a PCB to connect everything together
1. White Acrylic Case with PLA filament from 3Doodler to connect the pieces together 
1. Wooden Back Plate
1. Black Stylus (Nintendo DS)
1. Buzzer (For Notifications) (connects through expansion port)

Software:

1. Based on Raspbian Jessie
1. Crappily Coded in Python
1. Uses PyGame, with PiTFT Rotated 180
1. garthvh's menu_8button.py is under no license, and has been adapted into PitftGraphicLib.py for easier use with PyGame in my code
1. No Bitmaps or images used
1. Note that virtual keyboard, licensed under the GNU GPL, is included, used, and has not been modified.
1. The Main Menu, Notifcentral.py, has a Notifications  and Service system and an App drawer which layout apps as in App.py
1. Can actually Receive and send Phone Calls and SMS through Notifications and Service System
1. The Apps included are, Phone, Messages (just something that sends Messages), Contacts, Camera, X11 and Tab Mode.
1. The ones coded my me are Phone (just a dialer ), Messages (just something that sends Messages), Contacts (stores contacts in config file
1. The Camera app actually adafruit pi cam software , which is included under BSD license
1. X11 shows the X Server with Matchbox Desktop Environment on PiTFT, while Tab Mode actually shows the full Raspbian Desktop through the main TV Output, HDMI or Composite

What it can do:

1. Modular (Anything Major like the PiTFT, Camera, Pi, FONA etc. can be removed and replaced)(Small components like the buttons can be easily desoldered)
1. Expandable (All unused GPIO can be used through the female header connectors, I2C is also available)(4 Full USB ports)
1. Can be used in other projects (eg. Upcoming Home Automation System)
1. Full power of Command Line and X11 Linux (Programming)
1. Portable use (But battery is not that good and would be best used as a UPS)
1. Can Receive and send Phone Calls and SMS through embedded Earpiece
1. Why build This: Why not?

That's all. Thanks for reading. Have Fun!

Original Source at http://makingbuildingstuff.blogspot.sg/2016/03/blockcompi-block-of-computer-of.html for more info

## Hardware
The Schematics are in the Image foler as Design.jpg

## Commands for Installation

These commands are to be run indiviually, not as a script

First, enable Camera and Boot to commandline ,while disabling serial and expanding filesystem in raspi-config"

### Only for PiTFT ready to go images for Raspbian (Jessie 24/6/15)

Enable X11 and set up internet connection in X11:
```
sudo rm /etc/X11/xorg.conf.d/99-fbdev.conf # allow x11
FRAMEBUFFER=/dev/fb0 startx
```
Install Software:
`sudo apt-get install matchbox `

### Install the Pitft Software and other dependencies  only for Pure Raspbian image as of 30/10/2016:
```
curl -SLs https://apt.adafruit.com/add-pin | sudo bash
sudo apt-get install raspberrypi-bootloader adafruit-pitft-helper matchbox python-pip
sudo pip install picamera==0.8 #Adafruit Camera software install
```

Enable boot to command prompt and disable gpio 23 as on/off switch":

`sudo adafruit-pitft-helper -t 28r`

Change Rotaion settings to 180 and add the line "enable_uart=1":

`sudo nano +180 /boot/config.txt`

Fix Sofware problems:
```
sudo apt-get install libsmpeg0
cd /tmp
wget archive.raspbian.org/raspbian/pool/main/libs/libsdl1.2/libsdl1.2debian_1.2.15-5_armhf.deb
sudo dpkg -i libsdl1.2debian_1.2.15-5_armhf.deb 
wget archive.raspbian.org/raspbian/pool/main/p/pygame/python-pygame_1.9.1release+dfsg-10_armhf.deb
sudo dpkg -i python-pygame_1.9.1release+dfsg-10_armhf.deb
```

Copy Main Program Files(Software) to /home/pi or something '

Insert the following below inside rc.local before "exit 0":
```
rm -rf /etc/X11/xorg.conf.d/99-fbdev.conf
sudo adafruit-pitft-touch-cal -f -r 180
cd /home/pi/Software && sudo python Notifcentral.py
```

## Acknowledgments
garthvh's menu_8button.py is under no license, and has been adapted into PitftGraphicLib.py for easier use with PyGame in my cod
