#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:44:04 2020

@author: gongmeiting
"""

#Looking at disease spread in 2D
#import useful libraries
#set up model parameters 
#encode the different states in the form of numbers in an array
#0 for susceptible, 1 for infected 2 for recovered
#make a 100*100 array that is completely made of zeroes
#make array of all susceptible population
#loop 100
#follow the progression of disease through space and time

#import useful libraries
import numpy as np
import matplotlib.pyplot as plt
#set up model parameters 
beta=0.3
gamma=0.05
time=100
#make a 100*100 array that is completely made of zeroes
population=np.zeros((100,100))
#choose one rqandom point in the 100*100 array for where the outbreak happens
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
plt.imshow(population,cmap='viridis',interpolation='nearest')
#loop 100
for e in range(time):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself (I think if it can infect yourself, the probability of recover will be impacted.)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
                        #recover    
                        population[x, y] = np.random.choice((1,2),1, p=[1-gamma,gamma])[0]
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.show()