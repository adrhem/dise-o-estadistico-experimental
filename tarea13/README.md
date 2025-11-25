## Tarea 13: Análisis de bondad de ajuste de una distribución normal 

Para ejecutar el código, usa el siguiente comando en la terminal:
```bash
python main.py
```

### Salida del programa
```
Media: 0.730464096749811, Desviación estándar: 0.1128989899284073

Kolmogorov-Smirnov Test statistic: 0.1390686189258447, p-value: 0.0
Rechazamos la hipótesis nula. Los datos no siguen una distribución normal.
```

### Análisis de resultados
El análisis de bondad de ajuste se realizó sobre la variable "danceability" de la base de datos de Spotify México. La media y la desviación estándar calculadas son 0.7305 y 0.1129, respectivamente, lo que proporciona una idea general de la distribución de esta característica musical.

El test de Kolmogorov-Smirnov arrojó un estadístico de 0.1391 y un p-valor de 0.0, lo que nos lleva a rechazar la hipótesis nula de que los datos siguen una distribución normal. Esto indica que la variable "danceability" no se ajusta a una distribución normal, lo cual es importante considerar en futuros análisis estadísticos, ya que muchos métodos asumen normalidad en los datos. Este resultado sugiere que se deben explorar otras distribuciones o métodos no paramétricos para analizar adecuadamente esta variable.


