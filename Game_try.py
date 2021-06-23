# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 22:47:12 2021

@author: diana
"""
import random
import pygame as py

movement=0
WIDHT, HEIGHT = 900, 700
screen=py.display.set_mode([WIDHT,HEIGHT])
py.display.set_caption("Rehab Videogame")
back_color=(74,164,243)
bee_width=40
bee_height=40
bee_image=py.image.load('secondbee.png')
bee_image=py.transform.scale(bee_image,(70,70))
star_image=py.image.load('star.png')
star_image=py.transform.scale(star_image,(bee_width,bee_height))
fps=60
stars=[]

class bee:

    def __init__(self):
    
        self.img=bee_image
        self.velocity=5
        self.pos_x=100
        self.pos_y=100
        
    def update(self,user_movement):
        if user_movement >= 1 and self.pos_y>0:
            self.pos_y -= self.velocity
        elif user_movement < 1 and self.pos_y <= 645:
            self.pos_y += self.velocity
        
    def draw (self,screen):
        screen.blit(self.img, (self.pos_x,self.pos_y))
        py.display.update() 

class star:
    def __init__(self):
        self.image=star_image
        self.pos_x = WIDHT+random.randint(200,600)
        self.pos_y=random.randint(10, 600)
        self.width = self.image.get_width()
              
    def update(self):
        self.pos_x -=5
        if self.pos_x < -self.width:
            self.pos_x = WIDHT + random.randint(100, 900)
            self.pos_y = random.randint(10, 600)
    
    def draw(self,screen):
        screen.blit(self.image, (self.pos_x,self.pos_y))
        py.display.update()
        

def main():
    player=bee()
    for i in range(3): stars.append(star())
    clock=py.time.Clock() 
    run = True
    try:
        while run: 
            clock.tick(fps)
            for event in py.event.get():
                if event.type == py.QUIT:
                    run = False
            movement=1
            screen.fill(back_color)
            player.draw(screen)  
            player.update(movement)
            for i in range(3): 
                stars[i].draw(screen)
                stars[i].update()
            
        py.quit()
    except:
        print('lol')

  
if __name__=="__main__":
    main() 
      
        
        