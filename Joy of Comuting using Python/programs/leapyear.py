# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:43:49 2020

@author: saptarshi
"""

# check a year leap year or not, takes year as an argument
def leap_year(year):
    if(year%4 == 0 and year%100 != 0 or year%400 == 0):
        return True
    else:
        return False
"""
year = int(input("Enter a year: "))
if (leap_year(year)):
    print("Leap year.")
else:
    print("Not a leap year.")
"""