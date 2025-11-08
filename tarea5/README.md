## Tarea 5: Máximos, mínimos y normales teóricos

### Proporciones mínimas y máximas
Para ejecutar el código, usa el siguiente comando en la terminal:

```bash
python main.py
```
Proporción Mínima de "Danceability": **0.39176713**
Proporción Máxima de "Danceability": **1.06916107**

### Resultados

Para la proporción máxima de "Danceability", se observaron las siguientes características en las canciones:
- Límite Inferior: 0.39176713
- Límite Superior: 0.60823287

En la base de datos de Spotify el rango de "Danceability" está entre 0 y 1, por lo que la proporción máxima calculada excede el rango permitido. Esto indica que no hay canciones con una "Danceability" tan alta en la base de datos.

Sin embargo, la proporción mínima es válida y refleja canciones con baja "Danceability". Las canciones que caen dentro de este rango pueden ser consideradas menos bailables en comparación con otras en la base de datos. Además esto es relevante para identificar canciones con baja capacidad de baile, mientras que la proporción máxima calculada no es aplicable debido a las limitaciones del rango de valores en la base de datos.

<img width="640" height="480" alt="Gráfico" src="https://github.com/user-attachments/assets/2c1c5987-be12-4f86-b294-1e6fed2441bf" />

Finalmente la gráfica de frecuencia está orientada a la derecha, indicando que la mayoría de las canciones tienen una "Danceability" alta, con pocas canciones en el extremo inferior del rango. Esto puede explicar por qué la proporción máxima excede el rango permitido, ya que hay pocas canciones con valores bajos de "Danceability".