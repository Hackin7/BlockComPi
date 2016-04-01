#BlockComPi Contacts Menu
from PitftGraphicLib import *
 
page = 0
back = 0
indexno = 0
import Contactlist
class List():
 def __init__(self): pass
 
 def layout(self,):
  def slotconf(slot,list):
    def choose():
      clearall()
      global page
      pageold = page
      page = 0
      Menu().layout(list[0],list[1:])
      global back
      while 1: 
        touchdisch()
        if back == 1: break
      back = 0
      clearall()
      page = pageold
      List().layout()
    if slot == 1: make_button(list[0], 25, 58, 27, 205, 5, green, 25, choose)
    if slot == 2: make_button(list[0], 25, 95, 27, 205, 5, green, 25, choose)
    if slot == 3: make_button(list[0], 25, 132, 27, 205, 5, green, 25, choose)
    if slot == 4: make_button(list[0], 25, 170, 27, 205, 5, green, 25, choose) 
    if slot == 5: make_button(list[0], 25, 207, 27, 205, 5, green, 25, choose)
    if slot == 6: make_button(list[0], 25, 245, 27, 205, 5, green, 25, choose)
     
  def exit(): 
    global back
    back = 1 
  def nextpage():
    clearall()
    global page
    page = page + 1
    List().layout()
    global back
    while 1:
      touchdisch()
      if back == 1: break
    back = 0
    page = page - 1
    clearall()
    List().layout()
  
  counter = 1
  while counter <= 6: #Maximun no. of slots
    if page*6+counter-1 >= len(Contactlist.list): break #Stop at no. of programs
    slotconf(counter, Contactlist.list[page*6+counter-1])
    counter = counter + 1
  make_button('Back', 25, 21, 27, 205, 5, cyan, 25, exit)
  make_button('More', 25, 282, 27, 205, 5, cyan, 25, nextpage)
 
 def choice(self):
   global back
   def layout():
    def slotconf(slot,list):
      def choose():
        clearall()
        global chosen
        chosen = list
        global back
        back = -1 
      if slot == 1: make_button(list[0], 25, 58, 27, 205, 5, green, 25, choose)
      if slot == 2: make_button(list[0], 25, 95, 27, 205, 5, green, 25, choose)
      if slot == 3: make_button(list[0], 25, 132, 27, 205, 5, green, 25, choose)
      if slot == 4: make_button(list[0], 25, 170, 27, 205, 5, green, 25, choose) 
      if slot == 5: make_button(list[0], 25, 207, 27, 205, 5, green, 25, choose)
      if slot == 6: make_button(list[0], 25, 245, 27, 205, 5, green, 25, choose)
       
    def exit(): 
      global back
      back = 1 
    def nextpage():
      clearall()
      global page
      page = page + 1
      layout()
      global back
      while 1:
        touchdisch()
        if back == 1: break
      back = 0
      page = page - 1
      clearall()
      layout()
    
    counter = 1
    while counter <= 6: #Maximun no. of slots
      if page*6+counter-1 >= len(Contactlist.list): break #Stop at no. of programs
      slotconf(counter, Contactlist.list[page*6+counter-1])
      counter = counter + 1
    make_button('Back', 25, 21, 27, 205, 5, cyan, 25, exit)
    make_button('More', 25, 282, 27, 205, 5, cyan, 25, nextpage)
   layout()
   while 1: 
     touchdisch()
     if back == -1: break
   clearall()
   back = 0
   return chosen  

class Menu():
 def __init__(self): pass
  
 def layout(self,name,numbers):
  def slotconf(slot,no):
    def sms():
      disinitdis()
      os.system('sudo python Messages.py -n ' + no)
      initdis()
      Menu().layout(name,numbers)
    def ans(): 
      def done(): 
        global back
        fona.write('ATH\n')
        back = 1
      global back
      fona.write('ATD' + no + ';\n')
      fona.write('ATD' + no + ';\n')
      clearall()
      make_button("If you're done", 22, 20, 50, 205, 5, cyan, 40, done) 
      make_label(no,22,90,35,green)
      while True: 
        touchdisch()
        if back == 1: break
      back = 0 
      clearall()
      Menu().layout(name,numbers)
  
    if slot == 1:
        make_label(no, 20, 60, 35, green)
        make_button('Call', 30, 100, 35, 95, 10, white, 24, ans)
        make_button('SMS', 135, 100, 35, 95, 10, white, 24, sms)
    if slot == 2:
        make_label(no, 20, 130, 35, green)
        make_button('Call', 30, 170, 35, 95, 10, white, 24, ans)
        make_button('SMS', 135, 170, 35, 95, 10, white, 24, sms)

  def exit(): 
    global back
    back = 1 
  def nextpage():
    clearall()
    global page
    page = page + 1
    Menu().layout(name,numbers)
    global back
    while 1:
      touchdisch()
      if back == 1: break
    back = 0
    page = page - 1
    clearall()
    Menu().layout(name,numbers)
  
  counter = 1
  while counter <= 2: #Maximun no. of slots
    if page*2+counter-1 >= len(numbers): break #Stop at no. of programs
    slotconf(counter, numbers[page*2+counter-1])
    counter = counter + 1
    #if counter == 3:
    #   if numbers[page*2+3-1] != 0: numbers.insert(page*2+3-1, 0) #Spacer
  make_label(name, 20, 20, 47, cyan)
  make_button('Back', 30, 275, 35, 95, 10, white, 24, exit)
  make_button('More', 135, 275, 35, 95, 10, white, 24, nextpage)

#while 1: touchdisch()
#app = ('Test', cyan, 25,sys.exit)
#make_button(app[0], 25, 21, 27, 205, 5, app[1], app[2], app[3])
#make_button(app[0], 25, 58, 27, 205, 5, green, app[2], app[3])#
#make_button(app[0], 25, 95, 27, 205, 5, green, app[2], app[3])#
#make_button(app[0], 25, 132, 27, 205, 5, green, app[2], app[3])#
#make_button(app[0], 25, 170, 27, 205, 5, green, app[2], app[3])# 
#make_button(app[0], 25, 207, 27, 205, 5, green, app[2], app[3])#
#make_button(app[0], 25, 245, 27, 205, 5, green, app[2], app[3])#
#make_button(app[0], 25, 282, 27, 205, 5, app[1], app[2], app[3])

if __name__ == "__main__":
  initdis()
  import os
  import serial
  fona = serial.Serial('/dev/ttyAMA0',9600,timeout=0.01)
  list = List()
  list.layout()
  while 1: touchdisch()