"""
Description: Open a csv file containing the raw gps data (latitude and longitude) seperated by comma
and read it, then plot the values in google map using gmplot.
@author: Saptarshi Das
"""
#for using csv functions
import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(17.983344, 32.789876, 17)

gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

with open ("route.csv","r") as f:
    read = csv.reader(f)    #reading csv file and store data in read variable
    k = 0

    for row in read:        #iterate read variable and store data in row as list
        lat = float(row[0])     #latitude
        long = float(row[1])    #longitude

        if (k==0):
            gmap.marker(lat,long,'yellow')
            k = 1
        else:
            gmap.marker(lat,long,'blue')

gmap.marker(lat,long,'red')

gmap.draw("mymap.html")
    
