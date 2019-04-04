# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:20:14 2019

@author: Kenneth
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted
from scipy import interpolate


m=(r'\Jun26-27',r'\Jun27-28',r'\Jun28-29',r'\Jun29-30',r'\Jun30-01')

perpath=r'C:\Users\Kenneth\Desktop\MCM_AMTM_2017'

patha=perpath+m[0]+r'\BandOH1hr\BandOH*_TOTAL'
filesa=glob.glob(patha+'.csv')
filesa=natsorted(filesa)

pathb=perpath+m[1]+r'\BandOH1hr\BandOH*_TOTAL'
filesb=glob.glob(pathb+'.csv')
filesb=natsorted(filesb) 

pathc=perpath+m[2]+r'\BandOH1hr\BandOH*_TOTAL'
filesc=glob.glob(pathc+'.csv')
filesc=natsorted(filesc)

pathd=perpath+m[3]+r'\BandOH1hr\BandOH*_TOTAL'
filesd=glob.glob(pathd+'.csv')
filesd=natsorted(filesd)

pathe=perpath+m[4]+r'\BandOH1hr\BandOH*_TOTAL'
filese=glob.glob(pathe+'.csv')
filese=natsorted(filese)

a=128

dx=625.0
dy=dx
zpx=512.0
dt=74.0
zpt=2.0**11
Q=int(zpt/2.-zpt/int(3600.0/dt)) - int(zpt/2.-zpt/int(480.0/dt))+1


x=np.linspace(6.,80.,300)

plt.rcParams.update({'font.size': 20})
Hours=np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)+np.size(filese)
x5=np.linspace(0,Hours-1,400)
x6=np.linspace(0,Hours-1,400)

wavebin=np.zeros(Q)
wavebin2=np.zeros(Q)
wavepow=np.zeros((np.size(wavebin),Hours))
wavepow2=np.zeros((np.size(wavebin),Hours))
wavepow3=np.zeros(np.size(wavebin))
wavepow4=np.zeros((np.size(x),Hours))
wavepow5=np.zeros((np.size(x),np.size(x5)))

wavemean=np.zeros(np.size(wavebin))

waveTOT=np.zeros((np.size(x),np.size(x5)*2))
for n in range(0,5):
    pathq=r'C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[n]+'\BandOH1hr\BandOH*TOTAL'
    filesq=glob.glob(pathq+'.csv')
    filesq=natsorted(filesq)
    for k in range(0,np.size(filesq)):
        FILE=r'C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[n]+'\BandOH1hr\BandOH'+np.str(k)
        
        path=FILE+r'_WN_'
        files=glob.glob(path+r'*.csv')
        files=natsorted(files)
        if n ==1 :
            k=k+np.size(filesq)
        if n==2:
            k=k+np.size(filesa)+np.size(filesb)
        if n==3:
            k=k+np.size(filesa)+np.size(filesb)+np.size(filesc)
        if n==4:
            k=k+np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)
        
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
                if 1.0/((r*1.0)/(dx*zpx))/1000.0 <=80:
                    wavepow[bins,k]=np.log10(np.sum(10**data9[i,ii,:])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**wavepow[bins,k])
        for j in range (1,103):
            wavebin[j]=1.0/((j*1.0)/(dx*zpx))/1000.0
        wavepow3=wavepow[:,k]
        f=interpolate.interp1d(wavebin,wavepow3,kind='linear')
        wavepow4[:,k]=f(x)/((x)**(3.0)*1.0*10**-6)
        #plt.loglog(x,f(x)/((x)**(3.0)*1.0*10**-6),linewidth=0.5)  
    
plt.figure(figsize=(10,10))
x2=np.arange(0,Hours)
#wavepow4=np.flip(wavepow4[:,:],1)
#wavepow4=np.delete(wavepow4[:,:], 0, 1)
#wavepow4=np.flip(wavepow4[:,:],1)
for z in range(0,np.size(x)):
    f=interpolate.interp1d(x2,wavepow4[z,:],kind='linear')
    wavepow5[z,:]=f(x5)
wavepow5=np.log10(wavepow5)



plt.pcolormesh(x5,x,wavepow5[:,:],cmap='jet',vmin=np.min(wavepow5),vmax=np.max(wavepow5))
#ax2.plot(time,T,label='Intensity',color='r',linestyle='--')
#plt.title('MCM AMTM BandOH Wavelength Spectrum Jun17-18')
plt.xticks(np.arange(0,Hours-1,8))
plt.xlabel('Hours of Observation')
plt.ylabel('Wavelength [km]')
plt.colorbar(label='log$_{10}$(Power)')


#ax1=plt.gca()
#ax2=ax1.twinx()
#plt.title('Wavelength Power Spectrum with Intensity')
#ax2.plot(I,label='Intensity',color='r',linestyle='--')
#ax2.set_ylabel(' ')




