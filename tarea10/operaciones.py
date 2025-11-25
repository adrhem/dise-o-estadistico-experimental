import scipy.stats as stats
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

class Operaciones:

    @staticmethod
    def anova(data):
        # Seleccionamos cuatro variables continuas para el análisis ANOVA
        var1 = data['danceability']
        var2 = data['energy']
        var3 = data['loudness']
        var4 = data['valence']

        # H0: Las medias de las cuatro variables son iguales
        # H1: Al menos una media es diferente

        alpha = 0.05
        f_stat, p_value = stats.f_oneway(var1, var2, var3, var4)

        if p_value < alpha:
            decision = "Rechazamos la hipótesis nula"
        else:
            decision = "No rechazamos la hipótesis nula"

        # Resultados
        print("Estadístico F:", f_stat)
        print("Valor p:", p_value)
        print("Decisión:", decision)

        # Si se rechaza H0, realizar pruebas post-hoc (Tukey's HSD)
        if p_value < alpha:

            df_tukey = pd.DataFrame({
                'value': np.concatenate([var1, var2, var3, var4]),
                'group': ['danceability'] * len(var1) + ['energy'] * len(var2) + ['loudness'] * len(var3) + ['valence'] * len(var4)
            })

            tukey_result = pairwise_tukeyhsd(endog=df_tukey['value'], groups=df_tukey['group'], alpha=alpha)
            print(tukey_result)
        