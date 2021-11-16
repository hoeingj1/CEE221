# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:16:18 2021

@author: jhoei
"""

import numpy as np
import matplotlib.pyplot as plt
import os

work_path = r'C:\Users\jhoei\Documents\Dayton\CEE 221'
os.chdir(work_path)
print('Current working directory %s' %work_path)
#%%
N_total = 100000
limit = np.zeros(N_total)
x = np.arange(N_total)
for i, N in enumerate(np.arange(N_total)+1):
    iteration = np.sqrt(i+1) - np.sqrt(i)
    limit [i] = iteration

plt.plot(x, limit)
plt.show()
print (iteration)
if limit[i] < 0.01:
    print ('the limit is zero')
