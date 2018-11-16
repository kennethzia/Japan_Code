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
from scipy import interpolate

plt.rcParams.update({'font.size': 15})




path='C:\Users\Kenneth\Desktop\AMTM-ASI_24hr-18-19\AMTM_BandOH_18-19_WN_'
files=glob.glob(path+'*.csv')
files=natsorted(files)

a=128
Q=150
dx=625.0
dy=625.0
zpx=512.0
dt=74.0
zpt=2.0**11
data9=np.zeros((a,a+1,np.size(files)))
wavebin=np.zeros(Q)
wavepow=np.zeros(np.size(wavebin))

for i in range(0,np.size(files)):

    data2 = pd.read_csv(files[i])
    data9[:,:,i]=data2.values

b=a/2    
for i in range(0,a):
    for ii in range(0,a+1):
        r=np.sqrt((i-b)**2+(ii-b)**2)
        p=r/1.0
        bins=int(np.ceil(p))
        if bins <=Q-1:
            wavepow[bins]=np.log10(np.sum(10**data9[i,ii,:])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**wavepow[bins])
    for j in range (1,Q):
        wavebin[j]=1.0/((j*1.0)/(dx*zpx))/1000.0



a=204
dx=1000.0
dy=1000.0
zpx=512.0
dt=70.0
zpt=2048.0
Q=180
path='C:\Users\Kenneth\Desktop\AMTM-ASI_24hr-18-19\ASI_18-19_WN_'
files=glob.glob(path+'*.csv')
files=natsorted(files)
data1=np.zeros((a,a+1,np.size(files)))
wavebin2=np.zeros(Q)
wavepow2=np.zeros(np.size(wavebin2))



for i in range(0,np.size(files)-1):

    data2 = pd.read_csv(files[i])
    data1[:,:,i]=data2.values
b=a/2    
for i in range(0,a):
    for ii in range(0,a+1):
        r=np.sqrt((i-b)**2+(ii-b)**2)
        p=r/1.0
        bins=int(np.rint(p))
        if bins <=Q-1:
            wavepow2[bins]=np.log10(np.sum(10**data1[i,ii,:])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**wavepow2[bins])

    for j in range (1,Q):
        wavebin2[j]=1.0/((j*1.0)/(dx*zpx))/1000.0


x=np.linspace(6.,320.,300)
f=interpolate.interp1d(wavebin,wavepow,kind='linear')
f2=interpolate.interp1d(wavebin2,wavepow2,kind='linear')


plt.figure() 
plt.xlim(320,1)   
plt.loglog(x,f(x),label='AMTM-BandOH')  
plt.loglog(x,f2(x),label='ASI')  

plt.title('Wavelength Analysis (June 18-19)')
plt.xlabel('Wavelegnth (km)')
plt.ylabel('Power (1/km)')
#plt.loglog(wavebin,(wavebin)**(3.0)*1.0*10**-6,label='3-power')
#plt.loglog(wavebin,(wavebin)**(5.0/3.0)*1.0*10**-6,label='5/3-power')
plt.legend()
    


    
