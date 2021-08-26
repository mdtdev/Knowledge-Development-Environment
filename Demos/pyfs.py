import os
from datetime import datetime, timezone

# Temp hard path
path = 'Example_Files/z.md'

# Get the status of the specified path
statusObj = os.stat(path)

# Print the status object of the path
#print('\n', statusObj, '\n')

# Do some translations and fixing for humans readability
modified = datetime.fromtimestamp(statusObj.st_mtime)
created_windows = datetime.fromtimestamp(statusObj.st_ctime)
atimev = datetime.fromtimestamp(statusObj.st_atime)

# Here is some sample output...
print('---')
print('Full file path:\t', os.path.abspath(path), '\n---')
print('Modified (mtime)\t\t', modified)
print('Most recent access (atime)\t', atimev)
print('Created Win10 (ctime)\t\t', created_windows)
print('---\n')
