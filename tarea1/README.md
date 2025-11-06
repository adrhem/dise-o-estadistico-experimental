## Tarea 1: Planteamiento de un problema, marco teórico y alcance

### Selección de los datos
Como base de datos elegí el dataset [Top Spotify Songs in 73 Countries (Daily Updated)](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated) disponible en Kaggle. Esta contiene información sobre las canciones más populares en Spotify en 73 países diferentes, actualizada diariamente. Además incluye atributos como el nombre de la canción, el artista, el país, la fecha, y varias características musicales como la duración, el tempo, la energía, bailabilidad, entre otros. 

Para reducir el tamaño de la base de datos y facilitar su análisis, decidí filtrar los datos para quedarme únicamente con las canciones más populares en México. Esto no solo porque me interesa el análisis de la música popular en mi país, sino también porque la base de datos original es bastante grande y contiene información relevante en el ámbito de preferencias musicales y tendencias culturales en México.

Finalmente, según la descripción del dataset en Kaggle, los datos fueron recopilados utilizando la API de Spotify, lo que garantiza que la información es precisa y confiable.

### Planteamiento del problema
El objetivo de este proyecto es analizar las características musicales de las canciones más populares en Spotify en México y determinar si existen patrones o tendencias en estas características a lo largo del tiempo basado en los datos disponibles como duración, tempo, energía, bailabilidad, entre otros. La pregunta de investigación que guiará este análisis es:
1. ¿Qué tan variable es el atributo de "danceability" (bailabilidad) entre las canciones más populares en Spotify en México a lo largo del tiempo? 


### Marco Teórico de la investigación
Como parte del marco teórico de este proyecto, es importante entender algunos conceptos clave relacionados con el análisis de datos musicales y las características que se están evaluando. Según [Antoine Hennion](http://educa.fcc.org.br/scielo.php?script=sci_arttext&pid=S1988-32932010000100004&lng=pt&tlng=es)[1], el análisis de datos musicales es una técnica colectiva, cuyo análisis ayuda a entender la manera en la que nos hacemos sensibles a las cosas, a nosotros mismos, a las situaciones y los momentos, mientras en paralelo controla reflexivamente la forma en que esos sentimientos pueden ser compartidos y discutidos con los demás. Esto es relevante para nuestro proyecto, ya que al analizar las características musicales de las canciones populares, podemos obtener una mejor comprensión de las preferencias musicales y las tendencias culturales en México.

Además, en el artículo de [Mencía Gómez Luna](https://www.socyl.es/revistas/index.php/revista-socyl/article/view/46)[2], explica qué factores influyen en el gusto y en las prácticas musicales, así como de qué manera se da el consumo de música en la actualidad en España. Si bien los datos de nuestra investigación se centran en México, los conceptos discutidos en este artículo son aplicables a nuestro análisis, ya que nos ayudan a entender cómo las características musicales pueden influir en la popularidad de las canciones y cómo estas preferencias pueden variar entre diferentes grupos demográficos.

Finalmente en el artículo de [Luis María Plaza Chicote](https://docta.ucm.es/entities/publication/e9e1fb66-7712-4283-86d1-bd00a2fc4a53)[3], aborda el análisis predictivo del nivel de popularidad de una canción en la plataforma de streaming musical Spotify. El autor utiliza técnicas de machine learning para predecir la popularidad de una canción basándose en sus características musicales ofrecidas también por el API de Spotify. Este enfoque es relevante para nuestro proyecto, ya que nos proporciona una perspectiva sobre cómo las características musicales pueden ser utilizadas para predecir o influir en la popularidad de las canciones en Spotify.

### Bibliografía
1. Hennion, Antoine. (2010). Gustos musicales: De una sociología de la mediación a una pragmática del gusto. Comunicar: Revista Científica de Comunicacíon y Educacíon, 17(34), 25-33. Recuperado em 05 de novembro de 2025, de http://educa.fcc.org.br/scielo.php?script=sci_arttext&pid=S1988-32932010000100004&lng=pt&tlng=es.
2. Gómez Luna, M. (2024). Análisis del gusto, del consumo y de las prácticas musicales en España (2020-2024). Revista Trazas De Ciencias Sociales, 2(1). https://doi.org/10.48225/trzpsv2vg
3. Plaza Chicote, L. M. (2023). Análisis predictivo de la popularidad de una canción en Spotify. 