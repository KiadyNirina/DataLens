from dash import dcc, html

def create_layout():
    return html.Div(children=[
        html.H1(children='Upload a JSON or CSV file'),
        
        dcc.Upload(
            id='upload-data',
            children=html.Button('Uploader your file', className='button'),
            multiple=False  # Limiter à un seul fichier
        ),

        html.Div(id='output-data-upload'),
    ])
