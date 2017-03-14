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
import logging
import datetime
import sys

tls.set_credentials_file(username='nighthawk469', api_key='Jtnp5cN9CpVh342gb4SV', stream_ids=['4l2hzwbfqg'])


class PlotlyGraph:
    """
    A session of a plotly streaming graph
    """
    def __init__(self):
        self.stream_id = None
        self.stream_link = None

    def create_graph(self):
        """
        Initalize steaming graph or restart graph
        """
        stream_ids = tls.get_credentials_file()['stream_ids']

        # Get stream id from stream id list
        self.stream_id = stream_ids[0]

        # Make instance of stream id object
        stream_1 = go.Stream(
            token = self.stream_id,  # link stream id to 'token' key
            maxpoints = 288      # 1440 minutes in a day. plot every ten minutes
        )

        # Provide the stream link object the same token that's associated with the trace we wish to stream to
        self.stream_link = py.Stream(self.stream_id)

        # Initialize trace of streaming plot by embedding the unique stream_id
        trace1 = go.Scatter(
            x=[],
            y=[],
            mode='lines',
            stream=stream_1         # (!) embed stream id, 1 per trace
        )

        data = go.Data([trace1])

        # Add title to layout object
        layout = go.Layout(
            title='Herb Soil Moisture',
            xaxis=dict(
                title='Time'
            ),
            yaxis=dict(
                title='Soil Moisture',
                autorange=True
                #range=[0, 400]
            )
        )

        # Make a figure object
        fig = go.Figure(data=data, layout=layout)


        # Send fig to Plotly, initialize streaming plot by name, open new tab, extend data
        py.plot(fig, filename='arduino-garden', auto_open=False, fileopt='extend')
        # optional attributes, auto_open=False, fileopt='extend'

    def write_to_stream(self, data):
        """
        Write data to a live plotly stream link object

        If there is some sort of exception (wifi issue, plotly api issue),
        cleanly wait 30 secs and then try
        """
        # Current time on x-axis, random numbers on y-axis
        x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        # soil moisture data
        y = data

        # Send data to your plot
        self.stream_link.write(dict(x=x, y=y))
        logging.debug("plotted {}".format(data))

    def get_stream_id(self):
        return self.stream_id

    def open(self):
        """
        Open connection with plotly stream link object
        """
        self.stream_link.open()

    def close(self):
        """
        Close connection with plotly stream link object
        """
        self.stream_link.close()

    def heartbeat(self):
        """
        Keep stream alive. Streams will close after ~1 min of inactivity
        """
        self.stream_link.heartbeat()