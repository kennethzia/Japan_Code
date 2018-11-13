# -*- coding: utf-8 -*-
"""
Created on Wed Nov 07 15:15:07 2018

@author: Kenneth
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted

plt.rcParams.update({'font.size': 15})
plt.figure(figsize=(10,8))
plt.xlim(100,5)  
wavebin=np.zeros(101)
wavebin2=np.zeros(101)
wavepow=np.zeros((np.size(wavebin),8))
wavepow2=np.zeros((np.size(wavebin),8))
wavemean=np.zeros(np.size(wavebin))
for k in range(0,8):
    FILE='C:\Users\Kenneth\Desktop\AMTM-ASI-3hr-18-19\ASI'+np.str(k)
    
    path=FILE+'_WN_'
    files=glob.glob(path+'*.csv')
    files=natsorted(files)
    
    a=204
    
    dx=1000.0
    dy=1000.0
    zpx=512.0
    dt=70.0
    zpt=2.0**11
    data9=np.zeros((a,a+1,np.size(files)))

    
    for i in range(0,np.size(files)):
    
        data2 = pd.read_csv(files[i])
        data9[:,:,i]=data2.values
    
    b=a/2    
    for i in range(0,a):
        for ii in range(0,a+1):
            r=np.sqrt((i-b)**2+(ii-b)**2)
            x=r/1.0
            bins=int(np.ceil(x))
            if bins <=100:
                wavepow[bins,k]=np.log10(np.sum(10**data9[i,ii,:])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**wavepow[bins,k])
    for j in range (1,100):
        wavebin[j]=1.0/((j*1.0)/(dx*zpx))/1000.0

 
    plt.loglog(wavebin,wavepow[:,k],linewidth=0.5)  

    plt.title('Wavelength Analysis ASI (Jun18-19)')
    plt.xlabel('Wavelegnth (km)')
    plt.ylabel('Power (1/km)')

for i in range (0,np.size(wavebin)):
    wavemean[i]=np.average(wavepow[i,:])

plt.loglog(wavebin,wavemean,label='ASI-mean',linewidth=3)

wavepow24=np.zeros(np.size(wavebin))
FILE='C:\Users\Kenneth\Desktop\post-data\ASI_18-19'

path=FILE+'_WN_'
files=glob.glob(path+'*.csv')
files=natsorted(files)

a=204

dx=1000.0
dy=1000.0
zpx=512.0
dt=70.0
zpt=2.0**11
data9=np.zeros((a,a+1,np.size(files)))


for i in range(0,np.size(files)):

    data2 = pd.read_csv(files[i])
    data9[:,:,i]=data2.values

b=a/2    
for i in range(0,a):
    for ii in range(0,a+1):
        r=np.sqrt((i-b)**2+(ii-b)**2)
        x=r/1.0
        bins=int(np.ceil(x))
        if bins <=100:
            wavepow24[bins]=np.log10(np.sum(10**data9[i,ii,:])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**wavepow24[bins])

 
plt.loglog(wavebin,wavepow24,label='ASI-24hr',linewidth=3)  
plt.scatter(wavebin,wavepow24)
plt.loglog(wavebin,(wavebin)**(3.0)*1.0*10**-(16.0/2.0),linewidth=2,linestyle='--',label='3-slope')
plt.loglog(wavebin,(wavebin)**(5.0/3.0)*1.0*10**-(20.0/3.0),linewidth=2,linestyle='--',label='5/3-slope')
#plt.fill_between(wavebin,wavemean,wavepow24) 
#plt.fill_between(wavebin, wavepow24, wavemean, where=wavemean >= wavepow24,
#                 facecolor='green', interpolate=True)
#plt.fill_between(wavebin, wavepow24, wavemean, where=wavemean <= wavepow24,
#                 facecolor='red', interpolate=True)
plt.legend()
    