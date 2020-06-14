#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:44:07 2020

@author: gongmeiting
"""

#A simply SIR model
#import necessary libraries
#define the basic variables of the model
#creat arrays for each variables to track how they evolve over time 
#record the output of each time step
#plot the result
#save plots as a file


#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
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
#loop over 1000 time points
time=1000
for e in range(1,time+1):
    real_beta=beta*I/N
    # For a susceptible individual to be infected,
    # we consider not only the infection rate upon contact (beta), 
    # but also the probability of making contact with an infected individual.
    si=list(np.random.choice(range(2),S,p=[1-real_beta,real_beta])).count(1)
    #si represents the people who are new infected 
    #we choose numbers from range(2) (i.e. 0 or 1) S times,
    #with a probability of 1-real_beta of choosing 0 
    #and a probability of real_beta of choosing 1
    S=S-si
    I=I+si
    ir=list(np.random.choice(range(2),I,p=[1-gamma,gamma])).count(1)
    #ir represents the people who ae new recovered
    #we choose numbers from range(2) (i.e. 0 or 1) I times,
    #with a probability of 1-gamma of choosing 0 
    #and a probability of gamma of choosing 1
    I=I-ir
    R=R+ir
    #add elements to arrays
    s.append(S)
    i.append(I)
    r.append(R)
#set up the dimensions and resolution of plot
plt.figure(figsize=(6,4),dpi =150)
#set up xlabel, ylabel, title etc
plt.xlabel('time')
plt.ylabel('population')
plt.title('SIR model')
plt.plot(list(range(time+1)), s, 'b',label='Susceptible')
plt.plot(list(range(time+1)), i, 'r',label='Infected')
plt.plot(list(range(time+1)), r, 'g',label='Recovered')
legend = plt.legend(loc='upper right')
plt.savefig("SIR",type='png')
plt.show()
#by trial, I find that running the code several times produces different results