# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:45:55 2020

@author: Sansrit
"""

import cv2
import numpy as np


#loading iamge

image = cv2.imread('test_image.jpg')

lane_image = np.copy(image) #if we make any change that donesn't affect oringinal


#1st step to edege detection is  convert to greyscale

gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

#2nd step is to reduce noise so apply gussian blur to smooth image

blur = cv2.GaussianBlur(gray, (5,5), 0)

#3 use canny method to identify  edges i.e change in intensities or gradients strongest gradiensts 

canny = cv2.Canny(blur, 50,150)


#4 finding the lane lines and region of interest




cv2.imshow('picture', image)
#cv2.imshow('gray image', gray)
#cv2.imshow('blured image', blur)
cv2.imshow('edged image', canny)

cv2.waitKey(0) #displays image until you press any key

