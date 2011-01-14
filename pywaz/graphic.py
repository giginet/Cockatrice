# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from core import *
import os

class Obj(object):
    def __init__(self, x=0, y=0, w=100, h=100):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.angle = 0
        self.xscale = 1
        self.yscale = 1
        self.alpha = 1
        self.rect = pygame.rect.Rect(x, y, w, h)
        
    def act(self):
        pass
    
    def render(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.w = self.width
        self.rect.h = self.height
        
    def rotate(self, n):
        self.angle = n

class Image(Obj):
    def __init__(self, x=0 ,y=0 ,w=100, h=100, path=u""):
        super(Image, self).__init__(x,y,w,h)
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect()
        print x
        
    def render(self, x=None, y=None):
        super(Image, self).render()
        Game.get_screen().blit(self.image, self.rect)
        
class Font(Obj): 
    def __init__(self, string=u"", size=16):
        super(Font, self).__init__()
        font_path = os.path.join('/Library/Fonts','Osaka.ttf')
        self._font = pygame.font.Font(font_path, size)
        
        self._string = string
        self._color = (255, 255, 255)
        _generate_text()
        
    def resize(self, size):
        self._font = pygame.font.Font(None, size)
        _generate_text()
    
    def set_color(self, color):
        self._color = color
        _generate_text()
    
    def _generate_text(self):
        self._text = _font.render(self._string, True, self._color)
    
    def draw(self, string=u""):
        if string:
            self._string = string
            _generate_text()
        Game._screen.blit(text, (self.x,self.y))