## Buttons and labels
## First Row
#make_button("Phone", 30, 30, 55, 95, green, 24)
#make_button("Messages", 135, 30, 55, 95, cyan, 24)
## Second Row
#make_button("Contacts", 30, 105, 55, 95, yellow, 24)
#make_button("Notifications", 135, 105, 55, 95, white, 20)
## Third Row
#make_button("Notes", 30, 180, 55, 95, red, 24)
#make_button("Camera", 135, 180, 55, 95, orange, 24)
## Fourth Row

import subprocess, os, sys

#Do Not Edit
#colors     R    G    B
white   = (255, 255, 255)
red     = (255,   0,   0)
green   = (  0, 255,   0)
blue    = (  0,   0, 255)
black   = (  0,   0,   0)
cyan    = ( 50, 255, 255)
magenta = (255,   0, 255)
yellow  = (255, 255,   0)
orange  = (255, 127,   0)

def empty():pass
directory = "/mnt/RaspberryPi/BlockComPi/Software/"


def p():
  #Program launch
  print("Phone Dialer")
  #os.system("cd PiPhone-master/ && sudo python piphone.py ") #Write command to excute program
  os.system('sudo python Phone.py &')
def exit(): 
  os.system('pkill -f Phone.py')
  os.system("sleep 1")  
#Structure  (Label, colour, fontsize, setfunction, exitfunction)       
Phone = ("Phone", green, 24, p, exit)
###################################
def m():
  print("Messages")
  os.system("sudo python Messages.py &")
def exit(): 
  os.system('pkill -f Messages.py')
  os.system("sleep 1")
  #sys.exit()
Messages = ("Messages", cyan, 24, m, exit)
####################################
def c():
  print "Contacts"
  os.system('sudo python Contacts.py &')
def exit(): 
  os.system('pkill -f Contacts.py') 
  os.system('pkill -f Messages.py')
  os.system("sleep 1")  
Contacts = ("Contacts", yellow, 24, c, exit)
#####################################
def nn():
  print "Notes"
  sys.exit()

Notes = ("Notes", red, 24, nn, empty)
###############################
def cc():
  print "Camera"
  os.system("rmmod fb_ili9340")# Change rotation
  os.system("rmmod fbtft_device")# Change rotation
  os.system("modprobe fbtft_device name=pitft rotate=90")# Change rotation
  os.system("adafruit-pitft-touch-cal -f -r 90")# Change rotation
  os.system("cd Camera/adafruit-pi-cam-master/ && python cam.py ")
  #program = subprocess.Popen(["cd",directory+"Camera/adafruit-pi-cam-master","&&","sudo","python",directory+"Camera/adafruit-pi-cam-master/cam.py","&"], stdout=subprocess.PIPE)
  #return program
#def exit(): 
  os.system("rmmod fb_ili9340")# Change rotation
  os.system("rmmod fbtft_device")# Change rotation
  os.system("modprobe fbtft_device name=pitft rotate=180")# Change rotation
  os.system("adafruit-pitft-touch-cal -f -r 180")# Change rotation
def exit():
  os.system("sleep 1")
Camera = ("Camera", orange, 24, cc, empty)
#####################################
def p():
  print("Change Time")
  os.system("sudo python Changetime.py &")
def exit(): 
  os.system('pkill -f Changetime.py')
  os.system("sleep 1")
  #sys.exit()
Changetime = ("ChTime", cyan, 24, p, exit)
####################################
def s():
  print "Power Off"
  os.system("poweroff")

PowerOff = ("Power Off", red, 24, s, empty)
########################################
def x(): #Adding rotation increases risk of kernel errors
  print "X11"
  #os.system("mv /etc/X11/xorg.conf.d/99-calibration.conf /etc/X11/xorg.conf.d/99-calibration.conf.bak")
  #os.system("cp ../99-calibration.conf /etc/X11/xorg.conf.d/99-calibration.conf") #For X11 inaccurate caliobration
  os.system('tap /tmp/matchbox')
  os.system('echo "matchbox-desktop &" >> /tmp/matchbox') # desktop
  #os.system('echo "matchbox-panel &" >> /tmp/matchbox') #useless takes space
  os.system('echo "lxterminal -e matchbox-keyboard &" >> /tmp/matchbox') #doesnt work
  os.system('echo "matchbox-window-manager" >> /tmp/matchbox')
  os.system('FRAMEBUFFER=/dev/fb1 xinit /tmp/matchbox &')
def exit():
  os.system("pkill xinit")
  os.system('rm /tmp/matchbox')
  os.system("sleep 1")
matchbox  = ("X11", blue, 24, x, exit)
#########################################
def s():
  print "Exit"
  sys.exit()
Exit = ("Exit", white, 24, s, empty)
########################################
def x():
  print "Tablet Mode"
  os.system("sudo rmmod stmpe_ts") #Disable touchscreen interference
  #os.system('su pi -c startx &')
  os.system('startx &')
  #program = subprocess.Popen(["xinit","/tmp/matchbox","&"], stdout=subprocess.PIPE)
  #return program
def exit():
  os.system("pkill xinit")
  os.system("sudo modprobe stmpe_ts") #enable touchscreen
  os.system('sleep 1')
tabmode  = ("Tab Mode", red, 24, x, exit)

#Program layout can be according to piority
programs = [Phone,Messages,Contacts,Camera,matchbox,tabmode,Changetime,PowerOff,Exit]
