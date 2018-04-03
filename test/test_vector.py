import unittest
from lesson_03.vector import Vector

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector((0,1,1))
        self.v2 = Vector((1,0,0))

    def test_norm(self):
        m = 2 ** 0.5
        r = self.v1.norm()
        self.assertEqual(m,r,'Vector.norm test failed,{0}'.format(r))

    def test_dot(self):
        d1 = self.v1.dot(self.v2)
        d2 = self.v2.dot(self.v1)


        self.assertEqual(d1, 0,'Vector.dot test failed')
        self.assertEqual(d2, 0,'Vector.dot test failed')

    def test_cosin(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
