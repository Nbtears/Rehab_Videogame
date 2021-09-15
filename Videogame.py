import pandas as pd
from datetime import datetime
import csv
import time 
import numpy as np
import cv2 as cv
import pygame as py
import mediapipe as mp
import Interfaz as If

py.font.init()
side = None
score = 0
lives = 3
movement = 0
minang=180
maxang=0
c=0
t=0
WIDTH, HEIGHT = 900, 600
screen = py.display.set_mode([WIDTH,HEIGHT])
py.display.set_caption("Rehab Videogame")
back_image = py.image.load("sources/sea3.jpg")
back_image = py.transform.scale(back_image,(900,600))
bubble_dimension = 40
axo_dimension = 180
enemy_dimension = 100
heart_image = py.image.load("sources/heart.png")
heart_image = py.transform.scale(heart_image,(bubble_dimension,bubble_dimension))
first_image = py.image.load("sources/axo2.png")
first_image = py.transform.scale(first_image,(500,400))
axo_image = py.image.load('sources/axo3.png')
axo_image = py.transform.flip(py.transform.scale(axo_image,(axo_dimension,axo_dimension)),True,False)
bubble_image = py.image.load('sources/buble2.png')
bubble_image = py.transform.scale(bubble_image,(bubble_dimension,bubble_dimension))
enemy_image = py.image.load('sources/pez.png')
enemy_image = py.transform.scale(enemy_image,(enemy_dimension,enemy_dimension))
right_image = py.image.load('sources/right.png')
left_image = py.image.load('sources/left.png')


def angle_calculate(a,b,c):
    
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle=360-angle
    
    return angle   

def process(frame,mp_drawing,mp_holistic,holistic,side):
    global maxang, minang
    stage = None
    #cambios de color y aplicar módulo holistic
    image = cv.cvtColor(frame,cv.COLOR_RGB2BGR)
    result = holistic.process(image)
    image = cv.cvtColor(image,cv.COLOR_BGR2RGB)
            
    #Landmarks
    try: 
            landmarks = result.pose_landmarks.landmark
            
            #coordenadas de brazo izq
            shoulder_L = [landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].x,
                      landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow_L = [landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].x,
                      landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].y]
            wrist_L = [landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].x,
                      landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].y]
            
            #coordenadas de brazo derecho
            shoulder_R = [landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].x,
                      landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow_R = [landmarks[mp_holistic.PoseLandmark.RIGHT_ELBOW.value].x,
                      landmarks[mp_holistic.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist_R = [landmarks[mp_holistic.PoseLandmark.RIGHT_WRIST.value].x,
                      landmarks[mp_holistic.PoseLandmark.RIGHT_WRIST.value].y]
            
            if side == 1:
                #calculate angle
                angle = angle_calculate(shoulder_L,elbow_L,wrist_L)
                
                #look angle
                cv.putText(image,str(int(angle)),
                           tuple(np.multiply(elbow_L,[647,510]).astype(int)),
                                 cv.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2,cv.LINE_AA)
            else:
                #calculate angle
                angle = angle_calculate(shoulder_R,elbow_R,wrist_R)
            
                
                #look angle
                cv.putText(image,str(angle),
                           tuple(np.multiply(elbow_R,[640,480]).astype(int)),
                                 cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv.LINE_AA)
            if angle>maxang:
                maxang=angle
            elif angle<minang:
                minang=angle
                
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
            

class axolote:

    def __init__(self):
    
        self.img = axo_image
        self.velocity = 25
        self.pos_x = 100
        self.pos_y = 100
        self.mask = py.mask.from_surface(self.img)
        
    def update(self,user_movement):
        if user_movement == 1 and self.pos_y - self.velocity > 8:
            self.pos_y -= self.velocity
        elif user_movement == 0 and self.pos_y + axo_dimension < HEIGHT:
            self.pos_y += self.velocity
        
    def draw (self,screen):
        screen.blit(self.img, (self.pos_x,self.pos_y))
        py.display.update() 
        
class bubble:
    def __init__(self):
        self.imag = bubble_image
        self.pos_x = WIDTH+np.random.randint(80,600)
        self.pos_y = np.random.randint(40, 600 - bubble_dimension)
        self.mask = py.mask.from_surface(self.imag)
        
    def update(self):
        self.pos_x -= 10
        if self.pos_x < - bubble_dimension:
            self.pos_x = WIDTH + np.random.randint(10, 900)
            self.pos_y =np.random.randint(40, 600 - bubble_dimension)
    
    def draw(self,screen):
        screen.blit(self.imag, (self.pos_x,self.pos_y))
    
    def collision(self,obj):
        return collide(self,obj)
    
    def delete (self):
        self.pos_x = -bubble_dimension

class enemy():
      def __init__(self):
        self.imag = enemy_image
        self.pos_x = WIDTH + np.random.randint(10,600)
        self.pos_y = np.random.randint(40, 600 - enemy_dimension)
        self.mask = py.mask.from_surface(self.imag)
        
      def update(self):
        self.pos_x -= 5
        if self.pos_x < - enemy_dimension:
            self.pos_x = WIDTH + np.random.randint(10, 900)
            self.pos_y =np.random.randint(40, 600 - enemy_dimension)
    
      def draw(self,screen):
        screen.blit(self.imag, (self.pos_x,self.pos_y))
    
      def collision(self,obj):
        return collide(self,obj)
    
      def delete (self):
        self.pos_x = - enemy_dimension
        
class button:
    def __init__(self,image,x,scale):
        width = image.get_width()
        height = image.get_height()
        self.image=py.transform.scale(image,(int(width*scale),int(height*scale)))
        self.pos_x = x
        self.pos_y = 400
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,self.pos_y)
        self.click = False
    
    def draw(self):
        screen.blit(self.image,(self.pos_x,self.pos_y))
        pos=py.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if py.mouse.get_pressed()[0]==1 and self.click == False:
                return True       
             
def collide(obj1, obj2):
    offset_x = obj2.pos_x - obj1.pos_x
    offset_y = obj2.pos_y - obj1.pos_y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def game(side):
    
    fps = 60
    clock=py.time.Clock()
    run = True
    lives = 3
    score = 0
    
    bubbles = []
    enemies = enemy()
    player = axolote()
   
    py.mixer.init()
    sound_bubble = py.mixer.Sound('sources/blop1.wav')
    sound_dead = py.mixer.Sound('sources/Boing.mp3')
    for i in range(5): bubbles.append(bubble())
    
    main_font = py.font.SysFont("georgia", 40)
    lost_font = py.font.SysFont("georgia",100)
    
    capture =cv.VideoCapture(0)
    
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic  
    
    def redraw():
        global score, lives,c
           
        if lives == 0:
            if c==0:
                screen.blit(back_image,(0,0))
                lost_label = lost_font.render('Game Over',1,(255,255,255))
                screen.blit(first_image,(WIDTH/2 - first_image.get_width()/2,25))
                score_label = main_font.render(f"Score: {score} ",1,(255,255,255))
                progress1_label =main_font.render(f"Minimum angle:{int(minang)}°",1,(255,255,255))
                progress2_label =main_font.render(f"Maximum angle:{int(maxang)}°",1,(255,255,255))
                screen.blit(score_label,(WIDTH-score_label.get_width()-10,10))
                screen.blit(lost_label,(WIDTH/2-lost_label.get_width()/2,320))
                screen.blit(progress1_label,(WIDTH/2-progress1_label.get_width()/2,450))
                screen.blit(progress2_label,(WIDTH/2-progress2_label.get_width()/2,500))
                py.display.update()
                progress()
                c=1
            
        else:
            screen.blit(back_image,(0,0))
            score_label = main_font.render(f"Score: {score} ",1,(255,255,255))
            screen.blit(score_label,(WIDTH-score_label.get_width()-10,10))
        
            if lives >= 1:
                screen.blit(heart_image,(5,5))
                if lives >= 2:
                    screen.blit(heart_image,(55,5))
                    if lives == 3:
                        screen.blit(heart_image,(105,5))
            
            for i in range(5): 
                    bubbles[i].draw(screen)
                    bubbles[i].update()
                    if bubbles[i].collision(player):
                        sound_bubble.play()
                        score += 1
                        bubbles[i].delete()  
                         
            enemies.draw(screen)
            enemies.update()
            if enemies.collision(player):
                sound_dead.play()
                enemies.delete()
                lives -= 1
         
            player.draw(screen) 
            player.update(stage)
        
    with mp_holistic.Holistic(min_detection_confidence=0.8,min_tracking_confidence=0.8) as holistic:
        while run: 
            
            clock.tick(fps)
            data,frame = capture.read()
            frame=cv.flip(frame, 1)
            imag,stage = process(frame,mp_drawing,mp_holistic,holistic,side)
            
            cv.imshow('camera',imag)
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    run = False   
            
            redraw()
                            
    capture.release() 
    cv.destroyAllWindows()           

def progress():
    global minang, maxang,t, side
    
    if side==0:
        arm='Left'
    else: 
        arm='Right'
        
    elapsed = time.time()-t
    file=open("PROGRESO.csv","a",newline="")
    writer=csv.writer(file)
    try:
        pd.read_csv('PROGRESO.csv')
    except:
        writer.writerow(['Date','Session duration (s)','Chosen arm', 'Min. angle','Max. angle'])
            
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    info=(date,elapsed,arm,minang,maxang)
    writer.writerow(info)
    file.close()  
       
def main():
    global t, side
    
    #interfaz
    data,user = If.main()
    
    #pygame
    title_font = py.font.SysFont("georgia", 70)
    run = True
    r_button = button(right_image,500,0.2)
    l_button = button(left_image,200,0.2)
    while run:
        screen.blit(back_image,(0,0))
        screen.blit(first_image,(WIDTH/2 - first_image.get_width()/2,10))
        if r_button.draw():
            side = 1
        elif l_button.draw():
            side = 0
        
        title_label = title_font.render("Choose one...",1,(255,255,255))
        screen.blit(title_label,(WIDTH/2 - title_label.get_width()/2, 300))
        py.display.update()
        if side != None:
            t = time.time()
            game(side)
            run = False
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
    
    cv.destroyAllWindows() 
    py.quit()

if __name__=="__main__":
    main()