# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:54:32 2018

@author: Kenneth
"""

import matplotlib.pyplot as plt
import numpy as np

x1=np.arange(1,7)

myticks=['8-11','11-15','15-22','22-30','30-43','43-60']

x2=x1
y1=[8.74E-6,8.56E-6,1.31E-5,7.36E-6,7.88E-6,5.09E-6]
y2=[6.29E-5,1.07E-4,1.35E-4,1.09E-4,1.47E-4,1.01E-4]


plt.rcParams.update({'font.size': 15})
plt.figure(figsize=(10,8))

plt.ylabel('Total Power')
plt.xlabel('Wave Period (min)')
plt.semilogy(x1,y1,label='ASI',linewidth=5.0)
plt.semilogy(x1,y2,label='AMTM',linewidth=5.0)
plt.xticks(x1,myticks)
plt.legend()
plt.title('ASI and AMTM Power vs Period')
plt.show()