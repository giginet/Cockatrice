# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *

class MainScene(Scene):
    def __init__(self):
        self.image = Image(0,0,100,100,u"resources/kawaz.png")
        
    def act(self):
        if Key.is_press(K_a):
            self.image.x += 1
        if Mouse.is_press("RIGHT"):
            self.image.x -= 1
        
    def render(self):
        self.image.render()

def main():
    pygame.init() # pygameの初期化
    Game.get_scene_manager().set_scenes((MainScene(),))
    return Game.mainloop()

if __name__ == '__main__': main()