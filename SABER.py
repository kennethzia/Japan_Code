# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:46:51 2019

@author: Kenneth
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted
from scipy import interpolate


plt.rcParams.update({'font.size': 20})
date = [r'\1_12',r'\1_13']
file = [r'\1',r'\2',r'\3']

alt = np.arange(71,99,0.25)

OHver = np.zeros((np.size(alt)))
AvgTemp = np.zeros(np.size(alt))


ii=1
for i in range(0,3):
    path = r'C:\Users\Kenneth\Desktop\PFRR SABER'+date[ii]+file[i]
    
    data2 = pd.read_csv(path+'\Temp.csv')
    Temp = data2.values
    
    f=interpolate.interp1d(Temp[:,1],Temp[:,0],kind='linear')
    
    Temperature = f(alt)
    
    data2 = pd.read_csv(path+'\OHlayer.csv')
    OH = data2.values
    
    f=interpolate.interp1d(OH[:,1],abs(OH[:,0]),kind = 'linear')
    
    OHver = f(alt)
    
#    
#    if i > 0:
#        AvgTemp = np.average([AvgTemp[:],Temperature[:]],0)
#        AvgOH = np.average([AvgOH[:],OHver[:]],0)
#    else:
#        AvgTemp = Temperature
#        AvgOH = OHver
#if ii == 0:

    plt.figure(figsize=(8,8))
    ax1=plt.gca()

    ax1.plot(Temperature,alt)
    plt.xlabel('Temperature (K)')
    ax1.set_ylabel('Altitude (km)')
    plt.title('Jan 13')
        
    ax1=plt.gca()
    ax2=ax1.twiny()
    ax2.plot(OHver,alt,color='r',linestyle='--')
    ax2.set_ylabel('OH-Layer',color = 'r')
    ax1.grid()
    
    
#else:
#    plt.figure()
#    ax1=plt.gca()
#
#    ax1.plot(AvgTemp,alt)
#    plt.xlabel('Temperature (K)')
#    ax1.set_ylabel('Altitude (km)')
#    plt.title('Jan 13')
#        
#    ax1=plt.gca()
#    ax2=ax1.twiny()
#    ax2.plot(np.average(OHver[:],1),alt,color='r',linestyle='--')
#    ax2.set_ylabel('OH-Layer',color = 'r')
#    ax1.grid()