
						TFG
				ANALISIS BIG DATA DE SUBTITULOS DE TV

--------------------------------------------------------------------------------------------------

VERSION: 27052020
COMMIT: �modules lda and doc2vec working�


Cambios implementados en esta versi�n

* Implementaci�n de los sistemas doc2vec y lda en modulos que se ejecutar�n desde los scripts execute
* Ordenaci�n de la carpeta results
* Creaci�n del k_means de los resultados doc2vec as� como la impresi�n de los mismos en archivos Excel
* Implementaci�n de un archivo config encargado de las rutas de todo el programa
* Funci�n normalize_text y normalize_word dentro de cr�ate_corpus funcionando correctamente tanto las siglas como la uni�n de nombres compuestos y no lemmatizar nombres de personas

Cambios a implementar en futuras versiones

* EST� DANDO ERRORES CON LOS ART�CULOS, CREO QUE CUANDO LA PRIMERA LETRA EST� EN MAYUSCULAS LOS COGE
* Comprobar los key_errors, hay palabras que no las est� cogiendo el lda
* Validar el tama�o del vector en doc2vec
* Crear un corpus con el tama�o m�ximo de los subt�tulos para usar en el doc2vec
* Poner todas las rutas del programa en el archivo config
* Ver como clasificar con la similitud que nos proporciona doc2vec y no k_means
* Comprobar si se est� creado el corpus para usarlo en el doc2vec


