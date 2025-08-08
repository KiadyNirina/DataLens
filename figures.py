import plotly.express as px

def create_figure(df, filename, graph_type='line'):
    """Crée un graphique interactif en fonction du type choisi."""
    if graph_type == 'line':
        fig = px.line(df, x=df.columns[0], y=df.columns[1:], title=f"Données de {filename}")
    elif graph_type == 'bar':
        fig = px.bar(df, x=df.columns[0], y=df.columns[1:], barmode='group', title=f"Données de {filename}")
    elif graph_type == 'pie':
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