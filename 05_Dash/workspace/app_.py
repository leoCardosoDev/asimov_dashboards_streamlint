import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2],
    "City": ["SF", "SF", "SF"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(id="div1", 
    children=[
        html.H1("Hello Dash", id="h1"),
        html.Div(children="Dash: A web application framework for Python", id="div2"),
        dcc.Graph(
            id="graph",
            figure=fig
        ),
])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)