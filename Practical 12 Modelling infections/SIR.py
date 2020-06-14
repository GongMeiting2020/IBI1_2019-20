#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:44:07 2020

@author: gongmeiting
"""

#A simply SIR model
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(6,4),dpi =150)
#the total population is 10000
#define the basic variables of the model
I=1
#I represents infected people
S=9999
#S represents susceptible individuals 
R=0
#R represents recovered people
N=S+I+R
#N represents total people
beta=0.3
#beta is infection probability
gamma=0.05
#gamma is recovery probability
#creat arrays for each variables to track how they evolve over time 
i=[I]
s=[S]
r=[R]
time=1000
for tmp in range(1,time+1):
    curr_beta=beta*I/N
    s_inf=list(np.random.choice(range(2),S,p=[1-curr_beta,curr_beta])).count(1)
    S=S-s_inf
    I=I+s_inf
    i_rec=list(np.random.choice(range(2),I,p=[1-gamma,gamma])).count(1)
    I=I-i_rec
    R=R+i_rec
    s.append(S)
    i.append(I)
    r.append(R)
plt.xlabel('time')
plt.ylabel('population')
plt.title('SIR model')
plt.plot(list(range(time+1)), s, 'b',label='Susceptible')
plt.plot(list(range(time+1)), i, 'r',label='Infected')
plt.plot(list(range(time+1)), r, 'g',label='Recovered')
legend = plt.legend(loc='upper right', shadow=True)
plt.savefig("SIR",type='png')
#plt.close()
plt.show()