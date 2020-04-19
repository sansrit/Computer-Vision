# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:59:12 2020

@author: Sansrit
"""
import cv2
import numpy as np

#using the default camera
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out1.avi', fourcc, 20.0, (640,480))



while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    out.write(frame)
    

    
    
    cv2.imshow('Sansrit on video', frame)
    cv2.imshow('Sansrit on gray', gray)

    
#to get exit form video when pressed q  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    


cap.release()
out.release()
cv2.destroyAllWindows()