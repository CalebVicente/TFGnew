# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:26:23 2020

@author: cvicentm
"""
"""
df = topic_dataframe.T.reset_index()
df.rename(columns={'index':'name'}, inplace=True)
"""
import pandas as pd
import numpy as np


def get_date(subtitle):
    """"this funtion get the date from a subtitle title with this form:
            yyyy mm dd
        """
    import re
    date = re.search(r'\d{4} \d{2} \d{2}', subtitle)
    try:
        return str(date.group())
    except:
        print("error for subtitle: +"+str(subtitle))
    
    


df = pd.read_csv("..\\data\\df.csv") 
df.rename(columns={'index':'name'}, inplace=True)

names = list(df['name'])
days=[get_date(name) for name in names]
days_separated = [day.split(" ") for day in days]

days_np = np.array(days_separated)

df.insert(loc=1, column='year', value=days_np[:,0])
df.insert(loc=2, column='month', value=days_np[:,1])
df.insert(loc=3, column='day', value=days_np[:,2])
df['days_completed'] = days

df_pwbi=df
#df.to_csv("..\\data\\df_pbi.csv")
df_pwbi.to_csv("..\\data\\df_pbi2.csv")

df_hola = pd.read_csv("..\\data\\df_pbi.csv") 

