#Do Not Edit
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

#The Service/Notifications List
# Layout: import (service)
import FONAservice 
import FONAmessage

service = [] 
def run(sv):
  global service
  #print service
  if sv.check() == 1: service.insert(0,sv.func)

def code():
  print 'WHAT THE FRUCK IS THIS MOTHERFUCKING SHIT?'
 #Put code to direct to other program

notif = [("F", green, 24, code),("F", blue, 24, code),("F", red, 24, code),("F", cyan, 24, code),("F", yellow, 24, code)]

def putup(nc): 
  global notif
  #                Notif Structure  (Label, colour, fontsize, setfunction) 
  if nc.check() == 1: notif.insert(0, nc.layout)

shit = 1

def check():
  global notif
  #Notif layout: putup(notif)
  putup(FONAmessage) 
  global shit
  if shit == 1: 
     #Notif Structure  (Label, colour, fontsize, setfunction)       
     notif.insert(0, ("F", green, 24, code))
     shit = 0

  global service
 #Service layout: run(service)
  run(FONAservice)
