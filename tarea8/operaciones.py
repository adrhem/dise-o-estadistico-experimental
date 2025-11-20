import scipy.stats as stats
import numpy as np
class Operaciones:

    @staticmethod
    def distribucion_binomial(data):
        # Suponiendo que queremos calcular la probabilidad de que una canción tenga una bailabilidad mayor a 0.5
        p = np.mean(data['danceability'] > 0.5)
        n = 10  # número de ensayos
        
        for k in range(n + 1):
            if k == 0:
                continue
            # Cálculo de la probabilidad binomial usando scipy.stats
            prob = stats.binom.pmf(k, n, p)
            print(f'Probabilidad de que exactamente {k} canciones tengan bailabilidad mayor a 0.5 en {n} ensayos: {prob * 100:.2f}%')