# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:17:13 2019

@author: Kenneth
"""




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#xt = ['14-15','17-18','18-19','19-20','20-21','26-27','27-28']  #Nov
xt = ['08-09','13-14','21-22','22-23','23-24','24-25','26-27']    #dec

wavex=np.linspace(10.,100.,1000)
perx=np.linspace(5.05,60.,1000)


wavepowtot=[avgWave,avgWave000,avgWave001,avgWave002,avgWave003,avgWave004,avgWave005]
perpowtot = [avgPer,avgPer000,avgPer001,avgPer002,avgPer003,avgPer004,avgPer005]
t2tot = [np.average(t2),np.average(t2000),np.average(t2001),np.average(t2002),np.average(t2003),np.average(t2004),np.average(t2005)]
quadtot = [np.average(quad,1),np.average(quad000,1),np.average(quad001,1),np.average(quad002,1),np.average(quad003,1),np.average(quad004,1),np.average(quad005,1)]
quadtot = np.stack(quadtot)

wavepowtot = np.log10(wavepowtot)
perpowtot = np.log10(perpowtot)

plt.figure()
plt.pcolormesh(xt,wavex,np.transpose(wavepowtot),cmap='jet',vmin=np.min(wavepowtot),vmax=np.max(wavepowtot))
plt.xlabel('Date')


plt.ylabel('Wavelength')
plt.title('November')
plt.colorbar()


plt.figure()
plt.pcolormesh(xt,perx,np.transpose(perpowtot),cmap='jet',vmin=np.min(perpowtot),vmax=np.max(perpowtot))
plt.xlabel('Date')

plt.ylabel('Period')
plt.title('November')
plt.colorbar()


plt.figure(figsize=(10,8))

x=np.arange(-150,150,1)
y=np.arange(-150,150,1)


Averaged = np.average([Avgdata[:,:],Avgdata000[:,:],Avgdata001[:,:],Avgdata002[:,:],Avgdata003[:,:],Avgdata004[:,:],Avgdata005[:,:]],0)

Averaged=np.delete(Averaged, 0, 1)


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


plt.pcolormesh(x,y,Averaged[:,:],cmap='jet',vmin=-7.0,vmax=np.max(Averaged))#-7.0,vmax=-3.0)
#plt.contour(x,y,Chat2,levels = [0.0],colors=('k'),linestyles=('-'),linewidths=(2)) 
#x,y=np.meshgrid(x,y)
#f = interp2d(x, y, data, kind='cubic')
#xnew = np.arange(-150, 150, 1)
#ynew = np.arange(-150, 150, 1)
#data21 = f(xnew,ynew)
#Xn, Yn = np.meshgrid(xnew, ynew)
#plt.subplot(3, 2, 5)
#plt.pcolormesh(Xn, Yn, data21, cmap='jet',vmin=-6.5,vmax=-14)


plt.title('November')

#TP='Total Power'+"{:.2E}".format(Decimal(np.str(t)))
#plt.text(-150,140,TP,color='white',fontsize=12)
#plt.text(78,130,'Theta='+np.str(int(theta))+'[deg]',color='white',fontsize=12)
#plt.text(78,140,'Max_Val='+np.str(int(psmax))+'[m/s]',color='white',fontsize=12)


#plt.xlabel('Phase Speed (E-W) [m/s]')
#plt.ylabel('Phase Speed (N-S) [m/s]')
plt.colorbar(label='log$_{10}$(PSD) [s$^{2}$/m$^{2}$]')
#plt.plot((0.0,xmax),(0.0,ymax))
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
#plt.savefig(r'E:\PFRR\RESULTS\February\Feb23-24\TOTALps.jpg')



plt.figure(figsize=(10,10))
plt.ylabel('PS Total Power',color='r')
plt.plot(xt,t2tot, marker='x',color = 'r')
plt.xlabel('Date')


plt.figure(figsize=(10,10))
plt.xlabel('Date')
plt.ylabel('Total Power')
leg=['NE','NW','SW','SE']
for m in range(0,4): 
    plt.plot(xt,np.log10(quadtot[:,m]),label=leg[m])
plt.legend()
plt.title('T-prime Quadrant Power')






