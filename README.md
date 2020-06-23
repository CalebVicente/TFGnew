
						TFG
				ANALISIS BIG DATA DE SUBTITULOS DE TV

--------------------------------------------------------------------------------------------------

VERSION: 23062020
COMMIT: primera versión LDA y TFIDF


Cambios principales implementados en esta versión

* Script de comparación entre telediarios de diferentes cadenas, con palabras más importantes sacadas con TFIDF
* Prueba funcionamiento de LSA: Resultados no muy positivos actualmente
* Validación del LSA con coherencia u_mass
* Mejora de los csv necesarios para la visualización del dashboard
* Mejora de las 

Cambios a implementar en futuras versiones

* Indexación de nuevos datos en la base de datos del doc2vec
* Comprobar los key_errors, hay palabras que no las está cogiendo el lda 
* Poner todas las rutas del programa en el archivo config
* Ver como clasificar con la similitud que nos proporciona doc2vec y no k_means
* Hacer una investigación de summarization con lsa y otras técnicas

