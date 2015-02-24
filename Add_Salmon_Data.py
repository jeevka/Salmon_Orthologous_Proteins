import sys
import re

F1 = open(sys.argv[1],"r")
F2 = F1.readlines()
N = 3
Seq1 = ""
for i in xrange(3,len(F2)):
    
    # Splitting Seq 1
    temp = F2[N].split()
    Seq1 += temp[1]
    
    Trans = temp[0]
        
    N += 4
    if N >= len(F2):
        break

# Find Salmon Seq length
Seq = Seq1.replace("-","")
Qlen = len(Seq)

for i in xrange(1,Qlen+1):
    print "Salmon","\t",Trans,"\t",i,"\t",1,"\t",Qlen