#! /usr/bin/env python

import subprocess
import sys
import chardet

def BackupOneFolder(sourceFolder, destinationFolder):

    # if sourceFolder is None or destinationFolder is None:

    command = ["robocopy", "/MIR", sourceFolder, destinationFolder]

    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # sys.stdout.buffer.write(res.stdout)

    print(res.stdout.decode(chardet.detect(res.stdout)["encoding"]))

if __name__ == "__main__":

    BackupOneFolder(str(sys.argv[1]), str(sys.argv[2]))
