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

# La clasificación serán tomadas por la columna daily_rank, que va de 1 a 50
# El valor que queremos obtener es el promedio de cada clase basado en duration_ms

if len(sys.argv) < 2 or sys.argv[1] not in ['frecuencia', 'histograma']:
    print("Uso: python main.py <operacion>\n" \
    "          <operacion>: 'frecuencia', 'histograma'")
    sys.exit(1)

operacion = sys.argv[1]
data = pd.read_csv('../spotify_mx.csv')

if operacion == 'frecuencia':
    Operaciones.frecuencia(data)
elif operacion == 'histograma':
    Operaciones.histograma(data)