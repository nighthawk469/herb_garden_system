"""Reads and writes serial data from an attached arduino.

The data is given with a timestamp from python for graphing purposes.


TODO:
-use threading, instead of needing 2 seperate files
-use a better method than os.system
"""

import serial
import os
import time
import datetime
import sys
import pdb


def getSerialObject(port):
    """Attempt to create a serial object at a given port."""
    try:
        arduino = serial.Serial(port, 9600, timeout=1)
        return arduino
    except(serial.SerialException):
        print("Arduino device cannot be found at port {}\n".format(port))
        time.sleep(10)


def getData(arduino):
    """Read one line of data from serial object.

    The rate by which data comes is determined from the arduino program.
    """
    data = arduino.readline()[:-2]  # the last bit gets rid of new-line chars/empty data
    return data


# not good i think
def checkIfWateredRecently(data):
    """Check to see if arduino has watered recently to avoid over watering
    """
    if data == "watered\n" or data == "watered":
        # reset timer
        global start
        start = datetime.datetime.now()


def printSerialToFile(data, file):
    """Append serial data to a file and then close the file.
    """
    f = open(file, 'a')  #open and close repeatedly to update file

    # if data exists
    if data:
        # prints data to console
        print("{:%Y-%m-%d %H:%M:%S}  {}".format(datetime.datetime.now(), data.decode('utf-8')))
        # prints to file, from bytes to unicode
        print("{:%Y-%m-%d %H:%M:%S}  {}".format(datetime.datetime.now(), data.decode('utf-8')),
              file=f)
    f.close()


def sendToArduino():
    """Unused at moment
    """
    arduino.write(b'5')  # must convert unicode to byte
    b = mystring.encode('''
uploads a file to sheridan server every 10 seconds
''''utf-8')


def main():
    """Gets serial object, and write data constantly to file, until keyboard interrupt.
    """
    # find port with 'ls /dev/tty.*'
    arduino = getSerialObject('/dev/tty.usbmodemFD121')
    startTime = datetime.datetime.now()

    try:
        while True:
            data = getData(arduino)
            printSerialToFile(data, 'data/soilMoisture.csv')

            # check if its been 1 day since last watering
            # if startTime < datetime.datetime.now() - datetime.timedelta(days=1):
            #     sendToArduino()

    except(KeyboardInterrupt):
        sys.exit()


if __name__ == "__main__":
    main()
