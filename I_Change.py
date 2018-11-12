# -*- coding: utf-8 -*-
"""
Created on Tue Oct 02 14:30:25 2018

@author: Kenneth
Binned Image changes
"""

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
plt.rcParams.update({'font.size': 15})

#data = pd.read_csv("C:\Users\Kenneth\Desktop\ASI_I.csv")
#data=data.values
#data2 = pd.read_csv("C:\Users\Kenneth\Desktop\AMTM_BandOH_I.csv")
#data2=data2.values
#data3 = pd.read_csv("C:\Users\Kenneth\Desktop\AMTM_BandOH(1hrMean)_I.csv")
#data3=data3.values

data1 = pd.read_csv("C:\Users\Kenneth\Desktop\AMTM_BandOH(Norm).csv")
data1=data1.values
data2 = pd.read_csv("C:\Users\Kenneth\Desktop\ASI(Norm)_70.csv")
data2=data2.values
#data3 = pd.read_csv("C:\Users\Kenneth\Desktop\AMTM_Bkgd(1hrMean)_I.csv")
#data3=data3.values
#data4 = pd.read_csv("C:\Users\Kenneth\Desktop\AMTM_BandOH(1hrMean)_I.csv")
#data4=data4.values



#xasi=np.arange(0,np.size(data))*60.0/3600.0
xamtm=np.arange(0,np.size(data1))*74.0/3600.0
xamtm2=np.arange(0,np.size(data2))*70.0/3600.0


plt.figure(figsize=(10,8))
plt.title('Change of Center Pixel Delta_I (1hr mean)')
plt.plot(xamtm,data1[:,0],label='P12',linestyle='-.')
plt.plot(xamtm2,data2[:,0],label='P14',linestyle='--')
#plt.plot(xamtm2,data4[:,0],label='BandOH',linestyle=':')
plt.xlabel('Hours Over Night')
plt.ylabel('I-prime/I-mean')

plt.legend()
plt.show()

#mea=np.mean(abs((data1[:,0]-data3[:,0])-(data2[:,0]-data3[:,0]))/(data2[:,0]-data3[:,0]))


#
#han_asi=np.hanning(np.size(data))
#han_amtm=np.hanning(np.size(data2))
#
#spec_asi=np.fft.fft(data*han_asi)
#spec_amtm=np.fft.fft(data2*han_amtm)
#
#freq_asi=np.fft.fftfreq(np.size(data))
#freq_amtm=np.fft.fftfreq(np.size(data2))

#plt.figure()
#plt.plot(1/(freq_asi*60.0),spec_asi.real)
##plt.plot(1/(freq_amtm*60.0),spec_amtm.real)
#plt.show()




