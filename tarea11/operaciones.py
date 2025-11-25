import scipy.stats as stats
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

class Operaciones:

    @staticmethod
    def inferencia_desviaciones(data):
        # Selección de variables para el análisis
        variables = ['danceability', 'energy', 'loudness', 'valence']
        muestras = [data[var].dropna() for var in variables]

        # H0: Las desviaciones estándar de las muestras son iguales.
        # H1: Al menos una desviación estándar es diferente.

        alpha = 0.05

        desviaciones = [np.std(muestra, ddof=1) for muestra in muestras]
        print("Desviaciones estándar de las muestras:")
        for var, desv in zip(variables, desviaciones):
            print(f"{var}: {desv}")

        stat, p_value = stats.levene(*muestras)
        print(f"\nLevene's Test statistic: {stat}, p-value: {p_value}")

        if p_value < alpha:
            print("Rechazamos la hipótesis nula. Hay diferencias significativas en las desviaciones estándar.")
            
            data_melted = pd.melt(data[variables])
            tukey_result = pairwise_tukeyhsd(endog=data_melted['value'], groups=data_melted['variable'], alpha=alpha)
            print("\nResultados del comparativo por pares (Tukey's HSD):")
            print(tukey_result)
        else:
            print("No rechazamos la hipótesis nula. No hay diferencias significativas en las desviaciones estándar.")
