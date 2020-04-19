# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:49:18 2020

@author: sansrit
"""
import numpy as np
import cv2


img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

#makes line on image with points and BGR color with line width 5

cv2.line(img, (0,0), (80,80), (255,0,0), 4)

#for rectangle top left coordinate and botton right coordinate is used
cv2.rectangle(img,(5,5), (100,100), (0,0,255), 4)

#circle center point, radius, color , -1 linewith imples fillin cirlce

cv2.circle(img, (100,50), 30, (0,255,0),3)


#we can even do polygons
 

 
cv2.imshow('image of watch', img)
cv2.waitKey(0)
cv2.destoryAllWindows()