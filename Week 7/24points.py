#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:26:55 2020

@author: gongmeiting
"""

#Game of 24 points
# N numbers between 1 to 23   *+-/
#judge if the number is between 1 and 23
    #if not,input again
    #if yes,calculate
        #if the length of input 2
            #yes +-*/ to test if the can make 24
            #no merge the last two to reduce the length
            
#use data to list the input number 
data = list(map(int, input("Please input numbers to compute 24(the number should between 1 and 23):(use ',' to divide them)\n").split(',')))
N = len(data)
#the function is used to test if the number is bewteen 1 and 23
#if not, input again
def judge(data):
	flag_data= True
	for i in range(0, N):
		if data[i] <1 or data[i] >23:
			flag_data = False
	return flag_data
while not judge(data):
	print("The input number must be intergers from 1 to 23")
	data = list(map(int, input("Please input numbers to compute 24:(use ',' to divide them)\n").split(',')))
Recursion_times = 0
#the function is used to calculate
def get24(array):
	#global Recursion_times evaluates the recursion times, adding 1 for each call
	global Recursion_times
	Recursion_times += 1
	#find the length of the array
	length = len(array)
    #judge whether the number of elements is 2
    #if yes, the situation =2
	if length == 2:
		#calculate to test if tey can get 24, if ok returns True, otherwise returns False
		if array[0] + array[1] == 24:
			return True
		elif array[0] - array[1] or array[1] - array[0] == 24:
			return True
		elif array[0] * array[1] == 24:
			return True
		elif array[0] / array[1] or array[1] / array[0] == 24:
			return True
		else:
			return False
	#if the number of elements is not 2
	if length != 2:
		#get the last two elements of the data array to merge
		last1 = data[-1]
		last2 = data[-2]
		#pnn represents "possible new numbers" and is used to represent all possible new numbers for last1 and last2 by+-*/
		pnn = []
		#add the new number into the list pnn
		pnn.append(last1+last2)
		pnn.append(last1-last2)
		pnn.append(last2-last1)
		pnn.append(last1*last2)
		pnn.append(last1/last2)
		pnn.append(last2/last1)
        #For each number in merge_set, merge it with the previous len(array)-2 elements of data into the new list new_data
		for item in pnn:
			new_data = []
			#add the first len(array)-2 elements of data into the list new_data
			for i in range(length-2):
				new_data.append(data[i])
			#add the numbers in pnn into the list new_data       
			new_data.append(item)
			#Call get24() recursively to see if it satisfies. if so, return True; if not, return False
			if get24(new_data):
				return True
			else:
				return False

if get24(data):
	print("Yes")
	print("Recursion times: ", Recursion_times)
else:
	print("No")
	print("Recursion times: ", Recursion_times)

