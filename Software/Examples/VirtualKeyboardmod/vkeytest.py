#!/usr/bin/python

#import pygame
from PitftGraphicLib import *
from virtualKeyboard import VirtualKeyboard

#import os
# Init framebuffer/touchscreen environment variables

# for Adafruit PiTFT:
#os.putenv('SDL_VIDEODRIVER', 'fbcon')
#os.putenv('SDL_FBDEV'      , '/dev/fb1')
#os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
#os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

# for X11 
#os.putenv('DISPLAY'   , '192.168.1.100:0.0')

## Init pygame and screen
#pygame.display.init()
#pygame.font.init()
#pygame.mouse.set_visible(False)
#size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
#print "Framebuffer size: %d x %d" % (size[0], size[1])
##screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
#size = (240,320)
screen = pygame.display.set_mode(size)

initdis()
pygame.draw.rect(screen, black, (0,0,240,320),0)

vkey = VirtualKeyboard(screen)
txt = vkey.run('default text')
print txt

