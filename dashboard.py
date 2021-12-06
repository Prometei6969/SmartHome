import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

app_path = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(app_path, os.path.join("data", "smarthome.csv")))

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Enegry Consumption'),
                ],
            ),
        ],
    )


def build_graph():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df['Batch'][:50],
                    'y': df['Techniques'][:50],
                    'name': 'Techniques',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Workplace'][:50],
                    'name': 'Workplace',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Garage'][:50],
                    'name': 'Garage',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Kitchen'][:50],
                    'name': 'Kitchen',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Hall'][:50],
                    'name': 'Hall',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                },
                "title": {
                    "text": "Initial sesnors",
                },
                                
            }
            
        }
    )

def build_graph_2():
    return dcc.Graph(
        figure={
            'data': [
                {
                    'x': df['Batch'][:1000],
                    'y': np.random.normal(0, 10, 1000),
                    'name': 'My office',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                },
                "title": {
                    "text": "Additional sesnor",
                                },
            }
        }
    )


app.layout = html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph(),
                build_graph_2(),
            ]
        )
    ]
)
