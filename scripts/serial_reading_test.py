import serial
import sys
import time

try:
    port = '/dev/ttyACM0' #linux
    #port = '/dev/tty.usbmodemFD121' #mac
    arduino = serial.Serial(port, 9600, timeout=1)
except serial.SerialException as err:
    print(err)
    sys.exit()
while True:
    try:
        data = arduino.readline()[:-2]
        if data:
            print(data.decode('utf-8'))

        #time.sleep(3)
    except serial.SerialException as err:
        print(err)
        sys.exit()
