
#!/usr/bin/python
import os, sys
# Create directory
dirName = 'newFolder'

try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory ", dirName, " Created ")
except FileExistsError:
    print("Directory ", dirName, " already exists")



#foldername = sys.argv[0]
#os.mkdir(foldername)
