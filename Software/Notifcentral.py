#BlockComPi Notification Central
#Time Date check
import time
import datetime
#Batt Check
import serial
fona = serial.Serial('/dev/ttyAMA0',9600,timeout=0.1)
#Notif Button Setup
import RPi.GPIO as gpio
pin = 23 #GPIO pin for button
gpio.setmode(gpio.BCM)
gpio.setup(pin,gpio.IN,pull_up_down=gpio.PUD_UP)
#Buzzer Setup (disable I2C pins)
gpio.setup(17,gpio.OUT)

from PitftGraphicLib import *
initdis()

fona.write("atz\n") 
from Services import *
back = 0 
page = 0
prev = len(notif)
class NotificationsMenu:
 def __init__(self): pass
      
 # Slot Configuration
 def slotconf(self,slot, app):
    def rm(): 
      disinitdis()
      app[3]()
      notif.remove(app)
      initdis()
    if slot == 1:
        make_button(app[0], 25, 95, 27, 205, 5, app[1], app[2], rm) 

    if slot == 2:
        make_button(app[0], 25, 132, 27, 205, 5, app[1], app[2], rm) 

    if slot == 3:
        make_button(app[0], 25, 170, 27, 205, 5, app[1], app[2], rm) 

    if slot == 4:
        make_button(app[0], 25, 207, 27, 205, 5, app[1], app[2], rm)

    if slot == 5:
        make_button(app[0], 25, 245, 27, 205, 5, app[1], app[2], rm)

 def layout(self): 
   #Time and date 
   #global time
   time = datetime.datetime.now().time()
   make_label(str(time)[0:8], 20, 20, 47, cyan) #'10:30 am'
   date = datetime.date.today()
   make_label(date, 20, 55, 32, green) #'16/5/2015'
   
   #Battery Check
   fona.write('AT+CBC\n')
   output = fona.read(32)
   #print(output)
   battlevel = output[16:19]#length of string
   if len(battlevel) < 1: make_label('xxx%', 175, 30, 24, yellow)
   else: 
     if battlevel[2] == ',': make_label(battlevel[0:2]+'%', 175, 30, 24, yellow)
     else: make_label(battlevel+'%', 175, 30, 24, yellow)
   make_label('Battery', 175, 47, 18, yellow)    

   def exit(): 
     global back
     back = 1 
     if page == 0: back = 0
   def nextpage():
     clearall()
     global page
     page = page + 1
     NotificationsMenu().layout()
     global back
     NotificationsMenu().check(1)
     back = 0
     page = page - 1
     clearall()
     NotificationsMenu().layout()

   #counter = 0
   #while counter < 4: #Maximun no. of slots
   # if page*4+counter >= len(notif): break #Stop at no. of programs
   # NotificationsMenu().slotconf(counter+1, notif[page*4+counter])
   # counter = counter + 1
   # if counter == 5:
   #    if notif[page*4+5] != 0: notif.insert(page*4+5, 0) #Spacer
   counter = 1  
   while counter <= 4: #Maximun no. of slots
     if page*4+counter-1 >= len(notif): break #Stop at no. of programs
     NotificationsMenu().slotconf(counter, notif[page*4+counter-1])
     counter = counter + 1
     
   #make_button("Notification 1", 25, 95, 27, 205, 5, yellow, 24, empty)
   #make_button("Notification 2", 25, 132, 27, 205, 5, red, 24, empty)
   #make_button("Notification 3", 25, 170, 27, 205, 5, orange, 24, empty)
   #make_button("Notification 4", 25, 207, 27, 205, 5, cyan, 24, empty)
   #make_button("Notification 5", 25, 245, 27, 205, 5, blue, 24, empty)
   make_button('Back', 25, 245, 27, 95, 5, white, 24, exit)
   make_button('More...', 135, 245, 27, 95, 5, white, 24, nextpage)
   make_button("Programs", 25, 282, 27, 95, 5, white, 24, NotificationsMenu().programs) 
   make_button("Sleep", 135, 282, 27, 95, 5, white, 24, Sleep().start) 

 #Functions of buttons
 def empty(self):
   print('')
   sys.exit()
 def programs(self):
   global page
   page = 0
   clearall()
   ProgramsMenu().layout()
   global back
   while 1:
     touchdisch()
     NotificationsMenu().service(disinitdis,initdis,ProgramsMenu().layout)
     if back == 1: break
   back = 0
   clearall()
   NotificationsMenu().layout()

 def check(self,pgturn):
  while 1:
    touchdisch()
    #Notification/Service check
    NotificationsMenu().service(disinitdis,initdis,NotificationsMenu().layout)
    #Timedate check and notif update check
    if str(time)[0:8] != str(datetime.datetime.now().time())[0:8]: 
      clearall()  
      NotificationsMenu().layout()
    if pgturn == 1:
      if back == 1: break
   
 def service(self,setup,unsetup,layout):
   check()
   #Service check 
   global service
   if len(service) != 0:
    setup()
    service[0]()
    service.remove(service[0]) 
    unsetup()
    layout()
   global prev
   if prev < len(notif): 
     gpio.output(17,1)
     time.sleep(1)
     gpio.output(17,0)
   prev = len(notif)
  
lock = ''
code = '6969'
class Sleep():
 def __init__(self): pass
 def start(self):
   global back
   while True:
     Sleep().sleep()
     if back == 0: break
     else: back = 0
 def sleep(self):
   clearall()
   touchdisch()
   backlight(0)
   def nontouch():
     print('Service ACtivate') #Debugging
     while True:
       if not gpio.input(pin): break
     backlight(1)
     disinitdis()
   def backsleep():
     backlight(0)
     initdis()
   while True:
     NotificationsMenu().service(nontouch,initdis,Sleep().layout)
     if not gpio.input(pin): break
   backlight(1)
   #Pincode Input
   global back
   Sleep().layout()
   while True:
     NotificationsMenu().service(disinitdis,initdis,Sleep().layout)
     touchdisch()
     if str(time)[0:8] != str(datetime.datetime.now().time())[0:8]: 
       clearall()  
       Sleep().layout()
     if lock == code: break
     if not gpio.input(pin): 
       back = 1
       break  
   global lock
   lock = ''
   clearall()
   NotificationsMenu().layout()
 def layout(self):
     time = datetime.datetime.now().time()
     make_label(str(time)[0:8], 20, 20, 47, cyan) #'10:30 am'
     #Battery Check  
     fona.write('AT+CBC\n')
     output = fona.read(32)
     battlevel = output[16:19]#length of string
     if len(battlevel) < 1: make_label('xxx%', 175, 30, 24, yellow)
     else: 
       if battlevel[2] == ',': make_label(battlevel[0:2]+'%', 175, 30, 24, yellow)
       else: make_label(battlevel+'%', 175, 30, 24, yellow)
     make_label('Battery', 175, 47, 18, yellow)    
     #if battlevel[2] == ',': make_label(battlevel[0:2]+'%', 175, 30, 24, yellow)
     #else: make_label(battlevel+'%', 175, 30, 24, yellow)
     def exit(): pass
     def input(insert): 
       global lock
       lock = lock+insert
       clearall()
       Sleep().layout()
     def de():
      global lock
      lock = lock[:len(lock)-1]
      clearall()
      Sleep().layout()
     def one(): input('1')
     def two(): input('2')
     def three(): input('3')
     def four(): input('4')
     def five(): input('5')
     def six(): input('6')
     def seven(): input('7')
     def eight(): input('8')
     def nine(): input('9')
     def zero(): input('0')
     make_button(lock, 40, 70, 40, 166, 5, green, 40, exit)
     make_button('1', 40, 120, 35, 35, 5, cyan, 40, one)
     make_button('2', 103, 120, 35, 35, 5, cyan, 40, two)
     make_button('3', 166, 120, 35, 35, 5, cyan, 40, three)
     make_button('4', 40, 173, 35, 35, 5, cyan, 40, four)
     make_button('5', 103, 173, 35, 35, 5, cyan, 40, five)
     make_button('6', 166, 173, 35, 35, 5, cyan, 40, six)
     make_button('7', 40, 221, 35, 35, 5, cyan, 40, seven)
     make_button('8', 103, 221, 35, 35, 5, cyan, 40, eight)
     make_button('9', 166, 221, 35, 35, 5, cyan, 40, nine)
     make_button('0', 103, 269, 35, 35, 5, cyan, 40, zero)
     make_button('Del', 166, 269, 35, 35, 5, green, 25, de)

import subprocess
class ProgramsMenu():
 def __init__(self): pass
 
 # Slot Configuration
 def slotconf(self,slot, app):
    def setup():
      disinitdis()
      app[3]()
      def passs(): pass
      def killprogram(): app[4]()
      while True:
       #NotificationsMenu().service(app[4],app[3],passs)
       NotificationsMenu().service(killprogram,app[3],passs)
       if not gpio.input(pin):
         killprogram()
         break 
      initdis()
      ProgramsMenu().layout()
    # 1st Row, 1st Column
    if slot == 1:
        make_button(app[0], 30, 30, 55, 95, 10, app[1], app[2], setup)
  
   # 1st Row, 2nd Column
    if slot == 2:
        make_button(app[0], 135, 30, 55, 95, 10, app[1], app[2], setup)

    # 2nd Row, 1st Column
    if slot == 3:
        make_button(app[0], 30, 105, 55, 95, 10, app[1], app[2], setup)
        
    if slot == 4:
        make_button(app[0], 135, 105, 55, 95, 10, app[1], app[2], setup)
        
    if slot == 5:
        make_button(app[0], 30, 180, 55, 95, 10, app[1], app[2], setup)
        
    if slot == 6:
        make_button(app[0], 135, 180, 55, 95, 10, app[1], app[2], setup)
 
 def layout(self):
  def exit(): 
    global back
    back = 1 
  def nextpage():
    clearall()
    global page
    page = page + 1
    ProgramsMenu().layout()
    global back
    while 1:
      NotificationsMenu().service(disinitdis,initdis,ProgramsMenu().layout)
      touchdisch()
      if back == 1: break
    back = 0
    page = page - 1
    clearall()
    ProgramsMenu().layout()

  from App import programs
  global programs
  counter = 1
  while counter <= 6: #Maximun no. of slots
    if page*6+counter-1 >= len(programs): break #Stop at no. of programs
    ProgramsMenu().slotconf(counter, programs[page*6+counter-1])
    counter = counter + 1
  make_button('Back', 30, 255, 55, 95, 10, white, 24, exit)
  make_button('More', 135, 255, 55, 95, 10, white, 24, nextpage)

notifmenu = NotificationsMenu()
program = ProgramsMenu()
notifmenu.layout()
notifmenu.check(0)
