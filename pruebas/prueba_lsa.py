# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:58:29 2020

@author: cvicentm
"""

from gensim.test.utils import common_dictionary, common_corpus
from gensim.models import LsiModel

model = LsiModel(common_corpus, id2word=common_dictionary)
vectorized_corpus = model[common_corpus] 