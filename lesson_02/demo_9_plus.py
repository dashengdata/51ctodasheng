#!/usr/bin/python
# encoding: utf-8


"""
author: 大圣
contact: 626494970@qq.com 
@file: demo_9_plus.py
@time: 2018/3/23 0023 下午 8:37
@welcome to learn ai
"""
from demo_9 import Point

class Vector(Point):

    def dot(self,v2):
        result = 0
        for i,j in zip(self.c,v2.c):
            result += i*j
        return result

    def cosin(self,v2):
        o = Point(*[0 for i in range(len(self.c))])
        # o = Point([0] *len(self.c))
        d1 = self.dist(o)
        d2 = v2.dist(o)

        result = 1.0 * self.dot(v2) / (d1 * d2)
        return result


v1 = Vector(0,1,0)
v2 = Vector(1,0,0)
print(v2.cosin(v2))
