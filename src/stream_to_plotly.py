# OLD


# TODO, this is tightly coupled, not good
# create graph, import stream variables
from plotly_graph import *


### Stream Data ###

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_id)

# We then open a connection
s.open()

# (*) Import module keep track and format current time
import datetime
import time


# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5)

while True:
    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    # first element of returned array
    ################
    y = (np.random.randn(1))[0]

    # Send data to your plot
    s.write(dict(x=x, y=y))

    # save data to file
    # open and close repeatedly to update file
    f = open("data-file.txt", 'a')

    # timestamp and data
    print("{:%Y-%m-%d %H:%M:%S}  {}".format(datetime.datetime.now(), y), file=f)
    f.close()

    time.sleep(30)  # plot a point every 30 seconds. Should be same as Arduino code

# Close the stream when done plotting
s.close()

# TODO ???
# Embed never-ending time series streaming plot
tls.embed('streaming-demos','12')
