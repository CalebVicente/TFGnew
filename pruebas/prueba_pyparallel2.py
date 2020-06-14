# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:43:07 2020

@author: cvicentm
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:40:22 2020

@author: cvicentm
"""

import timeit
from tqdm import tqdm
import threading
import time

#Start CON HILOS--------------------------------------------------------
n_thread = 20

results = [None] * n_thread
def contar(i):
    h=0
    for f in range(1000000001):
        h=f
    results[i]=[h*i,h,i]
    
def checkThreadStop(threads):
    "this function check if on an array of threads are all stoped"
    def checkList(threads):
        print("inside the function checkList")
        for t in threads:
            v_list.append(str(t.isAlive()))
        if "True" not in v_list:
            print("all threads are finished")
        else:
            print("ha entrado en el esle")
            time.sleep(20)
            checkList(threads)
    
    t = threads[len(threads)-1]
    
    while t.isAlive():
        # sleep(1) make an sleeping of 1 second
        print("thread are still running")
        time.sleep(1)
    v_list=[]
    
    checkList(threads)
        
    toc=timeit.default_timer()
    print("hilos terminadossssssssss"+str(toc-tic)) 

print("EMPEZANDO CON HILOS") 


tic=timeit.default_timer()
threads = list()
for i in tqdm(range(n_thread)):
    t = threading.Thread(target=contar, args=(i,))
    threads.append(t)
    t.start()
 
checkThreadStop(threads)
#END CON HILOS--------------------------------------------------------