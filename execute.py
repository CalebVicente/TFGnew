# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 08:04:32 2020

@author: cvicentm
"""
"""
from nltk import word_tokenize
def get_word_dict(word):
    n=word.find("/")
    if n != -1:
        return word[0:n]
    else:
        return word
f=open("config\\es_ANY.txt","r",encoding='utf-8')
file=f.read()
dic=word_tokenize(str(file))
es_dict = [get_word_dict(word) for word in dic]
f.close()

"""
#lista=list(file)
#lista2=[item for item in lista if str(item).isnumeric()==False]
#import pandas as pd
#data = pd.read_csv("config\\es_ANY.dic.txt", sep=" ", header=None)
"""
#------------------------------------------------------
#INSERTAR DDBB DICCTIONARY Y GENERATOR NORMALIZE tv_storage
#------------------------------------------------------
from modules.pre import get_data as g
from modules.pre import create_corpus as c
[files, max_documents] = g.get_NameFiles()

[generator_normalize, dic_subtitles]=c.create_corpus(max_documents)
subtitles=list(dic_subtitles.keys())

def removing_none_words(word):
    if word != None:
        return word

gn=[]
for d in generator_normalize:
    gn.append(','.join(list(filter(removing_none_words,d))))

from modules.sql import dBAdapter
from modules.pre import create_corpus as c
dbAdapter= dBAdapter.Database()
dbAdapter.open()
for i in range(len(subtitles)):
    dbAdapter.update_body(subtitles[i],dic_subtitles[subtitles[i]])
    dbAdapter.update_generator(subtitles[i],gn[i])
dbAdapter.close()
dbAdapter= dBAdapter.Database()
dbAdapter.open()
"""

"""
#------------------------------------------------------
#INSERTAR DDBB DOC2VEC prueba
#------------------------------------------------------
from modules.pre import create_corpus as c
from modules.pre import get_data as g
[files, max_documents] = g.get_NameFiles()
[dic_subtitles,data]=c.create_d2v_corpus(max_documents)
subtitles=list(dic_subtitles.keys())
data_s=[]
for d in data:
    data_s.append(','.join(d))

from modules.sql import dBAdapter
dbAdapter= dBAdapter.Database()
dbAdapter.open()
for i in range(len(data)):
    dbAdapter.insert_dataDoc2Vec(subtitles[i],data[i])
dbAdapter.close()
"""
"""
fjdljf
"""
#------------------------------------------------------
#GET DDBB generator_normalalize from tv_storage
#------------------------------------------------------
from modules.sql import dBAdapter
dbAdapter= dBAdapter.Database()
dbAdapter.open()
listado=dbAdapter.selectGenerator_normalize_limit(5)
dic_subtitles = dict(dbAdapter.selectDic_subtitles_limit(5))
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

"""
#------------------------------------------------------
#GET DDBB DOC2VEC prueba
#------------------------------------------------------
dbAdapter.open()
listado=dbAdapter.select_dataDoc2Vec(5622)
dbAdapter.close()
print("finalizada consulta")
listado2=[]
for l in listado:
    listado2.append(l[0].split(","))
for l in listado2:
    while True:
        try:
            l.remove("")
        except ValueError:
            break
"""
"""
#------------------------------------------------------
#COMPROBACIÓN FUNCIONAMIENDTO NORMALIZE WORDS
#------------------------------------------------------
from modules.pre import create_corpus as c
word="microsoft"
change = c.normalize_word(word)
"""
"""
from modules.sql import dBAdapter
dbAdapter= dBAdapter.Database()
dbAdapter.open()
results=dbAdapter.selectAll()
dbAdapter.close()
dresults=dict(results)

from modules.pre import create_corpus as c
from tqdm import tqdm
from nltk import word_tokenize
print("\n tokenizing words ...")
list_subt_token = [word_tokenize(value) for (key,value) in tqdm(dresults.items())]
print("\n Creation of generator normalize")
generator_normalize = [list(c.normalize(document)) for document in tqdm(list_subt_token)]
generator_normalize = list(generator_normalize)

from modules.sql import dBAdapter
dbAdapter= dBAdapter.Database()
print("inserting into database generator_normalize...")
for i in tqdm(range(len(list(dresults.keys())))):
    dbAdapter.open()
    results=dbAdapter.insert_generator(list(dresults.keys())[i],generator_normalize[i])
    dbAdapter.close()


prueba=dresults['1_spa_2016 11 29_morning_new']
prueba_t=word_tokenize(prueba)
normalize=list(c.normalize(prueba_t))
"""
"""
----------------------------------------------------
INTENTAR INSERTAR MODELO LDA EN LA BASE DE DATOS
-----------------------------------------------------
import pickle
from modules.sql import dBAdapter
dbAdapter= dBAdapter.Database()
n_documents=9
n_topics=9
file_lda_model = 'pickle\\'+str(n_documents)+'\lda_model_'+str(n_topics)+'_'+str(n_documents)+'.bin'
f = open(file_lda_model,'rb')
fstring=f.read()
dbAdapter.open()
print("insertar lda model")
dbAdapter.insertLdaModel("lda9",str(fstring),fstring )
print("extraer lda model")
lda=dbAdapter.selectLdaModelByName("lda9")
dbAdapter.close()

f.close()
file_lda_model = 'pickle\\'+str(n_documents)+'\corpus_'+str(n_documents)+'.txt'
f=open(file_lda_model, 'rb')
corpus = pickle.load(f)
f.close()
-----------------------------------------------------
"""
"""
#----------------------------------------------------
#IMPORTACION DICTIONARIO Y GENERATOR_NORMALIZE DE LA BASE DE DATOS
#-----------------------------------------------------
from modules.sql import dBAdapter
dbAdapter= dBAdapter.Database()
dbAdapter.open()
dic_subtitles = dict(dbAdapter.selectDic_subtitles_limit(200))
gn = dbAdapter.selectGenerator_normalize_limit(200)
generator_normalize = [gni[0] for gni in gn]
dbAdapter.close()
#-----------------------------------------------------

from modules.sql import dBAdapter
dbAdapter= dBAdapter.Database()
dbAdapter.open()
max_columns= int(dbAdapter.get_maxDocuments()[0][0]);
dbAdapter.close()
"""
"""

from modules.sql import dBAdapter
dbAdapter= dBAdapter.Database()
dbAdapter.open()
key='1_spa_2016 11 06_afternoon_new'
result = dbAdapter.selectRowByName(key)
date=c.get_date(key)
dbAdapter.insert(key,dic_subtitles[key].replace("'",""),date)
dbAdapter.close()
"""
"""
from tqdm import tqdm
from nltk import word_tokenize
print("\n tokenizing words ...")
list_subt_token = [word_tokenize(value) for (key,value) in tqdm(dic_subtitles.items())]
print("\n Creation of generator normalize")
generator_normalize = [list(c.normalize(document)) for document in tqdm(list_subt_token)]
generator_normalize = list(generator_normalize)
"""
