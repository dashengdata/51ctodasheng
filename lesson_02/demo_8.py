#!/usr/bin/python
# encoding: utf-8


"""
author: 大圣
contact: 626494970@qq.com 
@file: demo_8.py
@time: 2018/3/23 0023 下午 7:53
@welcome to learn ai
"""

# def test():
#     '''
#     this function is babalaba
#     :return: int
#     '''
#     pass
#
# print(test.__doc__)

# def add(x,y,z):
#     return x+y+z

# f = lambda x,y,z:x+y+z
#
# print(f(1,2,3))

print(abs(-100))
x = [1,2,3,-1,0,-9]

x.sort(key = lambda x: x**2)

print(x)