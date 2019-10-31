# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:52:02 2019

@author: Kenneth
"""


#
#bins = np.linspace(-2,-7,50)
#
##72 min    257 max
#
#Pow=np.zeros(66*66)
#k=0
#
#for i in range(0,65):
#        for ii in range(0,65):
#            k=k+1
#            Pow[k] = np.log10(Low[i,ii])
#
#d = np.digitize(Pow,bins)
            
#hist,bins=np.histogram(np.log10(data1[:,:,]+10**-22))
#plt.bar(bins[:-1], hist, width=(bins[-1]-bins[-2]), align="edge")
            
hist,bins=np.histogram((Hi2[:,:]))
plt.bar(bins[:-1], hist, width=(bins[-1]-bins[-2]), align="edge")
            
            