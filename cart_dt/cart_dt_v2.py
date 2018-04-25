#!/usr/bin/python
# encoding: utf-8
from __future__ import print_function
from collections import defaultdict

"""
author: 大圣
contact: 626494970@qq.com
@file: cart_dt.py
@time: 2018/4/25 0025 下午 1:14

"""
import pandas as pd
import numpy as np
import math


def entropy(label):
    data = pd.DataFrame()

    data['label'] = label
    groups = data.groupby('label').size()
    ent = 0.0
    for g in groups:
        p = g * 1.0 / data.shape[0]
        ent -= p * math.log(p)
    return ent


def variance(label):
    if len(label) == 0:
        return 0
    x = np.array(label)
    mu = np.mean(x)
    var = np.sum((x - mu) ** 2) / len(label)
    return var


def gini_index(label):
    data = pd.DataFrame()

    data['label'] = label
    groups = data.groupby('label').size()
    gini = 0.0
    for g in groups:
        p = g * 1.0 / data.shape[0]
        gini += p ** 2
    return 1 - gini


class Node(object):
    """Binary tree implementation with true and false branch. """

    def __init__(self, col=-1, value=None,
                 true_branch=None, false_branch=None,
                 results=None, summary=None):
        self.col = col
        self.value = value
        self.true_branch = true_branch
        self.false_branch = false_branch
        self.results = results  # None for nodes, not None for leaves
        self.summary = summary


class CartTree(object):
    def __init__(self, max_depth=3, min_cov_records=10, eval_func=gini_index):
        self.eval_func = eval_func
        self.root_node = None
        self.max_depth = max_depth
        self.min_cov_records = min_cov_records

    def _split_dataset(self, X, y, col_idx, value):
        split_func = None
        if isinstance(value, float):
            split_func = lambda row: row[col_idx] > value
        else:
            split_func = lambda row: row[col_idx] == value

        X1, y1, X2, y2 = [], [], [], []
        for one_x, one_y in zip(X, y):
            if split_func(one_x):
                X1.append(one_x)
                y1.append(one_y)
            else:
                X2.append(one_x)
                y2.append(one_y)

        return X1, y1, X2, y2

    def _make_leaf_node(self, y, dcY):
        k_dict = defaultdict(int)
        for one_y in y:
            k_dict[one_y] += 1

        return Node(results=k_dict, summary=dcY)

    def _make_tree(self, X, y, depth=0):
        if len(X) == 0:
            return Node()

        root_score = self.eval_func(y)

        best_gain = 0.0
        best_attr = None
        best_set = None

        dcY = {'impurity': '%.3f' % root_score, 'samples': '%d' % len(y)}

        if (len(y) <= self.min_cov_records) or depth >= self.max_depth:
            return self._make_leaf_node(y, dcY)

        for col in range(len(X[0])):
            uni_values = set([x[col] for x in X])
            for val in uni_values:
                X1, y1, X2, y2 = self._split_dataset(X, y, col, val)

                w = len(y1) * 1.0 / len(y)
                gain = root_score - w * self.eval_func(y1) - (1 - w) * self.eval_func(y2)
                if gain > best_gain:
                    best_gain = gain
                    best_attr = (col, val)
                    best_set = (X1, y1, X2, y2)

        if best_gain > 0:
            true_branch = self._make_tree(best_set[0], best_set[1], depth + 1)
            false_branch = self._make_tree(best_set[2], best_set[3], depth + 1)
            return Node(col=best_attr[0], value=best_attr[1],
                        true_branch=true_branch,
                        false_branch=false_branch,
                        summary=dcY)
        else:
            return self._make_leaf_node(y, dcY)

    def fit(self, X, y):
        self.root_node = self._make_tree(X, y)

    def _predict(self, x, root_node):
        if root_node.results != None:  # leaf
            k_dict = root_node.results
            k_s = sorted(k_dict, key=lambda x: x[1])
            return k_s[0]
        else:
            v = x[root_node.col]
            branch = None
            if isinstance(v, float):
                if v >= root_node.value:
                    branch = root_node.true_branch
                else:
                    branch = root_node.false_branch
            else:
                if v == root_node.value:
                    branch = root_node.true_branch
                else:
                    branch = root_node.false_branch

        return self._predict(x, branch)

    def predict(self, X):

        """Classifies the observationss according to the tree.
        dataMissing: true or false if data are missing or not. """

        y = [self._predict(x, self.root_node) for x in X]
        return y
