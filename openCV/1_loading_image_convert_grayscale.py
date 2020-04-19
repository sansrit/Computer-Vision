# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:41:00 2020

@author: sansrit

importing an image and converting to grayscale image
"""



import cv2
import numpy as np
import matplotlib.pyplot as plt

#grayscale is to default to 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)


#to display an image


'''cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#ALTERNATIVELY WE CAN SHOW IMAGE WITH MATPLOTLIB 

plt.imshow(img, cmap = 'gray')
plt.plot([100,100], [50,100], 'r', linewidth = 3)
plt.show()