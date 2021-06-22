# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 22:47:12 2021

@author: diana
"""

import pygame as py
import Mano as video
import cv2 as cv


WIDHT, HEIGHT = 700, 700
screen=py.display.set_mode([WIDHT,HEIGHT])
py.display.set_caption("Rehab Videogame")
orange_color=(243,164,74)
bee_width=55
bee_height=55
bee_image=py.image.load('secondbee.png')
bee_image=py.transform.scale(bee_image,(bee_width,bee_height))
fps=60

class bee:

    def __init__(self):
    
        self.img=bee_image
        self.velocity=50
        self.pos_x=100
        self.pos_y=300
        
    def update(self,user_movement):
        if user_movement >= 25000:
            self.pos_y -= self.velocity
        else:
            self.pos_y += self.velocity
        
    def draw (self,screen):
        screen.fill(orange_color)
        screen.blit(self.img, (self.pos_x,self.pos_y))
        py.display.update() 


def main():
    
    player=bee()
    clock=py.time.Clock()
    run = True
    
    while run:
        clock.tick(fps)
        x=video.main()
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
         
        player.update(x)
        player.draw(screen)
             
    py.quit()
   
if __name__=="__main__":
    main() 
      
        
        