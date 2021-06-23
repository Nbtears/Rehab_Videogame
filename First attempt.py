# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 23:55:19 2021

@author: diana
"""
import numpy as np
import cv2 as cv
import pygame as py
import mediapipe as mp

movement=0
WIDHT, HEIGHT = 700, 700
screen=py.display.set_mode([WIDHT,HEIGHT])
py.display.set_caption("Rehab Videogame")
back_color=(74,164,243)
bee_width=55
bee_height=55
bee_image=py.image.load('secondbee.png')
bee_image=py.transform.scale(bee_image,(bee_width,bee_height))
star_image=py.image.load('star.png')
star_image=py.transform.scale(star_image,(bee_width,bee_height))
fps=60
stars=[]

def angle_calculate(a,b,c):
    
    a=np.array(a)
    b=np.array(b)
    c=np.array(c)
    
    radians=np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    angle=np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle=360-angle
    
    return angle   

def process(frame,mp_drawing,mp_holistic,holistic):
    stage = None
    #cambios de color y aplicar módulo holistic
    image= cv.cvtColor(frame,cv.COLOR_RGB2BGR)
    result=holistic.process(image)
    image= cv.cvtColor(image,cv.COLOR_BGR2RGB)
            
    #Landmarks
    try: 
            landmarks=result.pose_landmarks.landmark
            
            #coordenadas de brazo izq
            shoulder = [landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].x,
                      landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].x,
                      landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].x,
                      landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].y]
            
            #calculate angle
            angle = angle_calculate(shoulder,elbow,wrist)
            
            #look angle
            cv.putText(image,str(angle),
                       tuple(np.multiply(elbow,[640,480]).astype(int)),
                             cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv.LINE_AA)
            
            #repetitions
            if angle>120:
                stage = 0
            elif angle <=60:
                stage = 1
            
    except:
        pass
                  
    #dibujar las articulaciones en la imagen
    mp_drawing.draw_landmarks(image, result.pose_landmarks,mp_holistic.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(color = (102,31,208),thickness = 2,circle_radius = 2),
                              mp_drawing.DrawingSpec(color = (103,249,237),thickness = 2,circle_radius = 2))
            
    return image,stage
            

class bee:

    def __init__(self):
    
        self.img=bee_image
        self.velocity=30
        self.pos_x=100
        self.pos_y=100
        
    def update(self,user_movement):
        if user_movement == 1 and self.pos_y>10:
            self.pos_y -= self.velocity
        elif user_movement == 0 and self.pos_y <=630:
            self.pos_y += self.velocity
        
    def draw (self,screen):
        screen.fill(back_color)
        screen.blit(self.img, (self.pos_x,self.pos_y))
        py.display.update() 
        
class star:
    def __init__(self):
        self.image=star_image
        self.pos_x = WIDHT+np.random.randint(10,600)
        self.pos_y=np.random.randint(10, 600)
        self.width = self.image.get_width()
              
    def update(self):
        self.pos_x -=10
        if self.pos_x < -self.width:
            self.pos_x = WIDHT + np.random.randint(10, 900)
            self.pos_y =np.random.randint(10, 600)
    
    def draw(self,screen):
        screen.blit(self.image, (self.pos_x,self.pos_y))
        py.display.update()


def main():
    player=bee()
    for i in range(3): stars.append(star())
    clock=py.time.Clock()
    run = True
    capture =cv.VideoCapture(0)
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
    with mp_holistic.Holistic(min_detection_confidence=0.8,min_tracking_confidence=0.8)as holistic:
        while run: 
            clock.tick(fps)
            data,frame = capture.read()
            imag,stage=process(frame,mp_drawing,mp_holistic,holistic)
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    run = False
            player.draw(screen)  
            player.update(stage)
            for i in range(3): 
                stars[i].draw(screen)
                stars[i].update()
            cv.imshow('camera',imag)
            
            if cv.waitKey(2) == ord('q'):
                break
                
    capture.release()
    cv.destroyAllWindows()       
    py.quit()

  
if __name__=="__main__":
    main()