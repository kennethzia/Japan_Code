# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 15:45:20 2018

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
    FILE='C:\Users\Kenneth\Desktop\AMTM-ASI-3hr-18-19\AMTM'
    
    path=FILE+str(k)+'_WN_'
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
    

    
    for i in range(0,np.size(files)-1):
    
        data2 = pd.read_csv(files[i])
        data1[:,:,i]=data2.values
        x=i/10
        bins=int(np.rint(x))-1
        perpow[bins,k]=np.log10(600.0*np.sum(10**data1[:,:,i])/((dt*zpt)**2)+10**perpow[bins,k])
    for j in range (0,30,1):
        perbin[j]=1.0/(1.0/(8*60.0)-(j*10.0)/(dt*zpt))/60.0
        
    
    
    plt.loglog(perbin,perpow[:,k],linewidth=0.5)  
    plt.xlim(60,1)
    plt.title('Period Analysis AMTM-BandOH (Jun18-19)')
    plt.xlabel('Period (min)')
    plt.ylabel('Power (1/min)')
#    plt.loglog(perbin,(perbin)**(-1)*10**-0.5,label='5/3-power')
#    plt.loglog(perbin,(perbin)**(-0.5)*10**-1,label='3/1-power')

for j in range (0,30,1):
    permean[j]=np.average(perpow[j,:])


plt.loglog(perbin,permean,label='AMTM-BandOH-mean',linewidth=3)  




path='C:\Users\Kenneth\Desktop\AMTM-ASI_24hr-18-19\AMTM_BandOH_18-19_WN_'
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
for j in range (0,30,1):
    perbin[j]=1.0/(1.0/(8*60.0)-(j*10.0)/(dt*zpt))/60.0

    
#
plt.loglog(perbin,perpow,label='AMTM-BandOH-24hr',linewidth=3)
plt.scatter(perbin,perpow) 
plt.loglog(perbin,(perbin)**(1)*10**(-11.0/4.0),linewidth=2,linestyle='--',label='1-slope')
plt.loglog(perbin,(perbin)**(2)*10**(-11.0/3.0),linewidth=2,linestyle='--',label='2-slope')


#plt.fill_between(perbin,perpow,permean) 
#plt.fill_between(perbin, perpow, permean, where=permean >= perpow,
#                 facecolor='green', interpolate=True)
#plt.fill_between(perbin, perpow, permean, where=permean <= perpow,
#                 facecolor='red', interpolate=True)
plt.legend()
plt.xlim(60,8) 

#plt.savefig(FILE+str(k)+'Period.jpg')