#!/usr/bin/python
# encoding: utf-8
from __future__ import print_function

"""
author: 大圣
contact: 626494970@qq.com
@file: tree_example.py
@time: 2018/4/25 0025 下午 2:47

"""
# from cart_dt import CartTree
from cart_dt_v2 import CartTree,entropy,gini_index
import pandas as pd
from plot_tools import plot, dotgraph
import pydotplus

df = pd.read_csv('iris.csv')
col_names = df.columns

y = df.pop('Name')
X = df.values
print(X.shape)

ev_names = ['entropy','gini_index' ]
ev_funcs = [entropy,gini_index ]
for n,f in zip(ev_names,ev_funcs):
    tree = CartTree(eval_func=f)
    tree.fit(X, y)
    print(tree.predict([[6.0, 2.2, 5.0, 1.5]]))


    result = plot(tree.root_node, col_names)
    print(result)

    dot_data = dotgraph(tree.root_node, col_names)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("iris_{0}.pdf".format(n))
    graph.write_png("iris_{0}.png".format(n))


