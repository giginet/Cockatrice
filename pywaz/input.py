# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class Key(object):    
    def __init__(self):
        raise NotImplementedError
    
    @classmethod
    def poll(cls):
        cls._keyin = pygame.key.get_pressed()
    
    @classmethod
    def is_press(cls, key):
        return pygame.key.get_focused() and cls._keyin[key]
    
    @classmethod
    def is_release(cls, key):
        return pygame.key.get_focused() and not cls._keyin[key]

class Mouse(object):
    
    def __init__(self):
        raise NotImplementedError
    
    @staticmethod
    def is_press(key):
        MOUSENAME = {'LEFT':0,
                 'CENTER':1,
                 'RIGHT':2
        }
        return pygame.mouse.get_pressed()[MOUSENAME[key]]
    
    @staticmethod
    def get_pos():
        return pygame.mouse.get_pos()
    
    @staticmethod
    def show_cursol():
        pygame.mouse.set_visible(True)
        
    @staticmethod
    def hide_cursol():
        pygame.mouse.set_visible(False)
        
class JoyPad(object):
    pass