from os import listdir
from os.path import isfile
import sys
import re
import os
#############################################################################
############################ SUB PROGRAM ###################################
#############################################################################
def create_seq():
    T = ""
    for i in xrange(60):
        T += "-"
    
    return T


def format_data(File,Fish,outfile):
    F1 = open(File,"r")
    F2 = F1.readlines()
    F1.close()
    
    N = 3;Seq1 = "";Seq2 = "";Idn = ""
    for i in xrange(3,len(F2)):
        
        # Splitting Seq 1
        temp = F2[N].split()
        Seq1 += temp[1]
        
        Trans = temp[0]
        
        # Splitting Seq 2
        temp = F2[N+1].split()
        Seq2 += temp[1]
        
        N += 4
        if N >= len(F2):
            break
    
    # Find Salmon Seq length
    Seq = Seq1.replace("-","")
    Qlen = len(Seq)
    Out = open(outfile,"w")
    N = 0
    for i in xrange(1,len(Seq1)+1):
        if Seq1[i-1] == Seq2[i-1]:
            txt = Fish + "\t" + Trans + "\t" + str(i) + "\t" + str(1) + "\t" + str(Qlen) + "\n"
            #print Fish,"\t",Trans,"\t",i,"\t",1,"\t",Qlen
            Out.write(txt)
        else:
            txt = Fish + "\t" + Trans + "\t" + str(i) + "\t" + str(2) + "\t" + str(Qlen) + "\n"
            #print Fish,"\t",Trans,"\t",i,"\t",2,"\t",Qlen
            Out.write(txt)
            
    Out.close()

#############################################################################
############################ MAIN PROGRAM ###################################
#############################################################################
Files = [ f for f in listdir("ClustalW_Results/")]

N = 0
for i in Files:
    T1 = i.split("_")
    T2 = T1[2] + "_" + T1[3] 
    Trans = T2.replace(".aln","")
    
    Fname = "ClustalW_Results/" + i
    if re.search("Trout",Fname):
        Fish = "Trout"
    elif re.search("SBack",Fname):
        Fish = "Stickle"
    elif re.search("ZFish",Fname):
        Fish = "Zebra"
    else:
        Fish = "Cod"
    outfile = "Formatted_ClustalW_Output/Salmon_" + Fish + "_" + Trans +".csv"
    format_data(Fname,Fish,outfile)
    N += 1
    
    #if N >= 200:
    #    break

# Cat the Files for Plotting
for i in Files:
    T1 = i.split("_")
    T2 = T1[2] + "_" + T1[3] 
    Trans = T2.replace(".aln","")

    cat_file = "cat "
    Fname1 = "Formatted_ClustalW_Output/Salmon_Trout_" + Trans + ".csv"
    if isfile(Fname1):
        cat_file += Fname1 + " "
        
    Fname2 = "Formatted_ClustalW_Output/Salmon_Zebra_" + Trans + ".csv"
    if isfile(Fname2):
        cat_file += Fname2 + " "

    Fname3 = "Formatted_ClustalW_Output/Salmon_Stickle_" + Trans + ".csv"
    if isfile(Fname3):
        cat_file += Fname3 + " "

    Fname4 = "Formatted_ClustalW_Output/Salmon_Cod_" + Trans + ".csv"
    if isfile(Fname4):
        cat_file += Fname4 + " "
    
    cat_file += ">Formatted_Combined_For_Plot/Salmon_" + Trans + ".csv"
    os.system(cat_file)
