## Tarea 11: Inferencia de desviaciones

Para ejecutar el código, usa el siguiente comando en la terminal:
```bash
python main.py
```

### Salida del programa
```
Levene's Test statistic: 6464.288887222433, p-value: 0.0
Rechazamos la hipótesis nula. Hay diferencias significativas en las desviaciones estándar.

Resultados del comparativo por pares (Tukey's HSD):
    Multiple Comparison of Means - Tukey HSD, FWER=0.05     
============================================================
   group1     group2  meandiff p-adj   lower   upper  reject
------------------------------------------------------------
danceability   energy   -0.039 0.1822 -0.0888  0.0107  False
danceability loudness  -7.4505    0.0 -7.5002 -7.4008   True
danceability  valence  -0.0567 0.0179 -0.1064  -0.007   True
      energy loudness  -7.4115    0.0 -7.4612 -7.3618   True
      energy  valence  -0.0177  0.798 -0.0674  0.0321  False
    loudness  valence   7.3938    0.0  7.3441  7.4436   True
------------------------------------------------------------
```

### Análisis de resultados
La selección de las variables "danceability", "energy", "loudness" y "valence" se basa en su relevancia para entender las características musicales en la base de datos de Spotify México. Estas variables representan aspectos clave de las canciones que pueden influir en la percepción del oyente.

El resultado del test de Levene indica que hay diferencias significativas en las desviaciones estándar entre las variables analizadas (p-valor = 0.0). Esto sugiere que al menos una de las variables tiene una variabilidad diferente en comparación con las otras.

El análisis post-hoc mediante el test de Tukey revela que las desviaciones estándar de "loudness" son significativamente diferentes de las de "danceability", "energy" y "valence". Esto implica que la variabilidad en la percepción del volumen de las canciones es distinta en comparación con las otras características musicales.

Y como apoyo a mi pregunta de investigación, cómo la bailabilidad de una canción afecta su popularidad, los resultados sugieren que aunque "danceability" no mostró diferencias significativas en comparación con "energy", las características de "loudness" y "valence" sí lo hicieron, lo que podría indicar que otros factores además de la bailabilidad influyen en la popularidad de las canciones.