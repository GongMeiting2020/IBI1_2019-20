#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:35:51 2020

@author: gongmeiting
"""
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
#the four types of DNA nucleotides are represented by A, T, C and G
labels='A','T','C','G'
#use a, t,c,g to represent the number of times that the symbols 'A','T','C','G' occurs in DNA string
a=input("Please input the number of times that the symbols 'A' occurs in DNA string:")
t=input("Please input the number of times that the symbols 'T' occurs in DNA string:")
c=input("Please input the number of times that the symbols 'C' occurs in DNA string:")
g=input("Please input the number of times that the symbols 'G' occurs in DNA string:")
sizes=[a,t,c,g]
explode=(0,0,0,0)
plt.pie(sizes, explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
#equal aspect ratio ensures that the pie is dram as a circle
plt.axis('equal')
#set up the frequency dictionary
frequency_dict={}
frequency={'A':a,'T':t,'C':c,'G':g}
print(frequency)
#show the pie chat
plt.show()