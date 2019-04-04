# -*- coding: utf-8 -*-
"""
Created on Mon Mar 04 20:32:23 2019

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


Hours=np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)+np.size(filese)


x=np.linspace(1,149.,600)

plt.rcParams.update({'font.size': 20})
x5=np.linspace(0,Hours-2,100)
x5=x5
x2=np.arange(0,Hours)
x2=x2
psbin=np.zeros(150)
psbin2=np.zeros(150)
pspow=np.zeros((np.size(psbin),Hours))
pspow2=np.zeros((np.size(psbin),Hours))
pspow3=np.zeros(np.size(psbin))
pspow4=np.zeros((np.size(x),Hours))
pspow5=np.zeros((np.size(x),np.size(x5)))




for k in range(0,Hours-1):
    p=k
    if p <= (np.size(filesa)-1):
        a=pd.read_csv(filesa[0])
        a1=a.shape
        data=np.zeros((a1[0],a1[1]))
        data[:,:] = pd.read_csv(filesa[p])

    
    if p > (np.size(filesa)-1) and p <= (np.size(filesa)+np.size(filesb)-1):
        a=pd.read_csv(filesb[0])
        a1=a.shape
        data=np.zeros((a1[0],a1[1]))
        
        pp=p-np.size(filesa)
        data[:,:] = pd.read_csv(filesb[pp])


    if p > (np.size(filesa)+np.size(filesb)-1) and p<= (np.size(filesa)+np.size(filesb)+np.size(filese)-1):
        a=pd.read_csv(filesc[0])
        a1=a.shape
        data=np.zeros((a1[0],a1[1]))
        pp=p-(np.size(filesa)+np.size(filesb))
        data[:,:] = pd.read_csv(filesc[pp])
        
    if p > (np.size(filesa)+np.size(filesb)+np.size(filesc)-1) and p<=(np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)-1):
        a=pd.read_csv(filesd[0])
        a1=a.shape
        data=np.zeros((a1[0],a1[1]))
        pp=p-(np.size(filesa)+np.size(filesb)+np.size(filesc))
        data[:,:] = pd.read_csv(filesd[pp])
        
    if p > (np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)-1):
        a=pd.read_csv(filese[0])
        a1=a.shape
        data=np.zeros((a1[0],a1[1]))
        pp=p-(np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd))
        data[:,:] = pd.read_csv(filese[pp])

    a=300
    

    data9=np.zeros((a,a+1))


    
    b=a/2    
    for i in range(0,a):
        for ii in range(0,a+1):
            r=np.sqrt((i-b)**2+(ii-b)**2)
            p=r/1.0
            if r<149.0:
                bins=int(np.ceil(p))
                pspow[bins,k]=np.log10(np.sum(10**data[i,ii])+10**pspow[bins,k])
    psbin[:]=np.arange(0,150,1)
    pspow3=pspow[:,k]
    f=interpolate.interp1d(psbin,pspow3,kind='linear')
    pspow4[:,k]=f(x)/((x)**(3.0)*1.0*10**-6)
    #plt.loglog(x,f(x)/((x)**(3.0)*1.0*10**-6),linewidth=0.5)  

plt.figure(figsize=(10,10))

#pspow4=np.flip(pspow4[:,:],1)
#pspow4=np.delete(pspow4[:,:],(0),axis=0)
#pspow4=np.flip(pspow4[:,:],1)
for z in range(0,599):
    f=interpolate.interp1d(x2,pspow4[z,:],kind='linear')
    pspow5[z,:]=f(x5)
pspow5=np.log10(pspow5+20**(-22))


plt.pcolormesh(x5,x,pspow5[:,:],cmap='jet',vmin=-9,vmax=np.max(pspow5))

#plt.title('MCM AMTM BandOH Wavelength Spectrum Jun17-18')
plt.xticks(np.arange(0,Hours-1,8))
plt.xlabel('Hours of Observation')
plt.ylabel('Phase Speed [m/s]')
plt.colorbar(label='log$_{10}$(Power)')
plt.ylim(2,150)


