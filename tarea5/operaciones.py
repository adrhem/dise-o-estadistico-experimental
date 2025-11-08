class Operaciones:

    @staticmethod
    def proporciones(data):
        # observaciones
        danceability = data['danceability']
        # LCS = Media + 3*Desviación Estándar
        # LCI = Media - 3*Desviación Estándar

        lcs = danceability.mean() + 3 * danceability.std()
        lci = danceability.mean() - 3 * danceability.std()

        print(f'Proporción Mínima de "Danceability": {lci:.8f}')
        print(f'Proporción Máxima de "Danceability": {lcs:.8f}')