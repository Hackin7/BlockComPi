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
 
service = []

back = 0
from PitftGraphicLib import *
import serial
fona = serial.Serial('/dev/ttyAMA0',9600,timeout=0.01)
import RPi.GPIO as gpio
ring = 18 #GPIO pin for FONA RI
gpio.setmode(gpio.BCM)
gpio.setup(ring,gpio.IN,pull_up_down=gpio.PUD_UP)
def func(): 
  print('RING')
  initdis()
  make_label('RING', 20, 20, 94, green)
  def no(): 
    global back
    fona.write('ATH\n')
    back = 1
  def ans(): 
    global back
    fona.write('ATA\n')
    clearall()
    make_button("If you're done", 22, 20, 50, 205, 5, cyan, 40, no) 
    while True: 
      touchdisch()
      if back == 1: break
    back = 0 
  make_button('Answer', 22, 180, 50, 205, 5, cyan, 47, ans)
  make_button('Be an Asshole', 22, 240, 50, 205, 5, red, 40, no)
  while True:
    touchdisch()
    if gpio.input(ring): break
  disinitdis()
def callcheck(): 
  if not gpio.input(ring): 
    global service
    service.insert(0,func)

shit = 1
def code():
  print 'WHAT THE FRUCK IS THIS MOTHERFUCKING SHIT?'
 #Put code to direct to other program

notif = [("F", green, 24, code),("F", blue, 24, code),("F", red, 24, code),("F", cyan, 24, code),("F", yellow, 24, code)]

def check():
  global notif
  global shit
  if shit == 1: 
     #Notif Structure  (Label, colour, fontsize, setfunction)       
     notif.insert(0, ("F", green, 24, code))
     shit = 0

  global service
  #global crap
  #if crap == 1:
  #   #Service structure  (function)
  #   service.insert(0, function)
  #   #print service #Debugging
  #   crap = 0
  callcheck()
