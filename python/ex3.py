import sys

name = sys.argv[1]
copy = sys.argv[2]

f = open("%s" %name, "r")
fr = open("%s" %copy, "w")
for line in f :
    fr.write(line)

fr.close()
f.close()
    

