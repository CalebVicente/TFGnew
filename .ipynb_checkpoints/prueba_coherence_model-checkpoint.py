# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:23:51 2020

@author: cvicentm
"""
import pickle
from gensim.models import CoherenceModel
from modules.sql import dBAdapter

n_documents = 4992
n_topics = 37


print("Getting body subtitles from the database started ...")
dbAdapter= dBAdapter.Database()
dbAdapter.open()
listado=dbAdapter.selectGenerator_normalize_limit(n_documents)
dic_subtitles = dict(dbAdapter.selectDic_subtitles_limit(n_documents))
dbAdapter.close()
print("finalizada consulta")

generator_normalize = []
for l in listado:
    generator_normalize.append(l[0].split(","))
for gn in generator_normalize:
    while True:
        try:
            gn.remove("")
        except ValueError:
            break
print("Getting body subtitles from the database finished ...")

id2word = pickle.load(open("pickle\\"+str(n_documents)+"\id2word_"+str(n_documents)+".txt", "rb"))
print("id2word cargado")
corpus = pickle.load(open("pickle\\"+str(n_documents)+"\corpus_"+str(n_documents)+".txt", "rb"))
print("corpus cargado")
file_lda_model = 'pickle\\'+str(n_documents)+'\lda_model_'+str(n_topics)+'_'+str(n_documents)+'.sav'         
f=open(file_lda_model, 'rb')
lda = pickle.load(f)
print("lda cargado")


coherencemodel = CoherenceModel(model=lda, texts=generator_normalize, dictionary=id2word, coherence='c_v')
coherence_values = coherencemodel.get_coherence()
print(coherence_values)
