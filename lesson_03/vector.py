#!/usr/bin/python
# encoding: utf-8
from __future__ import print_function

"""
author: 大圣
contact: 626494970@qq.com
@file: vector.py
@time: 2018/4/3 0003 下午 12:39

"""

from point import Point
class Vector(Point):

    def norm(self):
        o = Point([0 for i in self.cor])
        return self.dist(o)

    def dot(self,v2):
        result = 0
        for i,j in zip(self.cor,v2.cor):
            result += i*j
        return result

    def cosin(self,v2):
        pass