class Operaciones:

    @staticmethod
    def desviacion_estandar(data):
        danceability = data['danceability']
        
        ## formula: sqrt( sum((x - media)^2) / (n - 1) )
        ## donde media = sum(x) / n
        n = len(danceability)
        media = danceability.sum() / n
        suma_cuadrados = sum((x - media) ** 2 for x in danceability)
        desviacion = (suma_cuadrados / (n - 1)) ** 0.5

        print(f'Desviación Estándar de "Danceability": {desviacion:.8f}')
        print(f'(Usando pandas: {danceability.std():.8f})')

    @staticmethod
    def varianza(data):
        danceability = data['danceability']
        
        ## formula: varianza = sum((x - media)^2) / (n - 1)
        ## donde media = sum(x) / n
        n = len(danceability)
        media = danceability.sum() / n
        suma_cuadrados = sum((x - media) ** 2 for x in danceability)
        varianza = suma_cuadrados / (n - 1) if n > 1 else 0

        print(f'Varianza de "Danceability": {varianza:.8f}')
        print(f'(Usando pandas: {danceability.var():.8f})')

    @staticmethod
    def coeficiente_variacion(data):
        danceability = data['danceability']
        
        ## formula: coeficiente_variacion = (desviacion / abs(media)) (* 100 si se quiere en porcentaje)
        n = len(danceability)
        media = danceability.sum() / n
        suma_cuadrados = sum((x - media) ** 2 for x in danceability)
        desviacion = (suma_cuadrados / (n - 1)) ** 0.5

        coeficiente_variacion = (desviacion / abs(media)) if media != 0 else float('inf')
        pandas_variacion = danceability.std() / abs(danceability.mean()) if danceability.mean() != 0 else float('inf')  

        print(f'Coeficiente de Variación de "Danceability": {(coeficiente_variacion * 100):.8f}%')
        print(f'(Usando pandas: {pandas_variacion * 100:.8f}%)')

    @staticmethod
    def precision(data):
        danceability = data['danceability']
        ## formula: Precision = 1 - CV (coeficiente de variación) (* 100 si se quiere en porcentaje)
        n = len(danceability)
        media = danceability.sum() / n
        suma_cuadrados = sum((x - media) ** 2 for x in danceability)
        desviacion = (suma_cuadrados / (n - 1)) ** 0.5

        coeficiente_variacion = (desviacion / abs(media)) if media != 0 else float('inf')
        precision = (1 - coeficiente_variacion)
        
        pandas_variacion = danceability.std() / abs(danceability.mean()) if danceability.mean() != 0 else float('inf')
        pandas_precision = (1 - pandas_variacion)

        print(f'Precisión de "Danceability": {(precision * 100):.8f}%')
        print(f'(Usando pandas: {pandas_precision * 100:.8f}%)')
