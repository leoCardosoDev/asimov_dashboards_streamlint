import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label("Dropdown"),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Option 1', 'value': 'option1'},
            {'label': 'Option 2', 'value': 'option2'},
            {'label': 'Option 3', 'value': 'option3'}
        ],
        value='option1'
    ),
    html.Label("Checklist"),
    dcc.Checklist(
        id='checklist',
        options=[
            {'label': 'Option 1', 'value': 'option1'},
            {'label': 'Option 2', 'value': 'option2'},
            {'label': 'Option 3', 'value': 'option3'}
        ],
        value=['option1'], style={'margin-bottom': '20px'}
    )
])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
