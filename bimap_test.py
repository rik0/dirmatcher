import bimap

__author__ = 'enrico'

import unittest

class SimpleTests(unittest.TestCase):
    def setUp(self):
        self.bimap = bimap.Bimap()

    def test_add(self):
        self.assertEquals(len(self.bimap), 0)
        left = 'foo'
        right = 'bar'
        self.bimap.add(left, right)
        self.assertEquals(len(self.bimap), 1)
        self.assertEquals(self.bimap[left], right)


class OneElementTests(unittest.TestCase):
    def setUp(self):
        self.key = 'foo'
        self.value = 'bar'
        self.bimap = bimap.Bimap()
        self.bimap,add(self.key, self.value)

    def testGetKey(self):
        self.assertEqual(self.bimap.get(self.key), self.value)
        self.assertEqual(self.bimap[self.key], self.value)
        self.assertEqual(self.bimap.left_get(self.key), self.value)

        
if __name__ == '__main__':
    unittest.main()
