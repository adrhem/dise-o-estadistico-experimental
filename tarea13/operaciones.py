from scipy import stats
import numpy as np

class Operaciones:

    @staticmethod
    def analisis_bondad(data):
        # Para confirmar que los datos de "danceability" siguen una distribución normal,
        # se puede utilizar la prueba de bondad de ajuste de Kolmogorov-Smirnov.
        
        # H0: Los datos siguen una distribución normal.
        # H1: Los datos no siguen una distribución normal.

        alpha = 0.05
        datos = data['danceability'].dropna()
        mu, std = np.mean(datos), np.std(datos, ddof=1)
        print(f"Media: {mu}, Desviación estándar: {std}")
        stat, p_value = stats.kstest(datos, 'norm', args=(mu, std))
        print(f"\nKolmogorov-Smirnov Test statistic: {stat}, p-value: {p_value}")

        if p_value < alpha:
            print("Rechazamos la hipótesis nula. Los datos no siguen una distribución normal.")
        else:
            print("No rechazamos la hipótesis nula. Los datos siguen una distribución normal.")
