import sys
import pandas as pd
from operaciones import Operaciones

# Headers ['spotify_id', 'name', 'artists', 'daily_rank', 
#          'daily_movement', 'weekly_movement', 'country', 
#          'snapshot_date', 'popularity', 'is_explicit',
#          'duration_ms', 'album_name', 'album_release_date', 
#          'danceability', 'energy', 'key', 'loudness', 'mode', 
#          'speechiness', 'acousticness', 'instrumentalness', 
#          'liveness', 'valence', 'tempo', 'time_signature']

# La clasificación serán tomadas por la columna 'danceability'.

operaciones_disponibles = [
    'desviacion-estandar',
    'varianza',
    'coeficiente-variacion',
    'precision',
]

if len(sys.argv) < 2 or sys.argv[1] not in operaciones_disponibles:
    print("Uso: python main.py <operacion>\n" \
    "          <operacion>: %s" % ', '.join(operaciones_disponibles))
    sys.exit(1)

operacion = sys.argv[1]
data = pd.read_csv('../spotify_mx.csv')

if operacion == 'desviacion-estandar':
    Operaciones.desviacion_estandar(data)
elif operacion == 'varianza':
    Operaciones.varianza(data)
elif operacion == 'coeficiente-variacion':
    Operaciones.coeficiente_variacion(data)
elif operacion == 'precision':
    Operaciones.precision(data)