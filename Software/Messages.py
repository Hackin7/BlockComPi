#!/usr/bin/python

#import pygame
from PitftGraphicLib import *
from virtualKeyboard import VirtualKeyboard
import sys

# Init framebuffer/touchscreen 
screen = pygame.display.set_mode(size)
initdis()

from optparse import OptionParser
parser = OptionParser()
parser.add_option('-n', '--number', dest='Number', help='Number to Message To')
options, arguments = parser.parse_args()

#FONA setup
import serial
fona = serial.Serial('/dev/ttyAMA0',9600)
fona.write('AT+CMGF=1\n')

back = 0
txt = '1234567890123456789012345'#25 characters can fit into one line. 25 in the keyboard
no = ""
if options.Number: no = options.Number

def layout():
  make_button(no, 20, 20, 40, 210, 5, green, 40, dialer)
  if len(txt) > 25: 
    print('exceed')
  make_button(txt, 20, 70, 190, 210, 5, blue, 22, input)
  make_button("Back", 20, 270, 40, 100, 5, white, 30, quit)
  make_button("Send", 130, 270, 40, 100, 5, white, 30, send)
def dialer():
  def exit(): 
    global back
    back = 1
  def input(insert): 
     global no
     no = no+insert
     clearall()
     dialer()
  def de():
   global no
   no = no[:len(no)-1]
   clearall()
   dialer()
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
  def plus(): input('+')
  clearall()
  make_button(no, 20, 20, 40, 210, 5, green, 40, exit)
  make_button('Del', 166, 269, 40, 40, 5, green, 30, de)
  make_button('1', 40, 80, 40, 40, 5, cyan, 40, one)
  make_button('2', 103, 80, 40, 40, 5, cyan, 40, two)
  make_button('3', 166, 80, 40, 40, 5, cyan, 40, three)
  make_button('4', 40, 143, 40, 40, 5, cyan, 40, four)
  make_button('5', 103, 143, 40, 40, 5, cyan, 40, five)
  make_button('6', 166, 143, 40, 40, 5, cyan, 40, six)
  make_button('7', 40, 206, 40, 40, 5, cyan, 40, seven)
  make_button('8', 103, 206, 40, 40, 5, cyan, 40, eight)
  make_button('9', 166, 206, 40, 40, 5, cyan, 40, nine)
  make_button('+', 40, 269, 40, 40, 5, cyan, 40, plus)
  make_button('0', 103, 269, 40, 40, 5, cyan, 40, zero)
  while 1: 
    touchdisch()
    if back == 1: break
  global back
  back = 0
  clearall()
  layout()
def input():
  global txt
  vkey = VirtualKeyboard(screen)
  txt = vkey.run(txt)
  print txt
  clearall()
  layout()
def send():
  fona.write('AT+CMGS="' + no + '"\n')
  fona.write(txt)
  fona.write('\x1A')
  sys.exit()
def empty(): pass

clearall()
layout()
while 1: touchdisch()
 
