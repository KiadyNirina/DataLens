from dash import dcc, html

def create_layout():
    return html.Div(
        [
            # Intégration de Tailwind CSS dans le head
            html.Link(
                rel='stylesheet',
                href='https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css'
            ),
            
            # Contenu principal
            html.Div(
                className="min-h-screen bg-gray-50 p-6",
                children=[
                    # Header
                    html.Div(
                        className="max-w-7xl mx-auto text-center mb-8",
                        children=[
                            html.H1(
                                'Analyse de Données',
                                className="text-3xl font-bold text-indigo-600 mb-2"
                            ),
                            html.P(
                                'Visualisez vos données CSV/JSON en temps réel',
                                className="text-gray-500"
                            )
                        ]
                    ),
                    
                    # Zone principale
                    html.Div(
                        className="max-w-7xl mx-auto bg-white rounded-xl shadow-md p-6",
                        children=[
                            # Zone d'upload
                            dcc.Upload(
                                id='upload-data',
                                className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center cursor-pointer hover:bg-indigo-50 transition-colors mb-6",
                                children=[
                                    html.Div([
                                        html.Span(
                                            "Cliquez ou glissez-déposez un fichier ",
                                            className="text-gray-600"
                                        ),
                                        html.Span(
                                            "(CSV ou JSON)",
                                            className="text-indigo-500 font-medium"
                                        ),
                                    ]),
                                    html.P(
                                        "Taille maximale : 10MB",
                                        className="text-sm text-gray-400 mt-2"
                                    )
                                ],
                                multiple=False
                            ),
                            
                            # Sélecteur de graphique
                            html.Div(
                                className="mb-6",
                                children=[
                                    html.Label(
                                        "Type de visualisation :",
                                        className="block text-sm font-medium text-gray-700 mb-2"
                                    ),
                                    dcc.Dropdown(
                                        id='graph-type-dropdown',
                                        options=[
                                            {'label': 'Lignes', 'value': 'line'},
                                            {'label': 'Barres', 'value': 'bar'},
                                            {'label': 'Camembert', 'value': 'pie'},
                                            {'label': 'Nuage de points', 'value': 'scatter'}
                                        ],
                                        value='line',
                                        clearable=False,
                                        className="border-gray-300 rounded-md shadow-sm"
                                    )
                                ]
                            ),
                            
                            # Stockage des données
                            dcc.Store(id='stored-data', storage_type='local'),
                            dcc.Store(id='stored-filename', storage_type='local'),
                            
                            # Zone de résultats
                            html.Div(
                                id='output-data-upload',
                                className="mt-6"
                            )
                        ]
                    ),
                    
                    # Footer
                    html.Footer(
                        className="mt-8 text-center text-gray-400 text-sm",
                        children="© 2025 DataLens - Tous droits réservés"
                    )
                ]
            )
        ]
    )