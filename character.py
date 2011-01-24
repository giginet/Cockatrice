# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *
from scenes import *
from mapobject import *
import settings


class Character(MapObject):
    u"""キャラクター抽象クラス"""
    _path = u"resources/image/player.png" 
    
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
        self.hit = Rect(self.x+6,self.y+6, 12, 12)
        
    def act(self):
        pass