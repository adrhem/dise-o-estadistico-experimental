## Tarea 10: ANOVA

Para ejecutar el código, usa el siguiente comando en la terminal:
```bash
python main.py
```
### Salida del programa
```
Estadístico F: 73424.2990708466
Valor p: 0.0
Decisión: Rechazamos la hipótesis nula
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

Para los grupos "danceability", "energy", "loudness" y "valence", se observa que hay diferencias significativas en las medias de "loudness" y "valence" en comparación con las otras variables. Esto sugiere que estas características tienen un impacto diferente en la música analizada, lo cual es relevante para entender cómo varían estas propiedades en las canciones populares en Spotify México.

Los niveles utilizados son cuatro, correspondientes a las cuatro variables seleccionadas. No se aplicó replicación ya que cada variable representa una característica distinta de las canciones.

Como conclusión, las diferencias significativas encontradas en "loudness" y "valence" indican que estas características pueden influir de manera diferente en la percepción y popularidad de la música, lo cual es valioso para estudios futuros en análisis musical y preferencias de los oyentes.

Y como apoyo a mi pregunta de investigación, cómo la bailabilidad de una canción afecta su popularidad, los resultados sugieren que aunque "danceability" no mostró diferencias significativas en comparación con "energy", las características de "loudness" y "valence" sí lo hicieron, lo que podría indicar que otros factores además de la bailabilidad influyen en la popularidad de las canciones.