#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:26:39 2020

@author: gongmeiting
"""
a=457
b=a*1000+a
print(b%7==0)
c=b/7
d=c/11
e=d/13
print(a==e)
print(a>e)
print(a<e)
#a==e is always True since b/a=7*11*13

#another code, to avoid same variables,use f~j to represnt a~e
f=input ("a three-digit number:")
g=int(f)*1000+int(f)
if g%7==0:
    h=g/7
    i=h/11
    j=i/13
    if int (f)>j:
        print("f>j")
    elif int (f)<j:
        print("f<j")
    else:
        print("f=j")
else:
    print("g cannot devided by 7")


X=True
Y=False
Z=(X and not Y) or (Y and not X)
print(Z)
W= X!=Y
print(Z==W)
