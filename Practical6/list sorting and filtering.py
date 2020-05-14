#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:10:16 2020

@author: gongmeiting
"""

#order the ten gene lengths
#delete the longest and shortest gene lengths
#draw the bloxplot

#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
#input ten gene lengths 
a=int(input("please input the gene length of the first gene:"))
b=int(input("please input the gene length of the second gene:"))
c=int(input("please input the gene length of the third gene:"))
d=int(input("please input the gene length of the fourth gene:"))
e=int(input("please input the gene length of the fifth gene:"))
f=int(input("please input the gene length of the sixth gene:"))
g=int(input("please input the gene length of the seventh gene:"))
h=int(input("please input the gene length of the eight gene:"))
i=int(input("please input the gene length of the ninth gene:"))
j=int(input("please input the gene length of the tenth gene:"))
#make them a list called gene_length
gene_length=[a,b,c,d,e,f,g,h,i,j]
#sort the gene_length list and store it as a new list called L
L=sorted(gene_length)
#delete the shortest gene length
del(L[0])
#delete the longest gene length
del(L[8])
print(L)
#make the box plots 
n=8
plt.boxplot(L,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
            )
plt.show()