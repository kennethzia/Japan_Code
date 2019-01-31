# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 13:25:37 2018

@author: Kenneth
"""

"""
Kenneth Zia
Phase Speed Plotter and Total Power Integration
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted
from decimal import Decimal

plt.rcParams.update({'font.size': 15})



path='E:\month 1\week 3\AMTM_HOURLY\AMTM*'
#path='C:\Users\Kenneth\Desktop\AMTM-3hr\AMTM*TOTAL'
files=glob.glob(path+'.csv')
files=natsorted(files)

t2=np.zeros(np.size(files))
x2=np.zeros(np.size(files))


data1=np.zeros((300,301,np.size(files)))
data=np.zeros((300,301))
data3=np.zeros((300,301))
data=np.zeros((300,301))
piece=np.zeros(12)



for i in range(0,np.size(files)):

    data2 = pd.read_csv(files[i])
    data1[:,:,i]=data2.values

x=np.arange(-len(data)/2,len(data)/2+1,1)
y=np.arange(-len(data)/2,len(data)/2+1,1)
x0=np.zeros(len(data)+1)
y0=np.zeros(len(data)+1)    

for k in range(0,np.size(files)): 
    for i in range(0,300):
        for ii in range(0,301):
        
            data[i,ii]= data1[i,ii,k]
    
    plt.figure(figsize=(10,8))
    t=np.sum(10**data[:,:])
    t2[k]=t
    x2[k]=k*3
    ind = np.unravel_index(np.argmax(data, axis=None), data.shape)
#    xmax=float(int(ind[1])-150)
#    ymax=float(int(ind[0])-150)
#    psmax=np.sqrt(xmax**2+ymax**2)
#    theta=np.arctan2(ymax,xmax)*180.0/(np.pi)
#    
#    circle1 = plt.Circle((0, 0), 50, color='k', fill=False)
#    circle2 = plt.Circle((0, 0), 100, color='k', fill=False)
#    circle3 = plt.Circle((0, 0), 150, color='k', fill=False)
#    
#    circle1 = plt.Circle((0, 0), 50, color='k', fill=False)
#    circle2 = plt.Circle((0, 0), 100, color='k', fill=False)
#    circle3 = plt.Circle((0, 0), 150, color='k', fill=False)
#    
#    circle11 = plt.Circle((0, 0), 10,linestyle=':', color='k', fill=False)
#    circle21 = plt.Circle((0, 0), 20,linestyle=':', color='k', fill=False)
#    circle31 = plt.Circle((0, 0), 30,linestyle=':', color='k', fill=False)
#    circle41 = plt.Circle((0, 0), 40,linestyle=':', color='k', fill=False)
#    
#    circle12 = plt.Circle((0, 0), 110,linestyle=':', color='k', fill=False)
#    circle22 = plt.Circle((0, 0), 120,linestyle=':', color='k', fill=False)
#    circle32 = plt.Circle((0, 0), 130,linestyle=':', color='k', fill=False)
#    circle42 = plt.Circle((0, 0), 140,linestyle=':', color='k', fill=False)
#    
#    circle13 = plt.Circle((0, 0), 60,linestyle=':', color='k', fill=False)
#    circle23 = plt.Circle((0, 0), 70,linestyle=':', color='k', fill=False)
#    circle33 = plt.Circle((0, 0), 80,linestyle=':', color='k', fill=False)
#    circle43 = plt.Circle((0, 0), 90,linestyle=':', color='k', fill=False)
#    
#    
#    plt.pcolormesh(x,y,data,cmap='jet',vmin=-11.5,vmax=-6.5)
#    plt.plot()
#    
#    plt.title('AMTM BandOH (3hr) Interval #'+np.str(k+1))
#    
#    plt.xlabel('Phase Speed (E-W) [m/s]')
#    plt.ylabel('Phase Speed (N-S) [m/s]')
#    plt.colorbar(label='log$_{10}$(PSD) [m$^{2}$/s$^{2}$]')
#    
#    plt.plot((0.0,xmax),(0.0,ymax))
#
#    plt.plot(x0,y,color='k',lw='0.5')
#    plt.plot(x,y0,color='k',lw='0.5')
#    plt.gcf().gca().add_artist(circle1)
#    plt.gcf().gca().add_artist(circle2)
#    plt.gcf().gca().add_artist(circle3)
#    plt.gcf().gca().add_artist(circle11)
#    plt.gcf().gca().add_artist(circle21)
#    plt.gcf().gca().add_artist(circle31)
#    plt.gcf().gca().add_artist(circle41)
#    plt.gcf().gca().add_artist(circle12)
#    plt.gcf().gca().add_artist(circle22)
#    plt.gcf().gca().add_artist(circle32)
#    plt.gcf().gca().add_artist(circle42)
#    plt.gcf().gca().add_artist(circle13)
#    plt.gcf().gca().add_artist(circle23)
#    plt.gcf().gca().add_artist(circle33)
#    plt.gcf().gca().add_artist(circle43)
#    TP='Total Power'+"{:.2E}".format(Decimal(np.str(t)))
#    plt.text(-150,140,TP,color='white',fontsize=12)
#    plt.text(78,130,'Theta='+np.str(int(theta))+'[deg]',color='white',fontsize=12)
#    plt.text(78,140,'Max_Val='+np.str(int(psmax))+'[m/s]',color='white',fontsize=12)

   # plt.show()
  #  plt.savefig('C:\Users\Kenneth\Desktop\AMTM-3hr\AMTM_#'+np.str(k)+'.jpg')
    for i in range(0,299):
      for j in range (0,299):
        theta=np.arctan2(j-150,i-150)
        if theta>=0:
            if theta>5.0*np.pi/6.0 and theta<=np.pi:
                piece[5]=piece[5]+10**data[i,j]
            if theta<=5.0*np.pi/6.0 and theta>4.0*np.pi/6.0:
                piece[4]=piece[4]+10**data[i,j]
            if theta<=4.0*np.pi/6.0 and theta>np.pi/2.0:
                piece[3]=piece[3]+10**data[i,j]
            if theta>np.pi/3.0 and theta<=np.pi/2.0:
                piece[2]=piece[2]+10**data[i,j]
            if theta<=np.pi/3.0 and theta>np.pi/6.0:
                piece[1]=piece[1]+10**data[i,j]
            if theta<=np.pi/6.0 and theta>0.0:
                piece[0]=piece[0]+10**data[i,j]
        if theta<0:
            if abs(theta)>5.0*np.pi/6.0 and abs(theta)<=np.pi:
                piece[6]=piece[6]+10**data[i,j]
            if abs(theta)<=5.0*np.pi/6.0 and abs(theta)>4.0*np.pi/6.0:
                piece[7]=piece[7]+10**data[i,j]
            if abs(theta)<=4.0*np.pi/6.0 and abs(theta)>np.pi/2.0:
                piece[8]=piece[8]+10**data[i,j]
            if abs(theta)>np.pi/3.0 and abs(theta)<=np.pi/2.0:
                piece[9]=piece[9]+10**data[i,j]
            if abs(theta)<=np.pi/3.0 and abs(theta)>np.pi/6.0:
                piece[10]=piece[10]+10**data[i,j]
            if abs(theta)<=np.pi/6.0 and abs(theta)>0.0:
                piece[11]=piece[11]+10**data[i,j]
      
      
      
      
    ax=plt.subplot(111,polar=True)
    thetaax=np.pi/12.0+np.linspace(0.0,2*np.pi,12,endpoint=False)
    radii=np.array(piece*10**5)
    width=np.array(np.pi/12.0+np.zeros(12))
    bars=ax.bar(thetaax[:],radii[:],
    edgecolor='k',
    label='x10^-5',
    width=0.5)
    ax.set_yticks(np.linspace(0,np.max(radii),4))
    ax.set_xticks(thetaax-np.pi/12.0)
    plt.legend()
    plt.grid(True)
    plt.title("Phase Speed Power Directionality")
    
    plt.show()
  

plt.figure(figsize=(10,8))
plt.title('3-Hourly Change in Power')
plt.xlabel('Time (hrs)')
plt.ylabel('Total Power')
plt.semilogy(x2,t2)
plt.show()

for i in range(0,300):
    for ii in range(0,301):
        data3[i,ii]=np.log10(np.average(10**data1[i,ii,:]))


t=np.sum(10**data3[:,:])
ind = np.unravel_index(np.argmax(data3, axis=None), data.shape)
xmax=float(int(ind[1])-150)
ymax=float(int(ind[0])-150)
psmax=np.sqrt(xmax**2+ymax**2)
theta=np.arctan2(ymax,xmax)*180.0/(np.pi)

plt.figure(figsize=(10,8))

#
#circle1 = plt.Circle((0, 0), 50, color='k', fill=False)
#circle2 = plt.Circle((0, 0), 100, color='k', fill=False)
#circle3 = plt.Circle((0, 0), 150, color='k', fill=False)
#
#circle1 = plt.Circle((0, 0), 50, color='k', fill=False)
#circle2 = plt.Circle((0, 0), 100, color='k', fill=False)
#circle3 = plt.Circle((0, 0), 150, color='k', fill=False)
#
#circle11 = plt.Circle((0, 0), 10,linestyle=':', color='k', fill=False)
#circle21 = plt.Circle((0, 0), 20,linestyle=':', color='k', fill=False)
#circle31 = plt.Circle((0, 0), 30,linestyle=':', color='k', fill=False)
#circle41 = plt.Circle((0, 0), 40,linestyle=':', color='k', fill=False)
#
#circle12 = plt.Circle((0, 0), 110,linestyle=':', color='k', fill=False)
#circle22 = plt.Circle((0, 0), 120,linestyle=':', color='k', fill=False)
#circle32 = plt.Circle((0, 0), 130,linestyle=':', color='k', fill=False)
#circle42 = plt.Circle((0, 0), 140,linestyle=':', color='k', fill=False)
#
#circle13 = plt.Circle((0, 0), 60,linestyle=':', color='k', fill=False)
#circle23 = plt.Circle((0, 0), 70,linestyle=':', color='k', fill=False)
#circle33 = plt.Circle((0, 0), 80,linestyle=':', color='k', fill=False)
#circle43 = plt.Circle((0, 0), 90,linestyle=':', color='k', fill=False)
#
#plt.pcolormesh(x,y,data3,cmap='jet',vmin=-11.5,vmax=-6.5)
#plt.plot()
#
#plt.title('AMTM 24hr Avgerage')
#
#plt.xlabel('Phase Speed (E-W) [m/s]')
#plt.ylabel('Phase Speed (N-S) [m/s]')
#plt.colorbar(label='log$_{10}$(PSD) [m$^{2}$/s$^{2}$]')
#plt.plot((0.0,xmax),(0.0,ymax))
#
#plt.plot(x0,y,color='k',lw='0.5')
#plt.plot(x,y0,color='k',lw='0.5')
#plt.gcf().gca().add_artist(circle1)
#plt.gcf().gca().add_artist(circle2)
#plt.gcf().gca().add_artist(circle3)
#plt.gcf().gca().add_artist(circle11)
#plt.gcf().gca().add_artist(circle21)
#plt.gcf().gca().add_artist(circle31)
#plt.gcf().gca().add_artist(circle41)
#plt.gcf().gca().add_artist(circle12)
#plt.gcf().gca().add_artist(circle22)
#plt.gcf().gca().add_artist(circle32)
#plt.gcf().gca().add_artist(circle42)
#plt.gcf().gca().add_artist(circle13)
#plt.gcf().gca().add_artist(circle23)
#plt.gcf().gca().add_artist(circle33)
#plt.gcf().gca().add_artist(circle43)
#
#TP='Total Power'+"{:.2E}".format(Decimal(np.str(t)))
#plt.text(-150,140,TP,color='white',fontsize=12)
#plt.text(78,130,'Theta='+np.str(int(theta))+'[deg]',color='white',fontsize=12)
#plt.text(78,140,'Max_Val='+np.str(int(psmax))+'[m/s]',color='white',fontsize=12)
#
#plt.show()
#plt.savefig('C:\Users\Kenneth\Desktop\AMTM-3hr\AMTM_24hrMean.jpg')

