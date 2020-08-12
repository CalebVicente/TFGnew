# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:25:36 2020

@author: cvicentm
"""

# pip install pymongo
from pymongo import MongoClient
import pandas as pd
client = MongoClient('localhost', 27017)
mydb = client["tfg_project"]
mycol = mydb["tv_storage"]


#INSERT INTO DATABASE
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

#GET AL COLLECTION
pcollection=pd.DataFrame(mydb.mycol.find( {} ))