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

m=('\Jun17-18','\Jun18-19')

patha='C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[0]+'\BandOH2hr\BandOH*TOTAL'
#path='C:\Users\Kenneth\Desktop\AMTM-3hr\AMTM*TOTAL'
filesa=glob.glob(patha+'.csv')
filesa=natsorted(filesa)

pathb='C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[1]+'\BandOH2hr\BandOH*TOTAL'
#path='C:\Users\Kenneth\Desktop\AMTM-3hr\AMTM*TOTAL'
filesb=glob.glob(pathb+'.csv')
filesb=natsorted(filesb)


x=np.linspace(1,149.,600)

plt.rcParams.update({'font.size': 20})
Hours=np.size(filesa)+np.size(filesb)
x5=np.linspace(0,Hours-2,100)
x5=x5*2
x2=np.arange(0,Hours)
x2=x2*2
psbin=np.zeros(150)
psbin2=np.zeros(150)
pspow=np.zeros((np.size(psbin),Hours))
pspow2=np.zeros((np.size(psbin),Hours))
pspow3=np.zeros(np.size(psbin))
pspow4=np.zeros((np.size(x),Hours))
pspow5=np.zeros((np.size(x),np.size(x5)))

psmean=np.zeros(np.size(psbin))



for k in range(0,Hours-2):
    if k > (np.size(filesa)-1):
        n=1
        kk=k-np.size(filesa)
        FILE='C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[n]+'\BandOH2hr\BandOH'+np.str(kk)
    else:
        n=0
        FILE='C:\Users\Kenneth\Desktop\MCM_AMTM_2017'+m[n]+'\BandOH2hr\BandOH'+np.str(k)
    
    path=FILE+'_TOTAL.csv'


        
    a=300
    

    data9=np.zeros((a,a+1))

    data2 = pd.read_csv(path)
    data9[:,:]=data2.values
    
    b=a/2    
    for i in range(0,a):
        for ii in range(0,a+1):
            r=np.sqrt((i-b)**2+(ii-b)**2)
            p=r/1.0
            if r<149.0:
                bins=int(np.ceil(p))
                pspow[bins,k]=np.log10(np.sum(10**data9[i,ii])+10**pspow[bins,k])
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
plt.xticks(np.arange(0,2*Hours-1,3))
plt.xlabel('Hours of Observation')
plt.ylabel('Phase Speed [m/s]')
plt.colorbar(label='log$_{10}$(Power)')


