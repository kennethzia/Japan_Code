"""
Kenneth Zia
Phase Speed Plotter and Total Power Integration
"""
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
from scipy.interpolate import interp2d
import pandas as pd

plt.rcParams.update({'font.size': 15})

data = pd.read_csv('C:\Users\Kenneth\Desktop\Analysis24hr\ASI_TOTAL.csv')
data=data.values

data=np.delete(data, 0, 1)
omega=1.0/(2.0**11*74.0)

x=np.arange(-150,150,1)
y=np.arange(-150,150,1)
x0=np.zeros(300)
y0=np.zeros(300)

plt.figure(figsize=(10,8))

t=np.sum(10**data[:,:])
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


plt.pcolormesh(x,y,data,cmap='jet',vmin=-11.5,vmax=-6.5)
#plt.contour(x,y,Chat2,levels = [0.0],colors=('k'),linestyles=('-'),linewidths=(2)) 
#x,y=np.meshgrid(x,y)
#f = interp2d(x, y, data, kind='cubic')
#xnew = np.arange(-150, 150, 1)
#ynew = np.arange(-150, 150, 1)
#data21 = f(xnew,ynew)
#Xn, Yn = np.meshgrid(xnew, ynew)
#plt.subplot(3, 2, 5)
#plt.pcolormesh(Xn, Yn, data21, cmap='jet',vmin=-6.5,vmax=-14)


plt.title('MCM_ASI 24hr Analysis')

TP='Total Power'+"{:.2E}".format(Decimal(np.str(t)))
plt.text(-150,140,TP,color='white',fontsize=12)
plt.text(78,130,'Theta='+np.str(int(theta))+'[deg]',color='white',fontsize=12)
plt.text(78,140,'Max_Val='+np.str(int(psmax))+'[m/s]',color='white',fontsize=12)


plt.xlabel('Phase Speed (E-W) [m/s]')
plt.ylabel('Phase Speed (N-S) [m/s]')
plt.colorbar(label='log$_{10}$(PSD) [m$^{2}$/s$^{2}$]')
plt.plot((0.0,xmax),(0.0,ymax))
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
plt.savefig('C:\Users\Kenneth\Desktop\Analysis24hr\ASI_TOTAL.jpg')
