# BlockComPi
A Block of a Computer of a Raspberry Pi phone 

Phone going to be useless by 2017

Check http://makingbuildingstuff.blogspot.sg/2016/03/blockcompi-block-of-computer-of.html for more info

##Hardware
THe Schematics are in the Image foler as Design.jpg

##Commands for Installation
\#These commands are to be run indiviually, not as a script

\#First, enable Camera and Boot to commandline ,while disabling serial and expanding filesystem in raspi-config"

###Only for PiTFT ready to go images for Raspbian (Jessie 24/6/15)
\#Enable X11 and set up internet connection in X11:
```
sudo rm /etc/X11/xorg.conf.d/99-fbdev.conf # allow x11
FRAMEBUFFER=/dev/fb0 startx
```
\#Install Software:
`sudo apt-get install matchbox `

###Install the Pitft Software and other dependencies  only for Pure Raspbian image as of 30/10/2016:
```
curl -SLs https://apt.adafruit.com/add-pin | sudo bash
sudo apt-get install raspberrypi-bootloader adafruit-pitft-helper matchbox python-pip
sudo pip install picamera==0.8 #Adafruit Camera software install
```

\#Enable boot to command prompt and disable gpio 23 as on/off switch":

`sudo adafruit-pitft-helper -t 28r`
\#Change Rotaion settings to 180 and add the line "enable_uart=1":

`sudo nano +180 /boot/config.txt`

\#Fix Sofware problems:
```
sudo apt-get install libsmpeg0
cd /tmp
wget archive.raspbian.org/raspbian/pool/main/libs/libsdl1.2/libsdl1.2debian_1.2.15-5_armhf.deb
sudo dpkg -i libsdl1.2debian_1.2.15-5_armhf.deb 
wget archive.raspbian.org/raspbian/pool/main/p/pygame/python-pygame_1.9.1release+dfsg-10_armhf.deb
sudo dpkg -i python-pygame_1.9.1release+dfsg-10_armhf.deb
```

\#Copy Main Program Files(Software) to /home/pi or something '

\#Insert the following below inside rc.local before "exit 0":
```
rm -rf /etc/X11/xorg.conf.d/99-fbdev.conf
sudo adafruit-pitft-touch-cal -f -r 180
cd /home/pi/Software && sudo python Notifcentral.py
```

## Acknowledgments
garthvh's menu_8button.py is under no license, and has been adapted into PitftGraphicLib.py for easier use with PyGame in my cod
