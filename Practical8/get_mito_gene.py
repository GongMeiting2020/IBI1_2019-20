#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:42:28 2020

@author: gongmeiting
"""

#read thefile 
#extract the sequences of mitochondria genes
#simplify the sequence name 
#output resulst in a new fasta file

#change the working directory to where the Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa is stored
import os
os.chdir("/Users/gongmeiting/Downloads")
import re
#read the file
sacc=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
#creat the newfile mito_gene.fa
newfile=open('mito_gene.fa',"w")
#Read ﬁle into a single string
s=sacc.read()
#use re.findall() to extract the matching strings
#*? Repeats the previous element zero or moretimes(non-greedy)
seq_mito=re.findall(r'(>.*?:Mito:[\d\D]+?gene:.*\n[\d\D]+?)>',s)

for gene in seq_mito:
    #delete the unnecessary part
    #r'>.*?(gene:.*? ).*?]',r'\1' to select only genen name and the length of the sequence
    simplify_seq_mito=re.sub(r'>.*?(gene:.*? ).*?]',r'\1',gene)
    #delete the '\n' and '>'
    new=simplify_seq_mito.replace('\n','')
    #-11 because we find that the lengths of genen name in Mito are the same
    length=len(new)-11
    sacc=">"+'gene length:'+str(length)+' '+new+"\n"
l1=[]
l1.append(sacc)
newfile.write(sacc)
#close mewfile
newfile.close()
print(open('mito_gene.fa').read())