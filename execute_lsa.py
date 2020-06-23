# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:13:04 2020

@author: cvicentm
"""

from gensim.models import TfidfModel
from gensim.models import LsiModel
from gensim.models import hdpmodel
from gensim.corpora import Dictionary
from nltk import word_tokenize
from tqdm import tqdm
from gensim.utils import simple_preprocess
import numpy as np
import pandas as pd
import pickle
from gensim.models import CoherenceModel
import matplotlib.pyplot as plt
import gc
from scipy.signal import savgol_filter
#---------------------------
from modules.sql import dBAdapter
from modules.pre import create_corpus as c

#START FUNCTIONS-------------------------------------------------------------------------
def knee_locator_coherence_u_mass(score, curve='convex', direction='decreasing'):
	"""This funtion localize where is the optimal number of clusters"""
	from kneed import KneeLocator

	x = range(1, len(score)+1)
	#son super importantes las variables curve y direction o el KneeLocator no funcionará correctaente
	kn = KneeLocator(x, score, curve=curve, direction=direction)
	
	return kn.knee

def graphic_coherence_u_mass(knee,score):
	"""This function print a graph score of all the validators scores"""
	import matplotlib.pyplot as plt

	x = range(1, len(score)+1)
	plt.xlabel('Number of topics, LSA')
	plt.ylabel('Coherence')
	plt.plot(x, score, 'bx-')
	plt.vlines(knee, plt.ylim()[0], plt.ylim()[1], linestyles='dashed')
    
#END FUNCTIONS---------------------------------------------------------------------------
    
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
print("empezado el TfidfModel")
tfidf = TfidfModel(corpus)
print("TfidfModel paso 2")
corpus_tfidf = tfidf[corpus]
print("Empieza el LSi")

coherencevalueArray = []
start = 10
end = 300
step = 3
n_documents = len(generator_normalize)
for i in tqdm(range(start,end,step)):

    file_lsa_model = 'pickle\\'+str(n_documents)+'\lsa_model_'+str(i)+'_'+str(n_documents)+'.sav'
    try:
       
        f=open(file_lsa_model, 'rb')
        lsa = pickle.load(f)
        print("The model has been trained previously with..."+str(i)+" n_topics") 
        coherencemodel = CoherenceModel(model=lsa, corpus=corpus_tfidf, dictionary=id2word, coherence='u_mass')
        #CoherenceModel(model=goodLdaModel, texts=texts, dictionary=dictionary, coherence='c_v')
        #coherencemodel = CoherenceModel(model=lda, texts=list(generator_normalize), dictionary=id2word, coherence='c_v')
        coherence_values = coherencemodel.get_coherence()
        coherencevalueArray.append(coherence_values)
        
    except IOError:
        
        print("FINALLY: the LSA model has to be trained for "+str(n_documents)+" n_documents and "+str(i)+" n_topics, trained")
        lsi = LsiModel(corpus_tfidf, id2word=id2word, num_topics=i)
        print("Lsi paso 2")
        corpus_lsi = lsi[corpus]
        
        n_words = sum( [ len(item) for item in corpus])
        topics_resume = lsi.show_topics(num_topics=i, num_words=n_words, log=False, formatted=True)
        print("coherence")
        coherencemodel = CoherenceModel(model=lsi, corpus=corpus_tfidf, dictionary=id2word, coherence='u_mass')
        coherencevalue = coherencemodel.get_coherence()
        coherencevalueArray.append(coherencevalue)
        #vaciar memoria RAM
        gc.collect()
    
        file_lsa_model = 'pickle\\'+str(len(generator_normalize))+'\lsa_model_'+str(i)+'_'+str(len(generator_normalize))+'.sav'
        pickle.dump(lsi, open(file_lsa_model, 'wb'))                  
        
#-------------------------------------------------------------------------------------
   
score = savgol_filter(coherencevalueArray, 51, 3)
knee=knee_locator_coherence_u_mass(score)
graphic_coherence_u_mass(knee,score)



"""
Hdp_model = hdpmodel.HdpModel(corpus=corpus, id2word=id2word)
topics_resume_hdp = Hdp_model.print_topics(num_topics=70, num_words=10)
"""