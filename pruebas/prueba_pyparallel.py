# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:40:22 2020

@author: cvicentm
"""

import timeit
from tqdm import tqdm
import threading
import time

#Start SIN HILOS--------------------------------------------------------
tic=timeit.default_timer()
h=0
for i in tqdm(range(100)):
    for f in range(5000000):
        h=f
toc=timeit.default_timer()
print(toc-tic)
#End SIN HILOS----------------------------------------------------------

#Start CON HILOS--------------------------------------------------------
def contar(i):
    h=0
    for f in range(5000000):
        h=f
print("EMPEZANDO CON HILOS") 

tic=timeit.default_timer()
threads = list()
for i in tqdm(range(100)):
    t = threading.Thread(target=contar, args=(i,))
    threads.append(t)
    t.start()
 

t = threading.Thread(target=contar, args=(i,))
t.start()
while t.isAlive():
    time.sleep(1)
print(t.isAlive())
toc=timeit.default_timer()
print("hilos terminadossssssssss"+str(toc-tic)) 
#END CON HILOS--------------------------------------------------------