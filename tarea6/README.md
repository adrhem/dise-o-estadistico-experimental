## Tarea 6: Calculo de probabilidades en la muestra

Para este caso se seleccionaron las columnas "danceability" y "instrumentalness" y se calculó la probabilidad de que un valor de "danceability" sea mayor o igual a un valor de 0.5 y la probabilidad de que un valor de "danceability" sea mayor a un valor de "instrumentalidad". 

Para ejecutar el código, usa el siguiente comando en la terminal:
```bash
python main.py
```
Probabilidad de que un valor de "danceability" sea mayor a un valor de 0.5: **0.97948877**
Probabilidad de que un valor de "danceability" sea mayor a un valor de "instrumentalidad": **0.98206555**
Probabilidad de que un valor de "danceability" sea mayor a un valor de "energy": **0.48216863**


#### 1. Dos diferentes eventos simples con la misma probabilidad de ocurrencia

Este resultado es lógico, ya que la instrumentalidad es una característica que indica que la canción no tiene instrumentación, por lo que es menos bailable. Y la dansabilidad es una característica que indica qué tan bailable es una canción, por lo que es mayor o igual a 0.5.


#### 2. Basado en la probabilidad de ocurrencia los eventos simples del punto 1, la unión de los  dos eventos. Explica si son dependientes, excluyentes o complementarios

Los eventos son complementarios, ya que la probabilidad de que un valor de "danceability" sea mayor o igual a un valor de 0.5 no tiene que verse afectada por la probabilidad de que un valor de "danceability" sea mayor a un valor de "instrumentalidad". Sin embargo, la probabilidad de que un valor de "danceability" sea mayor a un valor de "instrumentalidad" si tiene que verse afectada por la probabilidad de que un valor de "danceability" sea mayor o igual a un valor de 0.5.

#### 3. Dos o más eventos independientes unidos

Los eventos son independientes, ya que la probabilidad de que un valor de bailabilidad sea mayor a la instrumentalidad de una canción no tiene que verse afectada por la probabilidad de que un valor de bailabilidad sea mayor a un valor de 0.5.

#### 4. Dos o más eventos intersectados e independientes

Los eventos son independientes, ya que la probabilidad de que un valor de "danceability" sea mayor o igual a un valor de 0.5 no tiene que verse afectada por la probabilidad de que un valor de "danceability" sea mayor a un valor de "energy".

Los eventos son intersectados, ya que la probabilidad de que un valor de "danceability" sea mayor o igual a un valor de 0.5 y la probabilidad de que un valor de "danceability" sea mayor a un valor de "energy" son diferentes.

#### 5. Dos o más eventos con ocurrencia de todos.

Los eventos son con ocurrencia de todos, ya que la probabilidad de que un valor de "danceability" sea mayor o igual a un valor de 0.5, la probabilidad de que un valor de "danceability" sea mayor a un valor de "energy" y la probabilidad de que un valor de "danceability" sea mayor a un valor de "instrumentalidad" son diferentes.

#### 6. La repetición de un evento en un mismo espacio muestral
Para este caso se seleccionaron las columnas "danceability" y se calculó la probabilidad de que un valor de "danceability" sea mayor o igual a un valor de 0.5 y la probabilidad de que un valor de "danceability" sea mayor a un valor de 0.5.

Esto implica que la probabilidad de que un valor de "danceability" sea mayor o igual a un valor de 0.5 es la misma que la probabilidad de que un valor de "danceability" sea mayor a un valor de 0.5. Y tiene que ver con que las canciones son top 25 de México.