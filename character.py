# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *
from scenes import *

class Character(object):
    _path = u"resources/image/human.png" 
    
    u"""キャラクター抽象クラス"""
    def __init__(self, mx, my):
        pass
    
class Monster(Character):
    pass

class Human(Character):
    def __init__(self, mx, my):
        super(Human, self).__init(mx, my)
        self._stone = True