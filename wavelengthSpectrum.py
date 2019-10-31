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


#m=(r'\Jun26-27',r'\Jun27-28',r'\Jun28-29',r'\Jun29-30',r'\Jun30-01')
#
#perpath=r'C:\Users\Kenneth\Desktop\MCM_AMTM_2017'
m=(r'\SSTempOH2hr',r'\Jun27-28\TempOH2hrsmooth330',r'\Jun28-29\TempOH2hrsmooth330',r'\Jun29-30\TempOH2hrsmooth330',r'\Jun30-01\TempOH2hrsmooth330')

date=r'\Dec23-24'
phase=r''


#perpath=r'C:\Users\Kenneth\Desktop'
perpath = r'E:\PFRR\RESULTS\December'+date+r'\Results'

patha=perpath+phase+'\TempOH*_TOTAL'
filesa=glob.glob(patha+'.csv')
filesa=natsorted(filesa)



#pathb=perpath+m[1]+r'\TempOH*_PS'
#filesb=glob.glob(pathb+'.csv')
#filesb=natsorted(filesb) 
#
#pathc=perpath+m[2]+r'\TempOH*_PS'
#filesc=glob.glob(pathc+'.csv')
#filesc=natsorted(filesc)
#
#pathd=perpath+m[3]+r'\TempOH*_PS'
#filesd=glob.glob(pathd+'.csv')
#filesd=natsorted(filesd)
#
#pathe=perpath+m[4]+r'\TempOH*_PS'
#filese=glob.glob(pathe+'.csv')
#filese=natsorted(filese)

#Hours=np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)+np.size(filese)
Hours=np.size(filesa)

dx=625.0
zpx=512.0
dt=60.0
zpt=2.0**10
#a=128
a=64

Q=int(zpx/2.-zpx/int(100000.0/dx)) - int(zpx/2.-zpx/int(10000.0/dx))+2

b=int(a/2)

x=np.linspace(10.,100.,1000)

plt.rcParams.update({'font.size': 20})
x5=np.linspace(0,Hours-1,1000)
x6=np.linspace(0,Hours-1,1000)
tie = np.zeros(Hours)

wavebin=np.zeros(b+1)
wavebin2=np.zeros(b+1)
wavepow=np.zeros((np.size(wavebin),Hours))
wavepow2=np.zeros((np.size(wavebin),Hours))
wavepow3=np.zeros(np.size(wavebin))
wavepow4=np.zeros((np.size(x),Hours))
wavepow5=np.zeros((np.size(x),np.size(x5)))

wavemean=np.zeros(np.size(wavebin))

waveTOT=np.zeros((np.size(x),np.size(x5)*2))
#for n in range(0,5):
n=0
pathq=perpath+phase+'\TempOH*_PS'
filesq=glob.glob(pathq+'.csv')
filesq=natsorted(filesq)
for k in range(0,np.size(filesq)):
    FILE=perpath+phase+'\TempOH'+np.str(k)
    
    path=FILE+r'_WN_'
    files=glob.glob(path+r'*.csv')
    files=natsorted(files)
#    if n==0:
    z=k
    tie[z]=k/2+1
#    if n ==1 :
#        k=k+np.size(filesa)
#        z=k
#        tie[z] = k/2 +2
#    if n==2:
#        k=k+np.size(filesa)+np.size(filesb)
#        z=k
#        tie[z] = k/2 +4
#    if n==3:
#        k=k+np.size(filesa)+np.size(filesb)+np.size(filesc)
#        z=k
#        tie[z] = k/2 +6
#    if n==4:
#        k=k+np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)
#        z=k
#        tie[z] = k/2 +8
#    
    data9=np.zeros((a,a+1,np.size(files)))

    
    for i in range(0,np.size(files)):
    
        data2 = pd.read_csv(files[i])
        data9[:,:,i]=data2.values
    

    for i in range(0,a):
        for ii in range(0,a+1):
            r=np.sqrt((i-b)**2+(ii-b)**2)
            p=r/1.0
            bins=int(np.ceil(p))
            
            if r>=3.0 and r<=b:

                wavepow[bins,k]=(np.sum(10**data9[i,ii,:])*r/(zpt*dt*(zpx*dx))+wavepow[bins,k])
    for j in range (0,b):
        wavebin[j]=(1/(((j+0.01)*1.0)/(dx*zpx)))/1000.0
        wavepow3[j]=wavepow[j,k]
    f=interpolate.interp1d(wavebin,wavepow3,kind='linear')
    wavepow4[:,k]=f(x)
    #plt.loglog(x,f(x)/((x)**(3.0)*1.0*10**-6),linewidth=0.5)  
    
    print(n,k)
x2=np.arange(0,Hours)
#wavepow4=np.flip(wavepow4[:,:],1)
#wavepow4=np.delete(wavepow4[:,:], 0, 1)
#wavepow4=np.flip(wavepow4[:,:],1)
for z in range(0,np.size(x)):
    f=interpolate.interp1d(x2,wavepow4[z,:],kind='linear')
    wavepow5[z,:]=f(x5)
#wavepow5=np.log10(wavepow5)


plt.figure(figsize=(10,10))
plt.pcolormesh(x5,x,wavepow5[:,:],cmap='jet',vmin=np.min(wavepow5[:,:]),vmax=np.max(wavepow5[:,:]))
#ax2.plot(time,T,label='Intensity',color='r',linestyle='--')
#plt.title('MCM AMTM BandOH Wavelength Spectrum Jun17-18')

plt.xlabel('Hours of Observation')
plt.ylabel('Wavelength [km]')
plt.colorbar(label='Power')
plt.savefig(r'E:\PFRR\RESULTS\December'+date+phase+'\WavelengthPow.jpg')

#ax1=plt.gca()
#ax2=ax1.twinx()
#plt.title('Wavelength Power Spectrum with Intensity')
#ax2.plot(I,label='Intensity',color='r',linestyle='--')
#ax2.set_ylabel(' ')




