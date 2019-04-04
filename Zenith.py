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


m=('\Jun26-27','\Jun27-28','\Jun28-29','\Jun29-30','\Jun30-01')
perpath='F:\MCM AMTM 2017'

patha=perpath+m[0]+'\Processed\BandOH_caun****'
filesa=glob.glob(patha+'.tif')
filesa=natsorted(filesa)

pathb=perpath+m[1]+'\Processed\BandOH_caun****'
filesb=glob.glob(pathb+'.tif')
filesb=natsorted(filesb) 

pathe=perpath+m[2]+'\Processed\BandOH_caun****'
filese=glob.glob(pathe+'.tif')
filese=natsorted(filese)

pathg=perpath+m[3]+'\Processed\BandOH_caun****'
filesg=glob.glob(pathg+'.tif')
filesg=natsorted(filesg)

pathi=perpath+m[4]+'\Processed\BandOH_caun****'
filesi=glob.glob(pathi+'.tif')
filesi=natsorted(filesi)


pathc=perpath+m[0]+'\Processed\TempOH_caun****'
filesc=glob.glob(pathc+'.tif')
filesc=natsorted(filesc)

pathd=perpath+m[1]+'\Processed\TempOH_caun****'
filesd=glob.glob(pathd+'.tif')
filesd=natsorted(filesd)

pathf=perpath+m[2]+'\Processed\TempOH_caun****'
filesf=glob.glob(pathf+'.tif')
filesf=natsorted(filesf)

pathh=perpath+m[3]+'\Processed\TempOH_caun****'
filesh=glob.glob(pathh+'.tif')
filesh=natsorted(filesh)

pathj=perpath+m[4]+'\Processed\TempOH_caun****'
filesj=glob.glob(pathj+'.tif')
filesj=natsorted(filesj)

Hours=np.size(filesa)+np.size(filesb)+np.size(filese)+np.size(filesg)+np.size(filesi)

I=np.zeros(Hours)
T=np.zeros(Hours)
time=np.zeros(Hours)





for p in range(0,Hours):
    if p <= (np.size(filesa)-1):
        a=plt.imread(filesa[0])
        a1=a.shape
        data=np.zeros((a1[0],a1[1]))
        b=plt.imread(filesc[0])
        b1=a.shape
        data2=np.zeros((b1[0],b1[1]))#,b1[1],Hours))
        data[:,:] = plt.imread(filesa[p])
        data2[:,:] = plt.imread(filesc[p])

    
    if p > (np.size(filesa)-1) and p <= (np.size(filesa)+np.size(filesb)-1):
        a=plt.imread(filesb[0])
        a1=a.shape
        data=np.zeros((a1[0],a1[1]))
        b=plt.imread(filesd[0])
        b1=a.shape
        data2=np.zeros((b1[0],b1[1]))#,b1[1],Hours))
        
        pp=p-np.size(filesa)
        data[:,:] = plt.imread(filesb[pp])
        data2[:,:] = plt.imread(filesd[pp])


    if p > (np.size(filesa)+np.size(filesb)-1) and p<= (np.size(filesa)+np.size(filesb)+np.size(filese)-1):
        a=plt.imread(filese[0])
        a1=a.shape
        data=np.zeros((a1[0],a1[1]))
        b=plt.imread(filesf[0])
        b1=a.shape
        data2=np.zeros((b1[0],b1[1]))#,b1[1],Hours))
        pp=p-(np.size(filesa)+np.size(filesb))
        data[:,:] = plt.imread(filese[pp])
        data2[:,:] = plt.imread(filesf[pp])
        
    if p > (np.size(filesa)+np.size(filesb)+np.size(filese)-1) and p<=(np.size(filesa)+np.size(filesb)+np.size(filese)+np.size(filesg)-1):
        a=plt.imread(filesg[0])
        a1=a.shape
        data=np.zeros((a1[0],a1[1]))
        b=plt.imread(filesh[0])
        b1=a.shape
        data2=np.zeros((b1[0],b1[1]))#,b1[1],Hours))
        pp=p-(np.size(filesa)+np.size(filesb)+np.size(filese))
        data[:,:] = plt.imread(filesg[pp])
        data2[:,:] = plt.imread(filesh[pp])
        
    if p > (np.size(filesa)+np.size(filesb)+np.size(filese)+np.size(filesg)-1):
        a=plt.imread(filesi[0])
        a1=a.shape
        data=np.zeros((a1[0],a1[1]))
        b=plt.imread(filesj[0])
        b1=a.shape
        data2=np.zeros((b1[0],b1[1]))#,b1[1],Hours))
        pp=p-(np.size(filesa)+np.size(filesb)+np.size(filese)+np.size(filesg))
        data[:,:] = plt.imread(filesi[pp])
        data2[:,:] = plt.imread(filesj[pp])


    I[p]=np.mean(data[int(a1[0]/2)-2:int(a1[0]/2)+2,int(a1[1]/2)-2:int(a1[1]/2)+2])
    T[p]=np.mean(data2[int(a1[0]/2)-2:int(a1[0]/2)+2,int(a1[1]/2)-2:int(a1[1]/2)+2])

    time[p]=p*37.0/3600.0
    

plt.figure(figsize=(10,10))
ax1=plt.gca()
ax2=ax1.twinx()
ax1.plot(time,I,label='I-Prime',color='b')
ax1.set_ylabel('Intensity',color='b')
ax2.plot(time,T/100.0,label='Intensity',color='k')
ax2.set_ylabel('Temperature (K)',color='k')
plt.title('MCM Jun26-30 Temperature and Intesnity Variation')
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






