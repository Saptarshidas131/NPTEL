'''
Given two numbers (integers) as input, print the smaller number.

Input Format:
The first line of input contains two numbers separated by a space

Output Format:
Print the smaller number

Example:

Input:
2 3

Output:
2 
'''

a,b = input().split()
x = int(a) if int(a)<int(b) else int(b)
print (x)
