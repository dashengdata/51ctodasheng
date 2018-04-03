#!/usr/bin/python
# encoding: utf-8
from __future__ import print_function

"""
author: 大圣
contact: 626494970@qq.com
@file: point.py
@time: 2018/4/3 0003 下午 12:38

"""

class Point(object):
    def __init__(self,cor):
        self.cor = cor

    def dist(self,p2):
        dist = 0
        if len(self.cor) != len(p2.cor) :
            print('can not compute distance')
            return -1

        for i1,i2 in zip(self.cor,p2.cor):
            if i1 <0 or i2 < 0:
                dist  = -1
                break
            dist += (i1-i2)**2
        else :
            dist = dist ** 0.5
        return dist


if __name__ == '__main__':
    p = Point((1,2,3))
    print(p.__dict__)

