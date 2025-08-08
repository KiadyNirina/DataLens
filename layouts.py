from dash import dcc, html

def create_layout():
    return html.Div(children=[
        html.H1(children='Upload a JSON or CSV file'),
        
        dcc.Upload(
            id='upload-data',
            children=html.Button('Uploader votre fichier', className='button'),
            multiple=False
        ),

        html.Div([
            html.Label("Type de graphique :"),
            dcc.Dropdown(
                id='graph-type-dropdown',
                options=[
                    {'label': 'Lignes', 'value': 'line'},
                    {'label': 'Barres', 'value': 'bar'},
                    {'label': 'Camembert', 'value': 'pie'},
                    {'label': 'Nuage de points', 'value': 'scatter'}
                ],
                value='line',
                clearable=False
            )
        ], style={'margin': '20px 0'}),

        html.Div(id='output-data-upload'),
    ])