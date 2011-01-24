# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.utils import *
from pywaz.graphic import *
from character import *
from mapobject import *
import settings

class Map(object):
    u"""全体マップクラス"""
    def __init__(self, matrix=(())):
        self.x = 0
        self.y = 0
        self.generate_map(matrix)
        self.humans = []
        self.my = Mychara(1,1)
    
    def act(self):
        #キーの入力を取ってキャラを動かす
        v = Vector()
        if Key.is_press(K_LEFT):
            v.x -= 1
        elif Key.is_press(K_RIGHT):
            v.x +=1
                       
        if Key.is_press(K_UP):
            v.y -=1
        elif Key.is_press(K_DOWN):
            v.y +=1
        self.my = self._move(self.my,v)
        self.my.act()
    
    def _move(self, obj, v):
        u"""objをvの分だけ移動させる。マップチップとの当たりも取る"""
        v.resize(settings.SPEED)
        obj.move(v)
        r = Vector()
        chips = []
        x, y = Map.global_to_local(obj.x, obj.y)
        
        if v.x > 0:
            chips = [self.get_chip(x+1, y), self.get_chip(x+1, y+1), self.get_chip(x+1, y-1)]
        elif v.x < 0:
            chips = [self.get_chip(x, y), self.get_chip(x, y+1), self.get_chip(x, y-1)]
        for c in chips:
            if not c or (obj.hit_test(c) and not c.can_walk()):
                #何かに当たってる
                if v.x > 0:
                    pre_chip = self.get_chip(x-1, y)
                    if pre_chip:
                        r.x = pre_chip.get_bounds()['xmax'] - obj.get_bounds()['xmin'] 
                elif v.x < 0:
                    pre_chip = self.get_chip(x+1, y)
                    if pre_chip:
                        r.x = pre_chip.get_bounds()['xmin'] - obj.get_bounds()['xmin'] 
                break
        
        if v.y > 0:
            chips = [self.get_chip(x, y+1), self.get_chip(x+1, y+1), self.get_chip(x-1, y+1)]
        elif v.y < 0:
            chips = [self.get_chip(x, y), self.get_chip(x+1, y), self.get_chip(x-1, y)]
        for c in chips:
            if not c or (obj.hit_test(c) and not c.can_walk()):
                #何かに当たってる
                if v.y > 0:
                    pre_chip = self.get_chip(x, y-1)
                    if pre_chip:
                        r.y = pre_chip.get_bounds()['ymax'] - obj.get_bounds()['ymin'] 
                elif v.y < 0:
                    pre_chip = self.get_chip(x, y+1)
                    if pre_chip:
                        r.y = pre_chip.get_bounds()['ymin'] - obj.get_bounds()['ymin'] 
                break
        
        obj.move(r)
        return obj
        
    
    def render(self):
        u"""マップ全体を描画"""
        #マップチップ描画
        for column in self._map:
            for chip in column:
                chip.render()
        #オブジェクト描画
        
        self.my.render()

    def generate_map(self, matrix):
        u"""生の配列を元にマップを生成する
        可読性のため、row_matrixは転置行列である"""
        self._raw_matrix = matrix
        self._map = []
        cls = (Floor,Wall,Water)
        for y, row in enumerate(self._raw_matrix):
            column = []
            for x, k in enumerate(row):
                column.append(cls[k](x,y))
            self._map.append(column)
            
    def get_chip(self,x ,y):
        try:
            return self._map[y][x]
        except:
            return None
    
    @classmethod
    def local_to_global(cls, mx, my):
        pass
    
    @classmethod
    def global_to_local(cls,x ,y):
        u"""全体座標をマップ座標に変換する"""
        mx = (x - settings.MARGINX)/settings.CHIPSIZE
        my = (y - settings.MARGINY)/settings.CHIPSIZE
        return int(mx), int(my)
    
class Chip(MapObject):
    u"""チップの基底クラス"""
    _can_walk = True
    _can_through = True
    _name = u"上層チップ"
    _path = u'resources/image/chip.png'
    
    def can_walk(self):
        u"""通行可能かどうかをbooleanで返す"""
        return self._can_walk
        
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