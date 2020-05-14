#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:15:02 2020

@author: gongmeiting
"""
#input a positive integer and int it
n=int(input("please input a positive integer:"))
#if n==1, no while loop
if n==1:
    print(n)
#if n!=1 do the while loop
while n!=1:
    if n%2==0:
        n=n/2
    elif n%2==1:
        n=3*n+1
    print(n)
#the loop will stop if n=1
