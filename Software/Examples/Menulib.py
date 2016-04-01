from PitftGraphicLib import *
initdis()

def empty():
  print("")

# Slot Configuration
def slotconf(slot, app):
    # 1st Row, 1st Column
    if slot == 1:
        make_button(app[0], 30, 30, 55, 95, 10, app[1], app[2], app[3])
  
   # 1st Row, 2nd Column
    if slot == 2:
        make_button(app[0], 135, 30, 55, 95, 10, app[1], app[2], app[3])

    # 2nd Row, 1st Column
    if slot == 3:
        make_button(app[0], 30, 105, 55, 95, 10, app[1], app[2], app[3])
        
    if slot == 4:
        make_button(app[0], 135, 105, 55, 95, 10, app[1], app[2], app[3])
        
    if slot == 5:
        make_button(app[0], 30, 180, 55, 95, 10, app[1], app[2], app[3])
        
    if slot == 6:
        make_button(app[0], 135, 180, 55, 95, 10, app[1], app[2], app[3])
        
    if slot == 7:
        make_button(app[0], 30, 255, 55, 95, 10, app[1], app[2], app[3])
        
    if slot == 8:
        make_button(app[0], 135, 255, 55, 95, 10, app[1], app[2], app[3])

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

while 1:
  touchdisch()
