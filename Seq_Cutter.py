import sys
import re


# Input File
F1 = open(sys.argv[1],"r")

Seq = 0
N_File = 1

for i in F1:
	if re.search(">",i) and Seq > 0:
            F2.close()
	    Seq +=1
            Fname = "Individual_Seqs/Salmon_Protein_" + str(Seq) + ".fa"
            F2 = open(Fname,"w")
    
	if re.search(">",i) and Seq == 0:
	    Seq +=1
            Fname = "Individual_Seqs/Salmon_Protein_" + str(Seq) + ".fa"
            F2 = open(Fname,"w")
                

        F2.write(i)

F1.close()
F2.close()
