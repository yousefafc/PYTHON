
#!/usr/bin/python
import sys
firstarg = sys.argv[1]
# ["./pycat", "example.txt"]
f = open(sys.argv[1], 'r')
file_contents = f.read()
print (file_contents)
f.close()
