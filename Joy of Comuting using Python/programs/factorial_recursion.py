"""
Description: Factorial of positive numbers, using recursion.
@author: Saprarshi Das
"""

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter the number to find the factorial: "))

if (n<0):
    print ("Factorial is only for positive integers.")
else:
    f = factorial(n)
    print ("Factorial of ", n ,"is",f)
