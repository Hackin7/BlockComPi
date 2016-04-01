#Custom Built phone app
from PitftGraphicLib import *
initdis()
import serial
fona = serial.Serial('/dev/ttyAMA0',9600,timeout=0.01)
no = ''

def call(): 
    global back
    back = 0
    fona.write('ATD'+no+';\n')
    clearall()
    def hangup():
      global back
      fona.write('ATH\n')
      back = 1
    make_button("If you're done", 22, 20, 50, 205, 5, cyan, 40, hangup) 
    while True: 
      touchdisch()
      if back == 1: break
    back = 0 
    clearall()
    dialer()

def dialer():
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
  make_button(no, 20, 20, 40, 210, 5, green, 40, call)
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

dialer()
while 1: touchdisch()
