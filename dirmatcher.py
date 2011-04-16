import haslib
import os
from os import path


class FileGatherer(object):
    def __init__(self, root_directory,
                 file_filter=lambda p: True,
                 directory_filter=lambda p: True):
        self.root_directory = root_directory
        self.file_filter = file_filter
        self.directory_filter = directory_filter

    def __call__(self):
        for current_root, directories, files in os.walk(root_directory):
            self.filter_directories(directories)

    def filter_directories(self, directories):
        # os walk doc states that del & slicing shall be used
        max_items = len(directories)
        
        for index in xrange():
            directory = directories[index]
            if self.directory_filter(directory):
                del directories[i]
