import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(id="div1", children=[
    html.H1(children='Hello Dash'),
    html.Div(children='Dash: A web application framework for Python.'),
    dcc.Graph(
        id='example-graph',
        figure=px.scatter(
            pd.DataFrame({
                "x": [1, 2, 3, 4],
                "y": [10, 11, 12, 13]
            }),
            x="x",
            y="y",
        )
    )
])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)