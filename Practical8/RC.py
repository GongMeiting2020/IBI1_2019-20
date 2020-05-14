#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:48:09 2020

@author: gongmeiting
"""

#plan:
#reverse the seq
#use if-statements to make the reverse complementary sequence

seq='ATGCGACTACGATCGAGGGCCAT'
re=seq[::-1]#reverse the seq
rc= ""
#Loop through the sequence re
for i in re:
    #if the character is 'A'
    if i =='A':
        #Store 'T' to the string rc
        rc = rc+'T'
    #else if the character is 'G'
    elif i == 'G':
        #Store 'C' to the string rc
        rc = rc+'C'
    #else if the chracter is 'T'
    elif i == 'T':
        #Store 'A' to the srting rc
        rc= rc+'A'
    #else if the character is 'C'
    elif i == 'C':
        #Store 'G' to the srting rc
        rc = rc+'G'
#Print the outcome
print("the reverse complementary sequence of seq is:",rc)

