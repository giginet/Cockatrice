# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *
from scenes import *
from mapobject import *
from astar import *
import settings


class Character(MapObject):
    u"""キャラクター抽象クラス"""
    _path = u"resources/image/human.png"
    
    def get_vector(self):
        u"""移動するベクトルを返す"""
        return Vector()
    
class Monster(Character):
    pass

class Human(Character):
    u"""人間の抽象クラス"""
    _stone = False
    
    def is_stone(self):
        return self._stone
    
    def is_mychara(self):
        return isinstance(self, Mychara)
    
    def is_runaway(self):
        return not self.is_mychara() and not self.is_stone()
    
    def change_state(self, state):
        if state=="player":
            return Mychara(self.mx, self.my)
        elif state=="stone":
            return Stone(self.mx, self.my)
        elif state=="runaway":
            return Runaway(self.mx, self.my)
        else:
            raise ArgumentError
        
class Runaway(Human):
    u"""石化から解かれた人クラス"""
    _path = u"resources/image/human.png"
    
    def get_route(self, map):
        astar = AStar(map, self.mx, self.my)
        self.vectors = astar.get_route() 
    
    def get_vector(self):
        u"""ここにA-star実装するよ！"""
        if self.vectors and len(self.vectors) > 0:
            v = self.vectors[0]
            self.vectors = self.vectors[1:]
            return v
        return Vector(0,1)

class Stone(Human): 
    u"""石化している人クラス"""
    _stone = True
    _path = u"resources/image/stone.png" 
    
class Mychara(Human):
    u"""操作キャラクラス"""
    _path = u"resources/image/player.png" 
        
    def __init__(self, mx, my):
        super(Mychara, self).__init__(mx=mx, my=my)
        self.mx = mx
        self.my = my
        self._stone = False
        #self.hit = Rect(self.x+6,self.y+6, 12, 12)
   
    def get_vector(self):
        v = Vector()
        if Key.is_press(K_LEFT):
            v.x -= 1
        elif Key.is_press(K_RIGHT):
            v.x +=1              
        if Key.is_press(K_UP):
            v.y -=1
        elif Key.is_press(K_DOWN):
            v.y +=1
        v.resize(settings.SPEED)
        return v
    
    def act(self):
        pass