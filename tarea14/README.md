## Tarea 14: Análisis estadístico

¿Qué tan variable es el atributo de "danceability" (bailabilidad) entre las canciones más populares en Spotify en México a lo largo del tiempo? 

Para ejecutar el código, usa el siguiente comando en la terminal:
```bash
python main.py
```

### Salida del programa
```
Promedio "Danceability": 0.730464096749811
Desviación estándar de "Danceability": 0.1128989899284073
Valor p de la prueba de normalidad: 0.0
Rechazar H0: La distribución de "danceability" no es normal.
Conclusión: Hay alta variabilidad en la "danceability" de las canciones populares en Spotify en México a lo largo del tiempo.
```

### Análisis de resultados
<img width="1000" height="600" alt="Distribución de Danceability" src="https://github.com/user-attachments/assets/b474e6e4-2c96-4a14-9045-ecbdb63a4f3c" />


Analizando los resultados obtenidos del análisis estadístico, se observa que el valor p de la prueba de normalidad es 0.0, lo que indica que se rechaza la hipótesis nula (H0) de que la distribución de "danceability" es normal. Esto sugiere que la variabilidad en el atributo de "danceability" entre las canciones más populares en Spotify en México a lo largo del tiempo es alta. Esta alta variabilidad puede reflejar una diversidad significativa en las características musicales de las canciones que alcanzan popularidad en la plataforma, lo que podría estar influenciado por diversos factores culturales, demográficos y de tendencias musicales en México.

Esto a su vez implica que los gustos musicales en México son variados y que las canciones populares no se limitan a un solo estilo o característica musical, sino que abarcan una amplia gama de atributos que contribuyen a su popularidad. Este hallazgo es relevante para comprender mejor las preferencias musicales en el país y puede ser útil para artistas, productores y plataformas de streaming al momento de tomar decisiones relacionadas con la promoción y distribución de música.

Además observando la gráfica de distribución de "danceability", se puede notar que la distribución no sigue una forma normal, lo que refuerza la conclusión de alta variabilidad en este atributo. En resumen, el análisis estadístico indica que la "danceability" de las canciones populares en Spotify en México es altamente variable, reflejando una diversidad musical significativa en el país.
