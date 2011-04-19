import bimap

__author__ = 'enrico'

import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bimap = bimap.Bimap()

    def test_add(self):
        self.assertEquals(len(self.bimap), 0)
        self.bimap.add('foo', 'bar')
        self.assertEquals(len(self.bimap), 1)


if __name__ == '__main__':
    unittest.main()
