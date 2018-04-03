#!/usr/bin/python
# encoding: utf-8


"""
author: 大圣
contact: 626494970@qq.com 
@file: demo_9.py
@time: 2018/3/23 0023 下午 8:24
@welcome to learn ai
"""

class Point(object):
    def __init__(self,*c):
        self.c = c

    def dist(self,p2):
        dist = 0
        if len(self.c) != len(p2.c) :
            print('can not compute distance')
            return -1

        for i1,i2 in zip(self.c,p2.c):
            if i1 <0 or i2 < 0:
                dist  = -1
                break
            dist += (i1-i2)**2
        else :
            dist = dist ** 0.5
        return dist


# p1 = Point(1,2,3,4,5)
# p2 = Point(2,3,3,2,4)
#
# print p1.dist(p2)
# print p2.dist(p1)