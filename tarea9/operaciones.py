import scipy.stats as stats
import numpy as np
class Operaciones:

    @staticmethod
    def variables_continuas(data):
        # Seleccionamos la variable continua 'danceability'
        danceability = data['danceability']

        # Calculamos la media y desviación estándar
        mean = np.mean(danceability)
        std_dev = np.std(danceability)

        # Probabilidad de que la 'danceability' esté entre 0 y 0.3
        prob_0_03 = stats.norm.cdf(0.3, mean, std_dev) - stats.norm.cdf(0, mean, std_dev)
        print(f"Probabilidad de que la 'danceability' esté entre 0 y 0.3: {(prob_0_03 * 100):.4f}%")

        # Probabilidad de que la 'danceability' esté entre 0.3 y 0.6
        prob_03_06 = stats.norm.cdf(0.6, mean, std_dev) - stats.norm.cdf(0.3, mean, std_dev)
        print(f"Probabilidad de que la 'danceability' esté entre 0.3 y 0.6: {(prob_03_06 * 100):.4f}%")
        
        # Probabilidad de que la 'danceability' sea mayor a 0.6
        prob_greater_06 = 1 - stats.norm.cdf(0.6, mean, std_dev)
        print(f"Probabilidad de que la 'danceability' sea mayor a 0.6: {(prob_greater_06 * 100):.4f}%")
        