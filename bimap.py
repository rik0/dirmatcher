import collections

class Bimap(collections.Sequence):
    class PairProxy(object):
        def __init__(self, delegate, attribute_name):
            self.delegate = delegate
            self.attribute_name = attribute_name

        def __str__(self):
            return str(self.delegate)

        def __getattr__(self, item):
            this = getattr(self.delegate, self.attribute_name)
            return getattr(this, item)

    class Pair(collections.namedtuple('Pair', 'left, right')):
        def left_view(self):
            return Bimap.PairProxy(self, 'left')

        def right_view(self):
            return Bimap.PairProxy(self, 'right')

        def __str__(self):
            return '<%s, %s>' % self

    def __init__(self):
        self.left = set()
        self.right = set()
        self.pairs = set()

    def add(self, left_el, right_el):
        pair = Bimap.Pair(left_el, right_el)
        self.pairs.add(pair)
        self.left.add(pair.left_view())
        self.right.add(pair.right_view())

    def __str__(self):
        return '{%s}' % ''.join(
            str(pair) for pair in self.pairs
        )

    def __len__(self):
        assert len(self.pairs) == len(self.left) == len(self.right)
        return len(self.pairs)

    def __getitem__(self, index):
        return self.left[index].right

