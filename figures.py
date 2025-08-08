import plotly.express as px

def create_figure(df, filename, graph_type='line'):
    try:
        if graph_type == 'line':
            fig = px.line(df, x=df.columns[0], y=df.columns[1:], title=f"Données de {filename}")
        elif graph_type == 'bar':
            fig = px.bar(df, x=df.columns[0], y=df.columns[1:], barmode='group', title=f"Données de {filename}")
        elif graph_type == 'pie':
            if len(df.columns) != 2:
                raise ValueError("Le camembert nécessite 1 colonne de valeurs et 1 colonne de labels.")
            fig = px.pie(df, names=df.columns[0], values=df.columns[1], title=f"Données de {filename}")
        elif graph_type == 'scatter':
            fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title=f"Données de {filename}")
        else:
            fig = px.line(df, x=df.columns[0], y=df.columns[1:])

        fig.update_layout(
            xaxis_title=df.columns[0],
            yaxis_title="Valeur",
            hovermode='closest'
        )
        return fig

    except Exception as e:
        return px.scatter(title=f"Erreur : {str(e)}")