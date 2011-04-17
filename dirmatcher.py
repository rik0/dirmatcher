import os
import hashlib

from os import path

import bimap

def hash_file(make_hash, path):
    hash = make_hash()
    with file(path) as fh:
        hash.update(fh.read())
    return hash.digest()

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
        hashed_files = bimap.BiMap()
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


