"""
Use py.plot() to return the unique url and optionally open the url

Traces (objects that describe a single series of data in a graph

The Stream Id Object is a dictionary-like object that takes two parameters,
and has all the methods that are associated with dictionaries. We will need one of
these objects for each of trace that we wish to stream data to

The Stream Link Object is what will be used to communicate with the Plotly server in order
to update the data contained in your trace objects. This object is in the plotly.plotly
object, and can be referenced with py.Stream

"""


import numpy as np
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

tls.set_credentials_file(username='nighthawk469', api_key='Jtnp5cN9CpVh342gb4SV', stream_ids=['4l2hzwbfqg'])

### Create Graph ###

stream_ids = tls.get_credentials_file()['stream_ids']

# Get stream id from stream id list
stream_id = stream_ids[0]

# Make instance of stream id object
stream_1 = go.Stream(
    token=stream_id,  # link stream id to 'token' key
    maxpoints=1440*2      # 1440 minutes in a day
)

# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines',
    stream=stream_1         # (!) embed stream id, 1 per trace
)

data = go.Data([trace1])

# Add title to layout object
layout = go.Layout(title='Herb Soil Moisture')

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot by name, open new tab, extend data
py.plot(fig, filename='arduino-garden', auto_open=False)
#optional attribute, auto_open=False
