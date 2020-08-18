# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:40:42 2020

@author: Admin
"""

import cv2
import imutils

vid = cv2.VideoCapture('road.mp4')
#vid = cv2.VideoCapture("road.mp4") #store in variable

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame, (900,900))
    #print(ret)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5,5),0)
    edged = cv2.Canny(blurred, 20,70)
    cv2.imshow("edged detection", edged)
    #cv2.imshow('gray video', gray)
    cv2.imshow('color video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    

