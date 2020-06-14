# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:49:47 2020

@author: cvicentm
"""

import json

with open("prueba.json") as json_file:
    data = json.load(json_file)
    lead = data['body']
    raw_text = lead['raw_text']