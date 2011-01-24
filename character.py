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
    
    def render(self):
        super(Character, self).render()
        
    def get_local_point(self):
        return self.mx, self.my
    
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
        pass