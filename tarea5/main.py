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


data = pd.read_csv('../spotify_mx.csv')

Operaciones.proporciones(data)