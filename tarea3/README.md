## Tarea 3: Medidas centrales
Para este ejercicio, utilizaremos un conjunto de datos que contiene información sobre canciones en Spotify México. El objetivo es calcular y comparar la media de los datos con la media de clases.
Para la clasificación, utilizaremos la columna "daily_rank" como clases y la columna "duration_ms" para calcular las frecuencias.

## Frecuencia de clases
__Si los datos se encuentran agrupados en clases se toma el punto medio de la clase__
Para ejecutar el código, usa el siguiente comando en la terminal:

```bash
python main.py frecuencia
```
| Clases   | xi    | Duración min(fi) |  xi*fi      |
|----------|-------|------------------|-------------|
| 1-10     | 5.5   | 29.92            | 164.56      |
| 11-20    | 15.5  | 31.38            | 486.29      |
| 21-30    | 25.5  | 32.02            | 816.51      |
| 31-40    | 35.5  | 32.18            | 1144.39     |
| 41-50    | 45.5  | 31.53            | 1437.65     |
| __Total__|       | __157.01__       | __4049.40__ |


## Pasos a seguir:
1. Saca la frecuencia de clases
1.1 Crea un histograma y un polígono de clases.
2. Calcula la frecuencia relativa de cada clase
3. Calcula la media de tus datos 
4. Obtén la media de clases
5. Compara la meda de tus datos con la media de clases y explica el resultado.