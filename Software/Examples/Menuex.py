#Based on gerthvh's menu_8button.py
#BlockComPhone Pi Menu example
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

# define function that checks for touch location
def on_touch():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    #  x_min                 x_max   y_min                y_max
    # button 1 event
    if 30 <= touch_pos[0] <= 95 and 30 <= touch_pos[1] <=85:
            button(1)
    # button 2 event
    if 135 <= touch_pos[0] <= 230 and 30 <= touch_pos[1] <=85:
            button(2)
    # button 3 event
    if 30 <= touch_pos[0] <= 95 and 105 <= touch_pos[1] <=160:
            button(3)
    # button 4 event
    if 135 <= touch_pos[0] <= 230 and 105 <= touch_pos[1] <=160:
            button(4)
    # button 5 event
    if 30 <= touch_pos[0] <= 95 and 180 <= touch_pos[1] <=235:
            button(5)
    # button 6 event
    if 135 <= touch_pos[0] <= 230 and 180 <= touch_pos[1] <=235:
            button(6)
    # button 7 event
    if 30 <= touch_pos[0] <= 95 and 255 <= touch_pos[1] <=310:
            button(7)
    # button 8 event
    if 135 <= touch_pos[0] <= 230 and 255 <= touch_pos[1] <=310:
            button(8)

# Define each button press action
def button(number):
    print "You pressed menu item",number

    if number == 1:
        #time.sleep(5) #do something interesting here
        sys.exit()

    if number == 2:
        #time.sleep(5) #do something interesting here
        sys.exit()

    if number == 3:
        #time.sleep(5) #do something interesting here
        sys.exit()

    if number == 4:
        #time.sleep(5) #do something interesting here
        sys.exit()

    if number == 5:
        #time.sleep(5) #do something interesting here
        sys.exit()

    if number == 6:
        #time.sleep(5) #do something interesting here
        sys.exit()

    if number == 7:
        #time.sleep(5) #do something interesting here
        sys.exit()

    if number == 8:
        #time.sleep(5) #do something interesting here
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

#set size of the screen
size = width, height = 240, 320
screen = pygame.display.set_mode(size)

# Background Color
screen.fill(black)

# Outer Border
pygame.draw.rect(screen, blue, (0,0,240,320),10)

# Buttons and labels
# First Row
make_button("Menu Item", 30, 30, 55, 95, red, 24)
make_button("Menu Item 2", 135, 30, 55, 95, blue, 24)
# Second Row
make_button("Menu Item 3", 30, 105, 55, 95, red, 24)
make_button("Menu item 4", 135, 105, 55, 95, blue, 24)
# Third Row
make_button("Menu item 5", 30, 180, 55, 95, blue, 24)
make_button("Menu item 6", 135, 180, 55, 95, blue, 24)
# Fourth Row
make_button("Menu item 7", 30, 255, 55, 95, blue, 24)
make_button("Menu item 8", 135, 255, 55, 95, blue, 24)

# While loop to manage touch screen inputs
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print "screen pressed" #for debugging purposes
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            print pos #for checking
            pygame.draw.circle(screen, white, pos, 2, 0) #for debugging purposes - adds a small dot where the screen is pressed
            on_touch()

#ensure there is always a safe way to end the program if the touch screen fails

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    pygame.display.update()
