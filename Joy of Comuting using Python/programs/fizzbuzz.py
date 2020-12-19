# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:04:03 2020

@author: saptarshi
"""

# program for fizzbuzz, multiples of 3 prints fizz, multiples of 5 prints buzz and multiples of both 3 and 5 prints fizzbuzz
def fizzbuzz(n):
    for i in range(1,n):
        if i%3 == 0 and i%5 == 0:
            print(str(i) + " = fizzbuzz")
        elif i%3 == 0:
            print(str(i) + " = fizz")
        else:
            print(str(i) + " = buzz")

n = int(input("Enter a range: "))
fizzbuzz(n)