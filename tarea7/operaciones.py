import scipy.stats as stats
import numpy as np
class Operaciones:

    @staticmethod
    def comparativa_medias(data):

        # Seleccionar tres grupos basados en 'danceability' and 'energy' 
        grupo1 = data['danceability'].tolist()  # Grupo 1: Danceability
        grupo2 = data['energy'].tolist()        # Grupo 2: Energy

        # Medias de los grupos
        media1 = np.mean(grupo1)
        media2 = np.mean(grupo2)

        print(f"Media Grupo 1 (Danceability): {media1}")
        print(f"Media Grupo 2 (Energy): {media2}")

        # Desviaciones estándar de los grupos
        std1 = np.std(grupo1)
        std2 = np.std(grupo2)

        print(f"Desviación Estándar Grupo 1 (Danceability): {std1}")
        print(f"Desviación Estándar Grupo 2 (Energy): {std2}")

        # Realizar ANOVA
        f_stat, p_value = stats.f_oneway(grupo1, grupo2)

        print("ANOVA Results:")
        print(f"F-statistic: {f_stat}")
        print(f"P-value: {p_value}")

        alpha = 0.05 # Nivel de significancia del 95%
        print(f"Nivel de significancia (alpha): {alpha}")
        if p_value < alpha:
            print("Rechazamos la hipótesis nula: las medias son diferentes.")
        else:
            print("No rechazamos la hipótesis nula: las medias son iguales.")
            