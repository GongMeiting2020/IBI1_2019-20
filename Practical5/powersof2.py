#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:19:01 2020

@author: gongmeiting
"""

#for simplicity, we assume x is no larger than 8192
import random
x=random.randint(1,8193)
#use y to store the value of initial x
y=x
a=("")
#n is no larger than 13 and count down from 13
n=13
#if x equal to 0 break
#if not
   # if x no smaller than 2**n 
      # x=x-2^n n=n-1 
   #else n=n-1       
while x>0 and n>0:
    if x>=2**n:
        x=x-2**n
        n=n-1
        a=a+"+"+"2**"+str(n)
    else:
        n=n-1

print(str(y)+" is "+a[1:])
#use [1:] to  delete the first "+" in a 