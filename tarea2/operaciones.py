import matplotlib.pyplot as plt

class Operaciones:
    @staticmethod
    def frecuencia(data):
        ranks = data['daily_rank'].unique()
        frecuencias = {}
        for i in range(1, len(ranks) + 1, 10):
            clase = "{}-{}".format(i, i + 9)
            frecuencias[clase] = 0
            # Grupos de 10 en 10
            for j in range(i, i + 10, 1):
                frecuencias[clase] += data[data['daily_rank'] == j]['duration_ms'].mean()
            
        print("Frecuencias de clases:")
        print("| Clases   | xi    | Duración min(fi) |  xi*fi      |")
        print("|----------|-------|------------------|-------------|")
        total_fi = 0
        total_xifi = 0
        for clase, duracion_ms in frecuencias.items():
            duracion_min = duracion_ms / 1000 / 60  # Convertir a minutos
            rango = clase.split('-')
            xi = (int(rango[0]) + int(rango[1])) / 2
            xifi = xi * duracion_min
            total_fi += duracion_min
            total_xifi += xifi
            print("| {:<8} | {:<5} | {:<16.2f} | {:<11.2f} |".format(clase, xi, duracion_min, xifi))
        print("| Total    |       | {:<16.2f} | {:<11.2f} |".format(total_fi, total_xifi))

        # Histograma
        plt.title('Frecuencias de clases')
        plt.xlabel('Clases')
        plt.ylabel('Duración (min)')
        plt.bar(frecuencias.keys(), [duracion / 1000 / 60 for duracion in frecuencias.values()])
        plt.show()

    @staticmethod
    def histograma(data):
        durations_per_rank = {}
        for rank in data['daily_rank'].unique():
            durations_per_rank[rank] = data[data['daily_rank'] == rank]['duration_ms'].mean() / 1000 / 60  # Convertir a minutos

        print(durations_per_rank)

        # Crear histograma
        plt.title('Histograma de Duración (min) por # de Popularidad')
        plt.xlabel('# Popularidad')
        plt.ylabel('Duración (min)')
        plt.bar(durations_per_rank.keys(), durations_per_rank.values())
        plt.show()