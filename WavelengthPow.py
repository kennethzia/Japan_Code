# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:42:23 2018

Wavelength Power

@author: Kenneth
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted

plt.rcParams.update({'font.size': 15})




path='C:\Users\Kenneth\Desktop\Analysis24hr\AMTM_BandOH_WN_'
files=glob.glob(path+'*.csv')
files=natsorted(files)

a=128

dx=625.0
dy=625.0
zpx=512.0
dt=74.0
zpt=2.0**11
data9=np.zeros((a,a+1,np.size(files)))

wavebin=np.arange(1,201,1)
wavebin2=np.arange(1,201,1)

wavepow=np.zeros(np.size(wavebin))
wavepow2=np.zeros(np.size(wavebin))

#wavelen=np.zeros((128,129))

for i in range(0,np.size(files)-1):

    data2 = pd.read_csv(files[i])
    data9[:,:,i]=data2.values

b=a/2    
for i in range(0,a):
    for ii in range(0,a+1):
        r=np.sqrt((i-b)**2+(ii-b)**2)
        x=r/1.0
        bins=int(np.ceil(x))
        if bins <=48:
            wavepow[bins]=np.log10(np.sum(10**data9[i,ii,:])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**wavepow2[bins])
for j in range (0,200):
    wavebin[j]=1.0/(1.0/(100000.0)+(j*2.0)/(dx*zpx))/1000.0


#a=204
#dx=1000.0
#dy=1000.0
#zpx=512.0
#dt=70.0
#zpt=2048.0
#path='C:\Users\Kenneth\Desktop\post-data\ASI_WN_'
#files=glob.glob(path+'*.csv')
#files=natsorted(files)
#data1=np.zeros((a,a+1,np.size(files)))
#
#for i in range(0,np.size(files)-1):
#
#    data2 = pd.read_csv(files[i])
#    data1[:,:,i]=data2.values
#b=a/2    
#for i in range(0,a):
#    for ii in range(0,a+1):
#        r=np.sqrt((i-b)**2+(ii-b)**2)
#        x=r/1.0
#        bins=int(np.floor(x))
#        if bins <=48:
#            wavepow2[bins]=np.log10(np.sum(10**data1[i,ii,:])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**wavepow2[bins])
#for j in range (0,200):
#    wavebin2[j]=1.0/(1.0/(100000.0)+(j*2.0)/(dx*zpx))/1000.0



plt.figure() 
plt.xlim(100,1)   
plt.loglog(wavebin,wavepow,label='AMTM-BandOH')  
plt.loglog(wavebin2,wavepow2,label='ASI')  

plt.title('Wavelength Analysis')
plt.xlabel('Wavelegnth (km)')
plt.ylabel('Power (1/km)')
#plt.loglog(wavebin,(wavebin)**(3.0)*1.0*10**-6,label='3-power')
#plt.loglog(wavebin,(wavebin)**(5.0/3.0)*1.0*10**-6,label='5/3-power')
plt.legend()
    


    
