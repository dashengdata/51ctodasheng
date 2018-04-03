import unittest
from lesson_03.point import Point


class MyTestCase(unittest.TestCase):
    def test_dist(self):
        p1 = Point((0,1,1))
        p2 = Point((2,1,4))
        dist = 13 ** 0.5
        r1 = p1.dist(p2)
        r2 = p2.dist(p1)

        self.assertTrue(dist == r1,'Point.dist test failed,{0},{1} !!!'.format(dist,r1))
        self.assertTrue(dist == r2,'Point.dist test failed,{0},{1} !!!'.format(dist,r2))


if __name__ == '__main__':
    unittest.main()
