# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:15:36 2020

@author: saptarshi
"""

import random

# evolve takes a list then randomly picks an index and a random probability, if probability is '1' then change the index value to '0' otherwise change to '1'
def evolve(x):
    index = random.randint(0,len(x)-1)
    probability = random.randint(1,100)
    if probability==1:
        if x[index] == '0':
            x[index] = '1'
        else:
            x[index] == '0'

# dna_data.txt is opened in read mode and all the data is read in variable data and converted list
with open("dna_data.txt") as file:
    data = list(file.read())
    # call evolve 10000 times and print the data list value    
    for i in range(0,10000):
        evolve(data)
print(data)