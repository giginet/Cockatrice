# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from input import *

class Window(object):
    def __init__(self, width=640, height=480, caption=u"Hello, World"):
        self.window = pygame.display.set_mode( (width, height) ) # 画面を作る
        pygame.display.set_caption(caption) # タイトル
        pygame.display.flip() # 画面を反映
        
    def blit(self, image, imagerect):
        self.window.blit(image, imagerect)
        
    def fill(self, tuple):
        self.window.fill(tuple)
   
class SceneManager(object):
    def __init__(self):
        self._scenes_queue = []
        
    def set_scene(self, scene):
        self._scenes_queue.push(scene)
    
    def set_scenes(self, queue):
        self._scenes_queue = queue
        
    def change_scene(self, key):
        self._scenes_queue.pop(0)
        
    @property
    def current_scene(self):
        if self.is_empty():
            return None
        return self._scenes_queue[0]
    
    def is_empty(self):
        return len(self._scenes_queue) == 0
        
    def act(self):
        if not self.is_empty():
            self.current_scene.act()
    
    def render(self):
        if not self.is_empty():
            self.current_scene.render()
        
        
class Scene(object):
    key = u"AbstractScene"
    
    def act(self):
        raise NotImplementedError
    
    def render(self):
        raise NotImplementedError
             
class Game(object):
    _screen = Window(caption=u"Hello,Kawaz!")
    _clock = pygame.time.Clock()
    _scene_manager = SceneManager()
    
    @classmethod
    def get_screen(cls):
        return cls._screen
    
    @classmethod
    def act(cls):
        cls._scene_manager.act()
        
    @classmethod
    def render(cls):
        cls._scene_manager.render()
        
    @classmethod
    def get_scene_manager(cls):
        return cls._scene_manager
    
    @classmethod
    def mainloop(cls):
        while 1:
            cls._clock.tick(60)
            cls._screen.fill((0,0,0)) # 画面のクリア
            Key.poll()
            cls.act()
            cls.render()
            pygame.display.flip() # 画面を反映
            for event in pygame.event.get(): # イベントチェック
                if event.type == QUIT: # 終了が押された？
                    return
                if (event.type == KEYDOWN and
                    event.key  == K_ESCAPE): # ESCが押された？
                    return