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

perpath = r'E:\PFRR\RESULTS\November\Nov14-15\Results'

patha=perpath+r'\ATempOH*_TOTAL'
filesa=glob.glob(patha+'.csv')
filesa=natsorted(filesa)

#pathb=perpath+m[1]+r'\TempOH2hrsmooth\TempOH*_PS'
#filesb=glob.glob(pathb+'.csv')
#filesb=natsorted(filesb) 
#
#pathc=perpath+m[2]+r'\TempOH2hrsmooth\TempOH*_PS'
#filesc=glob.glob(pathc+'.csv')
#filesc=natsorted(filesc)
#
#pathd=perpath+m[3]+r'\TempOH2hrsmooth\TempOH*_PS'
#filesd=glob.glob(pathd+'.csv')
#filesd=natsorted(filesd)
#
#pathe=perpath+m[4]+r'\TempOH2hrsmooth\TempOH*_PS'
#filese=glob.glob(pathe+'.csv')
#filese=natsorted(filese)

Hours=np.size(filesa)


x=np.linspace(1,149.,1000)

plt.rcParams.update({'font.size': 20})
x5=np.linspace(0,Hours-2,1000)
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
tie = np.zeros(Hours)



for k in range(0,Hours-1):
    p=k
#    if p <= (np.size(filesa)-1):
    a=pd.read_csv(filesa[0])
    a1=a.shape
    data=np.zeros((a1[0],a1[1]))
    data[:,:] = pd.read_csv(filesa[p])
    tie[k]=k/2+1
    
#    if p > (np.size(filesa)-1) and p <= (np.size(filesa)+np.size(filesb)-1):
#        a=pd.read_csv(filesb[0])
#        a1=a.shape
#        data=np.zeros((a1[0],a1[1]))
#        
#        pp=p-np.size(filesa)
#        data[:,:] = pd.read_csv(filesb[pp])
#        tie[k] = k/2 +2
#
#    if p > (np.size(filesa)+np.size(filesb)-1) and p<= (np.size(filesa)+np.size(filesb)+np.size(filese)-1):
#        a=pd.read_csv(filesc[0])
#        a1=a.shape
#        data=np.zeros((a1[0],a1[1]))
#        pp=p-(np.size(filesa)+np.size(filesb))
#        data[:,:] = pd.read_csv(filesc[pp])
#        tie[k] = k/2 +4
#        
#    if p > (np.size(filesa)+np.size(filesb)+np.size(filesc)-1) and p<=(np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)-1):
#        a=pd.read_csv(filesd[0])
#        a1=a.shape
#        data=np.zeros((a1[0],a1[1]))
#        pp=p-(np.size(filesa)+np.size(filesb)+np.size(filesc))
#        data[:,:] = pd.read_csv(filesd[pp])
#        tie[k] = k/2 +6
#        
#    if p > (np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)-1):
#        a=pd.read_csv(filese[0])
#        a1=a.shape
#        data=np.zeros((a1[0],a1[1]))
#        pp=p-(np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd))
#        data[:,:] = pd.read_csv(filese[pp])
#        tie[k] = k/2 +8

    a=300
    

    data9=np.zeros((a,a+1))


    
    b=a/2    
    for i in range(0,a):
        for ii in range(0,a+1):
            r=np.sqrt((i-b)**2+(ii-b)**2)
            p=r/1.0
            if r<149.0:
                bins=int(np.ceil(p))
                pspow[bins,k]=(np.sum(data[i,ii])+pspow[bins,k])
    psbin[:]=np.arange(0,150,1)
    pspow3=pspow[:,k]
    f=interpolate.interp1d(psbin,pspow3,kind='linear')
    pspow4[:,k]=f(x)
    #plt.loglog(x,f(x)/((x)**(3.0)*1.0*10**-6),linewidth=0.5)  


#for z in range(0,1000):
#    f=interpolate.interp1d(x2,pspow4[z,:],kind='linear')
#    pspow5[z,:]=f(x5)
#pspow4 = np.log10(pspow)


plt.figure(figsize=(10,10))
plt.pcolormesh(tie[:],psbin[:],pspow[:,:],cmap='jet',vmin=np.min(pspow),vmax=np.max(pspow))
plt.xlabel('Hours of Observation')
plt.ylabel('Phase Speed [m/s]')
plt.colorbar(label='$Log_{10}$(Power)')








