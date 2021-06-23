# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 23:55:19 2021

@author: diana
"""
import numpy as np
import cv2 as cv
import pygame as py

movement=0
WIDHT, HEIGHT = 700, 700
screen=py.display.set_mode([WIDHT,HEIGHT])
py.display.set_caption("Rehab Videogame")
orange_color=(243,164,74)
bee_width=55
bee_height=55
bee_image=py.image.load('secondbee.png')
bee_image=py.transform.scale(bee_image,(bee_width,bee_height))
fps=60

def process(frame):
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
    return frame,filtered,movement
            

class bee:

    def __init__(self):
    
        self.img=bee_image
        self.velocity=5
        self.pos_x=100
        self.pos_y=100
        
    def update(self,user_movement):
        if user_movement == 1 and self.pos_y>0:
            self.pos_y -= self.velocity
        elif user_movement == 0 and self.pos_y < 700:
            self.pos_y += self.velocity
        
    def draw (self,screen):
        screen.fill(orange_color)
        screen.blit(self.img, (self.pos_x,self.pos_y))
        py.display.update() 


def main():
    player=bee()
    clock=py.time.Clock()
    run = True
    capture =cv.VideoCapture(0)
    
    while run: 
        clock.tick(fps)
        data,frame = capture.read()
        imag,filtered,movement=process(frame)
        
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
        player.draw(screen)  
        player.update(movement)
        cv.imshow('camera',imag)
        cv.imshow('o',filtered)
        
        if cv.waitKey(2) == ord('q'):
            break
            
    capture.release()
    cv.destroyAllWindows()       
    py.quit()

  
if __name__=="__main__":
    main() 
      
    