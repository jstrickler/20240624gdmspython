import sys
import os.path

for f in sys.argv[1:]:
    if os.path.isdir(f):
        os.path.is
        print(f"{f} is a directory")
        continue
    else:
        # size = os.stat(f).st_size
        print(f, os.path.getsize(f))
