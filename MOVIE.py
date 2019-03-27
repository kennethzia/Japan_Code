# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 13:28:14 2019

@author: Kenneth
"""

import cv2
import os

image_folder = 'C:\Users\Kenneth\Desktop\Jun19-20'
video_name = 'Jun19-20.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".tif")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 10, (width,height))
for image in images:
    ing = cv2.imread(os.path.join(image_folder, images))
    pimg(image)=cv2.equalizeHist(ing)

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, pimg)))

cv2.destroyAllWindows()
video.release()
