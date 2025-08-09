from dash import Dash
from layouts import create_layout
from callbacks import register_callbacks

app = Dash(__name__, title='DataLens')

app.layout = create_layout()  # fonction pour créer la mise en page

register_callbacks(app)  # Enregistrement des callbacks

if __name__ == '__main__':
    app.run(debug=False)
