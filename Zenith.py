# -*- coding: utf-8 -*-
"""
Created on Mon Mar 04 16:04:17 2019

@author: Kenneth
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted
from scipy import interpolate
import scipy.signal

plt.rcParams.update({'font.size': 15})


#path="C:\Users\Kenneth\Desktop\Jun17-18\BandOH_caun****"
#files=glob.glob(path+'.tif')
#Ifiles=natsorted(files)


m=('\Jun19-20')#,'\Jun18-19')

patha='C:\Users\Kenneth\Desktop'+m+'\BandOH_caun****'
filesa=glob.glob(patha+'.tif')
filesa=natsorted(filesa)

#pathb='C:\Users\Kenneth\Desktop'+m[1]+'\BandOH_caun****'
#filesb=glob.glob(pathb+'.tif')
#filesb=natsorted(filesb)


pathc='C:\Users\Kenneth\Desktop'+m+'\TempOH_caun****'
filesc=glob.glob(pathc+'.tif')
filesc=natsorted(filesc)

#pathd='C:\Users\Kenneth\Desktop'+m[1]+'\TempOH_caun****'
#filesd=glob.glob(pathd+'.tif')
#filesd=natsorted(filesd)

Hours=np.size(filesa)#+np.size(filesb)

I=np.zeros(Hours)
T=np.zeros(Hours)
time=np.zeros(Hours)


a=plt.imread(filesa[0])
a1=a.shape
data=np.zeros((a1[0],a1[1],Hours))
b=plt.imread(filesc[0])
b1=a.shape
data2=np.zeros((b1[0],b1[1],Hours))#,b1[1],Hours))


for p in range(0,Hours):
#    if p > (np.size(filesa)-1):
#        pp=p-np.size(filesa)
#        data[:,:,p] = plt.imread(filesb[pp])
#        data2[:,:,p] = plt.imread(filesd[pp])
#    else:
    data[:,:,p] = plt.imread(filesa[p])
    data2[:,:,p] = plt.imread(filesc[p])

    
    I[p]=np.mean(data[int(a1[0]/2)-2:int(a1[0]/2)+2,int(a1[1]/2)-2:int(a1[1]/2)+2,p])
    T[p]=np.mean(data2[int(a1[0]/2)-2:int(a1[0]/2)+2,int(a1[1]/2)-2:int(a1[1]/2)+2,p])

    time[p]=p*37.0/3600.0
    
Iprime=(I-np.mean(I)/np.mean(I))

plt.figure(figsize=(10,10))
ax1=plt.gca()
ax2=ax1.twinx()
ax1.plot(time,I,label='I-Prime',color='b')
ax1.set_ylabel('Intensity',color='b')
ax2.plot(time,T,label='Intensity',color='k')
ax2.set_ylabel('Temperature (K)',color='k')
plt.title('MCM Jun17-19 Temperature and Intesnity Variation')
plt.show()

#N=np.size(files)*10
#f=np.linspace(0.01,2.0,N)
#
#pgram= scipy.signal.lombscargle(time,I)
#plt.figure(figsize=(10,10))
#
#plt.plot(1/f,np.sqrt(4*(pgram/N)))

#T=T/np.sum(T)
#I=I/np.sum(I)
#plt.plot(time,I,label='Intensity')
#plt.plot(time,T,label='Temperature')
#plt.legend()

plt.show()
#
#FFT=np.fft.rfft(I,N)
#Freq=np.fft.rfftfreq(N,d=1.0/37.0)
#plt.figure(figsize=(10,10))
#plt.plot((1.0/Freq)/3600.0,FFT)
#plt.show()






