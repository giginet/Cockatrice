# -*- coding: utf-8 -*-
import math

class Vector(object):
    u"""2Dベクトルを扱うクラス"""
    def __init__(self, x=0, y=0):
        self.set(x, y)
        
    def set(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, v):
        if not isinstance(v, Vector):
            raise TypeError
        self.x += v.x
        self.y += v.y
        return self
        
    def __sub__(self, v):
        if not isinstance(v, Vector):
            raise TypeError
        self.x -= v.x
        self.y -= v.y
        return self
    
    def __eq__(self, v):
        if not isinstance(v, Vector):
            raise TypeError
        return self.x == v.x and self.y == v.y
    
    def __mul__(self, v):
        if isinstance(v, Vector):
            return scalar_product(v)
        elif isinstance(v, Number):
            return scale(v)
        raise TypeError
    
    def __div__(self, n):
        self.x /= n
        self.y /= n
        return self
    
    def scale(self, n):
        self.x *= n
        self.y *= n
        return self
        
    def scalar_product(self, v):
        return v.x+self.x+v.y*self.y
        
    def length(self):
        return math.sqrt(self.x**2+self.y**2)
    
    def normalize(self):
        if self.length()==0:
            return Vector(0, 0)
        else:
            return self.scale(1/self.length())
        
    def resize(self, size):
        return self.normalize().scale(size)
    
    def angle(self):
        if self.x == 0:
            return 90
        return Vector.rad_to_deg(math.atan(self.y/self.x))
    
    def rotate(self, deg):
        rad = Vector.deg_to_rad(deg)
        x = self.x
        y = self.y
        self.x = math.sin(rad)*y+math.cos(rad)*x 
        self.y = math.cos(rad)*y-math.sin(rad)*x
        return self
            
    def clone(self):
        return Vector(self.x, self.y)
    
    def reverse(self):
        self.x *= -1
        self.y *= -1
        return self
    
    def to_pos(self):
        return (self.x, self.y)
    
    def divide(self, length):
        times = int(self.length()/length)
        mod = self.length()-length*times
        vs = []
        for i in range(times):
            vs.append(self.clone().resize(length))
        vs.append(self.clone().resize(mod))
        return vs
    
    @classmethod
    def rad_to_deg(cls, rad):
        return rad*180/math.pi
        
    @classmethod
    def deg_to_rad(cls, deg):
        return deg*math.pi/180
    
class Timer(object):
    u"""フレーム管理を行うクラス"""
    timers = []
    
    def __init__(self, m=0):
        self.init(m)
        Timer.timers.push(self)

    def init(self, m):
        _time = 0
        set(m)
        _f_active = False
        _f_loop = False
        
    def set(self, m):
        self._max = m
    
    @property
    def now(self):
        return _time
    
    def tick(self):
        count()
        if self._is_end():
            if self._f_loop:
                self.reset()
            else:
                self.kill()
                self.stop()
                
    def kill(self):
        Timer.timers.remove(self)
    
    def play(self):
        self._f_active = True
        
    def stop(self):
        self._time = 0
        self._f_active = False
        
    def pause(self):
        self._f_active = False
        
    def reset(self):
        self._time = 0
        
    def count(self):
        if self._f_active:
            self._time +=1
            
    def is_move(self):
        return self._f_active
    
    def is_end(self):
        return self._time >= self._max

    def move(self, n):
        self._time += n
        if self.is_end():
            if self._f_loop:
                self._time = self._time % self._max
            else:
                self.stop()