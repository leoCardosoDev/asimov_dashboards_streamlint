import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
app.layout = html.Div([])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
