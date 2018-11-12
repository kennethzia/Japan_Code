# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:20:39 2018

@author: Kenneth
Period ANALYSIS
"""



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted


plt.rcParams.update({'font.size': 15})




path='C:\Users\Kenneth\Desktop\post-data\AMTM_BandOH_WN_'
files=glob.glob(path+'*.csv')
files=natsorted(files)

dx=625.0
zpx=512.0
dt=74.0
zpt=2.0**11
a=128
data1=np.zeros((a,a+1,np.size(files)))
data=np.zeros((a,a+1))
x1=np.zeros(np.size(files))
y1=np.zeros(np.size(files))

perbin=np.zeros(30)
perpow=np.zeros(np.size(perbin))

for i in range(0,np.size(files)-1):

    data2 = pd.read_csv(files[i])
    data1[:,:,i]=data2.values
    x=i/10
    bins=int(np.rint(x))-1
    perpow[bins]=np.log10(600.0*np.sum(10**data1[:,:,i])/((dt*zpt)**2)+10**perpow[bins])
for j in range (0,25,1):
    perbin[j]=1.0/(1.0/(3600.0)+(j*10.0)/(dt*zpt))/60.0
    

path='C:\Users\Kenneth\Desktop\post-data\ASI_WN_'
files=glob.glob(path+'*.csv')
files=natsorted(files)

dx=1000.0
zpx=512.0
dt=70.0
zpt=2048.0
a=204

data9=np.zeros((a,a+1,np.size(files)))
data=np.zeros((a,a+1))
x1=np.zeros(np.size(files))
y1=np.zeros(np.size(files))

perbin2=np.zeros(40)
perpow2=np.zeros(np.size(perbin2))

for i in range(0,np.size(files)-1):

    data2 = pd.read_csv(files[i])
    data9[:,:,i]=data2.values
    x=i/10
    bins=int(np.rint(x))
    perpow2[bins]=np.log10(600.0*np.sum(10**data9[:,:,i])/((dt*zpt)**2)+10**perpow[bins])
for j in range (0,25,1):
    perbin2[j]=1.0/(1.0/(3600.0)+(j*10.0)/(dt*zpt))/60.0
    
    
#

plt.figure() 
plt.loglog(perbin,perpow,label='AMTM-BandOH')  
plt.loglog(perbin2,perpow2,label='ASI')  
plt.xlim(60,1)
plt.title('Wave Period Analysis')
plt.xlabel('Period (min)')
plt.ylabel('Power (1/min)')
#plt.loglog(perbin,(perbin)**(1)*10**-4,label='5/3-power')
#plt.loglog(perbin,(perbin)**(2)*1.0*10**-3,label='3/1-power')
plt.legend()
    
