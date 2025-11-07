## Tarea 4: Medidas de dispersión
Para este ejercicio, utilizaremos un conjunto de datos que contiene información sobre canciones en Spotify México. Para la clasificación, utilizaremos la columna "danceability" (bailabilidad) que mide qué tan bailable es una canción en una escala de 0 a 1.

### Desviación estándar
Para ejecutar el código, usa el siguiente comando en la terminal:

```bash
python main.py desviacion-estandar
```

Desviación Estándar de "Danceability": **0.11289899**
(Usando pandas: **0.11289899**)

### Varianza
Para ejecutar el código, usa el siguiente comando en la terminal:

```bash
python main.py varianza
```
Varianza de "Danceability": **0.01274618**
(Usando pandas: **0.01274618**)

### Coeficiente de variación
Para ejecutar el código, usa el siguiente comando en la terminal:

```bash
python main.py coeficiente-variacion
```
Coeficiente de Variación de "Danceability": **15.45578906%**
(Usando pandas: **15.45578906%**)

### Precisión
Para ejecutar el código, usa el siguiente comando en la terminal:

```bash
python main.py precision
```
Precisión de "Danceability": **84.54421094%**
(Usando pandas: **84.54421094%**)

### Resultados
Tomando en cuenta los datos obtenidos podemos observar que la desviación estándar (0.11289899) y la varianza (0.01274618) indican que hay una dispersión moderada en los valores de "danceability". Esto significa que las canciones en el conjunto de datos tienen niveles de bailabilidad que varían, pero no de manera extrema.

El coeficiente de variación del 15.46% y la precisión del 84.54% sugieren que la variabilidad relativa es baja, lo que implica que la mayoría de las canciones tienen niveles de bailabilidad homogéneas.

Estos resultados pueden ser útiles para entender las preferencias musicales en Spotify México que estamos analizando.
