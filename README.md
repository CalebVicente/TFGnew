
						TFG
				ANALISIS BIG DATA DE SUBTITULOS DE TV

--------------------------------------------------------------------------------------------------

VERSION: 23062020
COMMIT: primera versi�n LDA y TFIDF


Cambios principales implementados en esta versi�n

* Script de comparaci�n entre telediarios de diferentes cadenas, con palabras m�s importantes sacadas con TFIDF
* Prueba funcionamiento de LSA: Resultados no muy positivos actualmente
* Validaci�n del LSA con coherencia u_mass
* Mejora de los csv necesarios para la visualizaci�n del dashboard
* Mejora de las 

Cambios a implementar en futuras versiones

* Indexaci�n de nuevos datos en la base de datos del doc2vec
* Comprobar los key_errors, hay palabras que no las est� cogiendo el lda 
* Poner todas las rutas del programa en el archivo config
* Ver como clasificar con la similitud que nos proporciona doc2vec y no k_means
* Hacer una investigaci�n de summarization con lsa y otras t�cnicas

