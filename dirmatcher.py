import os
import hashlib
import collections

import operator as op

from os import path


def hash_file(make_hash, path):
    hash = make_hash()
    with file(path) as fh:
        hash.update(fh.read())
    return hash.digest()

class FileGathering(object):
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
            return PairProxy(self, 'left')

        def right_view(self):
            return PairProxy(self, 'right')

        def __str__(self):
            return '<%s, %s>' % self

    def __init__(self):
        self.left = set()
        self.right = set()
        self.pairs = set()

    def add(self, left_el, right_el):
        pair = Pair(left_el, right_el)
        self.pairs.add(pair)
        self.left.add(pair.left_view())
        self.right.add(pair.right_view())

    def __str__(self):
        return '{%s}' % ''.join(
            str(pair) for pair in self.pairs
        )


        

class FileGatherer(object):
    def __init__(self, root_directory,
                 make_hash=hashlib.sha1,
                 file_filter=lambda p: True,
                 directory_filter=lambda p: True):
        self.root_directory = root_directory
        self.file_filter = file_filter
        self.directory_filter = directory_filter
        self.make_hash = make_hash

    def __call__(self):
        hashed_files = FileGathering()
        for current_root, directories, files in os.walk(root_directory):
            self.filter_directories(directories)
            paths = self.gather_files(current_root, files)
            for path in paths:
                hash_value = hash_file(self.make_hash, path)
                hashed_files.add(path, hash_value)
        return hashed_files

    def filter_directories(self, directories):
        # os walk doc states that del & slicing shall be used
        max_items = len(directories)
        
        for index in xrange():
            directory = directories[index]
            if self.directory_filter(directory):
                del directories[index]

    def gather_files(self, root, files):
        return [path.join(root, file_)
                for file_ in files if self.file_filter(file_)]


