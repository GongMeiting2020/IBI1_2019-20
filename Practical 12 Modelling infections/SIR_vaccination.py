#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:44:06 2020

@author: gongmeiting
"""

#the effect of vaccination
#import necessary libraries
#copy SIR.py
#extend model to include an additional group of vaccinated people
#try different percentages and plot the number of infected people for each of them

#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#use nice colour
from matplotlib import cm
#set up the plot dimensions and resolution
plt.figure(figsize=(6,4),dpi =150)
#define the basic variables of the model
N=10000
beta=0.3
gamma=0.05
time=1000
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
for percent in range(0,100,10):
    #it is a pity that I cannot contain 100
    R=int(percent*N/100)
    #R represents recovered people
    I=1
    #I represents infected people
    S=N-I-R
    #S represents susceptible individuals
    #creat arrays for each variables to track how they evolve over time 
    s=[S]
    i=[I]
    r=[R]
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
        s.append(S)
        i.append(I)
        r.append(R)
    plt.plot(list(range(time+1)), i, color=cm.viridis(percent*3),label=str(percent)+'%')
legend = plt.legend(loc='upper right')
plt.savefig("SIR_vaccination",type='png')
plt.show()