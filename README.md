
						TFG
				ANALISIS BIG DATA DE SUBTITULOS DE TV

--------------------------------------------------------------------------------------------------

VERSION: 14062020
COMMIT: �msql_complete


Cambios principales implementados en esta versi�n

* Implementaci�n de la base de datos, consultas e inserciones dentro de la misma
* Mejora de errores en la creaci�n del corpus, como la no adici�n de algunas palabras como art�culos, si estos est�n en may�scula, etc. Correcci�n de palabras inexistentes.
* Prueba de hilos realizada
* Prueba de speech recognition realizada

Cambios a implementar en futuras versiones

* Indexaci�n de nuevos datos en la base de datos si no est�n
* Creacion de un dashboard
* Prueba de scrapy
* Comprobar los key_errors, hay palabras que no las est� cogiendo el lda
* Validar el tama�o del vector en doc2vec
* Crear un corpus con el tama�o m�ximo de los subt�tulos para usar en el doc2vec
* Poner todas las rutas del programa en el archivo config
* Ver como clasificar con la similitud que nos proporciona doc2vec y no k_means
* Comprobar si se est� creado el corpus para usarlo en el doc2vec


