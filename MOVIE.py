# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 13:28:14 2019

@author: Kenneth
"""

import cv2
import numpy as np
import os
from pylab import array, plot, show, axis, arange, figure, uint8
import matplotlib.pyplot as plt


#m=('Jun26-27','Jun27-28','Jun28-29','Jun29-30','Jun30-01')
##image_folder = r'E:\\AMTMBandIntensity\\'+m[4]+'\\'
##image_folder = r'E:\\PFRR\\January\\Jan11-12\\'

#image_folder = 'C:\\Users\\Kenneth\\Desktop\\Temp\\'

image_folder = r'E:\MCM_AMTM_2018\MCM_AMTM_2018\July2018\Jul16-17\Figures'

video_name = 'Crazy.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

#a=plt.imread(image_folder+images[0])
#a1=a.shape
#data=np.zeros((a1[0],a1[1],np.size(images)))
#data1=np.zeros((a1[0],a1[1]))
#data3=np.zeros((a1[0],a1[1]))


frame = cv2.imread(image_folder+images[0],1)
height, width, layers = frame.shape
data3 = np.zeros((height,width,np.size(images)))
data1 = np.zeros((height,width))


video = cv2.VideoWriter(video_name, 0, 20, (width,height))



#for i in range(0,np.size(images)):
#    data3[:,:,i] = plt.imread(image_folder+images[i])
#
##    data[:,:,i] = plt.imread(image_folder+images[i])
##    
##for i in range(0,a1[0]-1):
##    for ii in range(0,a1[1]-1):
##        
##        data1[i,ii] = np.average(data[i,ii])
##
##
##
for i in range(0,np.size(images)):
#
#
#    if i <30:
#        data1[:,:]= data3[:,:,i]-np.average(data3[50:206,:,i:i+60])
#    if i > np.size(images)-61:
#        data1[:,:]= data3[:,:,i]-np.average(data3[50:206,:,i-60:i])
#    data1[:,:]= data3[:,:,i]-np.average(data3[50:206,i-30,i+30])
#    x= plt.pcolormesh(data1,cmap='jet',vmax=np.max(data1[108:148,:]),vmin=np.min(data1[108:148,:]))
#    plt.axis('off')
#
#    plt.savefig(image_folder+np.str(i)+'.jpg',bbox_inches='tight',pad_inches=0)
#
#    print,i
    img2 =cv2.imread(image_folder+images[i],1)


# #############################################################################   
#    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
#    
#    lab = cv2.cvtColor(img2, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
#    l, a, b = cv2.split(lab)  # split on 3 different channels
#    
#    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
#    
#    lab = cv2.merge((l2,a,b))  # merge channels
#    newImage0 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BG
#    newImage0 = array(newImage0,dtype=uint8)
#    
##    newImage0=cv2.fastNlMeansDenoising(img2,None,10,7,5)
##    
#    lab = cv2.cvtColor(newImage0, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
#    l, a, b = cv2.split(lab)  # split on 3 different channels
#    
#    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
#    
#    lab = cv2.merge((l2,a,b))  # merge channels
#    newImage0 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BG
#        
##        
#        lab = cv2.cvtColor(newImage0, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
#        l, a, b = cv2.split(lab)  # split on 3 different channels
#        
#        l2 = clahe.apply(l)  # apply CLAHE to the L-channel
#        
#        lab = cv2.merge((l2,a,b))  # merge channels
#        newImage0 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to 
    
    
#    frame3 = array(newImage0,dtype=uint8)
   #frame3 = cv2.imread(image_folder+np.str(i)+'.jpg',1)
    #final = cv2.applyColorMap(frame3, cv2.COLORMAP_JET)
#images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
#frame = cv2.imread(image_folder+images[0],1)
#height, width, layers = frame.shape


#
#video = cv2.VideoWriter(video_name, 0, 20, (width,height))
#for i in range(0,np.size(images)):
#
#    img2 =cv2.imread(image_folder+images[i],1)

    video.write(img2)

cv2.destroyAllWindows()
video.release()
