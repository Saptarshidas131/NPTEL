"""
Description: Factorial of a positive number.
@author: Saptarshi Das
"""

def factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact = fact*i
    return fact

n = int(input("Enter the number to find the factorial: "))

if (n<0):
    print ("Factorial if only for positive integers.")
else:
    f = factorial(n)
    print ("Factorial of ", n ,"is",f)
        
