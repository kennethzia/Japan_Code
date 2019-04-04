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


dx=625.0
zpx=512.0
dt=74.0
zpt=2.0**10
a=128
Q=int(zpt/2.-zpt/int(3600.0/dt)) - int(zpt/2.-zpt/int(480.0/dt))+1

x=np.linspace(8.,59.,300)

plt.rcParams.update({'font.size': 20})
x5=np.linspace(0,Hours-1,400)
x6=np.linspace(0,Hours-1,400)



perbin=np.zeros(Q)
perbin2=np.zeros(Q)
perpow=np.zeros((np.size(perbin),Hours))
perpow2=np.zeros((np.size(perbin),Hours))
perpow3=np.zeros(np.size(perbin))
perpow4=np.zeros((np.size(x),Hours))
perpow5=np.zeros((np.size(x),np.size(x5)))

wavemean=np.zeros(np.size(perbin))

waveTOT=np.zeros((np.size(x),np.size(x5)*2))
for n in range(0,5):
    pathq=r'C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[n]+'\BandOH1hr\BandOH*TOTAL'
    filesq=glob.glob(pathq+'.csv')
    filesq=natsorted(filesq)
    for k in range(0,np.size(filesq)):
        FILE=r'C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[n]+'\BandOH1hr\BandOH'+np.str(k)
        
        path=FILE+'_WN_'
        files=glob.glob(path+'*.csv')
        files=natsorted(files)
        if n ==1 :
            k=k+np.size(filesa)
        if n==2:
            k=k+np.size(filesa)+np.size(filesb)
        if n==3:
            k=k+np.size(filesa)+np.size(filesb)+np.size(filesc)
        if n==4:
            k=k+np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)
        
        print(k,n)
        
        data9=np.zeros((a,a+1,np.size(files)))
        data10=np.zeros((a,a+1,np.size(files)))

        
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
#                    if 1.0/((r*1.0)/(dx*zpx))/1000.0 <=80:
                    data10[j,ii,i]=data9[j,ii,i]
            perpow[i,k]=np.log10(np.sum(10**data10[:,:,i])*float(np.size(files))/(zpt*dt*(zpx*dx))+10**perpow[i,k])
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
plt.xticks(np.arange(0,Hours-1,8))
plt.xlabel('Hours of Observation')
plt.ylabel('Period [min]')
plt.colorbar(label='log$_{10}$(Power)')
