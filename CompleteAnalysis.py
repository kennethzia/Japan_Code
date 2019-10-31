# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:03:43 2019

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

#m=(r'\SSTempOH2hr',r'\Jun27-28\TempOH2hrsmooth330',r'\Jun28-29\TempOH2hrsmooth330',r'\Jun29-30\TempOH2hrsmooth330',r'\Jun30-01\TempOH2hrsmooth330')
#
date=r'\Jan12-13'
phase=r''


#perpath=r'E:\MCM_AMTM_2018\MCM_AMTM_2018\July2018\Jul16-17'
perpath = r'E:\PFRR\RESULTS\January\Jan12-13\Results'

#perpath = r'E:\PFRR\RESULTS\January\Jan27-28\Results'

#patha=perpath+phase+'\TempOH*_PS'
patha=perpath+'\TempOH*_PS'

filesa=glob.glob(patha+'.csv')
filesa=natsorted(filesa)

#pathb=perpath+m[1]+r'\TempOH*_PS'
#filesb=glob.glob(pathb+'.csv')
#filesb=natsorted(filesb) 
#
#pathc=perpath+m[2]+r'\TempOH*_PS'
#filesc=glob.glob(pathc+'.csv')
##filesc=natsorted(filesc)
##
##pathd=perpath+m[3]+r'\TempOH*_PS'
##filesd=glob.glob(pathd+'.csv')
##filesd=natsorted(filesd)
##
##pathe=perpath+m[4]+r'\TempOH*_PS'
##filese=glob.glob(pathe+'.csv')
##filese=natsorted(filese)
#
##Hours=np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)+np.size(filese)
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



perbin=np.zeros(Hours)
t4 = np.zeros(Hours)
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
#for k in range(0,2):
for k in range(0,np.size(filesq)):
    FILE=perpath+phase+'\TempOH'+np.str(k)
 
    path=FILE+'_WN_'
    files=glob.glob(path+'*.csv')
    files=natsorted(files)
    z=k
    tie[z]=k/2+1

    
    print(k)
    
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
                if r>=4.0 or r<=b:
                    data10[j,ii,i]=(data9[j,ii,i])
                else:
                    data10[j,ii,i] = 0.0
                
    perbin2=np.sum(np.sum((10**data10[:,:,:]/(zpx*dx)**2)))
#    perbin2 = (np.average(zztop[:,:]))
    
    perbin[k] = perbin[k]+perbin2
        
t4 = perbin
        
        
        
        
#    for j in range (0,np.size(files)-1):
#        perbin[j]=(dt/(0.5-(308+j)/2**10))/60.0
#    perpow3=perpow[:,k]
#    f=interpolate.interp1d(perbin,perpow3,kind='linear')
#    perpow4[:,k]=f(x)
#    
#    siz = data9.shape
#    Pow2[k] = np.log10(np.sum(10**data9)*float(siz[2]*siz[0]*siz[1])/(zpt*dt*(zpx*dx)**2))
#
#x2=np.arange(0,Hours)
#for z in range(0,np.size(x)):
#    f=interpolate.interp1d(x2,perpow4[z,:],kind='linear')
#    perpow5[z,:]=f(x5)
#perpow4 = np.log10(perpow4)
#
#
#plt.figure(figsize=(10,10))
#plt.pcolormesh(x5/2+1,x,np.log10(perpow5[:,:]),cmap='jet',vmin=np.min(np.log10(perpow5[:-500,:])),vmax=np.max(np.log10(perpow5[:-500,:])))
#plt.xlabel('Hours of Observation')
#plt.ylabel('Period [min]')
#plt.colorbar(label='log$_{10}$(Power)')
#plt.ylim(5,30)
#plt.savefig(r'E:\PFRR\RESULTS\January'+date+phase+'\FrequencyPow.jpg')
#
#
#
#
#Hours=np.size(filesa)
#
#dx=625.0
#zpx=512.0
#dt=60.0
#zpt=2.0**10
##a=128
#a=64
#
#Q=int(zpx/2.-zpx/int(100000.0/dx)) - int(zpx/2.-zpx/int(10000.0/dx))+2
#
#b=int(a/2)
#
#x=np.linspace(10.,100.,1000)
#
#plt.rcParams.update({'font.size': 20})
#x5=np.linspace(0,Hours-1,1000)
#x6=np.linspace(0,Hours-1,1000)
#tie = np.zeros(Hours)
#
#wavebin=np.zeros(b+1)
#wavebin2=np.zeros(b+1)
#wavepow=np.zeros((np.size(wavebin),Hours))
#wavepow2=np.zeros((np.size(wavebin),Hours))
#wavepow3=np.zeros(np.size(wavebin))
#wavepow4=np.zeros((np.size(x),Hours))
#wavepow5=np.zeros((np.size(x),np.size(x5)))
#
#wavemean=np.zeros(np.size(wavebin))
#
#waveTOT=np.zeros((np.size(x),np.size(x5)*2))
##for n in range(0,5):
#n=0
#pathq=perpath+phase+'\TempOH*_PS'
#filesq=glob.glob(pathq+'.csv')
#filesq=natsorted(filesq)
#for k in range(0,np.size(filesq)):
#    FILE=perpath+phase+'\TempOH'+np.str(k)
#    
#    path=FILE+r'_WN_'
#    files=glob.glob(path+r'*.csv')
#    files=natsorted(files)
##    if n==0:
#    z=k
#    tie[z]=k/2+1
##    if n ==1 :
##        k=k+np.size(filesa)
##        z=k
##        tie[z] = k/2 +2
##    if n==2:
##        k=k+np.size(filesa)+np.size(filesb)
##        z=k
##        tie[z] = k/2 +4
##    if n==3:
##        k=k+np.size(filesa)+np.size(filesb)+np.size(filesc)
##        z=k
##        tie[z] = k/2 +6
##    if n==4:
##        k=k+np.size(filesa)+np.size(filesb)+np.size(filesc)+np.size(filesd)
##        z=k
##        tie[z] = k/2 +8
##    
#    data9=np.zeros((a,a+1,np.size(files)))
#
#    
#    for i in range(0,np.size(files)):
#    
#        data2 = pd.read_csv(files[i])
#        data9[:,:,i]=data2.values
#    
#
#    for i in range(0,a):
#        for ii in range(0,a+1):
#            r=np.sqrt((i-b)**2+(ii-b)**2)
#            p=r/1.0
#            bins=int(np.ceil(p))
#            
#            if r>=3.0 and r<=b:
#
#                wavepow[bins,k]=(np.sum(10**data9[i,ii,:])*r/(zpt*dt*(zpx*dx))+wavepow[bins,k])
#    for j in range (0,b):
#        wavebin[j]=(1/(((j+0.01)*1.0)/(dx*zpx)))/1000.0
#        wavepow3[j]=wavepow[j,k]
#    f=interpolate.interp1d(wavebin,wavepow3,kind='linear')
#    wavepow4[:,k]=f(x)
#    #plt.loglog(x,f(x)/((x)**(3.0)*1.0*10**-6),linewidth=0.5)  
#    
#    print(n,k)
#x2=np.arange(0,Hours)
##wavepow4=np.flip(wavepow4[:,:],1)
##wavepow4=np.delete(wavepow4[:,:], 0, 1)
##wavepow4=np.flip(wavepow4[:,:],1)
#for z in range(0,np.size(x)):
#    f=interpolate.interp1d(x2,wavepow4[z,:],kind='linear')
#    wavepow5[z,:]=f(x5)
##wavepow5=np.log10(wavepow5)
#
#
#plt.figure(figsize=(10,10))
#plt.pcolormesh(x5/2+1,x,wavepow5[:,:],cmap='jet',vmin=np.min(wavepow5[:,:]),vmax=np.max(wavepow5[:,:]))
##ax2.plot(time,T,label='Intensity',color='r',linestyle='--')
##plt.title('MCM AMTM BandOH Wavelength Spectrum Jun17-18')
#
#plt.xlabel('Hours of Observation')
#plt.ylabel('Wavelength [km]')
#plt.colorbar(label='Power')
#plt.savefig(r'E:\PFRR\RESULTS\January'+date+phase+'\WavelengthPow.jpg')





#
Hours=np.size(filesa)

t2=np.zeros(Hours)
x2=np.zeros(Hours)
data1=np.zeros((300,301,Hours))
piece=np.zeros((12,Hours))
quad=np.zeros((4,Hours))


data=np.zeros((300,301))
Avgdata=np.zeros((300,301))
data3=np.zeros((300,301))
data=np.zeros((300,301))
piece=np.zeros((12,Hours))
quad=np.zeros((4,Hours))
tie = np.zeros(Hours)

pathq=perpath+phase+'\TempOH*_TOTAL'
filesq=glob.glob(pathq+'.csv')

for i in range(0,np.size(filesa)):

    data2 = pd.read_csv(filesq[i])
    data1[:,:,i]=(data2.values)
    tie[i]=i/2+1


x=np.arange(-len(data)/2,len(data)/2,1)
y=np.arange(-len(data)/2,len(data)/2,1)
x0=np.zeros(len(data))
y0=np.zeros(len(data))    

#for k in range(0,10):
for k in range(0,Hours): 
    for i in range(0,300):
        for ii in range(0,301):
        
            data[i,ii]= (data1[i,ii,k])

    plt.figure(figsize=(10,8))
    t=np.sum((data[:,:]))
    t2[k]=t
    x2[k]=k*2
    ind = np.unravel_index(np.argmax(data, axis=None), data.shape)
    xmax=float(int(ind[1])-150)
    ymax=float(int(ind[0])-150)
    psmax=np.sqrt(xmax**2+ymax**2)
    theta=np.arctan2(ymax,xmax)*180.0/(np.pi)
    
    circle1 = plt.Circle((0, 0), 50, color='k', fill=False)
    circle2 = plt.Circle((0, 0), 100, color='k', fill=False)
    circle3 = plt.Circle((0, 0), 150, color='k', fill=False)
    
    circle1 = plt.Circle((0, 0), 50, color='k', fill=False)
    circle2 = plt.Circle((0, 0), 100, color='k', fill=False)
    circle3 = plt.Circle((0, 0), 150, color='k', fill=False)
    
    circle11 = plt.Circle((0, 0), 10,linestyle=':', color='k', fill=False)
    circle21 = plt.Circle((0, 0), 20,linestyle=':', color='k', fill=False)
    circle31 = plt.Circle((0, 0), 30,linestyle=':', color='k', fill=False)
    circle41 = plt.Circle((0, 0), 40,linestyle=':', color='k', fill=False)
    
    circle12 = plt.Circle((0, 0), 110,linestyle=':', color='k', fill=False)
    circle22 = plt.Circle((0, 0), 120,linestyle=':', color='k', fill=False)
    circle32 = plt.Circle((0, 0), 130,linestyle=':', color='k', fill=False)
    circle42 = plt.Circle((0, 0), 140,linestyle=':', color='k', fill=False)
    
    circle13 = plt.Circle((0, 0), 60,linestyle=':', color='k', fill=False)
    circle23 = plt.Circle((0, 0), 70,linestyle=':', color='k', fill=False)
    circle33 = plt.Circle((0, 0), 80,linestyle=':', color='k', fill=False)
    circle43 = plt.Circle((0, 0), 90,linestyle=':', color='k', fill=False)
    
    

    plt.pcolormesh(x,y,(data[:,:-1]),cmap='jet',vmin=-8,vmax=-4)#,vmin=np.min(data),vmax=np.max(data))#100)
    plt.colorbar()
    
    plt.plot()
    plt.title('Hour #'+np.str(tie[k]))
    #    
    #    plt.xlabel('Phase Speed (W-E) [m/s]')
    #    plt.ylabel('Phase Speed (S-N) [m/s]')
    #    plt.colorbar()#label='log$_{10}$(PSD) [m$^{2}$/s$^{2}$]')
    
    #    plt.plot((0.0,xmax),(0.0,ymax))
    
    plt.plot(x0,y,color='k',lw='0.5')
    plt.plot(x,y0,color='k',lw='0.5')
    plt.gcf().gca().add_artist(circle1)
    plt.gcf().gca().add_artist(circle2)
    plt.gcf().gca().add_artist(circle3)
    plt.gcf().gca().add_artist(circle11)
    plt.gcf().gca().add_artist(circle21)
    plt.gcf().gca().add_artist(circle31)
    plt.gcf().gca().add_artist(circle41)
    plt.gcf().gca().add_artist(circle12)
    plt.gcf().gca().add_artist(circle22)
    plt.gcf().gca().add_artist(circle32)
    plt.gcf().gca().add_artist(circle42)
    plt.gcf().gca().add_artist(circle13)
    plt.gcf().gca().add_artist(circle23)
    plt.gcf().gca().add_artist(circle33)
    plt.gcf().gca().add_artist(circle43)
    #    TP='Total Power'+"{:.2E}".format(Decimal(np.str(t)))
    #    plt.text(-150,140,TP,color='white',fontsize=12)
    #    plt.text(78,130,'Theta='+np.str(int(theta))+'[deg]',color='white',fontsize=12)
    #    plt.text(78,140,'Max_Val='+np.str(int(psmax))+'[m/s]',color='white',fontsize=12)
    
    plt.xticks(np.arange(-150,150,50))
    plt.yticks(np.arange(-150,150,50))
    
    plt.xlim(-150,150)
    plt.ylim(-150,150)
    
    plt.show()
    #    plt.savefig(r'E:\PFRR\RESULTS\January'+date+phase+'\TempOH_#'+np.str(k+1)+'.jpg')
    plt.savefig(perpath+r'\Figures\TempOH_#'+np.str(k+1)+'.jpg')
  
#  
#    for i in range(0,300):
#      for j in range (0,301):
#        theta=np.arctan2(i-150,j-150)
#        if theta>=0.0:
#            if theta>5.0*np.pi/6.0 and theta<=np.pi:
#                piece[5,k]=piece[5,k]+10**data[i,j]
#            if theta<=5.0*np.pi/6.0 and theta>4.0*np.pi/6.0:
#                piece[4,k]=piece[4,k]+10**data[i,j]
#            if theta<=4.0*np.pi/6.0 and theta>np.pi/2.0:
#                piece[3,k]=piece[3,k]+10**data[i,j]
#            if theta>np.pi/3.0 and theta<=np.pi/2.0:
#                piece[2,k]=piece[2,k]+10**data[i,j]
#            if theta<=np.pi/3.0 and theta>np.pi/6.0:
#                piece[1,k]=piece[1,k]+10**data[i,j]
#            if theta<=np.pi/6.0 and theta>0.0:
#                piece[0,k]=piece[0,k]+10**data[i,j]
#        if theta<0.0:
#            if abs(theta)>5.0*np.pi/6.0 and abs(theta)<=np.pi:
#                piece[6,k]=piece[6,k]+10**data[i,j]
#            if abs(theta)<=5.0*np.pi/6.0 and abs(theta)>4.0*np.pi/6.0:
#                piece[7,k]=piece[7,k]+10**data[i,j]
#            if abs(theta)<=4.0*np.pi/6.0 and abs(theta)>np.pi/2.0:
#                piece[8,k]=piece[8,k]+10**data[i,j]
#            if abs(theta)>np.pi/3.0 and abs(theta)<=np.pi/2.0:
#                piece[9,k]=piece[9,k]+10**data[i,j]
#            if abs(theta)<=np.pi/3.0 and abs(theta)>np.pi/6.0:
#                piece[10,k]=piece[10,k]+10**data[i,j]
#            if abs(theta)<=np.pi/6.0 and abs(theta)>0.0:
#                piece[11,k]=piece[11,k]+10**data[i,j]
#        if theta>=0.0:
#            if theta>np.pi/2:
#                quad[1,k]=quad[1,k]+10**data[i,j]
#            else:
#                quad[0,k]=quad[0,k]+10**data[i,j]
#        if theta<0.0:
#            if abs(theta)>=np.pi/2:
#                quad[2,k]=quad[2,k]+10**data[i,j]
#            else:
#                quad[3,k]=quad[3,k]+10**data[i,j]
#
#
##    
plt.figure(figsize=(15,4))
#ax1=plt.gca()
#ax2=ax1.twinx()

plt.ylabel('T Variance $[K^2]$')
plt.plot(tie,((t4)), marker='x',color = 'r')

#plt.xlim(0,112)

plt.xlabel('Time (hrs)')
#plt.savefig(r'E:\PFRR\RESULTS\January'+date+phase+'\Variance.jpg')
#plt.savefig(r'C:\Users\Kenneth\Desktop\2hrSmooth\PSTotal.jpeg')
plt.savefig(perpath+r'\Figures\Variance.jpeg')

plt.show()


plt.figure(figsize=(15,4))
#ax1=plt.gca()
#ax2=ax1.twinx()

plt.ylabel('T Amplitude $[K]$')
plt.plot(tie,(t4)**(1/2), marker='x',color = 'r')


plt.xlabel('Time (hrs)')
#plt.savefig(r'E:\PFRR\RESULTS\January'+date+phase+'\Variance.jpg')
#plt.savefig(r'C:\Users\Kenneth\Desktop\2hrSmooth\PSTotal.jpeg')
plt.savefig(perpath+r'\Figures\Amplitude.jpeg')

plt.show()

#plt.figure(figsize=(10,10))
#
#plt.xlabel('Time (hrs)')
#plt.ylabel('Total Power')
#
#leg=['NE','NW','SW','SE']
#for m in range(0,4): 
#    plt.plot(tie,(quad[m,:]),label=leg[m])
#plt.legend()
#plt.title('T-prime Quadrant Power Hourly Analysis')
#
##plt.savefig(r'E:\PFRR\RESULTS\January'+date+phase+'\QuadPow.jpg')
#
#plt.show()
#

