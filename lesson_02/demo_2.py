#!/usr/bin/python
# encoding: utf-8
from __future__ import print_function


"""
author: 大圣
contact: 626494970@qq.com 
@file: demo_2.py
@time: 2018/3/23 0023 下午 3:52
@welcome to learn ai
"""

x1 = 10
y1 = 20

x2,y2 = 14,40

dist = ( (x1-x2) ** 2 + (y1-y2)**2 ) ** 0.5

print(dist)

print(dist > 3)
