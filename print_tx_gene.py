import re
import sys
import os, errno

with open(sys.argv[1]) as f1:
    sample = f1.read().splitlines()
with open(sys.argv[2]) as f2:
    gtf = f2.read().splitlines()

out_tRNA_gene_table = open(sys.argv[1] + '_gene_table','w')
out_tRNA_gene_list = open(sys.argv[1] + '_gene_list','w')

dict_tRNA_tx = {}
tRNA = sample[8].split('\t')[0]
item = sample[8].split('\t')
TX1 = item[1].split('%')
TX = TX1[1]
tx_tuple = (TX,)
for a in range(9,len(sample)):
    item = sample[a].split('\t')
    TX1 = item[1].split('%')
    TX = TX1[1]
    if item[0] == tRNA:
        tx_tuple = tx_tuple + (TX,)
    if item[0] != tRNA:
        dict_tRNA_tx[tRNA] = tx_tuple
        tx_tuple = (TX,)
        tRNA = item[0]


##read through genes.gtf and print transcript fasta file
dict_tx_gene = {}
for b in range(0,len(gtf)):
    if 'gene_name' in gtf[b]:
        column = gtf[b].split("\t")
        info = column[8].split()
        for i in range(0,len(info)):
            if info[i] == 'transcript_id':
                tx_id1 = info[i+1][1:len(info[i+1])-2]
            elif info[i] == 'gene_name':
                gene_name = info[i+1][1:len(info[i+1])-2]
        dict_tx_gene[tx_id1] = gene_name

##output tRNA and target genes
dict_tRNA_gene = {}
for tRNA in dict_tRNA_tx:
    gene=()
    for tx in dict_tRNA_tx[tRNA]:
        if tx in dict_tx_gene:
            gene = gene + (dict_tx_gene[tx],)
        else:
            print "No corresponding gene_name for " + tx + " in " + sys.argv[2]           
    dict_tRNA_gene[tRNA] = gene
    out_tRNA_gene_table.write(tRNA + '\t' + '\t'.join(map(str,gene)) + '\n')
    out_tRNA_gene_list.write('\n'.join(map(str,gene)) + '\n')
