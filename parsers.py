import pandas as pd
import base64
import chardet
import io

# Constantes pour les types de fichiers
CSV_MIME_TYPE = 'data:text/csv;base64'
JSON_MIME_TYPE = 'data:application/json;base64'

def detect_encoding(decoded_data):
    """Détecte l'encodage d'un fichier décodé."""
    result = chardet.detect(decoded_data)
    return result['encoding']

def parse_csv(contents):
    """Parse un fichier CSV à partir des données décodées."""
    encoding = detect_encoding(contents)
    return pd.read_csv(io.StringIO(contents.decode(encoding)))

def parse_json(contents):
    """Parse un fichier JSON à partir des données décodées."""
    return pd.read_json(io.BytesIO(contents))

def parse_contents(contents):
    """Parse les contenus du fichier en fonction de leur type."""
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    if content_type == CSV_MIME_TYPE:
        return parse_csv(decoded), None
    elif content_type == JSON_MIME_TYPE:
        return parse_json(decoded), None
    else:
        return None, "Unsupported file type"
