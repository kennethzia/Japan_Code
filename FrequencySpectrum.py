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


m=('\Jun17-18','\Jun18-19','Jun19-20')

patha='C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[0]+'\FixedBandOH\BandOH*TOTAL'
#path='C:\Users\Kenneth\Desktop\AMTM-3hr\AMTM*TOTAL'
filesa=glob.glob(patha+'.csv')
filesa=natsorted(filesa)

pathb='C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[1]+'\FixedBandOH\BandOH*TOTAL'
#path='C:\Users\Kenneth\Desktop\AMTM-3hr\AMTM*TOTAL'
filesb=glob.glob(pathb+'.csv')
filesb=natsorted(filesb)

pathc='C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[2]+'\FixedBandOH\BandOH*TOTAL'
#path='C:\Users\Kenneth\Desktop\AMTM-3hr\AMTM*TOTAL'
filesc=glob.glob(pathc+'.csv')
filesc=natsorted(filesc)


dx=625.0
zpx=512.0
dt=74.0
zpt=2.0**10
a=128
Q=int(zpt/2.-zpt/int(3600.0/dt)) - int(zpt/2.-zpt/int(480.0/dt))+1

x=np.linspace(8.,59.,300)

plt.rcParams.update({'font.size': 20})
Hours=np.size(filesa)+np.size(filesb)+np.size(filesc)
x5=np.linspace(0,Hours-1,400)
x6=np.linspace(0,Hours-1,400)

data9=np.zeros((a,a+1,Hours))

perbin=np.zeros(Q)
perbin2=np.zeros(Q)
perpow=np.zeros((np.size(perbin),Hours))
perpow2=np.zeros((np.size(perbin),Hours))
perpow3=np.zeros(np.size(perbin))
perpow4=np.zeros((np.size(x),Hours))
perpow5=np.zeros((np.size(x),np.size(x5)))

wavemean=np.zeros(np.size(perbin))

waveTOT=np.zeros((np.size(x),np.size(x5)*2))
for n in range(0,3):
    pathq='C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[n]+'\FixedBandOH\BandOH*TOTAL'
    filesq=glob.glob(pathq+'.csv')
    filesq=natsorted(filesq)
    for k in range(0,np.size(filesq)):
        FILE='C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[n]+'\FixedBandOH\BandOH'+np.str(k)
        
        path=FILE+'_WN_'
        files=glob.glob(path+'*.csv')
        files=natsorted(files)
        if n ==1:
            k=k+np.size(filesa)
        if n ==2:
            k=k+np.size(filesa)+np.size(filesb)

        a=128
        
        print(k,n)
        
        data9=np.zeros((a,a+1,np.size(files)))
    
        
        for i in range(0,np.size(files)-1):
        
            data2 = pd.read_csv(files[i])
            data9[:,:,i]=data2.values
            
            b=a/2    
            for j in it.chain(range(0,60),range(69,a)):
                for ii in it.chain(range(0,60),range(69,a+1)):
#                    r=np.sqrt((j-b)**2+(ii-b)**2)
#                    t=1.0/((r*1.0)/(dx*zpx))/1000.0
#                    if t>=80.0:
#                        print j,ii
                    perpow[i,k]=np.log10(np.sum(10**data9[j,ii,i])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**perpow[i,k])
        for j in range (0,150):
            perbin[j]=1/((1.0/(8*60.0))-((j*1.0)/(dt*zpt)))/60.0
        perpow3=perpow[:,k]
        f=interpolate.interp1d(perbin,perpow3,kind='linear')
        perpow4[:,k]=f(x)/((x)**(1.0*10**-5))
    
plt.figure(figsize=(10,10))
x2=np.arange(0,Hours)
for z in range(0,299):
    f=interpolate.interp1d(x2,perpow4[z,:],kind='linear')
    perpow5[z,:]=f(x5)
perpow5=np.log10(perpow5)
perpow5=perpow5[0:-1,:]



plt.pcolormesh(x5,x,perpow5[:,:],cmap='jet',vmin=np.min(perpow5),vmax=np.max(perpow5))
#ax2.plot(time,T,label='Intensity',color='r',linestyle='--')
#plt.title('MCM AMTM BandOH Wavelength Spectrum Jun17-18')
plt.xticks(np.arange(0,Hours-1,4))
plt.xlabel('Hours of Observation')
plt.ylabel('Wavelength [km]')
plt.colorbar(label='log$_{10}$(Power)')
