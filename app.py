import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)
server = app.server

df = pd.read_csv('https://raw.githubusercontent.com/srinathkr07/IPL-Data-Analysis/master/matches.csv')

fig = px.bar(df,x='venue',color='winner',title='Luckiest Venue for Each Team',animation_frame='winner',barmode='relative')

app.layout = html.Div([
    dcc.Graph(
        id='IPL',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
