import os
from os.path import isfile, join
import time
prompt = 'Please enter directory name\n'
prompt2 = 'Please enter min file size\n'

mypath = input(prompt)
min_size = int(input(prompt2))
for f in os.listdir(mypath):
    if os.path.isfile(join(mypath,f)) == True:
        if os.path.getsize(join(mypath,f)) > min_size:
            stats = os.stat(join(mypath,f))
            last_modified = time.ctime(stats.st_mtime)
            size = os.path.getsize(join(mypath,f))
            fmt = 'Filename: {}\t Size: {}\t Last Modified {}'
            print(fmt.format(f, size, last_modified))