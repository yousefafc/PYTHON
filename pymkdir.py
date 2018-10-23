
#!/usr/bin/python
import os, sys
path = ps.getwed()
path = "/tmp/year"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)




#foldername = sys.argv[1]
#os.mkdir(foldername)
