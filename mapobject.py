# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.utils import *
from pywaz.graphic import *
from character import *
import settings

class MapObject(Image):
    u"""マップ上に存在する物全ての基底クラス
    モンスター、罠、アイテム？、人間
    """
    _path = "resources/image/player.png"
    
    def __init__(self, mx, my):
        self.mx = mx
        self.my = my
        gp = self.get_global_point()
        super(MapObject, self).__init__(x=gp[0], y=gp[1], path=self._path)
        
    def render(self):
        u"""オブジェクトを描画する"""
        gp = self.get_global_point()
        super(MapObject, self).render()    

    def get_local_point(self):
        return self.mx, self.my
    
    def get_global_point(self):
        return self.mx*settings.CHIPSIZE+settings.MARGINX, self.my*settings.CHIPSIZE+settings.MARGINY
    
    def move(self, v):
        super(MapObject, self).move(v)
        self.mx = int((self.x - settings.MARGINX)/settings.CHIPSIZE)
        self.my = int((self.y - settings.MARGINY)/settings.CHIPSIZE)
        