#!/usr/bin/python
# encoding: utf-8
from __future__ import print_function

"""
author: 大圣
contact: 626494970@qq.com
@file: iris_knn_demo.py
@time: 2018/4/3 0003 下午 8:45

"""
from knn import KNN
def prepare_data():
    X = []
    y = []

    # f = open('iris.data')
    # for line in f :
    #     line
    #
    # f.close()

    with open('iris.csv') as f:
        for id,line in enumerate(f):
            if id == 0:
                continue
            segs = line.strip().split(',')
            X.append([float(i) for i in  segs[:4]])
            y.append(segs[-1])
    return X,y

if __name__ == '__main__':
    X,y = prepare_data()
    model = KNN()
    model.fit(X,y)

    sample = [5.0,3.4,2.5,0.5]
    print(model.predict(sample,k = 5))


