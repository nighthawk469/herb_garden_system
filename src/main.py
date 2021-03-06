"""Reads serial data from ardiuno, send data with timestamp to plotly graph.

The data is given with a timestamp from python for graphing purposes.


TODO:
-use threading, instead of needing 2 seperate files
-i shouldnt need to call data.decode()
-loose coupling, so i can test code even without arduino available

-get rid of eternal while, i can just restart from dataplicity to reboot
"""

import serial
import os
import time
import datetime
import sys
import logging
import random
import plotly.plotly as py
from plotly_graph import PlotlyGraph

logging.basicConfig(level=logging.DEBUG,
                    filename='/home/pi/herbGarden/src/errors.log',
                    format = '%(asctime)s %(message)s')

#fixes IOError: [Errno 32] Broken pipe
# from signal import signal, SIGPIPE, SIG_DFL
# signal(SIGPIPE,SIG_DFL)


def getSerialObject(port):
    """Attempt to create a serial object at a given port."""
    try:
        arduino = serial.Serial(port, 9600, timeout=1)
        return arduino
    except serial.SerialException as er:
        print(er)
        logging.exception("getting serial object error:")
        sys.exit()

def readData(arduino):
    """Read one line of data from serial object.

    The rate that the data comes is determined from the arduino program.
    """
    try:
        data = arduino.readline()[:-2]  # the last bit gets rid of new-line chars/empty data
        data = data.decode('utf-8') # decode from bytes
        return data
    except Exception as er:
        logging.exception("reading serial object error:")
        print(er)
        sys.exit()


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
        print("{:%Y-%m-%d %H:%M:%S}  {}".format(datetime.datetime.now(), data))
        # prints to file
        print("{:%Y-%m-%d %H:%M:%S}  {}".format(datetime.datetime.now(), data),
              file=f)
    f.close()

def sendToArduino():
    """Unused at moment
    """
    arduino.write(b'5')  # must convert unicode to byte
    b = mystring.encode('utf-8')



def main():
    """Gets serial object, and write data constantly to file, until keyboard interrupt.

    find port with 'ls /dev/tty.*'
    """
    # connect to serial object
    arduino = getSerialObject('/dev/ttyACM0') #linux
    #arduino = getSerialObject('/dev/tty.usbmodemFD121') #mac

    startTime = datetime.datetime.now()

    # create PlotlyGraph object
    plotly_graph = PlotlyGraph()
    plotly_graph.create_graph()

    # open a connection
    plotly_graph.open()

    # get and not use the first round of data, which is usually not accurate
    data = readData(arduino)

    # repeat until keyboard interrupt
    while True:
        try:
            data = readData(arduino)

            #temp
            #data = random.randint(0,10)

            # otherwise writes a bunch of nothing, or writes bad value
            if data:
                # if this takes a particularily long time
                # then the following heartbeat may fail because the connection will timeout
                plotly_graph.write_to_stream(data)
                #print("{:%Y-%m-%d %H:%M:%S}  {}".format(datetime.datetime.now(), data))

            #temp
            #time.sleep(10)
            #time.sleep(600) #10 minutes

            time.sleep(30)
            plotly_graph.heartbeat()


            # write to file
            # printSerialToFile(data, 'data/soilMoisture.csv')

            # check if its been 1 day since last watering
            # if startTime < datetime.datetime.now() - datetime.timedelta(days=1):
            #     sendToArduino()

        except Exception as er:
            logging.exception("general error:")
            print(er)
            # sys.exit()

            # in case of unpreventable issues (wifi problem, plotly server problem)
            # sleep 30s and restart graph and reopen connection
            time.sleep(30)
            plotly_graph.create_graph() #maybe don't need this
            plotly_graph.open()
        except KeyboardInterrupt:
            logging.exception("keyboard error:")
            plotly_graph.close() # Close the stream when done plotting
            sys.exit()


    # generate the HTML code to embed Plotly graphs
    tls.embed('https://plot.ly/~chris/1638')





if __name__ == "__main__":
    main()
