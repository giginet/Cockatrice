# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *
from map import *


class TitleScene(Scene):
    def __init__(self):
        self.image = Image(10,10,100,100,u"resources/image/kawaz.png")
        
    def act(self):
        if Mouse.is_press("RIGHT"):
            Game.get_scene_manager().change_scene('main')
        
    def render(self):
        self.image.render()


class MainScene(Scene):
    def __init__(self):
        #テスト用マップ
        self.map = Map((
                    (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
                    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
                    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
                    (1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
                    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
                    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
                    (1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1),
                    (1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1),
                    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
                    (1,0,0,0,0,0,2,2,2,2,0,0,0,0,0,1),
                    (1,0,0,0,0,0,2,2,2,2,0,0,0,0,0,1),
                    (1,0,0,0,0,0,2,2,2,2,0,0,0,0,0,1),
                    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
                    (1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1),
        ),(
           Stone(5, 1),
           Stone(3,4),
           Stone(5,9),
        ))
        
    def act(self):
        self.map.act()
        
    def render(self):
        self.map.render()
