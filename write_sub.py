from sub import pizza_challenge
import sys


file_name = str(sys.argv[1])
a,b = pizza_challenge(file_name)
f = open(file_name.split('.')[0]+".out","w")
f.write(str(a)+'\n'+' '.join([str(x) for x in b]))
f.close()