# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 09:29:57 2020

@author: cvicentm
"""
from modules.sql import dBAdapter
from modules.pre import create_corpus as c

n_documents = 4

#----------------------------------------------------------------------------
print("Getting body subtitles from the database started ...")
dbAdapter= dBAdapter.Database()
dbAdapter.open()
dic_subtitles = dict(dbAdapter.selectDic_subtitles_limit(n_documents))
dbAdapter.close()
print("finalizada consulta")

from sumy.parsers.plaintext import PlaintextParser
#for tokenization
from sumy.nlp.tokenizers import Tokenizer
file = "text//messi.txt" 
parser = PlaintextParser.from_file(file, Tokenizer("spanish"))

from sumy.summarizers.lsa import LsaSummarizer
summarizer_2 = LsaSummarizer()
summary_2 =summarizer_2(parser.document,2)
for sentence in summary_2:
    print(sentence)
