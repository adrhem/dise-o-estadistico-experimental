from statsmodels.sandbox.stats.runs import runstest_1samp

class Operaciones:

    @staticmethod
    def analisis_aleatoriedad(data):
        # Prueba de aleatoriedad de runs para la variable 'danceability'
        variable = data['danceability'].dropna()
        statistic, p_value = runstest_1samp(variable)
        print(f"Runstest statistic: {statistic}, p-value: {p_value}")   