# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:40:48 2018

@author: Kenneth
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted

plt.rcParams.update({'font.size': 15})




path='C:\Users\Kenneth\Desktop\Blocking\Time'
files=glob.glob(path+'*.csv')
files=natsorted(files)

xp=np.arange(0,300)
data1=np.zeros((71,3,np.size(files)))
data=np.zeros((300,301))
CH=np.zeros((300,300,99))

data3=np.zeros((301,301))
x=np.arange(-300/2,300/2,1)
y=np.arange(-300/2,300/2,1)
x0=np.zeros(300)
y0=np.zeros(300)  
Chat=np.zeros((300,300))
Chat2=np.zeros((300,300))

for i in range(0,np.size(files)):

    data2 = pd.read_csv(files[i])
    data2=data2.values
    
    data2=data2[::-1]
    dataU=np.interp(xp,data2[:,0],data2[:,1])
    dataV=np.interp(xp,data2[:,0],data2[:,2])
    for m in range(30,70):
        for j in range(0,300):
            for k in range(0,300):
                p=np.sqrt((j-150)**2+(k-150)**2)
                theta=np.arctan2((k-150),(j-150))
                CH[j,k,m]=p-(dataV[m]*np.cos(theta)+dataU[m]*np.sin(theta))
                if CH[j,k,m]<=0:
                    CH[j,k,m]=-100000000.0
 
    Chat[:,:]=np.sum(CH[:,:,:],axis=2)
    Chat2=Chat+Chat2

#    
            
    plt.figure(figsize=(8,8))
    
    
    
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
    
    plt.contour(x,y,Chat,levels = [0.0],colors=('k'),linestyles=('-'),linewidths=(2)) 
#    plt.pcolormesh(x,y,Chat,cmap='jet',vmin=data2.min(),vmax=data2.max())
#    plt.colorbar()
    plt.plot()
    
    plt.title('MERRA2 3 Hour Wind Data Blocking Region'+np.str(i+1))
    
    plt.xlabel('Phase Speed (E-W) [m/s]')
    plt.ylabel('Phase Speed (N-S) [m/s]')
    #plt.colorbar(label='blocking zone (-)')
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
    
    
    plt.show()
    plt.savefig('C:\Users\Kenneth\Desktop\Blocking\Time'+np.str(k)+'.jpg')
    
    
plt.figure(figsize=(8,8))



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
plt.contour(x,y,Chat2,levels = [0.0],colors=('k'),linestyles=('-'),linewidths=(2)) 
#    plt.pcolormesh(x,y,Chat,cmap='jet',vmin=data2.min(),vmax=data2.max())
#    plt.colorbar()
plt.plot()

plt.title('MERRA2 June 17th Total Blocking Region')

plt.xlabel('Phase Speed (E-W) [m/s]')
plt.ylabel('Phase Speed (N-S) [m/s]')
#plt.colorbar(label='blocking zone (-)')
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


plt.show()
plt.savefig('C:\Users\Kenneth\Desktop\Blocking\Time_TOTAL.jpg')