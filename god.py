# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *
from scenes import *

class God(object):
    u"""神クラス"""
    u"""
    スペースキーで神降臨。神モード時は時間が全停止。マウス移動で石化するキャラを選べる
    任意のキャラをクリック、またはスペースキーを再度押すことで神モード解除
    神モードに使用回数をつける？
    """
    pass