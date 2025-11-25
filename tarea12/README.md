## Tarea 12: Análisis de aleatoriedad de la muestra

Realiza un análisis de aleatoriedad de una de las variables de tu base de datos.
Explica la decisión de tu selección, tanto del tipo de prueba como de los datos, 
y cómo tu resultado afecta tu objetivo de investigación.

Para ejecutar el código, usa el siguiente comando en la terminal:
```bash
python main.py
```

### Salida del programa
```
Runstest statistic: 1.9639968705262099, p-value: 0.04953045482963787
```

### Análisis de resultados
El análisis de aleatoriedad se realizó utilizando la prueba de corridas (runs test) sobre la variable "danceability" de la base de datos de Spotify México. La elección de esta variable se debe a su relevancia en la investigación sobre cómo la bailabilidad de una canción afecta su popularidad. La prueba de corridas es adecuada para evaluar la aleatoriedad en una secuencia de datos, lo que es crucial para asegurar que las observaciones no estén influenciadas por patrones sistemáticos.

El resultado de la prueba arrojó un estadístico de 1.963 y un p-valor de aproximadamente 0.0495. Dado que el p-valor es menor que el umbral comúnmente utilizado de 0.05, se rechaza la hipótesis nula de aleatoriedad. Esto indica que la secuencia de valores de "danceability" no es completamente aleatoria, sugiriendo la presencia de algún patrón o tendencia en los datos.

Esta falta de aleatoriedad coincide ya que la base de datos fue tomada directamente de las listas de popularidad de Spotify México, lo que implica que las canciones más populares podrían tener características similares en términos de bailabilidad. Este hallazgo es relevante para la investigación, ya que sugiere que la popularidad de las canciones podría estar influenciada por factores relacionados con su bailabilidad, lo que justifica un análisis más profundo de esta variable en relación con la popularidad.