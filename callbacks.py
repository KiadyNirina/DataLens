from dash import Output, Input, State, html, dcc, dash_table
import pandas as pd
from parsers import parse_contents
from figures import create_figure

def register_callbacks(app):
    @app.callback(
        Output('output-data-upload', 'children'),
        Input('upload-data', 'contents'),
        State('upload-data', 'filename'),
        State('graph-type-dropdown', 'value'),
        prevent_initial_call=True
    )
    def update_output(contents, filename, graph_type):
        """Met à jour l'interface après upload."""
        if contents is not None:
            df, error = parse_contents(contents)
            if error:
                return html.Div([html.H5(error, className="error")])

            figure = create_figure(df, filename, graph_type)

            data_table = dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': col, 'id': col} for col in df.columns],
                page_size=10,
                filter_action='native',
                sort_action='native',
                style_table={'overflowX': 'auto'},
                style_cell={
                    'textAlign': 'left',
                    'padding': '10px',
                    'backgroundColor': 'white',
                    'color': 'black',
                },
                style_header={
                    'backgroundColor': 'lightblue',
                    'fontWeight': 'bold',
                    'border': '1px solid black',
                },
                style_data_conditional=[
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'lightgrey'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'white'},
                ],
            )

            return html.Div([
                html.H5(filename),
                dcc.Graph(figure=figure),
                html.Div(children=data_table)
            ])