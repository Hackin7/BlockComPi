import serial
fona = serial.Serial('/dev/ttyAMA0',9600,timeout=0.1)
print('Serial Length Tester and pyserial read code example')
def test():
  command = raw_input('Command to send please:')
  fona.write(command + '\n')
  #fona.write('AT+CBC\n')
  print('Wait a while and the output is :')
  output = fona.read(10000) #Max limit
  print(output)
  print('Length of output is ' + str(len(output)))

#fona.write('AT+CBC\n')
#output = fona.read(32)
#print(output)
while True: test()
