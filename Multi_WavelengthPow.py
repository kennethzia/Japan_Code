# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 15:59:56 2018

@author: Kenneth
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted
from scipy import interpolate


plt.rcParams.update({'font.size': 15})
Hours=23
plt.figure(figsize=(10,10))
wavebin=np.zeros(104)
wavebin2=np.zeros(104)
wavepow=np.zeros((np.size(wavebin),Hours))
wavepow2=np.zeros((np.size(wavebin),Hours))
wavepow3=np.zeros(np.size(wavebin))

wavemean=np.zeros(np.size(wavebin))

x=np.linspace(6.,100.,300)

for k in range(0,Hours-1):
    FILE='C:\Users\Kenneth\Desktop\MCM_AMTM_2017\Jun17-18\BandOH1hr\BandOH'+np.str(k)
    
    path=FILE+'_WN_'
    files=glob.glob(path+'*.csv')
    files=natsorted(files)
    
    a=128
    
    dx=625.0
    dy=dx
    zpx=512.0
    dt=74.0
    zpt=2.0**11
    data9=np.zeros((a,a+1,np.size(files)))

    
    for i in range(0,np.size(files)):
    
        data2 = pd.read_csv(files[i])
        data9[:,:,i]=data2.values
    
    b=a/2    
    for i in range(0,a):
        for ii in range(0,a+1):
            r=np.sqrt((i-b)**2+(ii-b)**2)
            p=r/1.0
            bins=int(np.ceil(p))
            if bins <=103:
                wavepow[bins,k]=np.log10(np.sum(10**data9[i,ii,:])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**wavepow[bins,k])
    for j in range (1,103):
        wavebin[j]=1.0/((j*1.0)/(dx*zpx))/1000.0
    wavepow3=wavepow[:,k]
    f=interpolate.interp1d(wavebin,wavepow3,kind='linear')
 
    plt.loglog(x,f(x)/((x)**(3.0)*1.0*10**-6),linewidth=0.5)  

plt.title('MCM AMTM BandOH Jun16-17 1hr sets')
plt.xlabel('Wavelegnth (km)')
plt.ylabel('Power (1/km)')

for i in range (0,np.size(wavebin)):
    wavemean[i]=np.average(wavepow[i,:])

f3=interpolate.interp1d(wavebin,wavemean,kind='linear')

plt.loglog(x,f3(x)/((x)**(3.0)*1.0*10**-6),label='AMTM-mean',linewidth=3)

#plt.loglog(x,(x)**(3.0)*1.0*10**-6,label='Stable Wave 10$^3$',linewidth=3)
plt.legend()
#wavepow24=np.zeros(np.size(wavebin))
#FILE='C:\Users\Kenneth\Desktop\MCM_AMTM_2017\Jun17-18\BandOH_WN_'
#
#files=glob.glob(path+'*.csv')
#files=natsorted(files)
#
#a=128
#
#dx=625.0
#dy=dx
#zpx=512.0
#dt=74.0
#zpt=2.0**11
#data9=np.zeros((a,a+1,np.size(files)))
#
#
#for i in range(0,np.size(files)):
#
#    data2 = pd.read_csv(files[i])
#    data9[:,:,i]=data2.values
#
#b=a/2    
#for i in range(0,a):
#    for ii in range(0,a+1):
#        r=np.sqrt((i-b)**2+(ii-b)**2)
#        p=r/1.0
#        bins=int(np.ceil(p))
#        if bins <=103:
#            wavepow24[bins]=np.log10(np.sum(10**data9[i,ii,:])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**wavepow24[bins])
#
#
#
#f2=interpolate.interp1d(wavebin,wavepow24,kind='linear')
#
# 
#plt.loglog(x,f2(x),label='AMTM-24hr',linewidth=3)  

#plt.loglog(x,(x)**(3.0)*1.0*10**-(13.0/2.0),linewidth=2,linestyle='--',label='3-slope')
#plt.loglog(x,(x)**(5.0/3.0)*1.0*10**-(17.0/3.0),linewidth=2,linestyle='--',label='5/3-slope')
plt.xlim(5,100)
#plt.fill_between(wavebin,wavemean,wavepow24) 
#plt.fill_between(x, f2(x), f3(x), where=f3(x) >= f2(x),
#                 facecolor='green', interpolate=True)
#plt.fill_between(x, f2(x), f3(x), where=f3(x) <= f2(x),
#                 facecolor='red', interpolate=True)
#plt.legend()
#  

    
#plt.figure(figsize=(10,8))
#plt.title('Wavelength AMTM Power Ratio Avg/24hr')
#plt.xlabel('Wavelegnth (km)')
#plt.ylabel('Power Ratio')
#plt.semilogx(x,f3(x)/f2(x))
    
    
    