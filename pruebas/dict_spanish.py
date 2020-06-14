# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:55:42 2020

@author: cvicentm
"""
"""
import enchant
brew remove aspell
brew install aspell --with-lang-es --with-lang-en

print(enchant.list_languages())
"""
"""
import nltk
nltk.download('words')
nltk.download('wordnet')
nltk.download('spanish_grammars')
stopwords   = set(nltk.corpus.words.words('spa'))
#english_vocab = set(w.lower() for w in nltk.corpus.words.words('spanish'))
import enchant
print(enchant.list_languages())

nltk.download('cess_esp')
from nltk.corpus import cess_esp as cess
cess_sents = cess.tagged_sents()
"""
"""
import enchant 
  
# Using 'en_US' dictionary 
d = enchant.Dict("en_US") 
  
word="helo"
  
d.check(word) 
print(d.suggest(word))

broker = enchant.Broker()
broker.describe()
broker.list_languages()
"""
from spellchecker import SpellChecker
spell = SpellChecker(language='es')
word="helo"
print(spell.correction(word))
print(spell.candidates(word))