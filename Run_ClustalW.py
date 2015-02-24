import sys
import re
import os

# Input File which Contains the info about Ortho
Ortho = open("Ortholog_Protein_List.csv","r")
N = 0
for i in Ortho:
    temp = i.split()
    Seq_ID = temp[2].strip()
    
    ##################################
    # Step 1: Sequence Extraction
    ##################################
    cmd_1 = "samtools faidx /mnt/users/jeevka/Salmon_Protein_Seqs/Sally_3p6_Protein.fasta " + temp[1] + " >Salmon.fasta"
    os.system(cmd_1)
        
    if temp[0] == "Trout" and Seq_ID != "NIL":
        cmd_1 = "samtools faidx /mnt/users/jeevka/Rainbow_Trout_Genome/Protein_DB/Oncorhynchus_mykiss_pep.fa " + Seq_ID + " >Trout.fasta"
        os.system(cmd_1)
        
        # ClustalW: Salmon vs Trout
        cmd_cat = "cat Salmon.fasta Trout.fasta >Salmon_Trout.fasta"
        os.system(cmd_cat)
        Fname = "ClustalW_Results/Salmon_Trout_" + temp[1] + ".aln"
        cmd_2 = "clustalw2 -infile=Salmon_Trout.fasta -type=DNA  -outfile=" + Fname + " -outorder=input"
        os.system(cmd_2)
        
    if temp[0] == "ZFish" and Seq_ID != "NIL":
        cmd_1 = "samtools faidx /mnt/users/jeevka/Zebra_Fish/Protein_DB/Danio_rerio.Zv9.75.pep.all.fa " + Seq_ID + " >ZFish.fasta"
        os.system(cmd_1)
        
        # ClustalW: Salmon vs ZFish
        cmd_cat = "cat Salmon.fasta ZFish.fasta >Salmon_ZFish.fasta"
        os.system(cmd_cat)
        Fname = "ClustalW_Results/Salmon_ZFish_" + temp[1] + ".aln"
        cmd_2 = "clustalw2 -infile=Salmon_ZFish.fasta -type=DNA  -outfile=" + Fname + " -outorder=input"
        os.system(cmd_2)
        
    if temp[0] == "Cod" and Seq_ID != "NIL":
        cmd_1 = "samtools faidx /mnt/users/jeevka/Cod_Fish_Genome/Protein_DB/Cod_Protein.fa " + Seq_ID + " >Cod.fasta"
        os.system(cmd_1)
        
        # ClustalW: Salmon vs Cod
        cmd_cat = "cat Salmon.fasta Cod.fasta >Salmon_Cod.fasta"
        os.system(cmd_cat)
        Fname = "ClustalW_Results/Salmon_Cod_" + temp[1] + ".aln"
        cmd_2 = "clustalw2 -infile=Salmon_Cod.fasta -type=DNA  -outfile=" + Fname + " -outorder=input"
        os.system(cmd_2)
        
    if temp[0] == "SBack" and Seq_ID != "NIL":
        cmd_1 = "samtools faidx /mnt/users/jeevka/Stickleback_Genome/Protein_DB/Stickleback.fa " + Seq_ID + " >SBack.fasta"
        os.system(cmd_1)
        
        # ClustalW: Salmon vs SBack
        cmd_cat = "cat Salmon.fasta SBack.fasta >Salmon_SBack.fasta"
        os.system(cmd_cat)
        Fname = "ClustalW_Results/Salmon_SBack_" + temp[1] + ".aln"
        cmd_2 = "clustalw2 -infile=Salmon_SBack.fasta -type=DNA  -outfile=" + Fname + " -outorder=input"
        os.system(cmd_2)
    N += 1
    
    #if N >=50:
    #    sys.exit()
        
Ortho.close()
