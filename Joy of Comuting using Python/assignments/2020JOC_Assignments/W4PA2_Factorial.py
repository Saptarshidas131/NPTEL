'''
Given an integer number n, you have to print the factorial of this number. To know about factorial please click on this link.

Input Format:

A number n.

Output Format:

Print the factorial of n.

Example:

Input:
4

Output:
24 
'''

n = int(input())
factorial = 1

if n==1 or n==0:
    print(1)
else:
    for i in range(n, 1, -1):
        factorial *= i

    print (factorial,end="")

