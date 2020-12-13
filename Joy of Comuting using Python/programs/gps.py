"""
Description: Open a csv file containing the raw gps data (latitude and longitude) seperated by comma
and read it, then add them as float values.
@author: Saptarshi Das
"""
#for using csv functions
import csv

with open ("route.csv","r") as f:
    read = csv.reader(f)    #reading csv file and store data in read variable

    for row in read:        #iterate read variable and store data in row as list
        lat = float(row[0])     #latitude
        long = float(row[1])    #longitude
        print (lat)
        print (long)
        print (lat+long)
    
    
