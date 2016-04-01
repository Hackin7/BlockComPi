# FONAmessage 

from PitftGraphicLib import *
green   = (  0, 255,   0)

import serial
fona = serial.Serial('/dev/ttyAMA0',9600,timeout=0.1)
fona.write('AT+CMGF=1\n')
def finder():
  global sms
  sms = 1
  fona.write('AT+CMGL=1\n')
  fona.read(10000)
  while True:
    fona.write('AT+CMGR='+str(sms)+'\n')
    output = fona.read(10000) #Max limit
    #print output
    char = 11 + len(str(sms)) - 1
    #print output[char:char+2]
    if output[char:char+2] =='OK': break # Max sms limit
    sms = sms + 1
  print sms # Debugging
  return sms
finder()

import time
def func(mmm):
  global back
  back = 0 
  initdis()
  print(mmm)
  fona.write('AT+CMGR='+str(mmm-1)+'\n')
  output = fona.read(10000) 
  #output = "123456789a123456789b123456789c123456789a123456789b123456789c" + output #For Debugging
  line = 0
  while line*17+16  <= len(output):
    make_label(output[line*17:line*17+17], 20, line*20+20, 30, green) #17 characters can fit on one line
    line = line + 1
  l = len(output)-line*17
  make_label(output[line*17:line*17+l+1], 20, line*20+20, 30, green)
  def quit(): 
    global back
    back = 1
  make_button("Back", 20, 270, 40, 100, 5, white, 30, quit)
  while True:
    touchdisch()
    if back == 1: break
  disinitdis()

def passs(): pass 
layout = ("New Message", green, 24, passs)
def check(): 
  fona.write('AT+CMGR='+str(sms)+'\n')
  output = fona.read(10000) #Max limit
  char = 11 + len(str(sms)) - 1
  #print output[char:char+2]
  if output[char:char+2] !='OK':
    finder()
    mms = sms
    def show(): func(mms)
    global layout
    layout = ("New Message "+str(sms-1), green, 24, show)
    return 1
  else: return 0 
