# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:40:04 2021

@author: diana
"""

import numpy as np
import cv2 as cv

def mano():
    capture =cv.VideoCapture(0)
    while capture.isOpened():
        data,frame = capture.read()
        
        need=frame[100:300,100:300]
        blur = cv.GaussianBlur(need,(3,3),0)
        hsv=cv.cvtColor(blur,cv.COLOR_BGR2HSV)
        mask2=cv.inRange(hsv,np.array([0,20,70]),np.array([20,255,255]))
        kernel = np.ones((2, 2))
        dilation = cv.dilate(mask2, kernel, iterations=2)
        erosion = cv.erode(dilation, kernel, iterations=4)
        filtered=cv.GaussianBlur(erosion,(3,3),0)
        data,thresh=cv.threshold(filtered,127,255,0)
        contours,hierarchy=cv.findContours(thresh,cv.THRESH_BINARY,cv.CHAIN_APPROX_SIMPLE)
         
        try:
            
            contour=max(contours,key=lambda x:cv.contourArea(x))
            x,y,w,h=cv.boundingRect(contour)
            a=w-x
            b=h-y
            if a*b >= 25000:
              cv.rectangle(frame,(100,100),(300,300),(255,0,0),3) 
              movement=1              
            else:
                movement=0 
           
        except:
            pass
            
        cv.imshow('camera',frame)
        cv.imshow('o',filtered)
        if cv.waitKey(2) == ord('q'):
            break
        
    capture.release()
    cv.destroyAllWindows()
    
if __name__=="__main__":
    main()          
        