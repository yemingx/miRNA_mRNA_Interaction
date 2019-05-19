#output whole transcript for each transcript ID
#input python print_transcript_fasta_V4.py genome_file gtf_file
import re
import sys
import os, errno
with open(sys.argv[1]) as f1:
    genome = f1.read().splitlines()
with open(sys.argv[2]) as f2:
    gtf = f2.read().splitlines()

out_tx_fasta = open(sys.argv[2]+'_TX.fa','w')

a = 0
dict1 = {}
for genome[a] in genome:
    if genome[a].startswith(">"):
        chr_name1 = genome[a]
        chr_name = chr_name1[1:]
        dict1[chr_name] = genome[a+1]
    a += 1


##read through genes.gtf and print transcript fasta file
for c in range(0,len(gtf)):
    column = gtf[c]
    column = gtf[c].split("\t")
    info = column[8].split()
    tx_id1 = info[1][1:len(info[1])-2]
    tx_id2 = info[3][1:len(info[3])-2]
    exon_num = info[5][1:len(info[5])-2]
    tx_id = ">" + tx_id1 + '%' + tx_id2 + '%' + exon_num + '%' + column[6]
    start = int(column[3]) - 1
    stop = int(column[4])
    strand = column[6]

    if column[0] in dict1:
        if exon_num == '1':   
                raw_seq1 = dict1[column[0]]
                raw_seq = raw_seq1[start:stop]
                seq = raw_seq
                if strand == '+':
                    out_tx_fasta.write(tx_id +"\n" + seq)
                    break
                elif strand == '.':
                    out_tx_fasta.write(tx_id + "\n" + seq )
                    break
                else:
                    seq_converted = []
                    for i in range(0,len(seq)):
                        if seq[i] == 'A':
                            seq_converted += "T"
                        elif seq[i] == 'T':
                            seq_converted += "A"
                        elif seq[i] == 'C':
                            seq_converted += "G"        
                        elif seq[i] == 'G':
                            seq_converted += "C"
                        elif seq[i] == 'a':
                            seq_converted += "t"
                        elif seq[i] == 't':
                            seq_converted += "a"
                        elif seq[i] == 'c':
                            seq_converted += "g"        
                        elif seq[i] == 'g':
                            seq_converted += "c"
                        elif seq[i] == 'N':
                            seq_converted += 'N'   
                        elif seq[i] == 'n':
                            seq_converted += 'n'                                                                
                    seq_join = ''.join(seq_converted)           
                    out_tx_fasta.write(tx_id + '\n' + seq_join[::-1])
                    break
    else:
        print "Fail to find " + column[0] + " in " + sys.argv[1]


for a in range(c+1,len(gtf)):
    column = gtf[a].split("\t")
    info = column[8].split()
    tx_id1 = info[1][1:len(info[1])-2]
    tx_id2 = info[3][1:len(info[3])-2]
    exon_num = info[5][1:len(info[5])-2]
    tx_id = ">" + tx_id1 + '%' + tx_id2 + '%' + exon_num + '%' + column[6]
    start = int(column[3]) - 1
    stop = int(column[4])
    strand = column[6]

    if exon_num == '1':
        if column[0] in dict1:   
            raw_seq1 = dict1[column[0]]
            raw_seq = raw_seq1[start:stop]
            seq = raw_seq
            out_tx_fasta.write("\n" + tx_id)
            if strand == '+':
                out_tx_fasta.write("\n" + seq)
            elif strand == '.':
                out_tx_fasta.write("\n" + seq )
            else:
                seq_converted = []
                for i in range(0,len(seq)):
                    if seq[i] == 'A':
                        seq_converted += "T"
                    elif seq[i] == 'T':
                        seq_converted += "A"
                    elif seq[i] == 'C':
                        seq_converted += "G"        
                    elif seq[i] == 'G':
                        seq_converted += "C"
                    elif seq[i] == 'a':
                        seq_converted += "t"
                    elif seq[i] == 't':
                        seq_converted += "a"
                    elif seq[i] == 'c':
                        seq_converted += "g"        
                    elif seq[i] == 'g':
                        seq_converted += "c"
                    elif seq[i] == 'N':
                        seq_converted += 'N'   
                    elif seq[i] == 'n':
                        seq_converted += 'n'                                                                
                seq_join = ''.join(seq_converted)           
                out_tx_fasta.write('\n' + seq_join[::-1])
        else:
            print "Fail to find " + column[0] + " in " + sys.argv[1]

    elif exon_num != '1':
        if column[0] in dict1:   
            raw_seq1 = dict1[column[0]]
            raw_seq = raw_seq1[start:stop]
            seq = raw_seq
            if strand == '+':
                out_tx_fasta.write(seq)
            elif strand == '.':
                out_tx_fasta.write(seq)
            else:
                seq_converted = []
                for i in range(0,len(seq)):
                    if seq[i] == 'A':
                        seq_converted += "T"
                    elif seq[i] == 'T':
                        seq_converted += "A"
                    elif seq[i] == 'C':
                        seq_converted += "G"        
                    elif seq[i] == 'G':
                        seq_converted += "C"
                    elif seq[i] == 'a':
                        seq_converted += "t"
                    elif seq[i] == 't':
                        seq_converted += "a"
                    elif seq[i] == 'c':
                        seq_converted += "g"        
                    elif seq[i] == 'g':
                        seq_converted += "c"
                    elif seq[i] == 'N':
                        seq_converted += 'N'   
                    elif seq[i] == 'n':
                        seq_converted += 'n'                                                                
                seq_join = ''.join(seq_converted)           
                out_tx_fasta.write(seq_join[::-1])
        else:
            print "Fail to find " + column[0] + " in " + sys.argv[1]

