# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:02:37 2019

@author: Kenneth
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2
from scipy import signal

plt.figure()
#Han=np.hanning(len(Tprime))
#HanI = Tprime*Han

#y = np.pad(I, (2000,2000),'constant')

####FFT
#Pow = np.fft.fft(HanI)   
#
#x=np.fft.fftfreq(len(HanI),d=0.010277)
#
#Pow2 = np.abs(Pow)**2
#plt.plot(1/x,Pow2,label='Zp')
#plt.legend()

#####Welch
#f, Pxx_den = signal.welch( HanI)
#plt.semilogy(1/f, Pxx_den)
#plt.xlabel('frequency [Hz]')
#plt.ylabel('PSD [V**2/Hz]')
#plt.show()

####CWT
#widths=np.arange(1,200)
#
#q=time
#Test1 = 30.0*np.sin(q*2*np.pi/24.0)
#Test2 = 20.0*np.sin(q*np.pi/5.0)
#Test3 = 20.0*np.sin(q*np.pi/11.0)
#
#TTest = Test1
#
#cwtmatr = signal.cwt(TTest-np.mean(TTest),signal.morlet,widths)
##plt.imshow(cwtmatr, extent=[-1, 1, 31, 1], cmap='PRGn', aspect='auto',
##           vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
#cwtmatr=((cwtmatr)**2)
#
#yax=np.arange(0,cwtmatr.shape[0])/60.0
#xax=np.arange(0,cwtmatr.shape[1])*37.0/3600.0
#
##plt.contourf(xax,yax,cwtmatr[:,:],cmap='jet',vmin=0.0,vmax=np.max(cwtmatr), levels=5)
#plt.pcolormesh(xax,yax,cwtmatr[:,:],cmap='jet',vmin=np.min(cwtmatr),vmax=np.max(cwtmatr))
#plt.colorbar()
#plt.show()
#plt.figure()
#plt.plot(q,TTest)


####STFT

fs = 3600.0/37.0
N=np.size(time)
Tprime = T-np.mean(T)

freq, tic, Zxx = signal.stft(Tprime,fs,nperseg=2336)

zxx=np.abs(Zxx**2)

plt.pcolormesh(tic, freq, np.abs(Zxx))









