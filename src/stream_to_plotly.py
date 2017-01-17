# create graph, import stream variables
from create_graph import *


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
    y = (np.random.randn(1))[0]

    # Send data to your plot
    s.write(dict(x=x, y=y))

    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot


    f = open("data-file", 'a')  # open and close repeatedly to update file

    # if data exists
    if data:
        print("{:%Y-%m-%d %H:%M:%S}  {}".format(datetime.datetime.now(), y),
              file=f)
    f.close()



    time.sleep(1)  # plot a point every second
# Close the stream when done plotting
s.close()

# Embed never-ending time series streaming plot
tls.embed('streaming-demos','12')
