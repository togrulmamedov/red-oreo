from __future__ import print_function

import os
import sys


class PVMergeTool(object):
    """Class for merging files into .txt with a parent path name."""
    topDir = '/home/pv/Downloads/JUnzips/'
    fileType = '.txt'

    def __init__(self, initial_directory = None, last_directory = None):
        if initial_directory is None and last_directory is None:
            print(self.start())
        else:
            print(self.start(initial_directory, last_directory))

    def start(self, initial_directory = None, last_directory = None):
        """Here starts merging."""
        print ('Initializing...')
        if initial_directory is None and last_directory is None:
            print (os.getcwd())
            os.path.walk(self.topDir, self.learn, self.fileType)
        else:
            print('Initial directory: %s' % initial_directory)
            print('Last directory: %s' % last_directory)

    def learn(self, ext, dirname, titles):
        """Go through all directories."""
        ext = ext.lower()
        fileContent = ''
        for title in titles:
            if title.lower().endswith(ext):
                print("Working on %s" % title)
                with open(os.path.join(dirname, title), 'r') as infile:
                    fileContent += infile.read()
                fileToWrite = "/home/pv/Downloads/Merged/" + os.path.basename(dirname) + ".txt"
                with open(fileToWrite, 'w') as outfile:
                    outfile.write(fileContent)

#                print (os.path.join(dirname, title))
#                print ("Basename = ", os.path.basename(dirname))


pv = PVMergeTool()