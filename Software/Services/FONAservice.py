# FONAservice 

back = 0
from PitftGraphicLib import *
import time
import serial
fona = serial.Serial('/dev/ttyAMA0',9600,timeout=0.01)
import RPi.GPIO as gpio
ring = 18 #GPIO pin for FONA RI
buzz = 2 #GPIO pin for buzzer
gpio.setmode(gpio.BCM)
gpio.setup(ring,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(buzz,gpio.OUT)
def func():
  time.sleep(1) 
  gpio.output(buzz,1)
  print('RING')
  initdis()
  make_label('RING', 20, 20, 94, green)
  def no(): 
    gpio.output(buzz,0)
    global back
    fona.write('ATH\n')
    back = 1
  def ans(): 
    gpio.output(buzz,0)
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
def check(): 
  if not gpio.input(ring): 
    global service
    return 1
    #service.insert(0,func)
  else: return 0 
