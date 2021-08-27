import os
from datetime import datetime

# Functions to get file access times in human terms

def get_stat(filepath):
    so = os.stat(filepath)
    modtime = datetime.fromtimestamp(so.st_mtime)
    createtime = datetime.fromtimestamp(so.st_ctime)
    atime = datetime.fromtimestamp(so.st_atime)
    return [createtime, modtime, atime]

def print_stat(filepath, timelist):
    print('Full file path:\t', filepath, '\n')
    print('Created Win10 (ctime)\t\t', timelist[0])
    print('Modified (mtime)\t\t', timelist[1])
    print('Most recent access (atime)\t', timelist[2])
    print('---')

# Demo

path = 'Example_Files'         # Temp hard path!
fp   = os.path.abspath(path)   # Excessive fully articulated path!
fl   = os.listdir(fp)

print('---')
for f in fl:
    nf = os.path.join(fp, f)
    el = get_stat(nf)
    print_stat(nf, el)
