'''
Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates. 

Input Format:
The first line contains n-1 numbers with each number separated by a space.

Output Format:
Print the missing number

Example:

Input:
1 2 4 6 3 7 8

Output:
5

Explanation:
In the above list of numbers 5 is missing and hence 5 is the input 
'''

n = sorted(list(int(x) for x in input().split()))
list = [x for x in range(1, n[-1]+1) if x not in n]
try:
  print(list[0],end='')
except:
  print(max(n)+1,end='')
