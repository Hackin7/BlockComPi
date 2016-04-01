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
#set size of the screen
size = width, height = 240, 320
#screen = pygame.display.set_mode(size)

def initdis():
  global screen
  screen = pygame.display.set_mode(size)
  # Initialize pygame and hide mouse
  pygame.init()
  pygame.mouse.set_visible(0)
  screen = pygame.display.set_mode(size)
  # Background Color
  screen.fill(black)
  # Outer Border
  pygame.draw.rect(screen, red, (0,0,240,320),10)

def disinitdis():
  pygame.quit()
  global touchlist
  touchlist = []  
  
def clear(xpos,ypos,length,height):
  pygame.draw.rect(screen, black, (xpos,ypos,length,height),0)

def clearall():
  pygame.draw.rect(screen, black, (0,0,240,320),0)
  pygame.draw.rect(screen, red, (0,0,240,320),10)
  global touchlist
  touchlist = []  
   
  
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

touchlist = []
# define function for printing text in a specific place with a specific width and height with a specific colour and border
def make_button(text, xpo, ypo, height, width, recspace, colour, fontsize, function):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))
    #Space between rec and label
    pygame.draw.rect(screen, colour, (xpo-recspace,ypo-recspace,width,height),3)
    #Touchscreen
    global touchlist 
    touchlist.append((xpo,width+xpo,ypo,height+ypo,function))

# define function for printing text in a specific place with a specific colour
def make_label(text, xpo, ypo, fontsize, colour):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

# define function that checks for touch location
def on_touch():
    counterst = 0
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    while counterst < len(touchlist):
      if touchlist[counterst][0] <= touch_pos[0] <= touchlist[counterst][1] and touchlist[counterst][2] <= touch_pos[1] <= touchlist[counterst][3]:
          touchlist[counterst][4]()
      counterst = counterst + 1
 

def touchdisch():

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
