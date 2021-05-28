import dash
import dash_core_components as dcc
import dash_html_components as html

from django_plotly_dash import DjangoDash

app = DjangoDash('SimpleExample')   # replaces dash.Dash

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i,
                  'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
        value='medium'
    ),
    html.Div(id='output-size')

])

@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value

@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." %(dropdown_size,
                                                  dropdown_color)


# import dash
# import dash_core_components as dcc
# import dash_html_components as html
#
# from django_plotly_dash import DjangoDash
#
# # Read plotly example dataframe to plot barchart
# import plotly.express as px
# df = px.data.gapminder().query("country=='India'")
#
# external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css']
#
# # Important: Define Id for Plotly Dash integration in Django
# app = DjangoDash('AnalyticsApp')
#
# app.css.append_css({
# "external_url": external_stylesheets
# })
#
# server = app.server
# app.layout = html.Div(
#     html.Div([
#         # Adding one extar Div
#         html.Div([
#             html.H1(children='Multiple Application'),
#             html.H3(children='Indian Population over time'),
#             html.Div(children='Dash: Python framework to build web application'),
#         ], className = 'row'),
#
#         html.Div([
#             html.Div([
#                 dcc.Graph(
#                     id='bar-chart',
#                     figure={
#                         'data': [
#                             {'x': df['year'], 'y': df['pop'], 'type': 'bar', 'name': 'SF'},
#                         ],
#                         'layout': {
#                             'title': 'Bar Chart Visualization'
#                         }
#                     }
#                 ),
#             ], className = 'six columns'),
#
#             # Adding one more app/component
#             html.Div([
#                 dcc.Graph(
#                     id='line-chart',
#                     figure={
#                         'data': [
#                             {'x': df['year'], 'y': df['pop'], 'type': 'line', 'name': 'SF'},
#                         ],
#                         'layout': {
#                             'title': 'Line Chart Visualization'
#                         }
#                     }
#                 )
#             ], className = 'six columns')
#
#         ], className = 'row')
#     ])
# )
#
# if __name__ == '__main__':
#     app.run_server(8052, debug=False)