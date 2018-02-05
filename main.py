# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:33:07 2018

@author: cold-
"""

from config import cfg_disp, cfg_input, cfg_color
import pygame

class Run():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(\
                        (cfg_disp['width'], cfg_disp['height']))
        pygame.display.set_caption(cfg_disp['caption'])
        
        self.exit = False
        self.gameLoop()
        pygame.quit()
        
    def gameLoop(self):
        while not self.exit:
            self.check_events()
            self.update_display()
            self.clock.tick(60)
            
        
    def check_events(self):
        cfg_input['mouse_x'], cfg_input['mouse_y'] = pygame.mouse.get_pos()
        cfg_input['mouse_0'], cfg_input['mouse_1'], cfg_input['mouse_2'] =\
            pygame.mouse.get_pressed()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
                print(event)
                
            elif event.type == pygame.KEYDOWN:
                if event.key in cfg_input.keys():
                    cfg_input[event.key] = True
                        
            elif event.type == pygame.KEYDOWN:
                if event.key in cfg_input.keys():
                    cfg_input[event.key] = False

        
    def update_display(self):
        # Fill background
        self.display.fill(cfg_color['black'])
        
        # Other display features
        
        # Update display
        pygame.display.update()
               
         
run = Run()
                
                
                
                
                
                
                
                