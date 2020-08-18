# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 12:06:53 2020

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:45:55 2020

@author: Sansrit
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt





def canny(image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 50,150)
    return canny

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([ [(200,height), (1100,height), (550,250) ]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image
    
    


image = cv2.imread('test_image.jpg')

lane_image = np.copy(image) #if we make any change that donesn't affect oringinal

canny= canny(lane_image)

cropped_image = region_of_interest(canny)
# 3rd min no of interaction required  , placeholder
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5)
line_image = display_lines(lane_image, lines)






#cv2.imshow('picture', image)
#cv2.imshow('gray image', gray)
#cv2.imshow('blured image', blur)
cv2.imshow('edged image', canny)
#plt.imshow(canny)
#plt.show()

cv2.imshow('edged image', cropped_image)

cv2.waitKey(0) #displays image until you press any key

