import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class Operaciones:

    @staticmethod
    def analisis_estadistico(data):
        """
        ¿Qué tan variable es el atributo de "danceability" (bailabilidad) 
        entre las canciones más populares en Spotify en México a lo largo del tiempo? 
        """

        # H0: La variabilidad de "danceability" es baja entre las canciones más populares.
        # H1: La variabilidad de "danceability" es alta entre las canciones más populares.

        alpha = 0.05

        danceability_data = data['danceability']

        mean_danceability = danceability_data.mean()
        std_danceability = danceability_data.std()
        print(f'Promedio "Danceability": {mean_danceability}')
        print(f'Desviación estándar de "Danceability": {std_danceability}')

        # Paso 5: Visualización de datos
        plt.figure(figsize=(10, 6))
        sns.histplot(danceability_data, bins=30, kde=True)
        plt.title('Distribución de "Danceability"')
        plt.xlabel('"Danceability"')
        plt.ylabel('Frecuencia')
        plt.show()

        k2, p_value = stats.normaltest(danceability_data)
        print(f'Valor p de la prueba de normalidad: {p_value}')

        if p_value < alpha:
            print("Rechazar H0: La distribución de \"danceability\" no es normal.")
            variability = 'high'
        else:
            print("No rechazar H0: La distribución de \"danceability\" es normal.")
            variability = 'low'

        if variability == 'high':
            print("Conclusión: Hay alta variabilidad en la \"danceability\" de las canciones populares en Spotify en México a lo largo del tiempo.")
        else:
            print("Conclusión: Hay baja variabilidad en la \"danceability\" de las canciones populares en Spotify en México a lo largo del tiempo.")