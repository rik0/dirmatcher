import bimap

__author__ = 'enrico'

import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bimap = bimap.Bimap()

    def test_add(self):
        self.assertEquals(len(self.bimap), 0)
        left = 'foo'
        right = 'bar'
        self.bimap.add(left, right)
        self.assertEquals(len(self.bimap), 1)
        self.assertEquals(self.bimap[left], right)


if __name__ == '__main__':
    unittest.main()
