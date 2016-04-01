#Based on gerthvh's menu_8button.py
#BlockComPhone Pi Menu 
import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
from subprocess import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

# Initialize pygame and hide mouse
pygame.init()
pygame.mouse.set_visible(0)

#set size of the screen
size = width, height = 240, 320
screen = pygame.display.set_mode(size)

# define function for printing text in a specific place with a specific width and height with a specific colour and border
def make_button(text, xpo, ypo, height, width, colour, fontsize):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))
    pygame.draw.rect(screen, colour, (xpo-10,ypo-10,width,height),3)

# define function for printing text in a specific place with a specific colour
def make_label(text, xpo, ypo, fontsize, colour):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

def empty():
  print("")

# Slot Configuration
def slotconf(slot, app):
    # 1st Row, 1st Column
    if slot == 1:
        make_button(app[0], 30, 30, 55, 95, app[1], app[2])
        global slot1 
        slot1 = app[3] 
  
   # 1st Row, 2nd Column
    if slot == 2:
        make_button(app[0], 135, 30, 55, 95, app[1], app[2])
        global slot2
        slot2 = app[3] 

    # 2nd Row, 1st Column
    if slot == 3:
        make_button(app[0], 30, 105, 55, 95, app[1], app[2])
        global slot3
        slot3 = app[3] 

    if slot == 4:
        make_button(app[0], 135, 105, 55, 95, app[1], app[2])
        global slot4
        slot4 = app[3]

    if slot == 5:
        make_button(app[0], 30, 180, 55, 95, app[1], app[2])
        global slot5 
        slot5 = app[3]

    if slot == 6:
        make_button(app[0], 135, 180, 55, 95, app[1], app[2])
        global slot6  
        slot6 = app[3]

    if slot == 7:
        make_button(app[0], 30, 255, 55, 95, app[1], app[2])
        global slot7
        slot7 = app[3]

    if slot == 8:
        make_button(app[0], 135, 255, 55, 95, app[1], app[2])
        global slot8
        slot8 = app[3]

# define function that checks for touch location
def on_touch():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    #  x_min                 x_max   y_min                y_max
    # button 1 event
    if 30 <= touch_pos[0] <= 95 and 30 <= touch_pos[1] <=85:
            print(1)
            pygame.quit()
            slot1()
            sys.exit()
    # button 2 event
    if 135 <= touch_pos[0] <= 230 and 30 <= touch_pos[1] <=85:
            print(2)
            pygame.quit()
            slot2()
            sys.exit()
    # button 3 event
    if 30 <= touch_pos[0] <= 95 and 105 <= touch_pos[1] <=160:
            print(3)
            pygame.quit()
            slot3()
            sys.exit()
    # button 4 event
    if 135 <= touch_pos[0] <= 230 and 105 <= touch_pos[1] <=160:
            print(4)
            pygame.quit()
            slot4()
            sys.exit()
    # button 5 event
    if 30 <= touch_pos[0] <= 95 and 180 <= touch_pos[1] <=235:
            print(5)
            pygame.quit()
            slot5()
            sys.exit()
    # button 6 event
    if 135 <= touch_pos[0] <= 230 and 180 <= touch_pos[1] <=235:
            print(6)
            pygame.quit()
            slot6()
            sys.exit()
    # button 7 event
    if 30 <= touch_pos[0] <= 95 and 255 <= touch_pos[1] <=310:
            print(7)
            pygame.quit()
            slot7()
            sys.exit()
    # button 8 event
    if 135 <= touch_pos[0] <= 230 and 255 <= touch_pos[1] <=310:
            print(8)
            pygame.quit()
            slot8()
            sys.exit()

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

# Set up the base menu you can customize your menu with the colors above

# Background Color
screen.fill(black)

# Outer Border
pygame.draw.rect(screen, red, (0,0,240,320),10)

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
#make_button("Settings", 30, 255, 55, 95, blue, 24)
#make_button("More", 135, 255, 55, 95, blue, 24)

from App import *
slotconf(1, Phone)
slotconf(2, Messages)
slotconf(3, Contacts)
slotconf(4, Notifications)
slotconf(5, Notes)
slotconf(6, Camera)
slotconf(7, Settings)
slotconf(8, More)

# While loop to manage touch screen inputs
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print "screen pressed" #for debugging purposes
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            print pos #for checking
            #pygame.draw.circle(screen, white, pos, 2, 0) #for debugging purposes - adds a small dot where the screen is pressed
            on_touch()

#ensure there is always a safe way to end the program if the touch screen fails

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    pygame.display.update()
