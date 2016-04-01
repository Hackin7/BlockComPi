#Changetime to make up for lack of RTC
from PitftGraphicLib import *
initdis()
#Time Date check
from time import sleep
import datetime
import os

switch = 0
back = 0
modtime = ''
def layout(what,info):
     make_label(info, 175, 30, 24, yellow)
     make_label('Set '+what, 20, 20, 47, cyan) #'10:30 am'
     def exit(): 
       clearall()
       global back
       back = 1
     def change():
       global switch
       switch = 1
     def input(insert): 
       global modtime
       modtime = modtime+insert
       clearall()
       layout(what,info)
     def de():
      global modtime
      modtime = modtime[:len(modtime)-1]
      clearall()
      layout(what,info)
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
     make_button(modtime, 40, 70, 40, 166, 5, green, 40, exit)
     make_button('1', 40, 120, 35, 35, 5, cyan, 40, one)
     make_button('2', 103, 120, 35, 35, 5, cyan, 40, two)
     make_button('3', 166, 120, 35, 35, 5, cyan, 40, three)
     make_button('4', 40, 173, 35, 35, 5, cyan, 40, four)
     make_button('5', 103, 173, 35, 35, 5, cyan, 40, five)
     make_button('6', 166, 173, 35, 35, 5, cyan, 40, six)
     make_button('7', 40, 221, 35, 35, 5, cyan, 40, seven)
     make_button('8', 103, 221, 35, 35, 5, cyan, 40, eight)
     make_button('9', 166, 221, 35, 35, 5, cyan, 40, nine)
     make_button('Switch', 40, 269, 35, 35, 5, green, 15, change)
     make_button('0', 103, 269, 35, 35, 5, cyan, 40, zero)
     make_button('Del', 166, 269, 35, 35, 5, green, 25, de)

def no():
  clearall()
  make_label('NO!', 20, 20, 94, green)
  touchdisch()
  sleep(1)
  clearall()

def show():
  clearall()
  #Time and date 
  #global time
  time = datetime.datetime.now().time()
  make_label(str(time)[0:8], 20, 20, 47, cyan) #'10:30 am'
  date = datetime.date.today()
  make_label(date, 20, 55, 32, green) #'16/5/2015'
  touchdisch()
  sleep(5)
  clearall()

def date():
  global switch
  global back
  global modtime
  layout('Date','dd')
  while True:
    touchdisch()
    if switch == 1: break
    if back == 1:
      back = 0
      if len(modtime) == 2: break
      else: 
        no()
        layout('Date','dd')
  date = modtime
  modtime = ''
  clearall()
  ###################################
  layout('Month','mm')
  while True:
    touchdisch()
    if switch == 1: break
    if back == 1:
      back = 0
      if len(modtime) == 2: break
      else: 
        no()
        layout('Month','mm')
  month = modtime
  modtime = ''
  clearall()
  ###################################
  layout('Year','yyyy')
  while True:
    touchdisch()
    if switch == 1: break
    if back == 1:
      back = 0
      if len(modtime) == 4: break
      else: 
        no()
        layout('Year','yyyy')
  year = modtime
  modtime = ''
  clearall()
  if len(date) != 2: pass
  elif len(month) != 2: pass
  elif len(year) != 4: pass
  elif switch == 1: pass
  else: os.system('sudo date +%Y%m%d -s "'+year+month+date+'"')
  switch = 0

def chtime():
  global switch
  global back
  global modtime
  layout('Time','h:m:s')
  while True:
    touchdisch()
    if len(modtime) == 2:
      if prev > len(modtime):
        modtime = modtime[0]
        clearall()
        layout('Time','h:m:s') 
      else:
        modtime = modtime+':'
        clearall()
        layout('Time','h:m:s')
    if len(modtime) == 5:
      if prev > len(modtime):
        modtime = modtime[0:4]
        clearall()
        layout('Time','h:m:s') 
      else:
        modtime = modtime+':'
        clearall()
        layout('Time','h:m:s')
    prev = len(modtime)
    if switch == 1: break
    if back == 1:
      back = 0
      if len(modtime) == 8: break
      else: 
        no()
        layout('Time','h:m:s')
  time = modtime
  modtime = ''
  clearall()
  ###################################
  if len(time) != 8: pass
  elif switch == 1: pass
  else: os.system('sudo date +%T -s "'+time+'"')
  switch = 0

while True:
  chtime()
  show()
  date()
  show()