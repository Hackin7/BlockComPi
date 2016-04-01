#BlockComPhone Pi Notification Central
from PitftGraphicLib import *
import sys
import os
import time
initdis()
  
# Slot Configuration
def slotconf(slot, app):
    if slot == 1:
        make_button(app[0], 25, 95, 27, 205, 5, app[1], app[2], app[3]) 

    if slot == 2:
        make_button(app[0], 25, 132, 27, 205, 5, app[1], app[2], app[3]) 

    if slot == 3:
        make_button(app[0], 25, 170, 27, 205, 5, app[1], app[2], app[3]) 

    if slot == 4:
        make_button(app[0], 25, 207, 27, 205, 5, app[1], app[2], app[3])

    if slot == 5:
        make_button(app[0], 25, 245, 27, 205, 5, app[1], app[2], app[3])

def empty():
  print('')
  sys.exit()

def menu():
  pygame.quit()
  os.system('sudo python Menulib.py')
  sys.exit()

ch = 0
def nextpage():
    print('Button Pressed') #Debugging
    global ch 
    if ch < 1:
       print('Next Page') #Debugging
       pygame.quit
       initdis()
       layout(1)
       ch = 1 #have timer to reset to zero after some time so can repeat press

# define function that checks for touch location (made obselete with lib)
#def on_touch():
#    # get the position that was touched
#    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
#    #  x_min                 x_max   y_min                y_max
#    # button 1 event
#    if 25 <= touch_pos[0] <= 230 and 95 <= touch_pos[1] <= 122:
#            print(1)
#            pygame.quit()
#            slot1()
#            sys.exit()
#    # button 2 event
#    if 25 <= touch_pos[0] <= 205 and 132 <= touch_pos[1] <= 159:
#            print(2)
#            pygame.quit()
#            slot2()
#            sys.exit()
#    # button 3 event
#    if 25 <= touch_pos[0] <= 205 and 170 <= touch_pos[1] <= 197:
#            print(3)
#            pygame.quit()
#            slot3()
#            sys.exit()
#    # button 4 event
#    if 25 <= touch_pos[0] <= 205 and 207 <= touch_pos[1] <= 234:
#            print(4)
#            pygame.quit()
#            slot4()
#            sys.exit()
#    # button 5 event
#    if 25 <= touch_pos[0] <= 205 and 245 <= touch_pos[1] <= 272:
#            print(5)
#            pygame.quit()
#            slot5()
#            sys.exit()
#    # button 6 event
#    if 25 <= touch_pos[0] <= 120 and 282 <= touch_pos[1] <= /////309:/
#            print(6)
#            pygame.quit()
#            slot6()
#            sys.exit()
#   
#    # button 7 event
#    if 135 <= touch_pos[0] <= 230 and 282 <= touch_pos[1] <= 309:
#            print(6)
#            pygame.quit()
#            initdis()
#            touch(empty)
#            #slot7()
#            #sys.exit()
# Set up the base menu you can customize your menu with the colors above

from Service import *
def layout(test):
  make_label('10:30 am', 20, 20, 47, cyan)
  make_label('16/5/2015', 20, 55, 32, green)
  make_label('100% ', 175, 30, 24, yellow)
  make_label('Charging', 175, 47, 18, yellow)

  #slotconf(1,("Notification 1", yellow, 24, empty))
  if test == 1: #Debugging
    slotconf(2,("Notification 2", red, 24, empty))
  slotconf(3,("Notification 3", yellow, 24, empty))
  slotconf(4,("Notification 4", cyan, 24, empty))
  slotconf(5,("Notification 5", blue, 24, empty))

  #make_button("Notification 1", 25, 95, 27, 205, 5, yellow, 24, empty)
  #make_button("Notification 2", 25, 132, 27, 205, 5, red, 24, empty)
  #make_button("Notification 3", 25, 170, 27, 205, 5, orange, 24, empty)
  #make_button("Notification 4", 25, 207, 27, 205, 5, cyan, 24, empty)
  #make_button("Notification 5", 25, 245, 27, 205, 5, blue, 24, empty)
  make_button("Menu", 25, 282, 27, 95, 5, white, 24, menu)
  make_button("More...", 135, 282, 27, 95, 5, white, 24, nextpage) 

layout(0)
while 1:
  touchdisch()
  #Notification/Service check
  p()
  counter = len(notif)
  counterst = 0
  while counterst < counter:
    slotconf(counterst + 1, notif[counterst])
    counterst = counterst + 1
