# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *

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
        self.image = Image(100,100,100,100,u"resources/image/kawaz.png")
        
    def act(self):
        if Mouse.is_press("RIGHT"):
            Game.get_scene_manager().change_scene('main')
        
    def render(self):
        self.image.render()
