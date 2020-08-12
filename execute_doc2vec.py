# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:38:18 2020

@author: cvicentm
"""

"""IN THIS PROGRAM THE CODE DOC2VEC WILL BE EXECUTED """

from modules.doc2vec import doc2vec as d2v
from modules.classificator import k_means_doc2vec as k
from modules.sql import dBAdapter 
import matplotlib.pyplot as plt
import timeit
import numpy as np
import pickle

database = 'tfg_project'
collection = 'tv_storage'
dbAdapter = dBAdapter.Database(database, collection)
dbAdapter.open()
max_documents = dbAdapter.get_maxDocuments()
dbAdapter.close()

max_clusters=20
n_documents = 200

[list_vec_doc2vec, arr_vec_doc2vec, train_data, model]=d2v.doc2vec_module(database, collection, n_documents = n_documents, vector_size = 50, max_clusters = max_clusters)

#Para saber las palabras más parecidas con el modelo DM
model.wv.most_similar('camión')

"""IMPORTANTE"""
#Poner el modelo de palabras en el Embedding Projector
model.wv.save_word2vec_format('doc2vec_model')
#ejecutar el siguiente comando en cmd donde se encuentre la ruta de model_name
#python -m gensim.scripts.word2vec2tensor --input doc2vec_model --output tf_name
#ir a la página de https://projector.tensorflow.org/
#salen demasiadas palabras, quitar unas cuantas

"""
#-----------------------------------------------------------------------------------------------------
#COMPARATION BETWEEN K_MEANS AND PCA KMEANS
#-----------------------------------------------------------------------------------------------------
plt.figure(0)
tic=timeit.default_timer()
knee_c=d2v.doc2vec_kmeans_similarity(arr_vec_doc2vec, max_clusters)
toc=timeit.default_timer()
print("Time using normal k_means: "+str(toc-tic))
plt.figure(1)
tic=timeit.default_timer()
[components,knee_pca]=d2v.doc2vec_kmeans_pca(arr_vec_doc2vec, max_clusters)
toc=timeit.default_timer()
print("Time using PCA k_means: "+str(toc-tic))
"""
#START PCA: ------------------------------------------------------------------------------------------




"""
plt.figure(3)
plt.scatter(components[:, 2], components[:, 1], c=prediction, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 2], centers[:, 1], c='black', s=200, alpha=0.5);


score_completed=validator_cluster(arr_vec_doc2vec,100)
knee2 = k.knee_locator_k_means(score_completed)
plt.figure(4)
k.graphic_k_means_validator(knee2,score_completed)
"""



#FINISHED PCA: -------------------------------------------------------------------------