import sys
import re

def pick_ortho_RBT(Fname,Fish):
    F1 = open(Fname,"r")
    ID = "NIL"
    for i in F1:
        if re.search(">",i):
            ID = i.split()[1]
            break
        
        if re.search("Query=",i):
            Qry = i.replace("Query=","")
            Qry = Qry.replace(" ","")

    print Fish,"\t",Qry.strip(),"\t",ID

    F1.close()
    
    return 0

for i in xrange(1,56001):
    Fname1 = "BLAST_Results/RBT_" + str(i) + ".out"
    Fname2 = "BLAST_Results/ZF_" + str(i) + ".out"
    Fname3 = "BLAST_Results/SB_" + str(i) + ".out"
    Fname4 = "BLAST_Results/CD_" + str(i) + ".out"
    
    pick_ortho_RBT(Fname1,"Trout")
    pick_ortho_RBT(Fname2,"ZFish")
    pick_ortho_RBT(Fname3,"SBack")
    pick_ortho_RBT(Fname4,"Cod")
    
    
