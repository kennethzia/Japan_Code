# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:12:18 2019

@author: Kenneth
"""

from pydap.client import open_url
from pydap.cas.urs import setup_session
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted
from scipy import interpolate

username='kennethzia'
password='Kusaineko2018!'

#'https://goldsmr5.gesdisc.eosdis.nasa.gov:443/opendap/MERRA2/M2I3NPASM.5.12.4/2018/01/MERRA2_400.inst3_3d_asm_Np.2018010'+np.str(i)+'.nc4'
url2 = ('https://goldsmr5.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=%2Fdata%2FMERRA2%2FM2T3NVASM.5.12.4%2F2018%2F02%2FMERRA2_400.tavg3_3d_asm_Nv.20180209.nc4&FORMAT=bmM0Lw&BBOX=-90%2C-180%2C90%2C180&LABEL=MERRA2_400.tavg3_3d_asm_Nv.20180209.SUB.nc&SHORTNAME=M2T3NVASM&SERVICE=SUBSET_MERRA2&VERSION=1.02&DATASET_VERSION=5.12.4&VARIABLES=T%2CU%2CV')

lons = np.arange(576)*0.625-180.
lats = np.arange(361)*0.5-90.
press = [1000.0,975.0,950.0,925.0,900.0,875.0,850.0,825.0,800.0,775.0,750.0,725.0,700.0,650.0,600.0,550.0,\
         500.0,450.0,400.0,350.0,300.0,250.0,200.0,150.0,100.0,70.0,50.0,40.0,30.0,20.0,10.0,7.0,5.0,4.0,3.0,2.0,1.0,0.7,\
         0.5,0.4,0.3,0.1]
press=np.asarray(press)
alt = (1-(press/1013.25)**0.190284)*145366.45*0.3048/1000.0


time = np.arange(8) * 3


session = setup_session(username, password, check_url=url2)
ds2 = open_url(url2, session=session)
Dataset(ds2,'20180209_TUV.nc')
#print(ds2['V'].shape)
#Vwind=(ds2['V'][0,:, 330, :])
#Nwind=Vwind.data
#
#print(ds2['U'].shape)
#Zwind = (ds2['U'][0,:, 330, :])
#Zonal=Zwind.data
#
#plt.figure()
#ZonalMean = np.zeros(42)
#for i in range(0,42):
#    ZonalMean[i] = np.mean(Zonal[0,i,0,:])
#    if ZonalMean[i] > 10000:
#        ZonalMean[i]=20.0
#
#plt.plot(alt[:],ZonalMean[:])

