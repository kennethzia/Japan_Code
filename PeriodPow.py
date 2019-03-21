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
from scipy import interpolate


plt.rcParams.update({'font.size': 15})




path='C:\Users\Kenneth\Desktop\MCM_AMTM_2017\Jun17-18\BandOHHam\BandOH0_WN_'
files=glob.glob(path+'*.csv')
files=natsorted(files)


x=np.linspace(8.,60.,200)

dx=625.0
zpx=512.0
dt=74.0
zpt=2.0**10
a=128
Q=int(zpt/2.-zpt/int(3600.0/dt)) - int(zpt/2.-zpt/int(480.0/dt))+1

data1=np.zeros((a,a+1,np.size(files)))
data=np.zeros((a,a+1))
x1=np.zeros(np.size(files))
y1=np.zeros(np.size(files))

perbin=np.zeros(Q)
perpow=np.zeros(np.size(perbin))

for i in range(0,np.size(files)-1):

    data2 = pd.read_csv(files[i])
    data1[:,:,i]=data2.values
    b=a/2    
    for j in range(0,a):
        for ii in range(0,a+1):
            r=np.sqrt((j-b)**2+(ii-b)**2)
            if  1.0/((r*1.0)/(dx*zpx))/1000.0 <=80:
                perpow[i]=np.log10(np.sum(10**data1[j,ii,i])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**perpow[i])
for j in range (0,150):
    perbin[j]=1/((1.0/(8*60.0))-((j*1.0)/(dt*zpt)))


#path='E:\JAPAN\Analysis24hr\ASI_WN_'
#files=glob.glob(path+'*.csv')
#files=natsorted(files)
#
#dx=1000.0
#zpx=512.0
#dt=70.0
#zpt=2.0**11
#a=204
#data1=np.zeros((a,a+1,np.size(files)))
#data=np.zeros((a,a+1))
#x1=np.zeros(np.size(files))
#y1=np.zeros(np.size(files))
#
#perbin2=np.zeros(Q)
#perpow2=np.zeros(np.size(perbin2))
#
#for i in range(0,np.size(files)-1):
#
#    data2 = pd.read_csv(files[i])
#    data1[:,:,i]=data2.values
#    p=i/10.0
#    bins=int(np.rint(p))-1
#    perpow2[bins]=np.log10(600.0*np.sum(10**data1[:,:,i])/((dt*zpt)**2)+10**perpow2[bins])
#for j in range (0,30,1):
#    perbin2[j]=1.0/(1.0/(8*60.0)-(j*10.0)/(dt*zpt))/60.0
#
#f=interpolate.interp1d(perbin,perpow,kind='linear')
#f2=interpolate.interp1d(perbin2,perpow2,kind='linear')


#
#plt.loglog(x,(x)**(1)*10**(-14.0/4.0),linewidth=2,linestyle='--',label='1-slope')
#plt.loglog(x,(x)**(2)*10**(-12.0/3.0),linewidth=2,linestyle='--',label='2-slope')

plt.figure(figsize=(8,8)) 
plt.loglog(perbin/60.0,(perpow),marker='x')
#plt.loglog(x,f(x)/((x)**(1)),label='AMTM-BandOH')  
#plt.loglog(x,f2(x)/((x)**(1)),label='ASI') 
#plt.loglog(x,((x)**(1)*10**(-14.0/4.0))/((x)**(1)*10**(-14.0/4.0))) 
plt.title('Wave Period Analysis')
plt.xlabel('frequency (min)')
plt.ylabel('Power (1/min)')
#plt.loglog(perbin,(perbin)**(1)*10**-4,label='5/3-power')
#plt.loglog(perbin,(perbin)**(2)*1.0*10**-3,label='3/1-power')
#plt.legend()
#plt.tight_layout()

