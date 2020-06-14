
						TFG
				ANALISIS BIG DATA DE SUBTITULOS DE TV

--------------------------------------------------------------------------------------------------

VERSION: 14062020
COMMIT: “msql_complete


Cambios principales implementados en esta versión

* Implementación de la base de datos, consultas e inserciones dentro de la misma
* Mejora de errores en la creación del corpus, como la no adición de algunas palabras como artículos, si estos están en mayúscula, etc. Corrección de palabras inexistentes.
* Prueba de hilos realizada
* Prueba de speech recognition realizada

Cambios a implementar en futuras versiones

* Indexación de nuevos datos en la base de datos si no están
* Creacion de un dashboard
* Prueba de scrapy
* Comprobar los key_errors, hay palabras que no las está cogiendo el lda
* Validar el tamaño del vector en doc2vec
* Crear un corpus con el tamaño máximo de los subtítulos para usar en el doc2vec
* Poner todas las rutas del programa en el archivo config
* Ver como clasificar con la similitud que nos proporciona doc2vec y no k_means
* Comprobar si se está creado el corpus para usarlo en el doc2vec


