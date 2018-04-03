#!/usr/bin/python
# encoding: utf-8


"""
author: 大圣
contact: 626494970@qq.com 
@file: demo_7.py
@time: 2018/3/23 0023 下午 7:40
@welcome to learn ai
"""

def myopen(filename):
    f = open(filename)
    for line in f :
        #do somethine
        result = line
        yield result
    f.close()

logs = myopen('test.log')
for line in logs:
    print(line)

