#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:49:28 2017


@author: elenizarogianni

For the bonus questions, I figured that instead of performing a linear search in each Sensor list,
a binary search in the list would be more computationally and time-wise efficient.

"""

# Imports
import os
import os.path
import time
import bisect

# Give the file's pathway
filename= raw_input("\n Hello! "
    "\n \n Please type in the path to your file and press 'Enter': ")

# check if there is a file 
if os.path.isfile(filename) and os.access(filename, os.R_OK):
    print "File exists and is readable"
else:
    print "Either file is missing or is not readable"


start_time = time.time()

#open file to read
with open(filename, 'r') as file:
    data=file.readlines()
    

## --- Data preprocessing
   
data=[line.rstrip() for line in data] # get rid of the /n character

# convert list of strings to a list of integers
for i in range(len(data)):
    data[i]=map(int, data[i].split(','))  # break the string into chunks, then convert it to int
    
    
no_sensors = data[0][0]
no_measurements= data[0][1]
thresholds = sorted(data[1])

limit= -(no_sensors)
Sensors=data[limit:]
Sensors= map(sorted, Sensors)

output_final = []
# do a binary search
for S1 in Sensors:
    output = []
    # for each threshold return the index-position to be inserted in sensor list S1
    index=[bisect.bisect_right(S1, item) for item in thresholds] 
    # substract it from the length of S1 list to get the desired frequency calculation
    output.append([len(S1)- i for i in index])
    output_final.append(output)
    
# Print out frequencies for every sensor
for k in range(len(Sensors)):
    print("Sensor {:}".format(k+1) + " " + str(output_final[k]))

elapsed_time = time.time() - start_time
print('time cost = ') , elapsed_time