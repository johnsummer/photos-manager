#! /usr/bin/env python

import subprocess
import sys
import chardet
import os

def BackupOneFolder(sourceFolder, destinationFolder):

    # if sourceFolder is None or destinationFolder is None:

    command = ["robocopy", "/MIR", sourceFolder, destinationFolder]

    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # sys.stdout.buffer.write(res.stdout)

    print(res.stdout.decode(chardet.detect(res.stdout)["encoding"]))

def SynchronizeFolders(sourceParentFolder, destinationParentFolder):

    # List sub folders of sourceParentFolder and destinationParentFolder
    sourceSubFolders = os.listdir(sourceParentFolder)
    destinationSubFolders = os.listdir(destinationParentFolder)

    # Find the pair of folders having same name from source list and destinaition list of sub folders
    # and synchronize

    sourceSubFolders.sort()
    destinationSubFolders.sort()

    indexDestSubFolder = 0

    for sourceSubFolder in sourceSubFolders:
        if sourceSubFolder < destinationSubFolders[indexDestSubFolder]:
            continue
        elif sourceSubFolder == destinationSubFolders[indexDestSubFolder]:
            BackupOneFolder(sourceParentFolder + "/" + sourceSubFolder, \
            destinationParentFolder + "/" + destinationSubFolders[indexDestSubFolder])
        else:
            while(sourceSubFolder > destinationSubFolders[indexDestSubFolder]):
                indexDestSubFolder = indexDestSubFolder + 1
            if indexDestSubFolder >= len(destinationSubFolders):
                break
            if sourceSubFolder == destinationSubFolders[indexDestSubFolder]:
                BackupOneFolder(sourceParentFolder + "/" + sourceSubFolder, \
                destinationParentFolder + "/" + destinationSubFolders[indexDestSubFolder])


# For test
if __name__ == "__main__":

    # BackupOneFolder(str(sys.argv[1]), str(sys.argv[2]))
    SynchronizeFolders(str(sys.argv[1]), str(sys.argv[2]))
