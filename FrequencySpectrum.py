# -*- coding: utf-8 -*-
"""
Created on Mon Mar 04 15:24:17 2019

@author: Kenneth
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted
from scipy import interpolate
import itertools as it


#m=(r'\Jun26-27\TempOH2hrsmooth330',r'\Jun27-28\TempOH2hrsmooth330',r'\Jun28-29\TempOH2hrsmooth330',r'\Jun29-30\TempOH2hrsmooth330',r'\Jun30-01\TempOH2hrsmooth330')
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

Q=int(zpt/2.-zpt/int(3600.0/dt)) - int(zpt/2.-zpt/int(5*60.0/dt))+1
QW=int(zpx/2.-zpx/int(100000.0/dx)) - int(zpx/2.-zpx/int(10000.0/dx))+2

x=np.linspace(5.05,60.,1000)

plt.rcParams.update({'font.size': 20})
x5=np.linspace(0,Hours-1,1000)
x6=np.linspace(0,Hours-1,1000)



perbin=np.zeros(Q)
perbin2=np.zeros(Q)
perpow=np.zeros((np.size(perbin),Hours))
perpow2=np.zeros((np.size(perbin),Hours))
perpow3=np.zeros(np.size(perbin))
perpow4=np.zeros((np.size(x),Hours))
perpow5=np.zeros((np.size(x),np.size(x5)))
Pow2 = np.zeros(Hours)
tie = np.zeros(Hours)

wavemean=np.zeros(np.size(perbin))

waveTOT=np.zeros((np.size(x),np.size(x5)*2))
#for n in range(0,5):
n=0
pathq=perpath+phase+'\TempOH*_PS'
filesq=glob.glob(pathq+'.csv')
filesq=natsorted(filesq)
for k in range(0,np.size(filesq)):
    FILE=perpath+phase+'\TempOH'+np.str(k)
 
    path=FILE+'_WN_'
    files=glob.glob(path+'*.csv')
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
    
    print(k,n)
    
    data9=np.zeros((a,a+1,np.size(files)))
    data10=np.zeros((a,a+1,np.size(files)))

    
    for i in range(0,np.size(files)-1):
    
        data2 = pd.read_csv(files[i])
        data9[:,:,i]=data2.values
        
        
        
        b=a/2    
        for j in range(0,a):
            for ii in range(0,a+1):
                r=np.sqrt((i-b)**2+(ii-b)**2)
                p=r/1.0
                bins=int(np.ceil(p))
                if r>=3.0 or r<=b:
                    data10[j,ii,i]=data9[j,ii,i]
        perpow[i,k]=(np.sum(10**data10[:,:,i])/((zpx*dx)**2)+perpow[i,k])
    for j in range (0,np.size(files)-1):
        perbin[j]=(dt/(0.5-(308+j)/2**10))/60.0
    perpow3=perpow[:,k]
    f=interpolate.interp1d(perbin,perpow3,kind='linear')
    perpow4[:,k]=f(x)
    
    siz = data9.shape
    Pow2[k] = np.log10(np.sum(10**data9)*float(siz[2]*siz[0]*siz[1])/(zpt*dt*(zpx*dx)**2))

x2=np.arange(0,Hours)
for z in range(0,np.size(x)):
    f=interpolate.interp1d(x2,perpow4[z,:],kind='linear')
    perpow5[z,:]=f(x5)
perpow4 = np.log10(perpow4)


plt.figure(figsize=(10,10))
plt.pcolormesh(x5/2+1,x,np.log10(perpow5[:,:]),cmap='jet',vmin=np.min(np.log10(perpow5[:,:])),vmax=np.max(np.log10(perpow5[:,:])))
plt.xlabel('Hours of Observation')
plt.ylabel('Period [min]')
plt.colorbar(label='log$_{10}$(Power)')

plt.savefig(r'E:\PFRR\RESULTS\December'+date+phase+'\FrequencyPow.jpg')



#plt.figure(figsize=(10,10))
#plt.plot(tie,10**Pow2,marker='x')


