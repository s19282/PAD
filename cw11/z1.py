import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv('winequelity.csv', delimiter=",")
print(df.head(10))

app = JupyterDash(__name__)
app.layout = html.Div([
    html.Label([
        'Select model'
    ]),
    dcc.RadioItems(['Regression', 'Classification'], id='model'),
    html.Div(id='output'),
], style={'color': 'white'}
)


@app.callback(Output(component_id='output', component_property='children'),
              Input(component_id='model', component_property='value'))
def update_output_div(input_value):
    return f'Output: {input_value}'


app.run_server(mode='inline')
