"""
Description: Fibonacci series, using recursion.
A series whose starting numbers are 0 and 1 and
then the next number is found by adding the previous
two numbers.
@author: Saptarshi Das
"""

def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#input
n = int(input("Enter a non-negative integer: " ))
if (n<0):
    print ("negative numbers are not defined.")
else:
    print ("Fibonacci number at position ",n," is ",fibonacci(n))
        
        
