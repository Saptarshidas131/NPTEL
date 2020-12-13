'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Input Format:
The first line of the input contains a statement.

Output Format:
Print the number of upper case and lower case respectively separated by a space.

Example:

Input:
Hello world!

Output:
1 9 
'''

s = input()
countUpper = 0
countLower = 0

for e in s:
  if e.isupper():
      countUpper += 1
  elif e.islower():
      countLower += 1
print(countUpper,countLower,sep=" ",end="")

