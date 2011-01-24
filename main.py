# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *
from scenes import *

def main():
    pygame.init() # pygameの初期化
    Game.get_scene_manager().set_scenes({'title':TitleScene(),'main':MainScene()})
    Game.get_scene_manager().change_scene('main')
    return Game.mainloop()

if __name__ == '__main__': main()