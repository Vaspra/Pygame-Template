# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 00:40:43 2018

@author: cold-
"""

from global_store import global_dict as glo

class Window():
    '''
    Basic window class including a display reference, update, apply input
    and update display methods.
    '''
    
    def __init__(self):
        
        self.display = glo['main'].display
        self.active = False
        
    def update(self):
        
        self.apply_input()
        self.update_display()
        
    def apply_input(self):
        pass
    
    def update_display(self):
        pass