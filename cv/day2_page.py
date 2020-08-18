# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:27:02 2020

@author: Admin
"""

import cv2
import imutils

image = cv2.imread('page.jpg')

image = cv2.resize(image,(500,600))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(blurred,50,150)
cv2.imshow('edged image', edged)
cv2.waitKey(0)

contur = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
count = imutils.grab_contours(contur)
print(len(count))

cv2.destroyAllWindows()