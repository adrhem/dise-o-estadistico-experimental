class Operaciones:

    @staticmethod
    def probabilidades(data):
        dansabilidad = data['danceability']
        energia = data['energy']
        instrumentalidad = data['instrumentalness']

        dansabilidad_mator_a_cero_cinco = 0
        dansabilidad_mayor_o_igual_instrumentalidad = 0
        dansabilidad_mayor_o_igual_energia = 0
        n = len(dansabilidad)

        for i in range(n):
            # Solo un decimal de precision
            if round(dansabilidad[i], 1) >= 0.5:
                dansabilidad_mator_a_cero_cinco += 1
            if round(dansabilidad[i], 1) > round(instrumentalidad[i], 1):
                dansabilidad_mayor_o_igual_instrumentalidad += 1

            if round(dansabilidad[i], 1) > round(energia[i], 1):
                dansabilidad_mayor_o_igual_energia += 1

        print(f'Probabilidad de que un valor de "danceability" sea mayor a un valor de 0.5: {dansabilidad_mator_a_cero_cinco / n:.8f}')
        print(f'Probabilidad de que un valor de "danceability" sea mayor a un valor de "instrumentalidad": {dansabilidad_mayor_o_igual_instrumentalidad / n:.8f}')
        print(f'Probabilidad de que un valor de "danceability" sea mayor a un valor de "energy": {dansabilidad_mayor_o_igual_energia / n:.8f}')