# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 09:34:03 2020

@author: cvicentm
"""


from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from nltk import word_tokenize
from tqdm import tqdm
from gensim.utils import simple_preprocess
import numpy as np
import pandas as pd
#---------------------------
from modules.sql import dBAdapter
from modules.pre import create_corpus as c

n_documents = 4000

#----------------------------------------------------------------------------
print("Getting body subtitles from the database started ...")
dbAdapter= dBAdapter.Database()
dbAdapter.open()
max_documents = int(dbAdapter.get_maxDocuments()[0][0]);
n_documents=max_documents
listado=dbAdapter.selectGenerator_normalize_limit(n_documents)
dic_subtitles = dict(dbAdapter.selectDic_subtitles_limit(n_documents))
dbAdapter.close()
print("finalizada consulta")

dic_subtitles2 = dic_subtitles

generator_normalize = []
for i in range(len(listado)):
    try:
        generator_normalize.append(listado[i][0].split(","))
    except:
        dic_subtitles2.pop(list(dic_subtitles.keys())[i])
        print("generator NonType------>"+str(i))

dic_subtitles = dic_subtitles2
        
for gn in generator_normalize:
    while True:
        try:
            gn.remove("")
        except ValueError:
            break
#------------------------------------------------------------------------------

id2word = Dictionary(generator_normalize)
corpus = [id2word.doc2bow(text) for text in generator_normalize]

model = TfidfModel(corpus, smartirs='ntc')  
vector = model[corpus[0]]  

print("imprimiendo los resultados del tf-idf")
results=[]
for doc in tqdm(model[corpus]):
    results.append([[id2word[num],freq] for num, freq in doc])

sort_results=[]
for result in tqdm(results):
    df_result = pd.DataFrame(result)
    sort_results.append(df_result.sort_values(1,ascending=False).values.tolist())

#sort_vector= vector.sort_values(1,ascending=False) 
#.sort(reverse=True) 
dates = []
for subtitle in tqdm(list(dic_subtitles.keys())):
    dates.append(c.get_date(subtitle))

final_df=pd.DataFrame(list(dic_subtitles.keys()),dates).reset_index()
select_index_from_day=list(final_df.loc[final_df['index'] == '2019 10 24'].index)
tfidf_day=[(list(dic_subtitles.keys())[idx],sort_results[idx]) for idx in select_index_from_day]

list_word_day = []
list_word_day = [word for document in tfidf_day for word,num in document[1]]
list_word_day = list(dict.fromkeys(list_word_day))

miw_day = np.zeros((len(list_word_day),len(tfidf_day)))

for i in tqdm(range(len(tfidf_day))):
    df = pd.DataFrame(tfidf_day[i][1])
    for j in range(len(list_word_day)):
        try:
            if len(df.loc[df[0]==list_word_day[j]][1])!=0:
                miw_day[j][i]=float(df.loc[df[0]==list_word_day[j]][1])
        except Exception as e:
            pass

tfidf_result = pd.DataFrame(list_word_day)

for i in range(np.shape(miw_day)[1]):
    tfidf_result.insert(i+1,tfidf_day[i][0],miw_day[:,i])
    
tfidf_result['sum'] = tfidf_result.sum(axis=1)

tfidf_result = tfidf_result.sort_values("sum",ascending=False)



