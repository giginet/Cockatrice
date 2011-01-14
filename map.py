# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.utils import *
from pywaz.graphic import *

CHIPSIZE = 24

class Map(object):
    u"""全体マップクラス"""
    def __init__(self, matrix):
        self.matrix = [[]]
        self.x = 0
        self.y = 0
        
    def render(self):
        u"""マップ全体を描画"""
        pass
    
class Chip(Image):
    u"""チップの抽象クラス"""
    self._can_through = True
    self._name = u"上層チップ"
    self._path = u'resources/image/chip.png'
    
    def __init__(self, mx, my):
        super(Chip, self).__init__(x=mx*CHIPSIZE, y=my*CHIPSIZE, path=self._path)
        self.mx = mx
        self.my = my
        
    def can_through(self):
        return self._can_through
        
class Wall(Chip):
    u"""壁クラス"""
    self._can_through = False
    self._name = u'壁'
    self._path = u'resources/image/wall.png'
          
class Floor(Chip):
    u"""床クラス"""
    self.__can_through = True
    self.__name = u'床'
    self._path = u'resources/image/floor.png'
    