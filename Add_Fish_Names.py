import re
import sys

FN = sys.argv[1]
F = open(sys.argv[2],"r")

for i in F:
	print FN,"\t",i.strip()


