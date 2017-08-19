"""
Created on Fri Aug 18 18:45:32 2017

@author: elenizarogianni

Sensor challenge

This script reads a list of sensor measurements from a file and for each sensor it prints out
how many measurements are above a given threshold.

The file input consists of n lines where:
    the first line consists of the number of sensors and number of measeurements taken
    the second line consists of the threshold values
    the rest n-2 lines consist of each sensor's measurements. 

NOTE: Files should be in txt or csv format and comma-separated.

In IDLE: execfile('sensor_challenge.py')

"""

# Imports
import os
import os.path
import time

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
# sort values in each list of Sensors list
Sensors= map(sorted, Sensors)

def threshold_comparison(sensor_list, thres_list):
    # initialize an empty list contain frequency of measurements surpassing values in thres_list
    output_final=[]
    # Loop over lists in Sensors 
    for s in sensor_list:
        output_list1=[]
        for item in thres_list:  # loop over items in threshold list
            new_list = [i for i in s if i>item]  # create new_list containing those values that are larger than threshold value 
            #new_list = sum(1 for i in s if i>item)
            output_list1.append(len(new_list)) # take the size of the new_list and append it to the output_list1
        output_final.append(output_list1) # append results to output list 
    return output_final    


# call function with Sensors and thresholds lists as arguments 
output = threshold_comparison(Sensors, thresholds)

# Print out frequencies for every sensor
for k in range(len(Sensors)):
    print("Sensor {:}".format(k+1) + " " + str(output[k]))

# calculate and print out time passed
elapsed_time = time.time() - start_time
print ('time cost = ') , elapsed_time







