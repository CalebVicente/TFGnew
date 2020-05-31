# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:07:17 2020

@author: cvicentm
"""

import pickle

f=open('corpus_7331.txt', 'rb')
corpus = pickle.load(f)
f.close()
f=open('id2word_7331.txt', 'rb')
id2word = pickle.load(f)
f.close()