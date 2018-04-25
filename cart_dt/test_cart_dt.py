import unittest

import sys

sys.path.append('.')
from cart_dt import gini_index, variance, entropy
import math


class CartTreeTestCase(unittest.TestCase):
    def test_gini_index(self):
        label = [1, 0, 1, 0, 1]
        gini = gini_index(label)
        r = 1 - 0.6 ** 2 - 0.4 ** 2
        self.assertEqual(gini, r)
        label = [1, 0, 1, 1, 1]
        gini = gini_index(label)
        r = 1 - 0.8 ** 2 - 0.2 ** 2
        self.assertEqual(gini, r)

    def test_variance(self):
        label = [1, 0, 1, 0, 1]
        var = variance(label)
        r = (3 * 0.4 ** 2 + 2 * 0.6 ** 2) / 5
        self.assertEqual(var, r)

    def test_entropy(self):
        label = [1, 0, 1, 0, 1]
        ent = 0.6 * math.log(0.6) + 0.4 * math.log(0.4)
        self.assertEqual(-ent, entropy(label))


if __name__ == '__main__':
    unittest.main()
