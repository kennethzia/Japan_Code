# -*- coding: utf-8 -*-
"""
Created on Wed Nov 07 14:45:39 2018

@author: Kenneth
"""



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted


plt.rcParams.update({'font.size': 15})

plt.figure(figsize=(10,8))

perbin=np.zeros(30)
perpow=np.zeros((np.size(perbin),8))
permean=np.zeros(np.size(perbin))

for k in range(0,8):
    FILE='C:\Users\Kenneth\Desktop\AMTM-ASI-3hr-18-19\ASI'
    
    path=FILE+str(k)+'_WN_'
    files=glob.glob(path+'*.csv')
    files=natsorted(files)
    
    dx=1000.0
    zpx=512.0
    dt=70.0
    zpt=2.0**11
    a=204
    data1=np.zeros((a,a+1,np.size(files)))
    data=np.zeros((a,a+1))
    x1=np.zeros(np.size(files))
    y1=np.zeros(np.size(files))
    
    
    for i in range(0,np.size(files)-1):
    
        data2 = pd.read_csv(files[i])
        data1[:,:,i]=data2.values
        x=i/10
        bins=int(np.rint(x))-1
        perpow[bins,k]=np.log10(600.0*np.sum(10**data1[:,:,i])/((dt*zpt)**2)+10**perpow[bins,k])
    for j in range (0,30,1):
        perbin[j]=1.0/(1.0/(8*60.0)-(j*10.0)/(dt*zpt))/60.0
        
    
    
    plt.loglog(perbin,perpow[:,k],linewidth=0.5)  
    plt.title('Period Analysis ASI (Jun18-19)')
    plt.xlabel('Period (min)')
    plt.ylabel('Power (1/min)')
#    plt.loglog(perbin,(perbin)**(-1)*10**-0.5,label='5/3-power')
#    plt.loglog(perbin,(perbin)**(-0.5)*10**-1,label='3/1-power')

for j in range (0,30,1):
    permean[j]=np.average(perpow[j,:])


plt.loglog(perbin,permean,label='ASI-mean',linewidth=3)  




path='C:\Users\Kenneth\Desktop\post-data\ASI_18-19_WN_'
files=glob.glob(path+'*.csv')
files=natsorted(files)

dx=1000.0
zpx=512.0
dt=70.0
zpt=2.0**11
a=204
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
for j in range (0,30,1):
    perbin[j]=1.0/(1.0/(8*60.0)-(j*10.0)/(dt*zpt))/60.0

    
plt.loglog(perbin,perpow,label='ASI-24hr',linewidth=3)
plt.scatter(perbin,perpow) 
plt.loglog(perbin,(perbin)**(1)*10**(-17.0/5.0),linewidth=2,linestyle='--',label='1-slope')
plt.loglog(perbin,(perbin)**(2)*10**(-13.0/3.0),linewidth=2,linestyle='--',label='2-slope')


#plt.fill_between(perbin,perpow,permean) 
#plt.fill_between(perbin, perpow, permean, where=permean >= perpow,
#                 facecolor='green', interpolate=True)
#plt.fill_between(perbin, perpow, permean, where=permean <= perpow,
#                 facecolor='red', interpolate=True)
plt.legend()
plt.xlim(60,8) 
#plt.savefig(FILE+str(k)+'Period.jpg')