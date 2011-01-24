# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.utils import *
from pywaz.graphic import *
from character import *
CHIPSIZE = 24

class Map(object):
    u"""全体マップクラス"""
    def __init__(self, matrix=(())):
        self.x = 0
        self.y = 0
        self.generate_map(matrix)
        self.humans = []
        self.my = Mychara(1,1)
    
    def act(self):
        self.my.act()    
    
    def render(self):
        u"""マップ全体を描画"""
        #マップチップ描画
        for column in self.map:
            for chip in column:
                chip.render()
        #オブジェクト描画
        
        self.my.render()

    def generate_map(self, matrix):
        u"""生の配列を元にマップを生成する
        可読性のため、row_matrixは転置行列である"""
        self._raw_matrix = matrix
        self.map = []
        cls = (Floor,Wall,Water)
        for y, row in enumerate(self._raw_matrix):
            column = []
            for x, k in enumerate(row):
                column.append(cls[k](x,y))
            self.map.append(column)
    
class Chip(Image):
    u"""チップの基底クラス"""
    _can_walk = True
    _can_through = True
    _name = u"上層チップ"
    _path = u'resources/image/chip.png'
    CHIPSIZE = 24
    
    def __init__(self, mx, my):
        super(Chip, self).__init__(x=mx*CHIPSIZE, y=my*CHIPSIZE, path=self._path)
        self.mx = mx
        self.my = my
        
    def can_walk(self):
        u"""通行可能かどうかをbooleanで返す"""
        return self._can_through
    
    def render(self):
        u"""マップチップを描画する"""
        super(Chip, self).render(self.mx*CHIPSIZE, self.my*CHIPSIZE)    
        
class Wall(Chip):
    u"""壁クラス"""
    _can_walk = False
    _can_through = False
    _name = u'壁'
    _path = u'resources/image/wall.png'
          
class Floor(Chip):
    u"""床クラス"""
    _can_walk = True
    _can_through = True
    _name = u'床'
    _path = u'resources/image/floor.png'
    
class Water(Chip):
    u"""水路クラス"""
    _can_walk = False
    _can_through = True
    _name = u'水'
    _path = u'resources/image/water.png'