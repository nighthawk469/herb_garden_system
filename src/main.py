"""Reads and writes serial data from an attached arduino.

The data is given with a timestamp from python for graphing purposes.


TODO:
-use threading, instead of needing 2 seperate files
-use a better method than os.system
"""

# TODO, this is tightly coupled, not good
# have one data.decode() statement

# create graph, import stream variables
import create_graph

import serial
import os
import time
import datetime
import sys
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    filename='logs/errors.log',
                    format = '%(asctime)s %(message)s')

#fixes IOError: [Errno 32] Broken pipe
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

#create plotly graph
from create_graph import *


def getSerialObject(port):
    """Attempt to create a serial object at a given port."""
    try:
        arduino = serial.Serial(port, 9600, timeout=1)
        return arduino
    except serial.SerialException as er:
        print(er)
        logging.exception("Error:")
        sys.exit()

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
    b = mystring.encode('utf-8')

def writeToPlotly(data,s):
    try:
        # Current time on x-axis, random numbers on y-axis
        x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        # decode from bytes
        data = data.decode('utf-8')

        # soil moisture data
        y = data

        # Send data to your plot
        s.write(dict(x=x, y=y))
    except Exception:
        logging.exception("Error:")

def main():
    """Gets serial object, and write data constantly to file, until keyboard interrupt.
    """

    # find port with 'ls /dev/tty.*'
    arduino = getSerialObject('/dev/ttyACM0') #linux
    #arduino = getSerialObject('/dev/tty.usbmodemFD121') #mac
    startTime = datetime.datetime.now()

    #import variable

    # Provide the stream link object the same token that's associated with the trace we wish to stream to
    s = py.Stream(create_graph.graph().stream_id)

    # We then open a connection
    s.open()

    # never let the program die
    while True:
        try:
            data = getData(arduino)

            #temp
            #data = random.randint(0,10)

            if data: # otherwise writes a bunch of nothing
                # write to plotly stream
                writeToPlotly(data, s)
                logging.debug("plotted {}".format(data))

            #temp
            #time.sleep(30)

            # write to file
            # printSerialToFile(data, 'data/soilMoisture.csv')


            # check if its been 1 day since last watering
            # if startTime < datetime.datetime.now() - datetime.timedelta(days=1):
            #     sendToArduino()

        except Exception as er:
            logging.exception("error:")
            #sys.exit()
            time.sleep(60*10) #sleep 10 mins
            create_graph.graph()

    # Close the stream when done plotting
    s.close()

    # TODO ???
    # Embed never-ending time series streaming plot
    tls.embed('streaming-demos', '12')





if __name__ == "__main__":
    main()
