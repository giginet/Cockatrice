# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *
from scenes import *

CHIPSIZE = 24

class Character(Image):
    _path = u"resources/image/player.png" 
    
    u"""キャラクター抽象クラス"""
    def __init__(self, mx, my):
        self.mx = mx
        self.my = my
        self.x = mx*24
        self.y = my*24
        super(Character, self).__init__(x=mx*CHIPSIZE, y=my*CHIPSIZE, path=self._path)
        
    def render(self):
        super(Character, self).render()
    
class Monster(Character):
    pass

class Human(Character):
    pass

class Mychara(Human):
    u"""操作キャラクラス"""
    def __init__(self, mx, my):
        super(Mychara, self).__init__(mx=mx, my=my)
        self.mx = mx
        self.my = my
        self._stone = False
        
    def act(self):
        if Key.is_press(K_LEFT):
            self.x -= 1
        elif Key.is_press(K_RIGHT):
            self.x +=1
                       
        if Key.is_press(K_UP):
            self.y -=1
        elif Key.is_press(K_DOWN):
            self.y +=1
