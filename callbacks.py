from dash import Output, Input, State, html, dcc, callback, dash_table
import pandas as pd
from parsers import parse_contents
from figures import create_figure

def register_callbacks(app):
    @app.callback(
        [Output('stored-data', 'data'),
         Output('stored-filename', 'data')],
        Input('upload-data', 'contents'),
        State('upload-data', 'filename'),
        prevent_initial_call=True
    )
    def store_data(contents, filename):
        if contents is not None:
            df, error = parse_contents(contents)
            if not error:
                return df.to_dict('records'), filename
        return None, None

    @app.callback(
        Output('output-data-upload', 'children'),
        Input('stored-data', 'data'),
        Input('graph-type-dropdown', 'value'),
        Input('stored-filename', 'data')
    )
    def update_output(data, graph_type, filename):
        if data is None:
            return html.Div("Aucune donnée chargée. Uploader un fichier CSV/JSON.")

        df = pd.DataFrame(data)
        
        title = f"Données de {filename}" if filename else "Données uploadées"

        figure = create_figure(df, title, graph_type)
        data_table = dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': col, 'id': col} for col in df.columns],
            page_size=10,
            filter_action='native',
            sort_action='native',
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left', 'padding': '10px'},
            style_header={'backgroundColor': 'lightblue', 'fontWeight': 'bold'}
        )

        return html.Div([
            html.H5(title),
            dcc.Graph(figure=figure),
            html.Div(children=data_table)
        ])

    @app.callback(
        Output('graph-type-dropdown', 'value'),
        Input('stored-data', 'data')
    )
    def init_graph_type(data):
        return 'line'