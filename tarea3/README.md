## Tarea 3: Medidas centrales
Para este ejercicio, utilizaremos un conjunto de datos que contiene información sobre canciones en Spotify México. El objetivo es calcular y comparar la media de los datos con la media de clases.
Para la clasificación, utilizaremos la columna "danceability" (bailabilidad) que mide qué tan bailable es una canción en una escala de 0 a 1.

## Frecuencia de clases
Para ejecutar el código, usa el siguiente comando en la terminal:

```bash
python main.py frecuencias-tabla
```

| Clases    | Frecuencia (fi) |
|-----------|-----------------|
| 0.0 - 0.1 | 0               |
| 0.1 - 0.2 | 295             |
| 0.2 - 0.3 | 14              |
| 0.3 - 0.4 | 243             |
| 0.4 - 0.5 | 562             |
| 0.5 - 0.6 | 1707            |
| 0.6 - 0.7 | 5200            |
| 0.7 - 0.8 | 14741           |
| 0.8 - 0.9 | 4832            |
| 0.9 - 1.0 | 1512            |
| Total     | 29106           |

Para obtener el gráfico de frecuencias, usa el siguiente comando en la terminal:

```bash
python main.py frecuencias-grafico
```


## Frecuencia relativa de clases
Para ejecutar el código, usa el siguiente comando en la terminal:

```bash
python main.py frecuencia-relativa
```

| Clases    | Frecuencia (fi) | Frecuencia Relativa (%)    |
|-----------|-----------------|----------------------------|
| 0.0 - 0.1 | 0               | 0.00                       |
| 0.1 - 0.2 | 295             | 1.01                       |
| 0.2 - 0.3 | 14              | 0.05                       |
| 0.3 - 0.4 | 243             | 0.83                       |
| 0.4 - 0.5 | 562             | 1.93                       |
| 0.5 - 0.6 | 1707            | 5.86                       |
| 0.6 - 0.7 | 5200            | 17.87                      |
| 0.7 - 0.8 | 14741           | 50.65                      |
| 0.8 - 0.9 | 4832            | 16.60                      |
| 0.9 - 1.0 | 1512            | 5.19                       |
| Total     | 29106           | 100.00                     |

## Media todos los datos
Para ejecutar el código, usa el siguiente comando en la terminal:

```bash
python main.py media
```

La media de 'Danceability' es: **0.7305**

## Media de claes
Para ejecutar el código, usa el siguiente comando en la terminal:

```bash
python main.py media-clases
```

| Clases    | xi    | Frecuencia (fi) |  xi*fi      |
|-----------|-------|-----------------|-------------|
| 0.0 - 0.1 | 0.05  | 0               | 0.00        |
| 0.1 - 0.2 | 0.15  | 295             | 44.25       |
| 0.2 - 0.3 | 0.25  | 14              | 3.50        |
| 0.3 - 0.4 | 0.35  | 243             | 85.05       |
| 0.4 - 0.5 | 0.45  | 562             | 252.90      |
| 0.5 - 0.6 | 0.55  | 1707            | 938.85      |
| 0.6 - 0.7 | 0.65  | 5200            | 3380.00     |
| 0.7 - 0.8 | 0.75  | 14741           | 11055.75    |
| 0.8 - 0.9 | 0.85  | 4832            | 4107.20     |
| 0.9 - 1.0 | 0.95  | 1512            | 1436.40     |
| Total     |       | 29106           | 21303.90    |


La media de 'Danceability' por clases es: **0.7319**

## Comparación de medias
La media de todos los datos es **0.7305**, mientras que la media de clases es **0.7319**. Ambas medias son bastante similares, lo que indica que la distribución de los datos es relativamente uniforme dentro de las clases definidas. Esto sugiere que la clasificación en clases no ha introducido una desviación significativa en el cálculo de la media.