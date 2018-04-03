#!/usr/bin/python
# encoding: utf-8

from __future__ import  print_function

"""
author: 大圣
contact: 626494970@qq.com 
@file: demo_5.py
@time: 2018/3/23 0023 下午 6:15
@welcome to learn ai
"""
import time

t1 = time.time()
y = xrange(1,10000000)
t2 = time.time()
x = range(1,10000000)
t3 = time.time()

print(t2-t1,t3-t2)