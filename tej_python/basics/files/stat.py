import os
from datetime import*
f=os.stat("file.py")
print (f)

print ("**********",datetime.fromtimestamp(f.st_mtime))
