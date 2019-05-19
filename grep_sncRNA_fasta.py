#!/usr/bin/env python
import re
import csv
import operator
import sys
##input: python print_IDs_fq_fa.py reads reference_fasta(reference_fasta fasta/fastq file)
def ID(csv1):
	item_set = {""}
	for row in csv1:
		item_set.add('>' + row + '%mmu_miRNA')
	return item_set

def IDs_fq(item_set, reference_fasta):
	a = 0
	for reference_fasta[a] in reference_fasta:
		if reference_fasta[a] in item_set:
			grep_sncRNA.write(reference_fasta[a] + '\n' + reference_fasta[a+1] + '\n')
		a += 1


with open(sys.argv[1],'r') as f1:
	input_ID = f1.read().splitlines()

IDs_set = ID(input_ID)
with open(sys.argv[2],'r') as f2:
	reference_fasta = f2.read().splitlines()


grep_sncRNA = open('grep_' + sys.argv[1],'w')
IDs_fq(IDs_set, reference_fasta)
grep_sncRNA.close
