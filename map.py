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
    def __init__(self, matrix=(()), humans=()):
        self.x = 0
        self.y = 0
        self.generate_map(matrix)
        self.my = Mychara(1,1)
        self.humans = list(humans) + [self.my,]
        
    def act(self):
        #キャラを動かす
        for i, human in enumerate(self.humans):
            v = human.get_vector()    
            human = self._move(human,v)
            human.act()
            if self.my.hit_test(human) and human.is_stone():
                human = human.change_state("runaway")
                self.humans[i] = human
                human.get_route(self)
            
    def _move(self, obj, v):
        u"""objをvの分だけ移動させる。マップチップとの当たりも取る"""
        obj.move(v)
        r = Vector()
        x, y = Map.global_to_local(obj.x, obj.y)
        
        chips = [self.get_chip(x-1, y-1), self.get_chip(x, y-1), self.get_chip(x+1, y-1), 
                 self.get_chip(x-1, y), self.get_chip(x, y), self.get_chip(x+1, y),
                 self.get_chip(x-1, y+1), self.get_chip(x, y+1), self.get_chip(x+1, y+1),
        ]
        for c in chips:
            if not c or (obj.hit_test(c) and not c.can_walk()):
                #何かに当たってる
                if v.x > 0:
                    pre_chip = self.get_chip(x, y)
                    if pre_chip:
                        r.x = pre_chip.get_bounds()['xmax'] - obj.get_bounds()['xmax'] 
                elif v.x < 0:
                    pre_chip = self.get_chip(x+1, y)
                    if pre_chip:
                        r.x = pre_chip.get_bounds()['xmin'] - obj.get_bounds()['xmin'] 
                if v.y > 0:
                    pre_chip = self.get_chip(x, y)
                    if pre_chip:
                        r.y = pre_chip.get_bounds()['ymax'] - obj.get_bounds()['ymax'] 
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
        
        for human in self.humans:
            human.render()

    def generate_map(self, matrix):
        u"""生の配列を元にマップを生成する
        生データ入力時の可読性のため、row_matrixは転置行列である"""
        self._raw_matrix = matrix
        self._map = []
        cls = (Floor,Wall,Water)
        for y, row in enumerate(self._raw_matrix):
            column = []
            for x, k in enumerate(row):
                column.append(cls[k](x,y))
            self._map.append(column)
        u"""このままでは、x,yの位置関係が真逆であり、使用しにくいため、行列を転置する
        http://d.hatena.ne.jp/xon/20090327/1238133267 Pythonクックブック参照
        """
        self._map = map(list, zip(*self._map))
            
    def get_chip(self,x ,y):
        try:
            return self._map[x][y]
        except:
            return None
        
    def get_map(self):
        return self._map
    
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