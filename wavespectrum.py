# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:10:20 2019

@author: Kenneth
"""





import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted
from scipy import interpolate


plt.rcParams.update({'font.size': 15})

x=np.linspace(8.,60.,200)
Hours=23
dx=625.0
zpx=512.0
dt=74.0
zpt=1024
Q=int(zpt/2.-zpt/int(3600.0/dt)) - int(zpt/2.-zpt/int(480.0/dt))+1
perbin=np.zeros(Q)
perpow=np.zeros((np.size(perbin),Hours))
perpow3=np.zeros(np.size(perbin))
perpow4=np.zeros((np.size(x),Hours))

permean=np.zeros(np.size(perbin))

for k in range(0,Hours-1):
    FILE='C:\Users\Kenneth\Desktop\MCM_AMTM_2017\Jun17-18\BandOH1hr\BandOH'
    
    path=FILE+str(k)+'_WN_'
    files=glob.glob(path+'*.csv')
    files=natsorted(files)
    

    a=128
    data1=np.zeros((a,a+1,np.size(files)))
    data=np.zeros((a,a+1))
    x1=np.zeros(np.size(files))
    y1=np.zeros(np.size(files))
    

    
    for i in range(0,np.size(files)-1):
    
        data2 = pd.read_csv(files[i])
        data1[:,:,i]=data2.values
        p=i
        bins=int(np.rint(p))-1
        perpow[bins,k]=np.log10(np.sum(10**data1[:,:,i])/((dt*zpt*(zpx*dx)))+10**perpow[bins,k])
    for j in range (0,Q,1):
        perbin[j]=1.0/((1.0/(8*60.0))-((j*1.0)/(dt*zpt)))/60.0
        
    perpow3=perpow[:,k]
    f=interpolate.interp1d(perbin,perpow3,kind='linear')
    perpow4[:,k]=f(x)
    

plt.figure(figsize=(10,8))

x2=np.arange(0,23)
perpow4=np.flip(perpow4[:,:],1)
perpow4=np.delete(perpow4[:,:], 0, 1)
plt.pcolormesh(x2,x,np.log10(perpow4[:,:]),cmap='jet',vmin=-6.0,vmax=-3.0)

plt.title('MCM AMTM BandOH Period Spectrum')

plt.xlabel('Hours of Observation')
plt.ylabel('Period [min]')
plt.colorbar(label='log$_{10}$(PSD) [min$^-1$]')



