import collections

class Bimap(collections.Sequence):
    def __init__(self):
        self.left = dict()
        self.right = dict()

    def add(self, left_el, right_el):
        self.left[left_el] = right_el
        self.right[right_el] = left_el

    def __str__(self):
        return '{<%s, %s>}' % ''.join(self.left.iteritems())

    def __len__(self):
        assert len(self.left) == len(self.right)
        return len(self.left)

    def __getitem__(self, index):
        return self.left[index]

