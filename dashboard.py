import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import dataset

from time import time

db = dataset.connect('sqlite:///server/test.db')
table = db.load_table("table2")


# Step 1. Launch the application
app = dash.Dash()

# Step 2. Import the dataset
raw = table.find(order_by='time')
xs = []
ys = []
ys2 = []

for n, entry in enumerate(raw):
    if n == 0:
        print(entry)
    xs.append(entry["time"])
    ys.append(entry["gyroX"])
    ys2.append(entry["gyroZ"])
print(ys[-1], ys2[-1])


# Step 3. Create a plotly figure
trace_1 = go.Scatter(x = xs, y = ys,
                    name = 'GYROX',
                    line = dict(width = 2,
                                color = 'rgb(255, 0, 0)'))
trace_2 = go.Scatter(x = xs, y = ys2,
                    name = 'GYROZ',
                    line = dict(width = 2,
                                color = 'rgb(0, 0, 255)'))
layout = go.Layout(title = 'Time Series Plot',
                   hovermode = 'closest')
fig = go.Figure(data = [trace_1, trace_2], layout = layout)

# Step 4. Create a Dash layout
app.layout = html.Div([
                dcc.Graph(id = 'plot_id', figure = fig)
                      ])

# Step 5. Add callback functions


# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)