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
from scipy import interpolate


plt.rcParams.update({'font.size': 15})

plt.figure(figsize=(10,10))
x=np.linspace(8.,60.,200)
Hours=23
dx=625.0
zpx=512.0
dt=74.0
zpt=1024
Q=int(zpt/2.-zpt/int(3600.0/dt)) - int(zpt/2.-zpt/int(480.0/dt))+1
perbin=np.zeros(Q)
perpow=np.zeros((np.size(perbin),Hours))
perpow3=np.zeros(np.size(perbin))

permean=np.zeros(np.size(perbin))

for k in range(0,Hours-1):
    FILE='C:\Users\Kenneth\Desktop\MCM_AMTM_2017\Jun17-18\BandOH1hr\BandOH'
    
    path=FILE+str(k)+'_WN_'
    files=glob.glob(path+'*.csv')
    files=natsorted(files)
    

    a=128
    data1=np.zeros((a,a+1,np.size(files)))
    data=np.zeros((a,a+1))
    x1=np.zeros(np.size(files))
    y1=np.zeros(np.size(files))
    

    
    for i in range(0,np.size(files)-1):
    
        data2 = pd.read_csv(files[i])
        data1[:,:,i]=data2.values
        p=i
        bins=int(np.rint(p))-1
        perpow[bins,k]=np.log10(np.sum(10**data1[:,:,i])/((dt*zpt*(zpx*dx)))+10**perpow[bins,k])
    for j in range (0,Q,1):
        perbin[j]=1.0/((1.0/(8*60.0))-((j*1.0)/(dt*zpt)))/60.0
        
    perpow3=perpow[:,k]

    f=interpolate.interp1d(perbin,perpow3,kind='linear')
    
    plt.plot(x,f(x)/((x)**(1)*10**(-5)),linewidth=0.5)  
    plt.title('MCM AMTM BandOH Jun16-17 1hr sets')
    plt.xlabel('Period (min)')
    plt.ylabel('Power (1/min)')
#    plt.loglog(perbin,(perbin)**(-1)*10**-0.5,label='5/3-power')
#    plt.loglog(perbin,(perbin)**(-0.5)*10**-1,label='3/1-power')

for j in range (0,Q,1):
    permean[j]=np.average(perpow[j,:])

f3=interpolate.interp1d(perbin,permean,kind='linear')

plt.plot(x,f3(x)/((x)**(1)*10**(-5)),label='AMTM-mean',linewidth=3)  




#path='C:\Users\Kenneth\Desktop\AMTM-ASI_24hr-18-19\ASI_18-19_WN_'
#path='C:\Users\Kenneth\Desktop\Analysis24hr\AMTM_BandOH_WN_'
#
#files=glob.glob(path+'*.csv')
#files=natsorted(files)
#
#dx=625.0
#zpx=512.0
#dt=74.0
#zpt=2.0**11
#a=128
#data1=np.zeros((a,a+1,np.size(files)))
#data=np.zeros((a,a+1))
#x1=np.zeros(np.size(files))
#y1=np.zeros(np.size(files))
#
#perbin=np.zeros(Q)
#perpow24=np.zeros(np.size(perbin))
#
#for i in range(0,np.size(files)-1):
#
#    data2 = pd.read_csv(files[i])
#    data1[:,:,i]=data2.values
#    p=i/10.0
#    bins=int(np.rint(p))-1
#    perpow24[bins]=np.log10(600.0*np.sum(10**data1[:,:,i])/((dt*zpt)**2)+10**perpow24[bins])
#for j in range (0,Q,1):
#    perbin[j]=1.0/(1.0/(8*60.0)-(j*10.0)/(dt*zpt))/60.0
#
#f2=interpolate.interp1d(perbin,perpow24,kind='linear')
#
#
#plt.loglog(x,f2(x),label='AMTM-24hr',linewidth=3)
#plt.scatter(perbin,perpow) 


#plt.loglog(x,(x)**(1)*10**(-5),linewidth=2,linestyle='--',label='1-slope')
#plt.loglog(x,(x)**(2)*10**(-12.0/3.0),linewidth=2,linestyle='--',label='2-slope')
#
#
##plt.fill_between(perbin,perpow,permean) 
#plt.fill_between(x, f2(x), f3(x), where=f3(x) >= f2(x),
#                 facecolor='green', interpolate=True)
#plt.fill_between(x, f2(x), f3(x), where=f3(x) <= f2(x),
#                 facecolor='red', interpolate=True)
#plt.legend()
plt.xlim(8,60) 

#
#plt.figure(figsize=(10,8))
#plt.title('Period AMTM Power Ratio Avg/24hr')
#plt.xlabel('Wavelegnth (km)')
#plt.ylabel('Power Ratio')
#plt.semilogx(x,f3(x)/f2(x))
#plt.savefig(FILE+str(k)+'Period.jpg')