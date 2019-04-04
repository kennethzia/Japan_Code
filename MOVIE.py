# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 13:28:14 2019

@author: Kenneth
"""

import cv2
import numpy as np
import os
from pylab import array, plot, show, axis, arange, figure, uint8

image_folder = 'C:\\Users\\Kenneth\\Desktop\\Temp\\'
video_name = 'Jun30-01_Temp.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".tif")]
frame = cv2.imread(image_folder+images[0])
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 10, (width,height))
for image in images:
    img2 = cv2.imread(image_folder+image,1)


 #############################################################################   
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
    
    lab = cv2.cvtColor(img2, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels
    
    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
    
    lab = cv2.merge((l2,a,b))  # merge channels
    newImage0 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BG
    newImage0 = array(newImage0,dtype=uint8)
    
    
#    
#    lab = cv2.cvtColor(newImage0, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
#    l, a, b = cv2.split(lab)  # split on 3 different channels
#    
#    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
#    
#    lab = cv2.merge((l2,a,b))  # merge channels
#    newImage0 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BG
#    
#    
#    lab = cv2.cvtColor(newImage0, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
#    l, a, b = cv2.split(lab)  # split on 3 different channels
#    
#    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
#    
#    lab = cv2.merge((l2,a,b))  # merge channels
#    newImage0 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to 
#    
#    
    frame3 = array(newImage0,dtype=uint8)
    
    final = cv2.applyColorMap(frame3, cv2.COLORMAP_JET)
    video.write(final)

cv2.destroyAllWindows()
video.release()
