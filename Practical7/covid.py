#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 01:14:31 2020

@author: gongmeiting
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/gongmeiting/jia")
os.listdir("/Users/gongmeiting/jia")
#read the content of the .csv file into a dataframe object
covid_data=pd.read_csv("full_data.csv")
#print(covid_data.head(5))
    #after try, we can see that the covid_data.head(4) can be used to show the first four row (expect the title row) of full_data.csv 
#covid_data.info()
#print(covid_data.describe())
    #we can see that the mean of new cases is 194.546773
    #the median is 0
    #the range of total deaths is 0.000000 to 37272.000000
#print(covid_data.iloc[0,1])
#print(covid_data.iloc[2,0:5])
#print(covid_data.iloc[0:2,])
#print(covid_data.iloc[0:10:2,0:5])
    #0:10:2  2 means every second row

#the next line shows all columns, and every third row between 0 and 15
print(covid_data.iloc[0:15:3,])

#print(covid_data.iloc[0:3,[0,1,3]])
    #the first three rows, the first, second and fourth column

#my_columns=[True,True,False,True,False,False]
#print(covid_data.iloc[0:3,my_columns])
    #only the data of True will be showed
    #by try, we can see that if my_columns is shorter or longer, we will get Error 

#print(covid_data.loc[2:4,"date"])
    #return is
    #2    2020-01-02
    #3    2020-01-03
    #4    2020-01-04
    #Name: date, dtype: object
    #loc uses column names

print(covid_data.loc[0:81,"total_cases"])
#another way to print(covid_data.loc[0:81,"total_cases"])
L = covid_data.loc[:,"location"]
row = []
for i in range(7995):
    if L.loc[i] == 'Afghanistan':# to find the location of 'Afghanistan'
        print ('True')
        row.append(i)
    else:
        print ('False')
A_total_cases = covid_data.loc[row,"total_cases"]
print (A_total_cases)
#by try, I find the two way get the same result 

#Examining the worldwide situation
row1=[]
for e in range(7995):
    if L.loc[e] == 'World':# to find the location of World
        row1.append(e)
    else:
        row1=row1
world_new_cases = covid_data.iloc[row1,2]
print (world_new_cases)
#compute both the mean dand median for new cases around the world
average=np.mean(world_new_cases)
median=np.median(world_new_cases)
print(average)
print(median)
print(average==median)#test are they same or different
a=average-median
print("the difference between average and median is:",a)
#compute the difference to find are they similar or different

#creat a boxplot of new cases worldwide
plt.boxplot(world_new_cases,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
            )
plt.show()

#make object contain data over time
world_dates= covid_data.iloc[row1,0]
print (world_dates)
plt.plot(world_dates,world_new_cases,'b+')
#the blue + represent new cases
#by try, I find that the b+, bo, r+ will change the color and shape of plot

#plot new cases and new deaths in different color 
#add title and axis lables
world_new_deaths=covid_data.iloc[row1,3]
plt.plot(world_dates,world_new_deaths,'r+')
#the red + represent new deaths
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('New cases and new deaths in world')
#add title 
plt.ylabel('Number')
#add y lable
plt.xlabel('date')
#add x lable

#answer to How have new cases and total cases developed in China?
row2=[]
for n in range(7995):
    if L.loc[n] == 'China':# to find the location of China
        row2.append(n)
    else:
        row2=row2
China_new_cases = covid_data.iloc[row2,2]
#make odject of new cases in China
China_total_cases = covid_data.iloc[row2,4]
#make odject of total cases in China
China_dates= covid_data.iloc[row2,0]
#make odject of dates in China
plt.plot(China_dates,China_new_cases,'bo')
#the blue dots represent new cases
plt.plot(China_dates,China_total_cases,'ro')
#the red dots represent total cases
plt.xticks(China_dates.iloc[0:len(China_dates):4],rotation=-90)
plt.title('New cases and total cases in China')
#add title 
plt.ylabel('Number')
#add y lable
plt.xlabel('date')
#add x lable










