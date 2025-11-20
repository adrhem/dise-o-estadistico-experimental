## Tarea 7: Comparativa de medias

### Descripción del análisis
Utilicé las variables 'danceability' y 'energy' del conjunto de datos de Spotify México para comparar sus medias. Estas variables fueron seleccionadas porque representan características clave de las canciones que pueden influir en la experiencia del oyente.
Los datos utilizados abarcan todas las canciones presentes en el archivo 'spotify_mx.csv', que contiene diversas métricas de canciones populares en México.
Además usé el análisis ANOVA que es adecuado para comparar las medias de dos o más grupos y determinar si existen diferencias significativas entre ellas usando la librería SciPy.

Para ejecutar el código, usa el siguiente comando en la terminal:
```bash
python main.py
```
### Salida del programa
```
Media Grupo 1 (Danceability): 0.730464096749811
Media Grupo 2 (Energy): 0.6914467285095856
Desviación Estándar Grupo 1 (Danceability): 0.11289705046644641
Desviación Estándar Grupo 2 (Energy): 0.15119205907058927
ANOVA Results:
F-statistic: 1244.4435715542336
P-value: 9.532788016241314e-270
Nivel de significancia (alpha): 0.05
Rechazamos la hipótesis nula: las medias son diferentes.
```

### Análisis de resultados
El análisis ANOVA mostró un valor F de 1244.44 y un valor p extremadamente bajo (9.53e-270), lo que indica que hay diferencias significativas entre las medias de 'danceability' y 'energy'. Dado que el valor p es menor que el nivel de significancia del 5%, rechazamos la hipótesis nula y concluimos que las medias de las dos variables son significativamente diferentes entre sí. Esto sugiere que las características de 'danceability' y 'energy' varían considerablemente en las canciones analizadas.