import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Altere o valor abaixo para ver o callback em ação"),
    html.Div(["Entrada: ", dcc.Input(id='my-input', value='', type='text')]),
    html.Hr(),
    html.Div(id='my-output'),
])

@app.callback(
    Output(component_id='my-output', component_property='children'), 
    [Input(component_id='my-input', component_property='value')],
)
def update_output(value):
    return f'Saída: {value}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
