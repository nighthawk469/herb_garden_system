import serial
import sys
import time

try:
    arduino = serial.Serial('/dev/cu.usbmodemFD121', 9600, timeout=1)
except serial.SerialException as err:
    print(err)
    sys.exit()
while True:
    try:
        data = arduino.readline()[:-2]
        print(data.decode('utf-8'))

        time.sleep(3)
    except serial.SerialException as err:
        print(err)
        sys.exit()
