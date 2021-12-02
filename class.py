# import
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import plotly.express as ex
import pandas as pd



# initialisation
app = dash.Dash('')


# layout
""" 
# adding styles from assets folder
app.layout = html.Div([
    html.H5('What is Lorem Ipsum?', className='centred_using_padding_and_width purple_text'),
    html.P('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', className='centred_using_padding_and_width blue_text')

])
"""

"""
app.layout = html.Div([
    html.Header([
            html.H1('Header with tabs', className='title')
        ], className='toolbar toolbar-header'),
    html.Div([
        html.Div([
            html.Span('Tab', className="icon icon-cancel icon-close-tab")
        ], className='tab-item'),
         html.Div([
            html.Span('Tab active', className="icon icon-cancel icon-close-tab")
        ], className='tab-item active'),
         html.Div([
            html.Span('Tab', className="icon icon-cancel icon-close-tab")
        ], className='tab-item'),
         html.Div([
            html.Span('Tab', className="icon icon-plus")
        ], className='tab-item tab-item-fixed'),
    ], className='tab-group')

])
"""


"""
app.layout = html.Form([
    html.Div([
        html.Label('Email Address'),
        dcc.Input(type='email' , className='form-control', placeholder='Email'),
    ], className='form-group minimised')
])

"""

# placing icons from the proton library
app.layout = html.Div([
    html.Span('', className="icon icon-note"),
    html.Br(),
    html.Span('', className="icon icon-note-beamed"),
    html.Br(),
    html.Span('', className="icon icon-music"),
    html.Br(),
    html.Span('', className="icon icon-search"),
    html.Br(),
    html.Span('', className="icon icon-flashlight"),
    html.Br()
])





# running
app.run_server(debug=True)
