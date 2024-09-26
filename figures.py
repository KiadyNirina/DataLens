def create_figure(df, filename):
    """Crée un graphique à partir du DataFrame."""
    figure = {'data': []}

    for column in df.columns[1:]:  # Ignore la première colonne pour les axes x
        figure['data'].append({
            'x': df[df.columns[0]],  # Utilise la première colonne comme x
            'y': df[column],
            'type': 'line',  # Type de graphique (line, bar, etc.)
            'name': column
        })

    figure['layout'] = {
        'title': f'Données de {filename}',
        'xaxis': {'title': df.columns[0]},  # Titre de l'axe x
        'yaxis': {'title': 'Valeur'},  # Titre de l'axe y
    }

    return figure
