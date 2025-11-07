import matplotlib.pyplot as plt

class Operaciones:

    @staticmethod
    def inicializar_frecuencias(data):
        frecuencias = {.1: 0, .2: 0, .3: 0, .4: 0, .5: 0, .6: 0, .7: 0, .8: 0, .9: 0, 1.0: 0}
        for danceability in data['danceability']:
            if danceability <= 0.1:
                frecuencias[.1] += 1
            elif danceability <= 0.2:
                frecuencias[.2] += 1
            elif danceability <= 0.3:
                frecuencias[.3] += 1
            elif danceability <= 0.4:
                frecuencias[.4] += 1
            elif danceability <= 0.5:
                frecuencias[.5] += 1
            elif danceability <= 0.6:
                frecuencias[.6] += 1
            elif danceability <= 0.7:
                frecuencias[.7] += 1
            elif danceability <= 0.8:
                frecuencias[.8] += 1
            elif danceability <= 0.9:
                frecuencias[.9] += 1
            else:
                frecuencias[1.0] += 1

        return frecuencias

    @staticmethod
    def tabla_frecuencias(data):
        frecuencias = Operaciones.inicializar_frecuencias(data)

        print("Frecuencias de clases:")
        print("| Clases    | Frecuencia (fi) |")
        print("|-----------|-----------------|")
        total_fi = 0
        for clase, frecuencia in frecuencias.items():
            clase_str = "{:.1f} - {:.1f}".format(clase - .1, clase)
            total_fi += frecuencia
            print("| {:<9} | {:<15.0f} |".format(clase_str, frecuencia))
        print("| Total     | {:<15.0f} |".format(total_fi))

    @staticmethod
    def grafico_frecuencias(data):
        frecuencias = Operaciones.inicializar_frecuencias(data)

        clases = []
        fi_values = []
        frecuencias_values = []
        n = len(data)
        for clase, danceability in frecuencias.items():
            clase_str = "{:.1f} - {:.1f}".format(clase - .1, clase)
            clases.append(clase_str)
            frecuencias_values.append(danceability / n * 100)
            fi_values.append(danceability)

        plt.bar(clases, fi_values, width=0.4, color='blue', alpha=0.7, label='Histograma')
        plt.xlabel('Clases de "Danceability"')
        plt.title('Histograma y Polígono de Frecuencias de "Danceability"')
        plt.xticks(rotation=45)

        ax2 = plt.twinx()
        ax2.set_ylim(0, max(frecuencias_values) * 1.1)
        ax2.plot(clases, frecuencias_values, marker='o', linestyle='-', color='red', label='Polígono')
        ax2.set_ylabel('Frecuencia Relativa (%)')
       
        plt.tight_layout()
        plt.show()

    @staticmethod
    def frecuencia_relativa(data):
        frecuencias = Operaciones.inicializar_frecuencias(data)
        total = sum(frecuencias.values())

        print("Frecuencias relativas de clases:")
        print("| Clases    | Frecuencia (fi) | Frecuencia Relativa (%)    |")
        print("|-----------|-----------------|----------------------------|")
        for clase, frecuencia in frecuencias.items():
            clase_str = "{:.1f} - {:.1f}".format(clase - .1, clase)
            frecuencia_relativa = frecuencia / total * 100
            print("| {:<9} | {:<15.0f} | {:<26.2f} |".format(clase_str, frecuencia, frecuencia_relativa))
        print("| Total     | {:<15.0f} | {:<26.2f} |".format(total, 100.0))

    @staticmethod
    def media(data):
        frecuencias = data['danceability']
        media = frecuencias.mean()
        print("La media de 'Danceability' es: {:.4f}".format(media))

    def media_clases(data):
        frecuencias = Operaciones.inicializar_frecuencias(data)

        print("Frecuencias de clases:")
        print("| Clases    | xi    | Frecuencia (fi) |  xi*fi      |")
        print("|-----------|-------|-----------------|-------------|")
        total_fi = 0
        total_xifi = 0
        for clase, danceability in frecuencias.items():
            clase_str = "{:.1f} - {:.1f}".format(clase - .1, clase)
            xi = clase - 0.05  # Punto medio de la clase
            xifi = xi * danceability
            total_fi += danceability
            total_xifi += xifi
            print("| {:<9} | {:<5.2f} | {:<15.0f} | {:<11.2f} |".format(clase_str, xi, danceability, xifi))
        print("| Total     |       | {:<15.0f} | {:<11.2f} |".format(total_fi, total_xifi))

        print("La media de 'Danceability' por clases es: {:.4f}".format(total_xifi / total_fi))