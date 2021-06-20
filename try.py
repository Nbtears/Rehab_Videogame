# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 17:48:46 2021

@author: diana
"""
import cv2 as cv
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_holistic=mp.solutions.holistic

capture =cv.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.8,min_tracking_confidence=0.8)as holistic:
     while capture.isOpened():
        
        data,frame = capture.read()
        image= cv.cvtColor(frame,cv.COLOR_RGB2BGR)
        result=holistic.process(image)
        
        print(result.pose_landmarks)
        
        image= cv.cvtColor(image,cv.COLOR_BGR2RGB)
        
        mp_drawing.draw_landmarks(image, result.pose_landmarks,mp_holistic.POSE_CONNECTIONS)
        
        cv.imshow('camera',image)
        if cv.waitKey(2) == ord('q'):
            break   




    
capture.release()
cv.destroyAllWindows()