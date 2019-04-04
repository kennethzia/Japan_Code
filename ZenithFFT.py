# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:02:37 2019

@author: Kenneth
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

plt.figure()
Han=np.hanning(len(t2))
HanI = t2*Han
#y = np.pad(I, (2000,2000),'constant')
Pow = np.fft.fft(t2)
x=np.fft.fftfreq(len(t2),d=1.0)

Pow2 = np.abs(Pow)**2

plt.plot(1/x,Pow2,label='Zp')
plt.legend()




