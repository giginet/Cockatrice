# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.utils import *
from pywaz.graphic import *
from character import *
import settings

class MapObject(Image):
    u"""マップ上に存在する物全ての基底クラス"""
    _path = "resources/image/player.png"
    
    def __init__(self, mx, my):
        self.mx = mx
        self.my = my
        super(MapObject, self).__init__(x=mx*settings.CHIPSIZE+settings.MARGINX, y=my*settings.CHIPSIZE+settings.MARGINY, path=self._path)
        
    def render(self):
        u"""オブジェクトを描画する"""
        super(MapObject, self).render(self.mx*settings.CHIPSIZE+settings.MARGINX, self.my*settings.CHIPSIZE+settings.MARGINY)    
